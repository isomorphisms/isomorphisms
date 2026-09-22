# Writing an easy to read programming language

[Idriç](https://github.com/isomorphisms/Idric) is an experiment in treating readability as part of language design rather than as a formatting preference.

The basic rule is that a reader should see what the program is doing before being forced to reconstruct it from implementation machinery.

A high-level operation can read like this:

```text
connection ← accept connection from listener
request ← read request from connection
response ← answer request
write response to connection
```

The implementation may eventually involve buffers, syscalls, pointers, parsers, allocation, or machine instructions. Those details matter, but they do not have to occupy the same conceptual level as the job being performed.

Several choices follow from that.

## Use names that carry information

Long names are cheap.

A compiler term named `Administrative_Normal_Form_Constructor_Alternative` is easier to inspect than `AConAlt` if the abbreviation forces every reader to keep a private decoding table in memory.

The same rule applies to application code. Prefer names that state the mathematical or domain role of a value instead of names inherited from an implementation accident.

## Let syntax express relationships

Words such as `from`, `to`, `with`, `using`, and `via` can make argument roles visible.

Mathematical notation can do the same where mathematics is the clearest language. Idriç uses symbols such as `←`, `→`, `=`, `≠`, `≟`, `⇒`, and `∘` where they express real structure.

The aim is not decorative Unicode or English cosplay. The aim is to reduce the amount of reconstruction a reader must do.

## Keep domain ideas visible

A direction should look like a direction. A duration should not become an arbitrary integer earlier than necessary. Text and bytes should not be confused. Mathematical vectors should not share a name with every fixed-length container.

When a computation is a composition of meaningful maps, the source should show those maps.

For example:

```text
sensor measurement
    → direction in the phone coordinate system
    → normalized direction
    → screen transformation
    → displayed level
```

That is much easier to inspect than one large block of arithmetic even when both compile to similar machine operations.

## Expose mechanism by descent

Top-level source should show purpose. Deeper files can expose the implementation.

A reader who only needs the idea should not have to read foreign-function declarations or raw syscalls. A reader who does need them should be able to descend directly to the layer where they live.

This also means hiding less in the compiler. Intermediate forms, lowering stages, and target boundaries should have readable names and explicit responsibilities.

## Readability is not an excuse to give up control

Idriç is intended for low-level work as well as high-level description.

The language experiments include direct machine-code, DEX, WebAssembly, GPU, embedded, and other backends. The goal is not to put a friendly layer on top of an opaque stack. It is to make the stack itself easier to inspect.

Readable source and low-level control should reinforce each other.

A program should be easier to understand because its structure is visible, not because the difficult parts have merely been hidden somewhere else.
