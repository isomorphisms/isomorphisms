# FPGA grep

Search, matching, parsing, classification, DOM walking, biological sequence work, and ordinary control flow are often written as piles of `if / then / else`.

That does not mean branches are the fundamental operation.

A better question is:

> what semantic operation is the program actually asking for, and what representation should implement it on this machine?

For a fixed-string search, the answer might be scalar branches, a word-level bitset, SIMD masks, a table-driven automaton, GPU predicates, or FPGA gates.

The source-level request should not have to choose too early.

## One meaning, several lowerings

A compiler or library can preserve operations such as:

```text
match fixed bytes
match any of these patterns
classify this symbol
select records satisfying these predicates
walk until this relation matches
tokenize this stream
```

and lower them differently:

```text
semantic operation
    ├── scalar comparisons and branches
    ├── jump table / finite case dispatch
    ├── Shift-And / Shift-Or bit-parallel state
    ├── Boyer-Moore-style skipping
    ├── DFA / NFA tables
    ├── Aho-Corasick-style many-pattern state
    ├── SWAR / SIMD masks
    ├── GPU predicates / ballots
    └── FPGA comparators, registers, gates, and wires
```

There is no universal winner.

Irregular pointer-heavy traversal may belong on a CPU. A flattened batch of the same predicates may map well to SIMD or a GPU. A bounded streaming matcher may be natural spatial hardware.

The point is to keep the semantic operation visible long enough that the backend can make the choice.

## The small FPGA experiment

The simplest FPGA version is deliberately boring.

Feed bytes through a bounded pipeline, compare several positions in parallel, combine the equality bits, and emit a match-position bitmap.

That already asks useful questions:

- how much matching state can become space rather than time?
- how much control flow disappears when comparisons exist simultaneously?
- how should match positions be returned?
- what happens when the pattern is longer than the available hardware window?
- what interface keeps the software oracle and hardware result exactly comparable?

From there the ladder can grow:

```text
fixed literal
    → several literals
    → bit-parallel state
    → streaming DFA / NFA
    → many-pattern engine
    → regex subset
    → multiple streams
```

The project should earn each step with fixtures and receipts rather than jumping directly to an impressive but opaque regex accelerator.

## Biology belongs here

Biological sequence processing is not an afterthought.

DNA gives unusually compact and structured workloads:

- a four-symbol unambiguous alphabet can be represented with two bits per base;
- ambiguity codes can be represented as masks;
- exact motif search is naturally comparable across scalar, bit-parallel, SIMD, GPU, and FPGA implementations;
- FASTA/FASTQ streams provide large realistic inputs;
- many-pattern sequence classification exercises different machinery from one-pattern grep.

