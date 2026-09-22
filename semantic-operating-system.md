# Semantic operating system

Unix gave us a small collection of durable ideas: files, directories, streams, processes, pipes, permissions, and ordinary tools that compose.

Those ideas are good.

They do not have to be the last ideas.

A semantic operating system asks:

> if some part of ordinary computing has been annoying for decades, what would we build if we were allowed to fix it now?

The goal is not to discard working Unix machinery for novelty.

The goal is to stop treating historical accidents as laws of nature.

## Start with meaning

A conventional command line often asks the user to remember syntax such as:

~~~text
-x
-X
--foo
--no-foo
--foo=bar
-fbar
~~~

The program may know that one argument is a destination, another is a time range, another is destructive, another chooses a representation, and another names an exception.

The shell mostly sees strings.

A semantic interface can preserve more of the roles:

~~~text
copy source to destination
search history from yesterday
render image using backend
delete files except protected files
~~~

The final syntax is not the important part.

The important part is that completion, validation, history, help, agents, and other programs can work with the **meaning** of an operation rather than rediscovering it from token positions and ad hoc flags.

## Command-line flags can be redesigned

Short flags were rational under older terminal, memory, and documentation constraints.

They are not sacred.

A modern shell can still support concise expert interaction while exposing:

- semantic argument roles;
- units;
- defaults;
- mutually exclusive choices;
- required relationships;
- destructive effects;
- accepted representations;
- and reusable completion information.

Every command should not have to independently reinvent an option parser, usage string, validation scheme, completion grammar, and machine-readable interface.

Some of that structure belongs in the language or operating environment.

[Grease](https://github.com/isomorphisms/grease) and the later `ish`/Odriç direction are places to test that.

## Index the hell out of things

[IB](https://github.com/isomorphisms/ib) already describes multiply indexing the same objects as a **semantic operating-system experiment**.

One durable object can participate in many rebuildable views:

~~~text
canonical object
    ├── by source
    ├── by destination
    ├── by relation
    ├── by document order
    ├── by strand
    ├── by topic
    ├── by task
    ├── by person
    ├── by time
    ├── by recency
    └── by learned category
~~~

There does not need to be one privileged hierarchy.

An object can be in several useful places without being copied several times.

Indexes are allowed to duplicate relationships because they optimize different questions.

## Filesystem views can become semantic views

Directories, filenames, and symlinks are already primitive indexes.

That makes them a good experimental surface.

A link can say:

~~~text
this object belongs in this view
~~~

without moving or duplicating the canonical object.

Forward and reverse indexes can answer different questions.

A strand can compile a graph traversal into a sequential object.

A category can overlap another category rather than forcing everything into one tree.

If the same patterns recur often enough, they become evidence for better operating-system primitives:

- typed links;
- reverse-link queries;
- stable object identity;
- indexed directories;
- graph-aware lookup;
- fast materialization of traversals;
- semantic completion.

## Hyperplanes and rotations can organize information too

The rotation/hyperplane work is not limited to sensor geometry.

In an embedding space, a category can have a decision surface.

A document, tab, image, command, or other object may lie on the positive side of several category hyperplanes at once.

That gives overlapping organization rather than one forced taxonomy.

Rotations or other orthogonal transforms can sometimes change coordinate systems while preserving important geometric relations.

The critical requirement is to keep the geometry honest:

- raw vectors are not automatically normalized sphere points;
- a separating hyperplane has scale and sign conventions;
- a classifier margin is not automatically a probability;
- a coordinate rotation is not automatically a semantic transformation.

Used carefully, this geometry gives the semantic system another indexing surface.

## Human corrections should become durable structure

If an agent proposes that something belongs to a category, that is a proposal.

If the human corrects it, that correction should not vanish after the current session.

IB's design treats corrections as durable events and model outputs as inspectable proposals rather than canonical truth.

That suggests a wider operating-system principle:

**interaction should leave useful semantic residue.**

When the user repeatedly says what something means, where it belongs, what should happen next, or which distinction matters, the system should become better organized rather than forcing the same correction forever.

## Search should not be one box

Once objects have stable identity and many relations, search can mean many things:

- text match;
- vector similarity;
- category membership;
- incoming links;
- outgoing links;
- recent activity;
- task context;
- source;
- destination;
- path through a graph;
- nearby objects after a correction;
- objects separated by a learned boundary.

Those mechanisms can coexist.

The system should expose which one produced an answer.

## The operating system can know more than bytes and paths

Low-level primitives still matter.

Bytes, files, processes, memory, devices, sockets, and permissions do not disappear.

The semantic layer should sit above them without lying about them.

The larger goal is the same as in Idriç:

~~~text
high-level meaning
    ↕
inspectable transformations
    ↕
low-level mechanism
~~~

The operating environment should help preserve the connection.

## Fix accumulated annoyances

This is also permission to revisit familiar irritations.

Command flags.

File organization.

Search.

History.

Completion.

Copy and paste.

Persistent tasks.

Tab recovery.

Naming.

Repeated context reconstruction.

Software has accumulated decades of conventions whose original constraints may no longer apply.

Not every old design is bad.

But "this is how Unix did it" or "this is how shells have always parsed flags" is evidence about compatibility, not a proof of optimality.

Keep what works.

Fix what does not.
