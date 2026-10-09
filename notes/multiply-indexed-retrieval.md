# Multiply indexed retrieval and high-dimensional rotations

## One object, many ways to find it

An email, web page, code symbol, geometry object, device event, and math note can all need multiple indexes. One universal search box does not supply all the needed relations.

The starting point should be a durable object with an identity, content provenance, and a history of changes. Indexes are **derived views** of it.

~~~text
retained objects + provenance
  ├── exact text and identifiers
  ├── full-text inverted lists / BM25
  ├── attributes, dates, permissions, and facets
  ├── citations, code imports, and graph relations
  ├── spatial and geometric indexes
  ├── embeddings and nearest-neighbor structures
  ├── human corrections and task-specific relations
  └── compressed, machine-specific materialized views
~~~

These indexes do not have to agree on a ranking. They answer different questions.

[IB / Pensieve](https://github.com/isomorphisms/ib), [semantic operating-system notes](../semantic-operating-system.md), and [My filesystem, my way](../my-filesystem-my-way.md) supply the systems context.

## Retain identity; rebuild the rest

A useful base record has:

- stable object identity;
- source identity and source revision;
- content hash or other integrity check;
- a declared extraction or parser version;
- permissions and deletion state;
- captured relationships;
- a record of derived transformations and index revisions.

A vector is not the object. It is a derived feature of the object. Re-embedding with a new model must not silently change the identity or history of the document.

Use explicit lineage:

~~~text
object revision
  → parser and extraction revision
  → embedding model and preprocessing revision
  → exact feature vector
  → transform revision
  → quantization revision
  → ANN index build revision
~~~

A correction from a human can change the object or add another relation. It should not vanish the next time an index is rebuilt.

Multiple indexes can be materialized lazily, in different files, layouts, or locations. Store only the state needed to reconstruct a view, when reconstruction is cheaper and safe enough.

## What "high dimensional" changes

Let the uncompressed embedding of an object be $x\in\mathbb R^d$. A query vector $q$ may be ranked by squared Euclidean distance,

$$
D(q,x)=\sum_{i=1}^{d}(q_i-x_i)^2,
$$

or by inner product $q^\mathsf Tx$. Cosine similarity uses the inner product after normalizing both nonzero vectors.

Those are different metrics and assumptions. Choosing the wrong one changes the retrieval question.

Exhaustive scan of $N$ dense vectors costs roughly $O(Nd)$ arithmetic per query, plus the cost of loading the vectors. Large $N$ and $d$ create a bandwidth problem even when each distance is easy.

High-dimensional geometry also weakens naive spatial intuition. Data distributions may concentrate in certain directions, and simple nearest-neighbor partitions can behave badly as dimension grows. Actual intrinsic structure matters more than the nominal dimension alone.

Compression and approximate indexing buy speed or capacity by allowing errors. Their errors must be measured against exact retrieval under the stated metric.

## Orthogonal transformations: what changes and what does not

For $R\in O(d)$, with $R^\mathsf TR=I$,

$$
\|Rq-Rx\|_2^2=\|q-x\|_2^2,\qquad
(Rq)^\mathsf T(Rx)=q^\mathsf Tx.
$$

A **common orthogonal rotation of both query and database** leaves exact Euclidean distance and exact inner product unchanged. For unit vectors it also leaves cosine similarity unchanged.

This is a mathematical invariance, not a claim about approximate indexes.

Suppose we compress after rotating. Write $C$ for a coordinate-sensitive compression method. In general,

$$
C(Rx)\ne RC(x).
$$

Product quantization splits coordinates into subspaces and quantizes them separately. A good rotation may place related information into blocks that are easier to encode. Another rotation may make quantization worse.

That is the point of **optimized product quantization (OPQ)**: choose a transform that reduces compression distortion for a given encoding family. The paper by **Tiezheng Ge, Kaiming He, Qifa Ke, and Jian Sun** addresses the transform and codebook jointly.

The interesting optimization is therefore:

~~~text
exact geometry (unchanged under a common rotation)
  → choose a coordinate frame
  → apply an axis-sensitive compression or index
  → compare its approximate answer with the exact answer
~~~

If a transform truncates dimensions, whitens by nonuniform scaling, or uses a nonorthogonal learned map, it does not preserve the same distances in general. State the new metric or loss.

## Example: harmless rotation, consequential rounding

Take two-dimensional points

$$
q=(1,0), \qquad x=(0,1).
$$

Their squared distance is $2$. Rotate both by $45^\circ$:

$$
R=\frac{1}{\sqrt2}
\begin{bmatrix}1&-1\\1&1\end{bmatrix}.
$$

Then $Rq=(1/\sqrt2,1/\sqrt2)$ and $Rx=(-1/\sqrt2,1/\sqrt2)$. Their squared distance remains $2$.

Now encode each coordinate independently to a coarse set of allowed values. Depending on the grid and rounding rules, the encoded distance need not remain $2$. A grid aligned with the original axes and a grid aligned with the rotated axes can have different error.

The rotation did not change the exact problem. It changed the approximation problem.

This is also why the numeric format and the index layout should be explicit, versioned derived state.

## A family of indexes, not a winner-take-all contest

**Exact lexical search:** token positions, phrase matching, filenames, identifiers, and exact equations. Needed when a symbol must be found as written.

**Inverted full text:** BM25 and related methods. Good when word evidence matters and relevance can be approximated from term statistics.

**Attribute indexes:** date, source, scope, language, device, repository, version, author, and user permissions. They can reject ineligible objects before ranking.

**Graph indexes:** citations, imports, parent/child geometry, issue references, user corrections, and causal or provenance links. They preserve structure that embedding distance may miss.

**Spatial indexes:** coordinates, bounding regions, nearest geometry, camera/world transforms. Their coordinate frame is part of the query.

**Vector indexes:** exact flat search, inverted-file partitions, product quantization, learned rotation, graph ANN, and combinations. Their usefulness depends on the query distribution and target machine.

A request might combine all of these. One example:

> Find a paper that cites a particular theorem, refers to a diagram with a specific kind of curve, and resembles a given screenshot.

That is not one similarity calculation. It has bibliographic, lexical, visual, and geometric constraints. Some are hard filters. Others are ranked evidence. A result should retain why it matched.

## The index plan itself is typed

A query needs to know:

~~~text
SourceRevision
Permissions
Field and Metric
IndexKind and BuildRevision
VectorDimension and CoordinateFrame
Preprocessing and RotationRevision
NumericEncoding
ExactOrApproximate
ScoreMeaning
EvidenceOfMatch
~~~

For example, an index built with normalized vectors cannot be queried as though it stored arbitrary magnitudes. An inner-product ranker is not automatically a Euclidean-distance ranker.

A transform revision is part of the index contract. If the database is rotated by $R_A$ but the query is rotated by $R_B$, the invariance proof is gone.

A deletion or permission revocation must invalidate **all** materializations that could expose the object. "It disappeared from lexical search but still appears in ANN" is a correctness and privacy defect.

## Search as a compositional operation

A plan can be explicit:

1. Resolve source and permission scope.
2. Select exact filters.
3. Choose candidate generators: text, graph, embedding, geometry.
4. Identify approximate steps and their known error.
5. Merge candidates without discarding provenance.
6. Apply a final scorer with a declared meaning.
7. Optionally re-rank using exact source data.
8. Return the score components and evidence.

An ANN index can supply candidates. It does not have to decide the final edit, citation, deletion, or build action. Fuzzy discovery and authorized mutation belong on opposite sides of a validation boundary.

A suitable experiment can preserve a query plan as data and compare alternative plans on the same corpus, instead of rebuilding the search architecture from scratch each time.

## Memory and multiple indexes

If a vector has $d=128$ binary32 coordinates, its raw payload is $512$ bytes. A product-quantized code with sixteen eight-bit subcodes uses $16$ bytes **for the code**, plus identifiers, tables, centroids, and index overhead.

That compression changes the workload: the query now scores codes and lookup tables instead of streaming all original vectors.

The E5M3 work of **Hiroyuki Ootomo and Akira Naruse** targets the nonnegative squared-distance fragment tables used by a GPU IVFPQ search. Their one-byte unsigned format can reduce shared-memory bank conflicts for that access pattern. It is not a replacement type for arbitrary signed vectors. See [E5M3 and memory costs](e5m3-memory-and-nano-optimization.md).

A storage decision may prefer one index on a phone and another on a GPU server. A durable semantic object need not force both onto the same allocation layout.

The correct question is not "which library owns my data?" It is "which representation answers this query under these machine and error constraints?"

## An evaluation that matters

For each index build and query workload, retain:

- exact reference top-$k$ under a stated metric;
- recall@$k$ of the approximate candidate generator;
- candidate count and filtering accuracy;
- wall time distribution, including tail latency;
- bytes stored per object including overhead;
- memory transfers and any measurable cache or bank effects;
- cost of updates, deletions, and rebuilding;
- consistency of permissions and provenance;
- cases where a human correction changes the answer.

A machine improvement that decreases recall needs to state the price paid. More indexes are useful only when they answer a distinct query or reduce cost without corrupting meaning.

## Rotations beyond retrieval

The same type distinctions can serve:

- rendering a high-dimensional object through a chosen projection;
- classifying activations with oriented hyperplanes;
- adapting coordinates before a compact numeric encoding;
- moving between mathematical bases without changing an underlying object;
- learning transforms that help a quantizer while protecting exact invariants.

The result is not a claim that all machine learning needs a rotation. It is a concrete reason to study rotations in $SO(n)$ as first-class operations rather than burying them in untyped matrices.

[Rotations from types to assembly](rotations-types-to-assembly.md) describes that semantic path. [Controlling AI and the compiler](ai-control-and-compiler-goals.md) describes how to verify the resulting code.

## References and credit

- **Hervé Jégou, Matthijs Douze, Cordelia Schmid**. *Product Quantization for Nearest Neighbor Search* (2011). [Original paper's DOI](https://doi.org/10.1109/TPAMI.2010.57).
- **Tiezheng Ge, Kaiming He, Qifa Ke, Jian Sun**. [*Optimized Product Quantization*](https://www.microsoft.com/en-us/research/publication/optimized-product-quantization/) (2013 technical report; later journal publication).
- **Hiroyuki Ootomo, Akira Naruse**. [*Custom 8-bit floating point value format for reducing shared memory bank conflict in approximate nearest neighbor search*](https://arxiv.org/abs/2301.06672) (2023).
- [Faiss index factory and vector transforms](https://github.com/facebookresearch/faiss/wiki/The-index-factory). Practical reference for IVF, OPQ, PQ, flat and graph indexes.
- [IB and semantic operating-system designs](../semantic-operating-system.md).
