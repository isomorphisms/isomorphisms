# iBrowser, Pensieve, Grease, and the semantic operating system

Unix gave us a small collection of durable ideas: files, directories, streams, processes, pipes, permissions, and ordinary tools that compose.

Those ideas are good.

They do not have to be the last ideas.

A semantic operating system asks:

> if some part of ordinary computing has been annoying for decades, what would we build if we were allowed to fix it now?

The goal is not to discard working Unix machinery for novelty.

The goal is to stop treating historical accidents as laws of nature.

## iBrowser is not a DOM-optimization project

Making DOM walking faster is useful.

Adding command-line hooks is useful.

Pensieve, persistent tabs, renderer recovery, semantic search, agent hooks, filesystem experiments, and better shell interfaces are useful too.

None of those is the whole project.

The larger iBrowser idea is to re-architect the environment so that state and operations stop being trapped inside unrelated application silos.

A useful sketch is:

```text
durable objects and events
    ↓
typed relationships and stable identities
    ↓
many rebuildable indexes and materialized views
    ↓
meaningful operations
    ├── phone UI
    ├── renderer
    ├── shell
    ├── agent
    ├── automation
    └── inspector
```

The renderer is a view onto durable state, not the owner of the state.

A tab is a navigation thread, not a process.

Search is not one box; it is a family of indexes and traversals over the same objects.

The shell is not merely a launcher; it is another semantic interface.

An agent is not a screen scraper; it is another client of the same operations.

DOM walking therefore matters twice: it is useful work in its own right, and it is a concrete workload for testing whether a better representation or machine lowering can make common semantic operations cheaper. It should not define the architecture.

## Mine good system designs instead of inheriting one system

The early Unix name worth keeping in this conversation is **Doug McIlroy**.

The useful inheritance is not a frozen 1970s interface. It is the habit of composing small understandable mechanisms into larger work. The Unix retrospective describes pipes as a major change in how utility programs were conceived, precisely because existing programs could be interconnected into new computations.

Other systems are worth mining for different reasons:

- **Plan 9** — per-process namespaces and 9P show how resources can be rearranged and presented through a uniform interface without requiring one global filesystem view.
- **BeOS / BFS** — file attributes, indexes, and queries show how filesystem objects can participate in database-like lookup without abandoning ordinary files.
- **Smalltalk** — persistent live objects and pervasive inspection are useful reference points for an environment where program state is meant to be understood and manipulated.
- **Oberon** — a compact integrated language/system is a useful counterexample to the assumption that a modern environment must be assembled from enormous independent stacks.
- **Lisp-machine environments** — interactive inspection, incremental development, and programmable system surfaces are useful references for making the environment itself malleable.

Primary historical references for the first three:

