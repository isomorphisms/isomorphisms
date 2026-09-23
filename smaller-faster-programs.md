# Making programs smaller and faster

A large amount of software exists only to support other software.

Source is translated into another language, passed through another compiler, linked against a runtime, wrapped in a framework, packaged by a build system, and finally delivered to a machine that often needs only a small fraction of that machinery.

One line of the Idriç work asks how much of that can be removed.

The current direct x86-64 path is a concrete example:

```text
checked Idriç source
    → compiler-owned intermediate form
    → x86-64 instructions
    → ELF64
    → execution
```

There is no generated C in that production route, and no C compiler, assembler, linker, libc, or CRT between the checked program and the emitted executable.

The Android DEX work follows the same principle. Idriç writes DEX structures directly instead of generating Java or Kotlin and then relying on `javac`, Gradle, or `d8` as compiler stages.

That direct DEX path can also be a deliberate portable holding pattern: ship useful Android programs now while architecture-specific native backends keep improving independently. The deployment side of that strategy is described in [Apps should be smaller than the totality of all Russian literature](apps-should-be-smaller-than-the-totality-of-all-russian-literature.md).

Other experiments push the same idea toward ARM, WebAssembly, GPUs, embedded systems, and specialized targets.

The goal is not “remove layers” as an aesthetic rule. A layer earns its place when it provides something useful. The question is whether a program should pay for machinery it does not need.

## C is not the universal target

For decades, targeting C has been a practical way to get portability and reuse an existing compiler toolchain.

That made sense.

It does not make C a mandatory middle layer for every new language.

A compiler can instead target the thing the machine actually consumes, or a target-specific language that already matches the problem:

~~~text
Idriç
    → x86-64 instructions / ELF
    → ARM / Thumb instructions
    → DEX
    → WebAssembly
    → GPU shader code
    → embedded target code
~~~

The exact target differs by program.

The principle is the same:

**do not route through C merely because languages traditionally route through C.**

C can still be useful as a reference implementation, compatibility boundary, oracle, or deliberately chosen backend.

It just does not get privileged status as the substrate underneath everything else.

## Direct targets make the lowering easier to inspect

A direct backend creates a shorter semantic path.

Instead of:

~~~text
source language
    → generated C
    → C frontend
    → C optimizer
    → compiler IR
    → assembler
    → linker
    → executable
~~~

a narrow backend can look more like:

~~~text
checked source
    → compiler-owned representation
    → target operations
    → target artifact
~~~

That shorter path is useful for more than speed.

It makes it easier to answer:

- which language operation produced these instructions?
- where was precision chosen?
- where was a value represented differently?
- which runtime service was introduced?
- what target feature is unsupported?
- which artifact did the test actually execute?

The low-level side of the project is therefore not an attempt to make the source look like assembly.

It is an attempt to make the descent from high-level meaning to the real target explicit.

## Use the representation the problem needs

Size and speed also depend on representation.

If a direction can be represented compactly with a controlled geometric encoding, carrying three general-purpose floating-point values forever may be unnecessary.

If Float16 is enough for a quantity, silently widening everything to a host `Double` and narrowing it later adds cost and can obscure the intended precision.

If a GPU program is finite and bounded, a specialized shader representation may be better than dragging a general-purpose runtime into the target.

Persistent storage is the same kind of choice. [My filesystem, my way](my-filesystem-my-way.md) asks why an append-heavy application, a multiply indexed data set, and a random-access application should all be forced through the same storage layout.

The same principle appears repeatedly:

**preserve meaning, then lower deliberately.**

## Reject unsupported work instead of quietly importing a runtime

A small backend becomes large very quickly if every unsupported language feature is “solved” by adding another runtime or fallback compiler.

The direct backends therefore try to fail closed. If a target cannot correctly implement a construct, rejecting it can be better than silently routing around the architecture.

That keeps the executable path understandable and makes costs visible.

## Measure the result

“Smaller” and “faster” are separate claims and should be measured separately.

Useful measurements include:

- executable or package size;
- runtime memory;
- startup cost;
- instruction count or execution time where relevant;
- compiler and build-tool footprint;
- generated-code size;
- energy or device cost on constrained hardware.

A direct backend is not automatically faster merely because it is direct, and compact code is not automatically good code.

The useful claim is narrower: removing unnecessary representation changes, runtimes, dependencies, and build stages creates opportunities for smaller and faster programs while making the path from source to machine easier to inspect.

The interesting part is that this does not have to conflict with readable source.

The same language can aim upward toward meaningful mathematics and ordinary language while also aiming downward toward exact bytes and instructions.
