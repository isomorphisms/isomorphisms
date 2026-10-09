# Controlling AI: mathematical meaning to machine evidence

## The project

I want a language and a work environment that let AI handle more of the detailed implementation without deciding what my program means.

Code generation is not the long-term intellectual goal. The goal is to explore representations that I can understand, question, and change—from geometry and types to instruction selection, memory layout, and a working interface.

A human should be able to say what must remain true. The machine should fill out routine details where that is possible, then show what it actually did.

"AI wrote a program" is not an acceptance criterion.

## There are several different authorities

They should not be merged into one answer:

| Authority | What it can establish |
| --- | --- |
| Mathematical definition | Objects, domains, laws, invariants |
| User's specification | Desired behavior, aesthetic choices, priorities |
| Language specification | Meaning of valid source programs |
| Compiler contract | Meaning and target assumptions of a lowering |
| ABI and hardware manual | Permitted machine interfaces and operations |
| Deterministic test | One stated property over specified cases |
| Proof or independent oracle | A stronger claim, within its hypotheses |
| Real device observation | What the actual built artifact did on that device |
| Benchmark | Performance on an identified machine and workload |

An agent can consult all of these. It cannot promote a prediction into the authority of an observation.

The point is to keep the arrows explicit:

~~~text
mathematics + intended behavior
  → type and representation contracts
  → source and intermediate forms
  → ABI / machine-specific lowering
  → exact built artifact
  → executable checks and observations
  → error, refinement, or revised specification
~~~

A false "done" at one step must not make downstream checks disappear.

## Type systems can expose the missing questions

Consider a screen control that rotates an object. Source code could be made to state:

~~~text
touch event
  → recognized gesture
  → command carrying a change in orientation
  → changed geometric state
  → rendered frame
  → observable response
~~~

A valid pointer handler by itself is not proof of a visible change. Nor is a visible pixel change enough to prove the correct mathematical operation occurred.

It may be necessary to compare a region, frame, or temporal aggregate because a one-pixel or one-frame criterion is too narrow for a phone display or a Fourier sound visualization.

The same idea applies without graphics:

~~~text
UnitDirection<PhoneFrame>
  → Rotation<PhoneFrame, WorldFrame>
  → Quantized<Direction, ExplicitCodec>
  → AndroidNativeBuffer
~~~

Each arrow has requirements. An optimizer can change the implementation of an arrow only if the resulting observable contract stays true.

A source-level type sketch is not proof that the target backend has working support. That is a separate obligation.

## Compiler families have different rules

The current ICK umbrella contains distinct technical lines. Do not describe all of them as one interchangeable compiler:

- **ICK** is the GCC-derived C/compiler and qualification line. It also exposes freestanding low-precision and finite geometric types.
- **IDK** is the deliberately divergent personal language/compiler line. It may change semantics, use Unicode syntax, and experiment with operation-specific precision or specialized geometry.
- **dmd-upstream** is the conservative DMD-facing line. It should preserve ordinary D semantics and solve portable compiler and backend problems.

