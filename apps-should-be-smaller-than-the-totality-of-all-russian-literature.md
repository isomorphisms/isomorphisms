# Apps should be smaller than the totality of all Russian literature

A simple Android utility should not arrive carrying runtimes, frameworks, and native libraries for processors it will never execute on.

The title is intentionally excessive. The engineering point is not.

Package size affects download cost, storage, installation, update bandwidth, startup, auditability, and the amount of machinery that can go wrong. The website obesity crisis has an app version too.

There is no reason to choose between **shipping useful software now** and **continuing to pursue very small, direct machine-level implementations**.

## DEX is a useful holding pattern

For Android, direct DEX is a good portable floor.

A compiler can emit DEX structures directly rather than generating Java or Kotlin and then sending them through `javac`, Gradle, or `d8` as compiler stages.

That gives a real Android program today:

```text
checked source
    → compiler-owned representation
    → DEX
    → ART
```

DEX is not the final answer to every performance or size question. It is also not merely a fake backend.

It is a useful shim:

- small enough for simple applications;
- independent of one native CPU ABI;
- executable on ordinary Android devices through ART;
- inspectable;
- testable;
- and available while native backends are still improving.

That means the software factory does not have to wait for every architecture-specific backend before it can generate and ship useful applications.

## A portable floor should not become an excuse to stop

The existence of a DEX path does not remove the reason to build direct native backends.

The portfolio can contain several levels at once:

```text
portable Android floor
    DEX

direct machine backends
    ARM / Thumb
    AArch64
    x86-64
    RISC-V
    WebAssembly where appropriate

specialized compute
    GPU shaders
    FPGA / other spatial hardware
```

The right backend depends on the program and the target.

A constrained Thumb target and a wide vector machine are not the same road. A GPU kernel is not an ordinary CPU procedure. An FPGA dataflow engine is not a branch predictor with different branding.

The compiler should preserve the program's meaning and let the lowering match the machine.

## Native code should not mean a fat universal package

When an application genuinely needs native code, the release system should build the native architectures separately.

A user on one CPU should not have to download every native library for every CPU merely because the publisher wants one enormous package.

The intended release shape is:

```text
accepted source revision
    ↓
checked compiler representation
    ├── DEX baseline
    ├── native artifact for ABI A
    ├── native artifact for ABI B
    └── native artifact for ABI C
            ↓
repository / installer selects a compatible artifact
```

Where the distribution mechanism supports architecture selection, publish per-architecture artifacts and let the repository or installer choose.

Where it does not, a small portable DEX build is often a better fallback than stuffing every native ABI into a simple app.

A universal multi-ABI package should be a deliberate compatibility decision, not the default definition of Android support.

## Make architecture selection part of the builder

The build system should know what it produced.

For every releasable artifact, record at least:

- source revision;
- compiler/backend revision;
- backend;
- target or Android ABI;
- package identifier and version;
- exact artifact filename;
- checksum;
- package size;
- acceptance result;
- and the device or execution environment used for the receipt.

Then architecture-aware release automation becomes a normal build-matrix problem rather than a hand-maintained collection of mystery APKs.

The store-facing metadata should be generated from those receipts.

## Keep a small path open while the hard paths improve

Some compiler backends need more human attention than others.

That is fine.

The factory can keep mechanically checkable backends moving when good oracles exist, while human time goes to places where representation, instruction selection, hardware constraints, or semantics are genuinely unresolved.

That is especially useful for very small programs. A flashlight, sensor viewer, color screen, file utility, mathematical toy, or tiny renderer should not be blocked because the most ambitious backend is unfinished.

Ship the small correct implementation.

Then keep making the lowering better.

## Size is an acceptance property

Package size should be tested, not admired after the fact.

For small applications, the build can carry a size budget and fail or flag a regression when a release suddenly acquires megabytes of unexplained machinery.

The useful measurements include:

- APK size;
- compressed download size;
- installed size;
- native library size by ABI;
- DEX size;
- startup memory;
- runtime memory;
- and toolchain/runtime dependencies introduced by the build.

A direct backend is not automatically good because it is direct.

A DEX backend is not automatically bloated because it runs on a virtual machine.

The rule is simpler:

**make the costs visible, ship the smallest honest implementation available, and keep the path open for a better lowering later.**
