# Making programming languages do what they say they do

Most programming languages do not care whether a program's words are true.

A function called `normalize_direction` can return an unnormalized direction. A function called `safe_write` can do something unsafe. The compiler normally treats those names as arbitrary labels.

That creates a basic problem for human inspection: the source can look meaningful without the meaning having much authority over the behavior.

The [RHS](https://github.com/isomorphisms/rhs) project is an attempt to tighten that relationship.

The first step is empirical rather than magical. Give a program a human-facing claim, observe what the program actually does, and compare the two against an independently defined expectation.

For example:

```text
what the source says
        ↓
what behavior would make that statement true
        ↓
what the program actually does
        ↓
agreement, disagreement, or insufficient evidence
```

RHS currently uses controlled examples where the intended meaning can be established independently. It includes ordinary positive controls and adversarial examples where names or apparent purpose are misleading. That matters because a system that merely agrees with plausible-looking source code is not checking meaning.

This is different from ordinary testing.

A unit test usually asks whether a selected input produced an expected output. RHS asks an additional question: **does the human-facing description of the operation correspond to its observed behavior?**

It is also different from a proof system. A model score or classifier judgment is evidence about that classifier, not proof that the program is correct. The immediate goal is to build measurable semantic checks with known ground truth.

The longer-term language-design question is more ambitious.

Can names, semantic roles, equations, invariants, and domain descriptions participate in checking the implementation instead of existing only for the reader?

Not every English sentence can or should become a theorem. The goal is not to pretend that informal language has suddenly become perfectly formal. The goal is to move useful statements from “comment with no authority” toward “claim that the system can test, constrain, or require evidence for.”

That connects RHS directly to Idriç and the other language experiments. Readable source is valuable, but readable source becomes much more valuable when there is increased confidence that what it appears to say is actually related to what executes.

The eventual target is not merely code that looks good.

It is code whose visible meaning has consequences.
