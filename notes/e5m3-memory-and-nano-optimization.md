# E5M3, memory channels, and nano-optimization

## The useful question

How much computation and storage does a particular mathematical operation need **on a particular machine**?

A small datatype is not automatically a faster program. A faster instruction is not automatically a faster kernel. The answer depends on numeric meaning, access patterns, memory banks, cache, transfers, the target ABI, and the workload.

Low precision is worth exploring because it makes each choice visible.

## Five formats with different contracts

[ICK's current freestanding header](https://github.com/dilapidated-shed/ick/blob/main/ick/include/ick/imprecise.h) exposes five distinct types:

| Name | Sign bits | Exponent bits | Fraction bits | Storage | Current policy |
| --- | ---: | ---: | ---: | ---: | --- |
| Float16 | 1 | 5 | 10 | 2 bytes | IEEE binary16 storage |
| E4M3 | 1 | 4 | 3 | 1 byte | OCP FP8; saturating conversions |
| E5M2 | 1 | 5 | 2 | 1 byte | OCP FP8; saturating conversions |
| E3M2 | 1 | 3 | 2 | 1 byte, 6 used bits | OCP FP6 payload |
| E5M3 | **0** | 5 | 3 | 1 byte | unsigned storage only |

The sum matters. **One sign bit + five exponent bits + three mantissa bits is nine bits.** The last format fits in one byte because it has *no sign bit*.

The E5M3 here is not a standard, signed FP8 arithmetic type. It follows the unsigned storage format studied by **Hiroyuki Ootomo and Akira Naruse** for approximate-nearest-neighbor lookup tables. Their paper is [Custom 8-bit floating point value format for reducing shared memory bank conflict in approximate nearest neighbor search](https://arxiv.org/abs/2301.06672) (2023).

The point of their special format was not generalized eight-bit arithmetic. Squared-distance lookup fragments are nonnegative. Removing a sign bit frees a bit for exponent or fraction. Smaller stored entries can reduce GPU shared-memory bank conflicts in the authors' target access pattern.

The paper reports better throughput with a small recall tradeoff on its evaluated GPU ANN workloads. It does not prove a speedup for every GPU, CPU, sensor calculation, or matrix.

[Open Compute Project's MX specification](https://www.opencompute.org/documents/ocp-microscaling-formats-mx-v1-0-spec-final-pdf) is the separate reference for the standard E4M3, E5M2, and E3M2 layouts.

## Storage and arithmetic must be separate types

The current ICK semantics are explicit:

- Float16, E4M3, E5M2, E3M2: decode to binary32, perform one binary32 operation, encode to the declared destination format.
- E5M3: encode/decode storage only. Conversion of a binary32 value to E5M3 is **partial**. The documented input domain is positive normal binary32 values. ICK implements the published midpoint reconstruction for payload decoding.
- The E5M3 wrapper rejects ordinary arithmetic rather than inventing an operation with no agreed semantics.

The fact that zero and negative quantities often matter in physical geometry makes the partial domain important.

A positive-only table of squared distances is a natural E5M3 candidate. A signed Jacobian is not.

A future signed representation must choose among real tradeoffs:

1. **Nine-bit payload:** keep a sign + E5M3 magnitude. Bitpack or occupy two bytes. Neither is the current one-byte format.
2. **Separate sign bitmap:** one E5M3 magnitude byte per entry, plus one bit per entry. Zero needs its own representation rule or exception path.
3. **Different FP8 type:** E4M3 or E5M2 changes range and precision.
4. **Context-specific transform:** encode a known nonnegative quantity instead of the original signed one.
5. **Explicit failure:** retain a wider value when the requested format cannot represent it.

A silent sign drop is never quantization; it is a semantic error.

## Quantization is an operation

Write $Q$ for the explicitly chosen encode/decode approximation.

There are at least three different policies for a computation $F$:

$$
Q(F(x)), \qquad F(Q(x)), \qquad Q(F(Q(x))).
$$

They are generally different. A longer sequence with requantization after every primitive can differ further.

The type of the intermediate value matters. Widening storage to binary32 before multiplication is not the same as doing every operation in an exact real field. Binary32 has rounding and exceptional values too.

For each test, record:

~~~text
format and exact bit layout
input domain and special-value policy
encode/decode function and rounding mode
intermediate computation type
point(s) where requantization occurs
reference value
observed value
residual = observed − reference
~~~

Relative residual is useful away from zero. Near zero it can be misleading; preserve absolute residual and raw values.

For ICK's actual rules, see [docs/imprecise-types.md](https://github.com/dilapidated-shed/ick/blob/main/docs/imprecise-types.md) and [the residual sweep](https://github.com/dilapidated-shed/ick/blob/main/qualification/imprecise-types/residuals.c).

## A concrete 14 × 26 Jacobian

A previously used geometry experiment had fourteen output quantities and twenty-six inputs. The Jacobian has $14\times26=364$ scalar entries.

If every entry were stored as binary32, the numerical payload would use

$$
364\times4=1456\text{ bytes}.
$$

Binary16 needs 728 bytes. A byte-sized format needs 364 bytes. A hypothetical tightly packed nine-bit representation needs

$$
\left\lceil364\times9/8\right\rceil=410\text{ bytes}.
$$

These are payload sizes only. They exclude headers, alignment, codebooks, sign/zero exceptions, and any layout padding.

A matrix with both positive and negative entries **cannot simply be stored as the current unsigned E5M3**. Encoding absolute values plus 364 sign bits also takes 410 bytes *before* any zero or domain handling. Larger or more expensive handling may erase a supposed win.

If 278 of 364 Jacobian entries round to zero in a particular six-bit E3M2 experiment, that is a data point about **that fixture and its scale**. It is not a universal sparsity theorem. Store the exact 364-entry fixture and count again under each policy.

The full test should compare:

- applying a stored matrix to a vector;
- storing the inputs and recomputing the Jacobian;
- storing a factorization or geometric operation instead;
- propagating input uncertainty through the representation;
- numerical residuals and geometric invariants under each choice.

Raw compression is not the only objective.

## Why memory layout can outrank arithmetic

A value travels through several layers:

~~~text
mathematical scalar
  → numeric representation
  → field and array layout
  → cache line / SIMD load / memory transaction
  → memory-bank or channel mapping
  → register or local buffer
  → arithmetic
  → result storage and visibility
~~~

A program that fetches four bytes but uses only one may waste bandwidth. A program that packs four values into one word may save bandwidth but spend instructions unpacking. A SIMD load can be fast but lose to a scalar loop if alignment or trip count is poor.

On GPUs, **shared-memory bank conflict** is a different problem from capacity. The same number of useful bytes can take more transactions when simultaneous lanes contend for the same bank. Ootomo and Naruse optimized the width of a particular IVFPQ norm-fragment table to reduce that contention.

That mechanism does not transfer automatically to an Android CPU. CPUs have caches, cache-line fills, prefetch behavior, store forwarding, register pressure, and sometimes different cache-bank or TLB limits. A phone's GPU has its own unrelated memory hierarchy.

Do not assume one machine's diagram describes another.

## What a machine specification must contain

Before claiming a nano-optimization, record the actual target:

| Boundary | Required evidence |
| --- | --- |
| ISA | A32, Thumb, AArch64, x86-64, GPU ISA, and permitted extensions |
| ABI | pointer width, alignment, argument passing, calling variant |
| Execution | core/model, clock conditions, SIMD or vector width |
| Storage | cache levels, cache-line size, alignment, main-memory behavior |
| GPU | workgroup/wave rules, shared memory size, bank width/count where documented |
| Compiler | exact source revision, flags, transformations and emitted instructions |
| Workload | dimensions, access order, batch size, sparsity, reuse, input distribution |
| Measurement | warm-up, repeated timing, counter availability, variance, device temperature |
| Quality | numeric residual, application error, ANN recall, or invariant violated |

Separate *documented fact*, *machine capability detection*, and *measured observation*. Do not invent undocumented per-core cache geometry or cycle counts.

For ARMv7, [AAPCS32](https://github.com/ARM-software/abi-aa/blob/main/aapcs32/aapcs32.rst) defines the public call boundary. ICK's [ARMv7 NEON FFT qualification](https://github.com/dilapidated-shed/ick/blob/main/qualification/android-boundary/armv7-neon-fft.md) is an example of checking an actual four-lane SIMD lowering without claiming an arbitrary application is faster.

The MIRO A1 Android target and a desktop NVIDIA GPU need separate evidence. A test run in an emulator does not fill the physical-phone row.

## Micro versus nano

**Micro-optimization** changes local code: hoisting a conversion, reducing branches, choosing a table layout, changing vector width.

**Nano-optimization** here means testing one precisely specified low-level choice against another: an instruction sequence, packing order, access stride, or scheduling arrangement. It is not a distinct formal field.

An honest trial:

1. Pin the mathematical operation and numerical contract.
2. Pin the target and baseline binary.
3. Write a second implementation and declare what it changes.
4. Test ordinary, extreme, and known-bad inputs against an independent oracle.
5. Inspect generated instructions and memory access.
6. Measure time, transfers, footprint, and output quality on the target.
7. Keep every result, including regressions and cases where the baseline wins.

If a saved load costs two extra instructions, performance is an experiment. If a narrow format gives bad residuals, its speed is irrelevant to that use.

A faster benchmark on a different input distribution is not the same result.

## What would be especially interesting

There is a direct meeting of two lines that look separate:

- high-dimensional search wants compact tables and fast candidate scoring;
- a compiler wants mathematical types that state exactly what values its operations mean.

A norm fragment is nonnegative by construction. That property can justify an unsigned format like E5M3. The mathematical fact saves a sign bit. The byte layout changes memory-bank behavior. The actual machine may then run a query faster.

That is the desired top-to-bottom argument:

~~~text
nonnegative geometric quantity
  → verified range/type
  → eight-bit unsigned representation
  → table layout
  → specified GPU access pattern
  → measured memory-bank behavior
  → recall and throughput compared with reference
~~~

It works only when every arrow is checked. Do not generalize the format from squared norms to signed residuals without changing the type contract.

[Multiply indexed retrieval](multiply-indexed-retrieval.md) develops the search side. [Rotations: types to assembly](rotations-types-to-assembly.md) develops the compiler side. [Uncertainty and vehicle geometry](uncertainty-and-vehicle-jacobians.md) covers the risks of narrowing Jacobians.

## Credit and sources

- **Hiroyuki Ootomo and Akira Naruse**, *Custom 8-bit floating point value format for reducing shared memory bank conflict in approximate nearest neighbor search* (2023), [arXiv:2301.06672](https://arxiv.org/abs/2301.06672). The unsigned E5M3 storage concept and GPU shared-memory motivation come from this work.
- **Open Compute Project**, [Microscaling Formats (MX) Specification](https://www.opencompute.org/documents/ocp-microscaling-formats-mx-v1-0-spec-final-pdf). Its standard FP8/FP6 layouts are distinct from unsigned E5M3.
- [ICK, low-precision types and qualification](https://github.com/dilapidated-shed/ick/blob/main/docs/imprecise-types.md). Contract and implementation facts above refer to this repository.
- [ICK, compiler lines](https://github.com/dilapidated-shed/ick/blob/main/docs/compiler-lines.md). Divergent numeric policy belongs to IDK rather than being silently attributed to ordinary upstream D.
