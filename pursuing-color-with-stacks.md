# Pursuing color with stacks

This is a research sketch, not a result.

More than fifteen years ago I had a vague feeling that ideas from topology ought to say something interesting about paintings, novels, color, and other things where the identity of an object depends partly on how it sits inside a larger structure.

At the time I did not have the right mathematical language for the thought.

I am still not claiming that I have it now.

But stacks feel much closer to the kind of abstraction I was looking for.

## Why stacks feel worth learning

Mathematics is full of machinery.

Once you understand that mathematicians can invent new objects and new structures whenever the old ones are inadequate, the next question is not whether more mathematics can be invented.

Of course it can.

The question is:

**Which machinery is worth carrying around?**

Terry Gannon's *Moonshine Beyond the Monster* has a wonderful recurring attitude toward mathematics as a sandbox full of structures worth playing with. The point is not generalization for its own sake. The interesting generalizations are the ones that reveal something.

I remember Frank Adams's *Infinite Loop Spaces* in a similar spirit. Spectral sequences and the surrounding machinery are a lot to learn. The bargain is that the machinery eventually earns its cost.

That is how stacks currently feel to me.

They are difficult enough that I would not want to learn them merely because they exist.

But they appear to solve a problem that comes up everywhere:

~~~text
we want to identify things
without destroying the structure of how they are identified
~~~

That seems unusually valuable.

## The stack of triangles

A particularly persuasive entrance is the stack of triangles.

Kai Behrend's *Introduction to Algebraic Stacks* uses triangles as an elementary example: triangles vary in families, some triangles have more symmetry than others, and a coarse moduli space loses information exactly where those symmetries become important.

Behrend repeats the reputed remark of Michael Artin that understanding the stack of triangles is enough to understand a great deal about stacks.

There is also newer work on the same theme, including Eric Brussel, Madeleine Goertz, Elijah Guptill, and Kelly Lyle's *The Stack of Triangles up to Similarity*.

The attraction of the example is that the stack is not being introduced to make an elementary object sound sophisticated.

The elementary object exposes the need for the abstraction.

A scalene triangle, an isosceles triangle, and an equilateral triangle do not merely occupy different points in a parameter space. Their symmetry changes. If we quotient too aggressively, the most interesting points are exactly where the quotient becomes badly behaved.

Stacks keep more of that information alive.

That is the feature I care about.

## Pursuing Josef Albers

[Albers](https://github.com/walnut-burgundy/albers) is the concrete place where I want to see whether this instinct goes anywhere.

Josef Albers spent a career demonstrating that a color is not exhausted by an isolated numerical specification.

The same physical color can look different in different surroundings.

Different physical colors can be made to look surprisingly alike.

Boundaries, neighborhoods, ordering, contrast, repetition, and presentation matter.

A computer naturally wants to turn a color into something like:

~~~text
(r, g, b)
~~~

or a point in another color space.

That is useful, but it encourages us to think of the point as the thing.

Albers keeps reminding us that the presentation is part of the phenomenon.

Stacks suggest a different kind of question.

Instead of asking only:

~~~text
what point represents this color?
~~~

ask:

~~~text
what are the presentations?
what transformations relate them?
which presentations should count as equivalent?
what symmetries or stabilizers occur?
what information survives a change of context?
what changes only because the presentation changed?
how do these objects vary in families?
~~~

I do not yet know the right objects, morphisms, topology, or notion of equivalence.

That is the project.

It may turn out that stacks are exactly the right language.

It may turn out that only a small piece of stacky thinking is useful.

It may turn out that the analogy breaks.

The point is to find out.

## An old idea that is newly cheap to pursue

Fifteen or twenty years ago this kind of idea was easy to lose.

To pursue it seriously I would have needed to sustain attention across several difficult areas of mathematics, learn a large body of machinery, find the relevant literature, work out examples, write code, and probably spend years discovering that some part of the idea had already been formulated better by somebody else.

For an unpaid side project, that is a severe filter.

Maybe after several decades of continued mathematical work I would eventually have produced an interesting paper.

Maybe not.

AI changes the cost structure.

It can help search terminology, locate references, translate between mathematical dialects, construct small examples, write exploratory programs, check calculations, and preserve the trail of an idea while I move on to something else.

That does not make the mathematics automatic.

It makes a speculative idea cheaper to keep alive long enough to discover whether it contains anything.

That is enough.

## The project can sit still

This does not need to become an active program of research right now.

It is allowed to remain a rough sketch.

The useful state may simply be:

- preserve the Albers experiments;
- preserve the stack intuition;
- collect examples where ordinary quotienting loses something important;
- keep notes on moduli, symmetry, groupoids, deformation, and context;
- occasionally build one executable example;
- and wait to see whether a coherent mathematical object begins to emerge.

There is no need to manufacture progress for the sake of having a project.

The hypothesis can sit on the shelf.

## Maybe there is a computer-science problem here too

There is a second, even more speculative direction.

Computer science also throws away structure very aggressively.

Programs are normalized.

Representations are lowered.

Equivalent states are collapsed.

Intermediate explanations disappear.

A compiler preserves the output and discards the path that made the output intelligible.

A build system decides two artifacts are interchangeable without necessarily preserving the meaningful relationship between them.

An AI coding system repeatedly reconstructs context that earlier stages already knew.

Perhaps some of these problems have a stack-like formulation.

That does **not** mean "rewrite computer science using algebraic stacks."

It means asking the same question that made stacks useful elsewhere:

**Are we quotienting too early?**

Could a program representation preserve:

- multiple presentations of the same object;
- explicit witnesses relating them;
- symmetries and automorphisms;
- local descriptions;
- provenance;
- controlled deformations;
- and paths through transformations?

Would that make programs easier to inspect?

Would it make equivalence more meaningful than either textual equality or "the tests happened to pass"?

Would an agent need to reconstruct less hidden context?

Could a compiler simplify more safely because it knows which transformations justify the simplification?

I do not know.

## Why the computer-science speculation matters

If richer structure makes software easier for humans and agents to understand, it may connect back to the cost of AI-assisted computing.

A system that preserves why two states correspond may require fewer attempts to rediscover that relationship.

A system that preserves semantic transformations may make fewer wrong edits.

A system that carries provenance may make verification cheaper.

If those effects are real, they could reduce the amount of computation required to get from a request to an accepted result.

That would connect this speculative mathematics to the same concern described in [Trying not to melt the polar ice caps](trying-not-to-melt-the-polar-ice-caps.md): reducing computation per useful result.

But this is several hypotheses downstream from anything established.

It belongs here as a reason to keep looking, not as a claim of an optimization already achieved.

## The standard

The standard for this project is not:

> stacks are deep mathematics, therefore applying them must be interesting.

The standard is:

> stacks appear to preserve structure that simpler quotients destroy; find a concrete case where preserving that structure actually teaches us something.

Color is the first place I want to look.

Computer science may be another.

For now, both are sketches.

That is fine.