- [The UNIX Time-sharing System — A Retrospective](https://www.bell-labs.com/usr/dmr/www/retro.pdf)
- [Plan 9 from Bell Labs — Overview](https://9p.io/plan9/about.html)
- [Practical File System Design: The Be File System](https://www.haiku-os.org/legacy-docs/practical-file-system-design.pdf)

The point is not to clone any of them.

With cheap automated code reading and experimentation, obscure operating systems, papers, books, abandoned interfaces, and old implementation tricks can all be treated as an architectural corpus. Good mechanisms can be tested against the current semantic model instead of being accepted or rejected because of their age.


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

## A browser should not have separate bookmark and history silos

[IB](https://github.com/isomorphisms/ib) starts from the idea that the browser should own **durable browsing state**, not a collection of renderer tabs plus two side databases called bookmarks and history.

A resource, tab, visit, task, assertion, and saved representation are different objects.

A tab is a durable navigation thread, not a renderer process.

A visit is an append-only event.

A task can span many tabs, searches, resources, and actions and survive after every renderer has died.

In that model, a traditional bookmark is not a special species of browser data. It is a durable assertion, pin, relationship, or membership attached to an object that already has an identity.

Likewise, "history" should not mean a disposable reverse-chronological URL list owned by a browser UI. Visits, searches, redirects, duplicate-tab actions, corrections, and handoffs are durable events that can be indexed in many useful ways.

So the browser does not lose memory when a tab closes, and it does not need a special bookmark silo to remember that something matters.

## The browser should have hooks, not just buttons

The browser should expose the same meaningful operations to several frontends:

~~~text
phone UI
command line
agent
inspector
automation
~~~

A chat agent should be able to ask the browser core things such as:

- what task is this tab part of?
- what has already been fetched?
- what points to this fragment?
- what was I doing when I opened this?
- show the unread continuation of this investigation;
- preserve this page and its source identity;
- propose a category without silently changing accepted state;
- open or wake a renderer only when interaction is actually required.

Those should be browser operations, not screen-scraping tricks.

The agent is another client of durable browser state.

It should not need to reverse-engineer the browser's interface every time it wants to help.

## Pensieve is the indexing surface

The useful separation is between durable content and the structures used to find and relate it.

Pensieve is the link/index side of that idea: stable fragment identities, typed relationships, forward and reverse indexes, categories, recency, tasks, and ordered **strands** that sew useful pieces together without copying the underlying content into every view.

The same object may therefore be reachable by source, destination, task, subject, person, time, relationship, or learned category.

A strand can materialize one useful traversal for sequential reading while the underlying graph remains available for other traversals.

This is why the browser and the semantic operating system are the same architectural conversation.

## Persistent chat belongs in the same world

[iGPT](https://github.com/isomorphisms/iGPT) applies the same local-first rule to model conversations.

Its first command surface already includes:

~~~text
new
list
append
send
show
pending
sync
~~~

The important ordering is local first:

~~~text
user event
    → durable local record
    → local outbox
    → remote submission
~~~

Already-seen conversation text should be available without reloading remote history.

Remote API state is synchronization state, not the only copy of the conversation.

That makes persistent agent threads another ordinary durable object that can be indexed, searched, resumed, and connected to tasks rather than a transient window owned by one application process.

## Expose operating-system actions directly enough to be useful

"Kernel functions" is slightly too low-level for the current good boundary.

Grease presently exposes readable native actions such as:

~~~text
mmap      munmap      mprotect      msync
openat    fallocate   close
linkat    symlinkat   unlinkat
~~~

through the existing native runtime, which reaches libc/Bionic and then the kernel.

The language surface uses named flags and opaque mappings/file descriptors instead of raw syscall numbers and arbitrary pointers.

That is the direction I want:

~~~text
meaningful shell action
    → explicit native boundary
    → ordinary libc / Bionic
    → kernel
~~~

A shell should be able to reach serious operating-system facilities without turning every program into C or exposing a bag of untyped integers.

The same applies to files, mappings, links, preallocation, process creation, networking, and other low-level facilities as the vocabulary grows.

## Android storage is a real systems problem

Android often presents shared storage through a mediated filesystem view rather than the lower filesystem directly.

That means the pathname an application sees and the filesystem that ultimately stores the bytes are not always the same operational surface.

The practical lesson is not "ignore Android security."

It is:

**do not let one mediated filesystem interface define the architecture.**

That is also the point of [My filesystem, my way](my-filesystem-my-way.md): different applications should be allowed to use different storage layouts and allocation structures when their workloads call for them.

Where permissions and deployment context allow it, the system should be able to use different storage backends and lower-level native operations while keeping the higher-level storage semantics unchanged.

The exFAT/FUSE work is useful precisely because it forces us to distinguish:

~~~text
logical file operation
    → Android-visible filesystem interface
    → lower filesystem implementation
    → block allocation / persistence behavior
~~~

If the high-level program knows which guarantee it needs, the implementation can choose the appropriate path instead of assuming that every visible pathname supports every filesystem operation.

## Rewrite the shell too

Grease is the working Oils/YSH-derived experiment.

`ish` is the separate successor direction being co-designed with Odriç.

That distinction matters because the shell itself is part of the factory.

It is not merely a command launcher underneath the interesting programs.

The shell is where we can rethink:

- command argument roles;
- byte/text/path distinctions;
- pipelines;
- redirection;
- completion;
- history;
- process lifetime;
- native OS actions;
- structured results;
- and the boundary between human-readable commands and exact process invocation.

Unix shell behavior is valuable reference material.

It is not the final word on how a shell should express intent.

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

A concrete retrieval stack can be deliberately boring at the first layer:

~~~text
exact identifiers and links
    → BM25 lexical candidates
    → vector-similar candidates
    → category / hyperplane filters
    → task and graph context
    → explicit reason for each result
~~~

BM25 is useful here precisely because it is not a semantic embedding. It ranks documents or fragments by the query words they actually contain, giving more weight to informative terms and discounting terms that are common everywhere. In ordinary user terms, it is a much better version of “find pages containing these words,” not a model that claims to understand the page.

Vector indexing answers a different question: “what else is close in meaning even when it uses different words?” A support-vector-machine-style classifier answers another: “which side of this learned category boundary is this object on?” Neither replaces BM25. They can all point at the same durable object through different indexes.

For someone following a [Pixegami](https://www.youtube.com/@pixegami)-style AI coding tutorial, the interface should not require any of those names. The user should be able to ask something like “find the part where I configured the agent that can edit files” and get useful results. Underneath, one result may have matched the actual words, another may have been semantically similar, and another may belong to the current coding task. The system should preserve those reasons rather than flattening them into one mysterious score.

This becomes especially useful for [contextual find and replace](contextual-find-and-replace.md): retrieval proposes candidate places; exact structure and verification decide what may actually change.

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
