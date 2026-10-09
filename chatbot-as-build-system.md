# Chatbot as build system

A person cannot memorize every CPU ABI, sensor manual, or register layout. I test whether a bot can work from the manuals instead.

Compiler experiments: [ARM/Thumb](https://github.com/fuego-ironworks/idric-arm-thumb) and [GPU](https://github.com/fuego-ironworks/idris-shader-backend). [Android NDK](https://github.com/isomorphisms/android-NDK) handles APK packaging, DEX/ART, JNI, and native interfaces.

One non-stripped ELF was 43 KB. It needed no libc.

## Measured Android builds

These sizes came from successful CI artifacts.

| Program | Package | ARMv7 native code | APK |
| --- | --- | ---: | ---: |
| [Accelerometer](https://github.com/Ashtray-Archer/utilities-android-phone-user/tree/228e303b49deb35fc021655ddaf6098365d9f95e/accelerometer) | one ABI, DEX-free | 19,056 B | 45,591 B |
| [Pauli](https://github.com/isomorphismes/pauli/tree/5d43e69a63173b44120782d684c77283316120bd/android) | one ABI, DEX-free | 36,128 B | 20,923 B |
| [Unicode Picker](https://github.com/Ashtray-Archer/utilities-android-phone-user/tree/9f586c3d5b2be3ade1739dfa7846caed3ed16aa9/math-characters) | three-ABI, DEX-free | 169,812 B | 610,952 B |
| [Wegert](https://github.com/isomorphismes/wegert/tree/d326c1512079fd4440a7289cf95f634e48d0f912) | three-ABI, DEX-free | 169,652 B | 1,039,143 B |

APK size is compressed size on disk. It can be smaller than the ELF inside it.

The bot can fill out compiler backends and interfaces. I have not found it reliable at nano-optimization without a benchmark.

[How I check AI-built software](reliable-vibe-coding.md) · [Small apps](apps-should-be-smaller-than-the-totality-of-all-russian-literature.md)
