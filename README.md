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


## Projects

**Readable notation (`← → λ ≠ ≟`):** [Icky C](icky-c.md) · [Idriç](https://github.com/dilapidated-shed/Idric) · [i-thon](https://github.com/dilapidated-shed/ithon) · [IR](https://github.com/isomorphisms/ir) · [Compact Math Keyboard](https://github.com/Ashtray-Archer/utilities-android-phone-user/tree/main/math-keyboard-sample)

**Search / editing:** [IB / Pensieve](https://github.com/dilapidated-shed/ib), an experimental browser and durable task workbench · [BM25, vector, and SVM-style retrieval](semantic-operating-system.md#search-should-not-be-one-box) · [Contextual find and replace](contextual-find-and-replace.md)

**Systems / reliability:** [Grease](https://github.com/dilapidated-shed/grease), the Oils-derived shell · [Cat Food](https://github.com/isomorphisms/catfood), workbench provisioning and runtime delivery · [Android NDK](https://github.com/isomorphisms/android-NDK), reusable DEX/JNI/NativeActivity/NDK and APK substrate · [ai-ci](https://github.com/isomorphisms/ai-ci), shared verification and evidence gates · [Cockswain](https://github.com/isomorphisms/cockswain), agent-work supervision · [Small apps](apps-should-be-smaller-than-the-totality-of-all-russian-literature.md) · [FPGA grep](fpga-grep.md)

**Mathematics checks:** [Walnut & Burgundy verification](applying-highbrow-math.md#make-the-mathematics-verify-the-program) · [fulton](https://github.com/walnut-burgundy/fulton) · [tymoczko](https://github.com/walnut-burgundy/tymoczko)

**Direction:** [Space age](space-age.md)


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

- push forward ([Cockswain](https://github.com/isomorphisms/cockswain))
- push back (deterministic tests)
- factor through (strongly typed programs)
- anchor to exact references