The distinction is recorded in [ICK's compiler-line note](https://github.com/dilapidated-shed/ick/blob/main/docs/compiler-lines.md).

An IDK rule like "widen only this operand during multiplication" is not automatically an acceptable upstream D optimization. It changes language semantics unless there is a proof that the ordinary language already permits it.

General backend correctness fixes may migrate upstream. Divergent type policy should remain identified as divergent.

## What makes language design helpful to an agent

I am interested in readable notation: $←$, $→$, $λ$, $≠$, $≟$, $×$, and $÷$ where they clarify rather than obstruct the language.

But syntax is only the surface. More important:

- state the domain and unit of an operation;
- distinguish mathematically different kinds of values;
- expose which transformations lose information;
- keep effects, permissions, or target resources explicit;
- make uncertainty and dependence representable;
- preserve the intended numerical contract through compilation;
- reject unsupported lowering instead of silently choosing a host fallback.

In a good environment, small changes to a generated program should have local, inspectable consequences where possible. Nearby text should not unpredictably choose an entirely different interpretation without a recorded boundary.

This is a research direction. It is not a solved theorem about model-generated code.

## Do not erase the mathematics too early

Some operations should remain recognizable as operations until close to the target:

~~~text
rotation
direction normalization
finite reflection
structured conditional
bounded loop
quantized multiply
interval containment
retained immutable object write
authorized UI operation
~~~

If a rotation becomes anonymous multiplications too early, the compiler loses the chance to select a quaternion operation, a Givens factorization, a small exact table, or a vector kernel.

If a conditional becomes an eager numerical select, the compiler may evaluate both branches when the source intended one. If a recorded E5M3 value is treated like ordinary signed FP8, a storage-only numeric contract is destroyed.

[Rotations: types to assembly](rotations-types-to-assembly.md) gives a vertical example. [E5M3 and memory costs](e5m3-memory-and-nano-optimization.md) develops the precision case.

## Target instructions are not the goal either

A generated ARM instruction listing is evidence of a particular compilation. It is not a semantic proof by itself.

The route needs to retain:

- source revision and language version;
- mathematical and behavioral contract;
- selected type representations;
- intermediate steps and transformations;
- target ISA, ABI, CPU/GPU feature flags, linker and packaging details;
- actual emitted instructions;
- the executable's identity and hash;
- tests and reference data consumed;
- target runtime observations;
- failures and limitations.

"Compiles for Android" cannot replace "the exact APK installed and responded correctly on this phone." "Runs under QEMU" cannot replace the same physical observation.

Nor can one 32-bit ARM test prove every ABI or CPU extension.

The [Android NDK repository](https://github.com/isomorphisms/android-NDK) is the platform substrate. [Cat Food](https://github.com/isomorphisms/catfood) keeps deployment assumptions explicit. [ai-ci](https://github.com/isomorphisms/ai-ci) stores checks and evidence classes.

## AI needs bounded jobs, not vague trust

A useful generation request carries a machine-readable task contract:

~~~text
goal
  + allowed source and authority
  + scope of changes
  + exact starting revision
  + semantic invariants
  + target environment
  + known-good fixture
  + deliberately broken fixture
  + outputs and evidence required
  + explicit stop or refusal conditions
~~~

A worker should distinguish:

- incomplete implementation;
- unavailable external evidence;
- failed reproducible test;
- unsupported target feature;
- conflicting source requirements;
- a genuine human-only choice.

False completion is especially costly. So is summoning the user for something the system can establish mechanically.

[Cockswain](https://github.com/isomorphisms/coxswain) experiments with supervision states. [Kitchen](https://github.com/isomorphisms/kitchen) keeps actual scripts and fixtures outside chat. [Reliable vibe coding](../reliable-vibe-coding.md) contains the detailed evidence framework.

But green checks, merged PRs, and a short queue are merely hygiene. They are not a measure of the intellectual worth of a question. The research may be most interesting before the implementation is settled.

## Specifying a machine closely enough for optimization

Nano-optimization is plausible only after the objective is fixed.

A useful machine profile distinguishes:

1. **Documented interface:** ISA, ABI, legal instructions, alignment and exception behavior.
2. **Documented or measured microarchitecture:** issue behavior, register resources, cache/memory hierarchy, vector width, GPU bank structure where applicable.
3. **Workload:** input size, distributions, precision demands, concurrency, reuse and transfer costs.
4. **Observed cost:** cycles, wall time, cache misses, transactions, energy or temperature where measurable.
5. **Quality:** semantic correctness, output residual, domain failures, recall, display response.

A model can propose instruction schedules, memory layouts, or narrower formats. Each proposal should state why the target might benefit. Then a local benchmark and independent correctness check should decide.

Optimizing without measurements is still useful speculation. It should be labeled speculation, not reported as a speedup.

The striking E5M3 example is concrete: a **nonnegative** distance fragment admits a signless format; a smaller memory word can reduce GPU shared-memory conflicts in a particular approximate search design. That chain gives the compiler something meaningful to exploit.

## How to keep exploration open

I want separate pages for ideas that are not yet built. A mathematical connection can be worth discussing before anyone knows what it will become.

Keep:

- statements proved or directly documented;
- conjectures and questions;
- model choices;
- counterexamples;
- small worked cases;
- original source and bibliography;
- implementation experiments when they exist.

Do not turn every note into a feature roadmap. Do not treat exploratory breadth as an error. Use finished artifacts where they help make an idea more precise; leave room for unfinished mathematics.

Some lines may converge:

~~~text
algebraic constraints
    ↘
rotations → typed operations → numeric storage → hardware layout
    ↗                                 ↓
uncertainty                           multiply indexed retrieval
                                       ↓
                               fast, inspectable search
~~~

The value is in identifying the real common structure, not assigning every project to one fashionable framework.

## First complete vertical experiment

A useful candidate is a small rotation with uncertainty:

1. Define a typed angle and coordinate frame.
2. Define one precise rotation and its inverse.
3. Attach two separately named uncertainty sources.
4. Compute a high-precision reference.
5. Choose a finite or low-precision representation.
6. Lower to the declared ARM32 ABI.
7. Inspect the generated code and reject unsupported operations.
8. Execute the exact artifact on the declared target.
9. Compare transformed geometry, residuals, and visible behavior.
10. Record machine-specific performance only after correctness.

Repeat the same semantic fixture with a second lowering. If the implementations disagree, the durable output is the discrepancy and its reproducer.

This connects a mathematical question to a machine without pretending one necessarily determines the other.

## Sources

- [ICK compiler lines and semantics](https://github.com/dilapidated-shed/ick/blob/main/docs/compiler-lines.md).
- [ICK precision types](https://github.com/dilapidated-shed/ick/blob/main/docs/imprecise-types.md).
- [Arm AAPCS32](https://github.com/ARM-software/abi-aa/blob/main/aapcs32/aapcs32.rst).
- [Reliable vibe coding](../reliable-vibe-coding.md).
- [Semantic operating system](../semantic-operating-system.md).
- [Mathematics as executable constraints](../applying-highbrow-math.md).
- [Multiply indexed retrieval](multiply-indexed-retrieval.md).
