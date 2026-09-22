# Trying not to melt the polar ice caps

AI changes the cost of bad programs.

A confusing program used to waste mostly human time. Now it can also waste repeated model inference, builds, test runs, CI, retries, review, and deployment work. If a language model misunderstands the source, implements the wrong feature, or cannot tell whether a change actually satisfies the request, the whole loop may run again.

So one reason to build a more inspectable programming language is simply to reduce the amount of computation required to get a correct result.

~~~text
clearer program
    → easier inspection
    → fewer misunderstandings
    → fewer wrong changes
    → fewer retries
    → less computation per accepted result
~~~

That has both economic and environmental consequences.

## Make programs easier for language models to inspect

Today's language models can work with ordinary source code, but they still have to infer a great deal that the source does not state clearly.

Names may be misleading. Important invariants may exist only in a programmer's head. One conceptual operation may be spread across layers of boilerplate. A simple request may require reconstructing a build system, framework conventions, hidden state, generated code, and a large dependency graph before the actual behavior becomes visible.

A language designed for human inspectability can also be designed for machine inspectability.

The Idriç work therefore has an AI-facing consequence even though that is not its only purpose:

- make semantic roles explicit;
- give important transformations names;
- expose mathematical structure rather than flattening it into arithmetic;
- keep target and representation boundaries visible;
- make unsupported behavior fail clearly;
- make tests and invariants correspond to the concepts visible in the source;
- and use the RHS work to investigate whether what a program says agrees with what it actually does.

The goal is not to write code *for* a language model. Humans and models benefit from many of the same things: explicit structure, meaningful names, small semantic steps, visible boundaries, and behavior that can be checked against the claims made by the source.

## Correctness can save more than a small optimization

There are at least two different efficiency projects here.

One is ordinary computational efficiency:

~~~text
smaller programs
fewer dependencies
less memory
less data movement
faster execution
less build machinery
~~~

Those savings matter. A program that performs the same job with 2% less computation has, to first order, reduced the computation required for that job by 2%. A much smaller executable can also reduce storage, transfer, loading, memory pressure, and surrounding machinery.

The other project may have a larger effect in AI-assisted development: **reduce wasted iterations.**

A wrong feature is not just a few inefficient instructions. It may cause another model call, another patch, another build, another test suite, another CI run, another review, and perhaps another deployment attempt.

The same is true when a model cannot inspect an existing program well enough to know what must change.

So the important quantity is not merely instructions per second. It is something closer to:

~~~text
total computation required
--------------------------
one accepted useful result
~~~

Improving the numerator locally matters. Avoiding an unnecessary repetition of the entire process can matter more.

This is one reason correctness, testability, inspectability, and semantic honesty belong in the same conversation as performance.

## Programs that say what they do are cheaper to verify

The [RHS](https://github.com/isomorphisms/rhs) work asks whether human-facing claims about a program correspond to observable behavior.

That matters for AI systems because a model should not have to trust a plausible function name or a convincing comment.

If important claims can be checked against behavior, fixtures, invariants, or independently stated transformations, an automated system has a better chance of distinguishing:

~~~text
looks plausible
~~~

from

~~~text
there is evidence that this does what it says
~~~

That can make the development loop more reliable and reduce the number of expensive attempts required to reach the state the user actually wanted.

## Smaller and faster still matter

The direct backend work attacks another source of waste: unnecessary layers between the program and the machine.

If a program can go directly from a checked representation to machine code, DEX, WebAssembly, or a GPU target, it may not need a generated intermediate language, a second compiler, a large runtime, a general framework, or libraries that provide far more machinery than the program uses.

Likewise, better representations can reduce the amount of data that needs to be stored, moved, decoded, or processed.

These are mostly direct efficiency gains. They may be smaller than eliminating whole failed iterations, but they repeat every time the program is built, moved, loaded, or run.

There is no reason to choose between the two:

~~~text
need fewer attempts to get the right program
                    +
need less computation to run that program
~~~

Both reduce computation per useful result.

## This does not automatically mean lower total electricity use

Efficiency at one level does not guarantee lower consumption for the whole system.

This is the point behind the **Jevons paradox** and related rebound effects: making a resource cheaper or more efficient to use can increase demand enough that total consumption stays flat or even rises.

That problem can apply to AI. If inference becomes dramatically cheaper, people may simply perform much more inference. If software becomes cheaper to produce, more software may be produced.

So this project should not claim that a faster compiler, a smaller binary, or fewer model turns automatically lowers the total electricity consumption of the world's data centers.

The narrower claim is still important:

**for a given useful result, do less unnecessary computation.**

Whether society spends the savings or uses them to reduce total consumption is a larger economic and political question.

But efficiency is still a real first-order improvement. Wasting less electricity, hardware time, network traffic, storage, and human attention per successful result is preferable to wasting more of them for the same result.

The International Energy Agency's work on [energy and AI](https://www.iea.org/reports/energy-and-ai) documents rapidly growing data-center electricity demand and substantial uncertainty about future demand. That makes computation-per-useful-result a material engineering concern, even though it is not by itself a complete climate policy.

## The engineering target

The target is not merely a fast programming language.

It is a development system in which:

- the program is easier to understand;
- the program's claims are easier to check;
- a language model is less likely to misunderstand the existing state;
- wrong changes are discovered earlier;
- fewer iterations are needed to obtain the requested behavior;
- the resulting program contains less unnecessary machinery;
- and the machine performs less work to deliver the useful result.

That is simultaneously a correctness problem, a language-design problem, a cloud-cost problem, and an energy problem.

If AI is going to write and maintain a growing fraction of software, then making software easier for AI to inspect may be one of the more important forms of optimization.
