# Contextual find and replace

Ordinary find and replace answers an exact textual question:

> where does this byte or character sequence occur?

That is still useful. It is not enough for many edits people actually mean.

A contextual replacement asks for something closer to:

> find the places where this idea is being used in this role, show me the candidates, and change only the ones that satisfy the intended condition.

Examples:

- replace `vector` when it means a fixed-length container, but do not touch mathematical vectors;
- change an old API only at executable call sites, not inside quoted examples or historical notes;
- replace ASCII `->` with `→` where the parser says it is an operator, not where the same characters occur inside a URL, string, or data file;
- find every place that still describes a tab as a renderer process when the current browser model treats a tab as a durable navigation thread.

The hard part is not generating replacement text. It is deciding which occurrences belong to the requested context.

## Retrieval proposes candidates

The first phase can combine several indexes:

~~~text
user intention
    → exact names / links
    → BM25 lexical retrieval
    → vector similarity
    → learned category boundaries
    → graph and task context
    → candidate spans
~~~

BM25 is the simple lexical layer. It ranks fragments that contain the query words, rewarding informative matches and discounting words that occur almost everywhere. In user terms: it is a ranked, document-aware search for the words you actually typed.

Vector similarity adds candidates that use different wording but mean something nearby.

A support-vector-machine-style classifier or another learned boundary can add a different signal: this fragment looks like a member of a category that previous examples placed on this side of the boundary.

Graph and task context can say that two fragments belong to the same investigation, source, person, repository, or durable browser strand.

These signals should remain distinguishable. A lexical match is not the same fact as a vector-nearest neighbor, and neither is the same as an accepted human category.

## Replacement requires a stricter boundary

Fuzzy retrieval is allowed to be generous.

Mutation should be conservative.

A useful boundary is:

~~~text
retrieval can nominate
verification can authorize
~~~

For source code, authorization may come from a parser, syntax tree, type information, symbol identity, or another exact structural check.

For prose, it may come from an exact selected span plus surrounding context that the user or agent has accepted.

For a repository-wide transformation, the replacement should also have hostile cases. If the rule claims not to modify strings, comments, mathematical vectors, quoted examples, or generated files, keep examples of those cases and prove that they remain unchanged.

## Preview is a first-class result

The useful command is not merely:

~~~text
replace A with B
~~~

It is closer to:

~~~text
find A in this role
show accepted candidates
show excluded near-misses
explain why each candidate was selected
preview the patch
apply the patch
run the verifier
~~~

That makes the search result inspectable before it becomes repository state.

The user-facing interface can stay much simpler than the machinery. A person should be able to say:

> change the old name where it refers to the browser task object, but leave historical quotations alone

and see a small, concrete patch.

## Keep a receipt

A contextual replacement can retain a compact receipt:

~~~text
request
candidate retrieval methods
accepted spans
rejected / protected spans
exact replacement rule
patch
verification command or oracle
PASS / FAIL / UNKNOWN
~~~

That makes later review possible without preserving private model reasoning.

It also lets an agent answer useful questions later:

- Why was this occurrence changed?
- Why was that similar occurrence left alone?
- Was the parser involved or was this a prose-only edit?
- Which test would fail if the contextual rule became too broad?

## Pensieve is a natural home for candidate retrieval

Pensieve already treats durable objects as multiply indexed.

Contextual find and replace can use those same indexes without making any one of them authoritative:

~~~text
canonical object
    ├── lexical index
    ├── vector index
    ├── category boundaries
    ├── incoming / outgoing links
    ├── task membership
    └── recency
~~~

The search system finds likely places.

The editing system proves which place is actually safe to change.

That separation is the important part.
