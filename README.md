Installable releases:

### Wegert

<!-- software-release:wegert:begin -->
**Wegert Android test 0.1.50** — prerelease — [Download APK](https://github.com/isomorphismes/wegert/releases/download/v0.1.50/wegert-0.1.50.apk) · [Release notes and checksum](https://github.com/isomorphismes/wegert/releases/tag/v0.1.50) · [Source](https://github.com/isomorphismes/wegert)
<!-- software-release:wegert:end -->

Drag zeros and poles; the phase portrait updates live. [Demo](https://github.com/isomorphismes/wegert/blob/main/rendered_images/add-and-drag-two-zeros-and-two-poles.mp4?raw=1).

[![Wegert Android interaction demo](https://raw.githubusercontent.com/isomorphismes/wegert/main/rendered_images/add-and-drag-two-zeros-and-two-poles-preview.gif)](https://github.com/isomorphismes/wegert/blob/main/rendered_images/add-and-drag-two-zeros-and-two-poles.mp4?raw=1)


### Accelerometer

<!-- software-release:accelerometer:begin -->
**Accelerometer native 0.2.0** — [Download APK](https://github.com/Ashtray-Archer/utilities-android-phone-user/releases/download/accelerometer-native-v0.2.0/accelerometer-native-v0.2.0.apk) · [Release notes and provenance](https://github.com/Ashtray-Archer/utilities-android-phone-user/releases/tag/accelerometer-native-v0.2.0) · [Source](https://github.com/Ashtray-Archer/utilities-android-phone-user)
<!-- software-release:accelerometer:end -->

Native Android accelerometer path; DEX-free ARMv7/Thumb app. [Sensor code](https://github.com/Ashtray-Archer/utilities-android-phone-user/blob/main/accelerometer/android/android_accelerometer.c) · [ARM/Thumb development line](https://github.com/dilapidated-shed/idric-arm-thumb/tree/native-arm). The backend repository's default branch is the separate direct DEX compiler.

[![Accelerometer recorded replay](https://github.com/Ashtray-Archer/utilities-android-phone-user/releases/download/accelerometer-native-v0.2.0/accelerometer-native-v0.2.0-replay.gif)](https://github.com/Ashtray-Archer/utilities-android-phone-user/releases/download/accelerometer-native-v0.2.0/accelerometer-native-v0.2.0-replay.mp4)


### Algebraic Variety Explorer

<!-- software-release:algebraic-variety-explorer:begin -->
[Source](https://github.com/isomorphismes/algebraic-variety-explorer-mobile)
<!-- software-release:algebraic-variety-explorer:end -->

Type a polynomial in `x`, `y`, and `z`; see its real zero set. [Build and F-Droid notes](https://github.com/isomorphismes/algebraic-variety-explorer-mobile#f-droid-submission).

![Algebraic Variety Explorer interaction demo](https://github.com/isomorphisms/isomorphisms/raw/refs/heads/main/media/algebraic-variety-explorer-demo-preview.gif)


### Pauli

[Source](https://github.com/isomorphismes/pauli) · [Atom in a Box](https://daugerresearch.com/orbitals/mac.shtml) · [App Store](https://apps.apple.com/us/app/atom-in-a-box/id284788633)

**Homage to the OG Dane Dauger, an original gangster of real-time orbital visualization** — using a computational notebook and irreducible representations to get the spherical harmonics symbolically.


## Working snippets

### Florence Nightingale / Fourier Voice

A Fourier/Wegert rendering driven by Florence Nightingale's 1890 recording.

> “When I am no longer even a memory, just a name, I hope my voice may perpetuate … Florence Nightingale.”

<video controls preload="metadata" width="360">
  <source src="https://raw.githubusercontent.com/isomorphismes/Fourier-sound/refs/heads/experiments/nightingale-fourier-movie/media/florence-nightingale-fourier-voice.mp4" type="video/mp4">
</video>

[MP4](https://raw.githubusercontent.com/isomorphismes/Fourier-sound/refs/heads/experiments/nightingale-fourier-movie/media/florence-nightingale-fourier-voice.mp4) · [Fourier Voice](https://github.com/isomorphismes/Fourier-sound)


## Projects

**Readable notation (`← → λ ≠ ≟`):** [Icky C](icky-c.md) · [Idriç](https://github.com/dilapidated-shed/Idric) · [i-thon](https://github.com/dilapidated-shed/ithon) · [IR](https://github.com/isomorphisms/ir) · [Compact Math Keyboard](https://github.com/Ashtray-Archer/utilities-android-phone-user/tree/main/math-keyboard-sample)

**Search / editing:** [IB / Pensieve](https://github.com/dilapidated-shed/ib), an experimental browser and durable task workbench · [BM25, vector, and SVM-style retrieval](semantic-operating-system.md#search-should-not-be-one-box) · [Contextual find and replace](contextual-find-and-replace.md)

**Systems / reliability:** [Grease](https://github.com/dilapidated-shed/grease), the Oils-derived shell · [Cat Food](https://github.com/isomorphisms/catfood), workbench provisioning and runtime delivery · [Android NDK](https://github.com/isomorphisms/android-NDK), reusable DEX/JNI/NativeActivity/NDK and APK substrate · [ai-ci](https://github.com/isomorphisms/ai-ci), shared verification and evidence gates · [Cockswain](https://github.com/isomorphisms/cockswain), agent-work supervision · [Small apps](apps-should-be-smaller-than-the-totality-of-all-russian-literature.md) · [FPGA grep](fpga-grep.md)

**Mathematics checks:** [Walnut & Burgundy verification](applying-highbrow-math.md#make-the-mathematics-verify-the-program) · [fulton](https://github.com/walnut-burgundy/fulton) · [tymoczko](https://github.com/walnut-burgundy/tymoczko)

**Direction:** [Space age](space-age.md)


## Low precision and honest error

Real measurements rarely justify thousandths, much less millionths. Even Float16 often carries more precision than the inputs deserve. The extra headroom is useful when a calculation — especially multiplication, accumulation, linear algebra, or trigonometry — needs it; it is not a reason to invent precision in the measurements.

Instead of collapsing everything into one anonymous ±ε, I want to keep different sources of error distinct: data-entry error, meter-reading error, didn't-see-it error, holding-it-upside-down error, ordinary engineering tolerance, and small angular or alignment tolerances that can cast a very long geometric shadow. Some of these are bounded numerical uncertainty. Some are discrete mistakes and should not be disguised as Gaussian noise.

One experiment is to carry several symbolic ε's through the program rather than resolving them immediately, then bracket them wherever topology, order, continuity, sign, geometry, or a known physical bound gives useful information. Alongside that: definite interval data types with executable lower and upper bounds, starting with addition and subtraction and widening only as much as the operation requires.

Then push both representations through purposefully complicated but definite linear algebra and trigonometry. Compare symbolic bounds, interval bounds, and a higher-precision reference. Look for where uncertainty grows, cancels, changes branch, is amplified by geometry, or becomes smaller than quantization.


##### Chatbot as build system

We're used to packaging many builds into one APK, and even to accepting approximate interfaces (such as the JVM), because it's too much for one person to remember every machine architecture, every hardware sensor manual, or how every memory layout might pair with every register layout.

Yeah. Too much for one _person_.

I experiment with downloading these manuals and having the bot fill in the details. (Compiler backends, for example: [ARM/Thumb](https://github.com/fuego-ironworks/idric-arm-thumb) and [GPU](https://github.com/fuego-ironworks/idris-shader-backend).) A companion idea is to develop intermediate representations, compiler front ends, and even see if the bot can nano-optimize without a bench (so far, no on the last one—but a decisive yes on the others).

[Android NDK](https://github.com/isomorphisms/android-NDK) collects the reusable Android-native side of that experiment: DEX/ART, JNI/NativeActivity, NDK interfaces, APK construction, and hardware-reference boundaries.

Build sizes for a non-stripped ELF reach 43 KB for the simplest program ***because I don't even need libc***.

Some less toy-like Android builds, measured from successful CI artifacts rather than estimated:

| program | package shape | ARMv7 native code | APK |
| --- | --- | ---: | ---: |
| [Accelerometer](https://github.com/Ashtray-Archer/utilities-android-phone-user/tree/228e303b49deb35fc021655ddaf6098365d9f95e/accelerometer) | one ABI, DEX-free | 19,056 B | 45,591 B |
| [Pauli](https://github.com/isomorphismes/pauli/tree/5d43e69a63173b44120782d684c77283316120bd/android) | one ABI, DEX-free orbital viewer | 36,128 B | 20,923 B |
| [Programmer's Unicode Picker](https://github.com/Ashtray-Archer/utilities-android-phone-user/tree/9f586c3d5b2be3ade1739dfa7846caed3ed16aa9/math-characters) | three-ABI, DEX-free debug APK | 169,812 B | 610,952 B |
| [Wegert](https://github.com/isomorphismes/wegert/tree/d326c1512079fd4440a7289cf95f634e48d0f912) | three-ABI, DEX-free F-Droid build | 169,652 B | 1,039,143 B |

The APK column measures the package on disk, not the uncompressed contents. ZIP compression can make a one-ABI APK smaller than the ELF inside it.


## Getting AI to behave

- **push forward:** [Cockswain](https://github.com/isomorphisms/cockswain) supervises agent work instead of treating one-shot generation as the finished product.
- **push back:** deterministic tests and [ai-ci](https://github.com/isomorphisms/ai-ci) turn failures into evidence and regressions.
- **externalize the work:** [Kitchen](https://github.com/isomorphisms/kitchen) is the place where casual scripts and terminal instructions are prepared before they are served. Requirements, target assumptions, fixtures, aggressive cases, tests, exact script versions, and failure notes live in files instead of disappearing into conversational memory. That leaves a deterministic history: what program was actually written, what was tried, what failed, and what should become a regression test or an improvement to the generation/verification process.
- **let implementations teach one another:** parallel versions in different languages should not only be compared inside a model's temporary context. Put the semantics, fixtures, and conformance cases outside the conversation and make every implementation run the same harness. [mbox](https://github.com/isomorphisms/mbox) does this with Idriç, D, Agda, and Idris: a discrepancy or invariant found through one branch becomes a shared regression that all the others must face. The durable artifact is the contract, fixture, test, and per-language result—not the model's memory of the comparison. [More detail](reliable-vibe-coding.md#let-implementations-teach-one-another).
- **stretch goal — languages for model generation:** [Idriç](https://github.com/dilapidated-shed/Idric) and [English-major C](https://github.com/dilapidated-shed/English-major-C) already move source toward more readable, semantically explicit forms. A future language can go further and account for the local, bootstrapping character of language-model output: nearby generated programs should, where possible, be accepted and given nearby deterministic meanings rather than letting small textual drift produce arbitrary behavior.

Across all five: factor through strongly typed programs and anchor claims and code to exact references.
