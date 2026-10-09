# Rotations: from types to assembly

## Question

Can one program say **rotation** and keep that meaning through machine code?

The answer has to cover the whole path. A mathematical object has invariants. A type records them. An intermediate representation must not forget them. Storage may approximate them. An ABI decides how values move between routines. Instructions finally implement the operation.

None of those stages is interchangeable with the others.

This is a design note. The proposed Idriç types and lowering stages are not a claim that one compiler already implements them all.

## Begin with the right spaces

A nonzero vector in $\mathbb R^3$ has a magnitude and a direction. Its normalized direction is a point of $S^2$.

A full rigid orientation is an element of $SO(3)$, not a point of $S^2$. Knowing the direction of gravity does not tell us rotation about gravity.

A rotation in $n$ dimensions belongs to

$$
SO(n)=\{R\in\mathbb R^{n\times n}:R^\mathsf{T}R=I,\ \det(R)=1\}.
$$

The determinant condition excludes reflections. The orthogonality condition preserves inner products.

In three dimensions a unit quaternion lies in $S^3$. The map from unit quaternions to $SO(3)$ identifies $q$ with $-q$. The double cover explains the distinction between a returned ordinary orientation at $2\pi$ and the returned lifted state at $4\pi$. [Spinor](https://github.com/isomorphismes/spinor) makes that distinction visible.

A direction, an orientation, a lifted orientation, and a change of coordinates should have different types.

## The types to preserve

Sketch, not executable syntax:

~~~text
Frame                 // named physical or computational coordinate frame
Angle<Unit>           // degrees and radians are not silently interchangeable
Vector<n, Frame, Unit>
Direction<n, Frame>   // normalized; construction can fail for zero input
Rotation<n, SourceFrame, TargetFrame>
Orientation<Frame>    // convention stated
SpinLift3             // retains the lift, not only the SO(3) image
Reflection<n, Frame>
Tangent<Manifold, AtPoint>
Quantized<Value, Encoding, RoundingPolicy>
Uncertain<Value, ErrorModel>
~~~

Composition checks frame endpoints. A rotation from phone coordinates to world coordinates cannot multiply a vehicle-frame vector until the conversion is supplied.

A constructor for a unit direction rejects the zero vector. A constructor for a rotation checks or proves orthogonality and orientation. Merely naming a matrix "rotation" proves nothing.

A quantized rotation must not promise exact orthogonality unless the representation really preserves it. It may instead carry an explicit error bound, a reconstruction law, or a tested finite-group contract.

A coordinate frame also includes axis order, handedness, and unit conventions. These are not optional comments when the result drives a camera or sensor calculation.

## Representations are choices, not identities

A rotation can be represented as:

- a dense matrix;
- an axis and angle in three dimensions;
- a unit quaternion in three dimensions;
- an ordered product of Householder reflections;
- an ordered product of Givens plane rotations;
- a word in generators of a finite reflection or Coxeter group;
- a specialized exact finite rotation object.

Each representation has different storage, arithmetic, and composition costs.

A Householder reflection in a nonzero normal $v$ is

$$
H_v=I-\frac{2vv^\mathsf T}{v^\mathsf Tv}.
$$

It is orthogonal with determinant $-1$. Two reflections compose to a proper rotation in the appropriate plane. General orthogonal maps can be decomposed into reflections.

A Givens rotation changes only two coordinates at a time. This matters in high dimensions. An $n\times n$ matrix costs $n^2$ stored scalars, while a sequence of $k$ explicitly recorded coordinate-plane rotations may use $O(k)$ parameters and $O(k)$ scalar-pair updates per vector. The factorization is beneficial only when $k$ is small enough, or when its structure pays for the extra indirection.

For $n=3$, quaternion composition can be compact. For general $n$, assuming every rotation has a four-scalar quaternion carrier is wrong.

See [Rotations and hyperplanes](../rotations-and-hyperplanes.md) and [Coxeter](https://github.com/isomorphismes/coxeter).

## A vertical semantic trace

~~~text
typed mathematical operation
  → normalized, frame-correct expression
  → proof obligations / checked invariants
  → typed intermediate operation
  → chosen carrier (matrix, quaternion, reflection word, finite table)
  → chosen numeric contract (exact, Float32, Float16, quantized, ...)
  → layout: fields, alignment, order, address space
  → target ABI and calling convention
  → instructions and actual artifact
  → independent numerical and physical checks
~~~

An optimizer may reorder operations only when the numeric contract permits it. For floating point, two algebraically equal formulas can produce different rounding, overflow, or exceptional values.

There must be an explicit boundary between mathematical equality and acceptable numerical residual.

The compiler must also distinguish:

1. **Type correctness**: frames, units, dimensions, and categories are valid.
2. **Representational correctness**: decoding means what the source promised.
3. **Algorithmic correctness**: the intended rotation or approximation was computed.
4. **ABI correctness**: data and control cross the machine boundary correctly.
5. **Execution evidence**: the exact executable ran on the declared target.

A pass in one class cannot be passed off as evidence for another.

## Example: a steering angle

Suppose the steering-wheel angle is $360^\circ$ and the measured or specified steering ratio is $17.4:1$. In a deliberately simplified model,

$$
\theta=360^\circ/17.4\approx20.689655^\circ.
$$

This is a test input, not a claim about the exact behavior of a particular vehicle.

A rotation in the plane uses

$$
R(\theta)=
\begin{bmatrix}
\cos\theta &-\sin\theta\\
\sin\theta & \cos\theta
\end{bmatrix}.
$$

A calculation may need $\sin\theta$, $\cos\theta$, or the caster-like sensitivity factor $1/(2\sin\theta)$. The latter becomes ill-conditioned as $\theta$ approaches zero.

The type of $\theta$ carries its unit. The trigonometric operations accept the angle in radians internally. The result's rounding policy is explicit. Quantizing the angle, its sine, and the final multiplier at different stages gives different residuals. These are distinct experiments.

A useful fixture records the input, the expected high-precision result, the observed result, and **residual = observed − reference**.

## From rotation to bytes

Consider a normalized physical direction:

~~~text
measured vector
  → unit direction on S²
  → selected geometric encoding
  → rounded finite representation
  → bytes in a particular layout
~~~

An octahedral mapping, for example, compresses a direction before quantization. Decoding gives an approximation, not a mathematical inverse of a lossy step. A program must keep the representation map and its quantization policy apart.

When composing quantized rotations, there is a further choice: reconstruct and compose in a wider type, then requantize; or operate in a format with an exact finite composition law. The latter cannot be assumed for an arbitrary byte encoding.

[ICK's Circle96 note](https://github.com/dilapidated-shed/ick/blob/main/docs/circle96.md) is a useful finite model. Exact operations in a 96-position model are not automatically exact operations in continuous $SO(2)$ or $SO(3)$.

## The ARM32 boundary

The specific ABI matters more than broad claims about "ARM."

For the Android ARMv7 target, inspect at least:

- the instruction set selected: A32 or Thumb;
- the target triple and minimum Android API;
- the AAPCS32 procedure-call variant, including softfp versus hard-float rules;
- which arguments travel through core registers and the stack;
- 32-bit pointer layout and stack alignment at a public interface;
- the permitted VFP/NEON instructions and their numerical behavior;
- object attributes, relocations, and the native Android entry point.

A conventional Android armeabi-v7a softfp call boundary need not use the same register path as hard-float. Internal SIMD arithmetic does not itself change the public calling convention.

The [Arm AAPCS32 specification](https://github.com/ARM-software/abi-aa/blob/main/aapcs32/aapcs32.rst) is the authority for data sizes and calling rules. Do not infer them from a desktop C experiment.

[ICK's ARMv7 NEON FFT qualification](https://github.com/dilapidated-shed/ick/blob/main/qualification/android-boundary/armv7-neon-fft.md) deliberately checks the instruction path and keeps its relaxed floating-point policy local. NEON use, strict IEEE semantics, and ABI conformance are separate claims.

The exact instruction sequence is a result of a chosen backend and target. It is not part of the abstract Rotation type.

## What a machine-specific optimizer may change

After choosing a target, one might:

- choose a pairwise Givens sequence rather than a dense multiply;
- store columns or rows to match an actual access pattern;
- fuse multiply-add operations if the rounding policy allows;
- precompute sin/cos for an explicit finite angle set;
- group independent rotations for vector execution;
- choose a narrower storage format with wider arithmetic;
- avoid repeated decoding within a hot loop;
- change instruction scheduling or data alignment.

None is an unconditional improvement. For a single small matrix, simpler scalar code may win. A different processor, working-set size, or memory layout may reverse the ranking.

## Checks worth retaining

**Mathematical:** $R^\mathsf TR\approx I$, $\det R\approx+1$, norm preservation, composition, identity, inverse, and frame consistency. Use a separate exact or higher-precision oracle. Include adversarial near-degenerate inputs.

**Representation:** round-trip a dense sample of encoded values; verify domain exclusions, signs, NaNs, special values, and the exact quantization stage.

**Backend:** compare generated instructions against the declared ABI and required instruction capabilities. Reject silent host fallbacks.

**Runtime:** execute on the intended target. A simulator pass is not physical-device evidence.

**Performance:** measure latency, size, bandwidth, energy where possible, and numerical residual. Keep the compiler flags and processor description with the result.

## Why higher dimensions matter

Rotation is not merely graphics. High-dimensional embeddings and model activations are vectors in spaces where an orthogonal transform can reorganize coordinates without changing exact Euclidean distances.

That does **not** make the transform an improvement by itself. Its value appears when subsequent operations are axis-sensitive: scalar quantization, product quantization, coordinate partitioning, or hardware layout. A rotation can move a correlated point cloud into coordinates that compress or index better.

This connects [multiply indexed retrieval](multiply-indexed-retrieval.md) to [E5M3 and memory costs](e5m3-memory-and-nano-optimization.md). A representation that preserves exact geometry may still alter approximate retrieval after compression.

The long-term goal is one comprehensible path from geometry to executable machine operations, not a large vocabulary wrapped around ordinary arrays.

## Sources and related work

- [Arm, Procedure Call Standard for the Arm Architecture](https://github.com/ARM-software/abi-aa/blob/main/aapcs32/aapcs32.rst).
- [ICK's low-precision type contracts](https://github.com/dilapidated-shed/ick/blob/main/docs/imprecise-types.md).
- [ICK compiler lines: IDK and upstream DMD](https://github.com/dilapidated-shed/ick/blob/main/docs/compiler-lines.md).
- [High-level rotation and hyperplane notes](../rotations-and-hyperplanes.md).
- [Machine lowering and small programs](../smaller-faster-programs.md).
- [Spinor's provenance and Jason Hise's work](https://github.com/isomorphismes/spinor/blob/main/notes/jason-hise.md).

Credit belongs with each borrowed model. In particular, the Spinor interaction owes a substantial visual debt to **Jason Hise**. These notes propose a compiler architecture; they do not claim to reproduce his source.
