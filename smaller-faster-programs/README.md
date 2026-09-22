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

Other experiments push the same idea toward ARM, WebAssembly, GPUs, embedded systems, and specialized targets.

The goal is not “remove layers” as an aesthetic rule. A layer earns its place when it provides something useful. The question is whether a program should pay for machinery it does not need.

## Use the representation the problem needs

Size and speed also depend on representation.

If a direction can be represented compactly with a controlled geometric encoding, carrying three general-purpose floating-point values forever may be unnecessary.

If Float16 is enough for a quantity, silently widening everything to a host `Double` and narrowing it later adds cost and can obscure the intended precision.

If a GPU program is finite and bounded, a specialized shader representation may be better than dragging a general-purpose runtime into the target.

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