[Biostrings](https://bioconductor.org/packages/Biostrings/) is useful as a mature biological-string reference surface.

[Bioawk](https://github.com/isomorphisms/bioawk) is useful because it combines streaming biological records with ordinary text-processing control flow.

This gives the hardware work a serious workload rather than a synthetic benchmark invented only to flatter the accelerator.

## grep, ag, find, and filesystem search

Text search is another natural test surface.

`grep` asks about byte or character streams.

Tools such as `ag` add recursive directory traversal, ignore rules, candidate selection, and faster literal/regex search.

Filesystem search adds a second problem: deciding **which objects should be inspected at all**.

Those stages should remain distinguishable:

```text
walk namespace
    → prune candidates
    → read bytes / metadata
    → match
    → rank or materialize results
```

Accelerating the matcher does not automatically accelerate directory walking.

Conversely, a better index can avoid scanning enough data that the matcher stops being the dominant cost.

That reaches into storage design itself: [My filesystem, my way](my-filesystem-my-way.md) allows an application to choose an index and allocation layout around the access pattern instead of assuming one general filesystem organization is always the right one.

## DOM walking is one workload, not the whole idea

[iBrowser](https://github.com/isomorphisms/ib) provides several useful workloads:

- exact fragment search;
- selector-like predicates;
- tag and attribute classification;
- tokenization;
- parent / child / sibling traversal;
- early exit;
- and repeated queries over materialized or flattened document structures.

A literal pointer-chasing DOM may remain CPU-shaped.

A flattened or indexed representation can expose batches that are much friendlier to word-parallel, SIMD, GPU, or FPGA execution.

The important design rule is not “put the DOM on an FPGA.”

It is “do not confuse the current representation with the meaning of the query.”

## Parsing and dispatch belong in the same notebook

The same control-flow question appears in:

- HTML/XML tokenizers;
- parsers;
- compiler token and operator dispatch;
- Unicode classification;
- protocol state machines;
- routing and filter rules;
- finite UI state;
- and other code usually expressed as nested conditionals.

On ARM/Thumb, the good lowering may be ordinary branches, conditional instructions, or table branches.

On a wide CPU it may be masks and table lookups.

On a GPU it may be predicates, ballots, or compacted batches.

On an FPGA the state machine may literally be spatial.

The semantic program should not be rewritten from scratch for each answer.

## Sorting is adjacent, not identical

Sorting is not grep.

But it uses related compare/select primitives and exposes the same architecture question.

Sorting networks, partition-based algorithms, radix methods, merge machinery, SIMD compare/exchange operations, GPU sorting, and spatial hardware all move the control/data boundary differently.

That makes sorting another useful workload for the larger question:

> which operations are we expressing as sequential control merely because that is how the current machine model was presented to us?

## Be precise about “speedup”

There is no defensible blanket statement that “FPGA gives a polynomial speedup.”

Several different gains can be mixed together:

1. **Algorithmic improvement.**  
   A different algorithm can change the number of operations as input or pattern size grows.

2. **Bit or vector parallelism.**  
   One machine operation can advance many logical states at once.

3. **Spatial parallelism.**  
   Hardware can instantiate many comparators or automaton states simultaneously.

4. **Throughput from pipelining.**  
   After a pipeline fills, it may accept new data every cycle even when the latency of one item is longer.

5. **Data-movement reduction.**  
   Moving a matcher near the data can matter as much as arithmetic.

6. **Energy efficiency.**  
   A specialized engine can be valuable even when wall-clock asymptotics are unchanged.

With a fixed hardware width, a very large FPGA throughput gain can still be a constant-factor asymptotic improvement with respect to input length.

A genuine complexity-class or polynomial improvement has to come from the algorithm/model comparison, not from saying “FPGA.”

The project should therefore record what kind of gain is being claimed.

## Preserve the operation through the compiler

This is why the compiler work matters.

[Idriç issue #21](https://github.com/isomorphisms/Idric/issues/21) tracks preserving fixed-string-search semantics through the intermediate representation instead of lowering immediately to a branch loop.

[idric-arm-thumb issue #10](https://github.com/isomorphisms/idric-arm-thumb/issues/10) is one concrete packed-bit lowering experiment.

That architecture can generalize:

```text
readable source operation
    ↓
semantic search / classify / select representation
    ↓
target-specific lowering
    ├── scalar CPU
    ├── Thumb
    ├── SIMD
    ├── GPU
    └── FPGA
```

This is more interesting than hand-writing one fast grep.

It lets the same semantic operation become a test of several machine models.

## A concrete experimental ladder

A useful order is:

1. fixed-string byte matcher with a boring scalar oracle;
2. stable fixtures including no-match, overlap, boundary, and Unicode-byte cases;
3. word-level Shift-And/Shift-Or lowering;
4. SIMD/SWAR version where the target makes it natural;
5. FPGA fixed-string pipeline with match-position output;
6. multiple patterns and automaton state;
7. biological sequence fixtures;
8. iBrowser exact-fragment and flattened-predicate fixtures;
9. parser/tokenizer fixtures;
10. compare throughput, latency, memory traffic, package/code size, energy where measurable, and implementation complexity.

The long-term question is larger than grep:

**how much sequential control flow is essential, and how much is merely one representation of matching, selection, and state?**
