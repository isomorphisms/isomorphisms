# Reliable vibe coding

AI makes it cheap to produce code.

That does not make it cheap to produce **correct software**.

The weak point in AI-assisted programming is often not code generation. It is everything around generation:

- knowing which checkout is real;
- knowing which artifact was actually built;
- knowing which target actually ran it;
- knowing whether a test proves the claim we care about;
- knowing whether a failure is mechanical, semantic, environmental, or genuinely human-only;
- and knowing when a pull request is actually ready to merge.

Several projects attack different parts of that problem.

## ai-ci: prove the claim, not just "CI is green"

[ai-ci](https://github.com/isomorphisms/ai-ci) is a shared contract-test system for AI-authored project work.

Its core rule is stronger than ordinary green CI:

> a check should demonstrate the promised result, and it should also demonstrate that it rejects a deliberately broken version of that result.

That second half matters.

A test that only passes the good case may itself be meaningless.

So ai-ci keeps known-bad fixtures for the properties it claims to verify.

It also treats evidence classes separately:

~~~text
source exists
    ≠
build succeeded
    ≠
artifact packaged
    ≠
artifact executed
    ≠
artifact executed on the claimed target
~~~

An emulator result does not become physical-phone evidence.

A fallback compiler does not become evidence for the intended backend.

A generated artifact is not automatically the exact artifact later consumed.

Those distinctions are boring until an agent starts moving quickly enough to blur them.

Then they become essential.

## Exact-head PR evidence

A particularly important ai-ci direction is pull-request merge evidence.

A merge decision should be bound to the exact PR head being considered, not vaguely to "a recent green run."

That means retaining things such as:

- repository and PR identity;
- exact head;
- live base;
- changed paths;
- checks;
- dependency revisions;
- artifacts;
- target/evidence class;
- blockers;
- and whether the evidence actually consumed the artifact it claims to validate.

The goal is to make the question

~~~text
can this merge?
~~~

answerable from durable evidence instead of an agent's impression that everything looked fine.

## Cat Food: know what machine and artifact you actually have

[Cat Food](https://github.com/isomorphisms/catfood) attacks another recurring failure of AI programming systems: they lose track of the physical environment.

An agent should not repeatedly guess:

~~~text
maybe the repo is in ~/project
maybe the compiler is installed
maybe this binary came from that branch
maybe the phone has a source checkout
maybe we should rebuild everything
~~~

Cat Food keeps an explicit tool inventory and target model.

Cloud/container machines are workbenches.

The ARMv7 phone and AArch64 tablet are runtime targets.

The phone does not suddenly become a source-build workstation merely because an agent needs a test.

For Android delivery, the intended path is:

~~~text
build elsewhere
    → publish exact package
    → download
    → verify hash and provenance
    → install
    → run
    → retain the evidence actually observed
~~~

Cat Food also records where known checkouts live instead of scanning arbitrary storage and guessing from directory names.

That sounds mundane.

It prevents a remarkable amount of wasted AI work.

## The factory needs physical reality

This is part of the app factory.

A software factory cannot just know source code.

It has to know:

- what tools exist;
- where they are;
- which target they belong to;
- what was built;
- from which source;
- where the artifact went;
- whether it installed;
- whether it ran;
- and what evidence class the result belongs to.

Otherwise the AI system spends computation reconstructing its own workshop every time it starts a task.

Cat Food is the workshop inventory.

ai-ci is the inspection station.

## Cockswain: decide what happens next

[Cockswain](https://github.com/isomorphisms/cockswain) works one level above the deterministic evidence.

Its job is to supervise ongoing AI-assisted work and choose one next state:

~~~text
CONTINUE
WAIT
HUMAN
DONE
~~~

The important asymmetry is deliberate.

False `DONE` is the worst error.

False `HUMAN` is also expensive because it interrupts the user for something the system could have handled itself.

A supervisor should therefore distinguish:

- useful mechanical work remains;
- an external check is still genuinely in flight;
- a human-only choice is required;
- the goal appears satisfied and is ready for independent completion verification.

This is a better abstraction than an agent repeatedly asking:

> should I keep going?

## Separate mechanical truth from judgment

The intended relationship among these systems is roughly:

~~~text
Cat Food
    → what environment, checkout, package, and target are real?

ai-ci
    → what objective evidence exists, and what blockers remain?

Cockswain
    → given that evidence and the task context, what is the correct next action?
~~~

Cockswain should not reinvent GitHub checks.

ai-ci should not pretend to understand every human intention.

Cat Food should not decide whether a mathematical argument is good.

The systems are more reliable when each owns a smaller kind of truth.

## Human authorization is data too

Merging introduces one extra problem.

A PR can be technically perfect and still not be authorized to merge.

Conversely, a user may already have given clear authority and should not need to repeat the instruction after every green check.

The current ai-ci/Cockswain work therefore treats merge authority as something that can be recorded and checked.

The important distinction is between:

~~~text
the PR is mechanically ready
~~~

and

~~~text
the human authorized this merge
~~~

Both matter.

Neither should be hallucinated from the other.

## Vibe coding needs hostile tests

The optimistic AI workflow is:

~~~text
ask for feature
    → model writes code
    → tests pass
    → merge
~~~

The more realistic workflow needs adversarial boundaries:

~~~text
ask for feature
    → recover actual project context
    → edit exact source
    → build exact artifact
    → run targeted positive test
    → run a known-bad or hostile case
    → inspect target-specific evidence
    → classify remaining blockers
    → merge exact head
~~~

That costs more per attempted change.

It can cost much less per **accepted correct change**.

## "Green" should mean something specific

One theme across all three projects is refusing to let vague success labels accumulate.

Useful states are explicit:

- PASS;
- FAIL;
- UNKNOWN;
- NOT_VERIFIED;
- CANCELLED;
- SKIPPED;
- BLOCKED;
- READY.

A skipped physical-device test is not a pass.

Missing evidence is not necessarily proof of product failure.

A cancelled model-evaluation lane does not erase evidence from another lane that completed.

A green package build does not prove runtime behavior.

The system becomes more trustworthy when these distinctions survive automation.

## The point is not bureaucracy

It would be easy to reproduce the worst parts of corporate CI: huge pipelines, endless gates, and ritual checklists that everybody ignores.

That is not the goal.

The goal is the opposite:

**make routine AI work automatic enough that humans only see the genuinely interesting failures.**

If a PR is mechanically clean, correctly tested, within authorized scope, and has the required evidence, the system should be able to say so clearly.

If one thing is wrong, it should name that thing.

If a physical test is required, it should ask for the physical test.

If the user has to decide a real product question, it should ask the user.

Everything else should continue.

## The larger factory loop

The full loop begins to look like:

~~~text
human goal
    → agent edits source
    → Cat Food resolves the real environment
    → build produces a bound artifact
    → ai-ci verifies the claimed behavior and evidence
    → Cockswain chooses CONTINUE / WAIT / HUMAN / DONE
    → exact-head merge decision
    → receipts become evidence for the next job
~~~

That is much closer to an actual software factory than "prompt until the code looks right."

The point of these projects is to let the AI move quickly **without requiring the human to trust vibes**.
