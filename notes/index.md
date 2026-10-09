# Geometry, uncertainty, and the machine

These are working notes, not the GitHub front page. Each is allowed to be long. Open questions remain open.

## The threads

**[Rotations: types to assembly](rotations-types-to-assembly.md)** — $S^2$, $SO(3)$, $SO(n)$, quaternions, reflections, Givens rotations, frame types, quantization, ARM32 calling conventions, and target checks.

**[E5M3, memory channels, and nano-optimization](e5m3-memory-and-nano-optimization.md)** — signed versus unsigned low precision, storage and arithmetic, a 14 × 26 Jacobian, cache and shared-memory access, and what machine-specific performance claims require.

**[Multiply indexed retrieval](multiply-indexed-retrieval.md)** — one retained object with text, graph, geometric, and vector indexes. Why high-dimensional rotations matter for lossy compression even though exact distances stay fixed.

**[Uncertainty and vehicle Jacobians](uncertainty-and-vehicle-jacobians.md)** — intervals as one definite case, named interacting epsilons, unknown nesting, nonlinear three-dimensional geometry, derivatives, singularities, pseudoinverses, and inverse feasible regions.

**[Eisenbud, econometrics, and geometry](eisenbud-econometrics-and-geometry.md)** — the mathematical motivation dating from reading David Eisenbud in 2014. Polynomial models, rank, tangent spaces, identifiability, and learning by experiments rather than formal enrollment.

**[Controlling AI and compiler goals](ai-control-and-compiler-goals.md)** — mathematical and human authority, separate compiler lines, type-to-machine evidence, physical execution, test oracles, and bounded machine-specific optimization.

## One connection across all six

A rotation belongs to a mathematical space. Its type and frame specify what it means. A numeric representation chooses how much of that information to retain. Its layout determines which memory operations are needed. A particular processor runs those operations. An optimizer must preserve the declared invariants and report real performance.

The same chain appears in high-dimensional retrieval. Exact orthogonal rotations preserve distance. Quantizers do not generally commute with rotations. An unsigned eight-bit representation can be justified for a nonnegative squared-distance lookup fragment. That choice can change GPU shared-memory bank contention. This is a concrete route from geometry to a machine-specific gain, not just a metaphor.

Uncertainty enters at every stage: measured geometry, model assumptions, numerical rounding, index approximation, and observed hardware behavior. Distinguish each cause. Do not compress them into an unnamed confidence score.

## Existing notes

- [Rotations and hyperplanes](../rotations-and-hyperplanes.md)
- [Statistics, econometrics, and error propagation](../statistics-econometrics-and-error-propagation.md)
- [Semantic operating system](../semantic-operating-system.md)
- [My filesystem, my way](../my-filesystem-my-way.md)
- [Smaller and faster programs](../smaller-faster-programs.md)
- [Reliable vibe coding](../reliable-vibe-coding.md)
- [Applying highbrow math](../applying-highbrow-math.md)

Details and citations belong on the relevant page. The profile README stays short.
