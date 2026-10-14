# isomorphisms

What I’m working on:
- the programming keyboard we always needed
- programs that run on the cheapest phone available on Amazon: the $60 Miro.A1
- fun math interactions
- a "pensieve" browser which saves what you *intend* to read, to disk
- playing with compilers, assembly, and language front-ends. Can we get rid of API’s entirely in this new world?
- rewriting favorite cli tools to compile with a smaller tool chain, owned by me
- hooking cli tools up to the rest of the operating system! McElroy told us to do this; the Plan9 team pushed everything-is-a-file further, but with a networking focus that's not so important to me. AOSP has a different goal set but can also be adapted.
- seeing if proper dimensional accounting can prevent a class of errors in CNC G-code
- using LMs’ ability to translate to bootstrap insights into code quality
- trying to tame the slop
- focusing on readability above all else

## Programs

### Spinor

<!-- software-release:spinor:begin -->
**Spinor 0.0.1-pre.1** — prerelease — [MIRO A1 APK](https://github.com/isomorphismes/spinor/releases/download/v0.0.1-pre.1/spinor-miro-a1-armeabi-v7a.apk) · [MIRO C67 APK](https://github.com/isomorphismes/spinor/releases/download/v0.0.1-pre.1/spinor-miro-c67-arm64-v8a.apk) · [Release notes and checksums](https://github.com/isomorphismes/spinor/releases/tag/v0.0.1-pre.1) · [Source](https://github.com/isomorphismes/spinor)
<!-- software-release:spinor:end -->

Rotate through 2π, then 4π. [Video](https://github.com/isomorphismes/spinor/releases/download/v0.0.1-pre.1/spinor-4pi-demo.mp4).

[![Spinor 0 → 2π → 4π animation](https://github.com/isomorphismes/spinor/releases/download/v0.0.1-pre.1/spinor-4pi-demo-preview.gif)](https://github.com/isomorphismes/spinor/releases/download/v0.0.1-pre.1/spinor-4pi-demo.mp4)

**Visual construction: Jason Hise.** Spinor's rotating central body, **six attached belts/ribbons**, and their untwisting over a 720° turn closely follow Hise's original [six-belt *Belt Trick* animation](https://commons.wikimedia.org/wiki/File:Belt_Trick.ogv) and [96-strand *Antitwister*](https://commons.wikimedia.org/wiki/File:Antitwister.ogv). This is an independently coded implementation of **Hise's distinctive visualization**, not a claim to have invented it or the older mathematical belt trick. [Hise's explanation](https://diff.wikimedia.org/2016/09/22/math-gifs/) · [Entropy Games](https://entropygames.net/) · [Detailed attribution](https://github.com/isomorphismes/spinor/blob/main/notes/jason-hise.md).

### Wegert

<!-- software-release:wegert:begin -->
**Wegert Android test 0.1.50** — prerelease — [Download APK](https://github.com/isomorphismes/wegert/releases/download/v0.1.50/wegert-0.1.50.apk) · [Release notes and checksum](https://github.com/isomorphismes/wegert/releases/tag/v0.1.50) · [Source](https://github.com/isomorphismes/wegert)
<!-- software-release:wegert:end -->

**Mathematical visualization: Elias Wegert.** This independently coded Android app explores complex functions with phase portraits, following Wegert's [*Visual Complex Functions: An Introduction with Phase Portraits*](https://doi.org/10.1007/978-3-0348-0180-5). The app does not claim to have originated his approach. Wegert and **Gunter Semmler**, later joined by **Pamela Gorkin and Ulrich Daepp**, produced the original [*Complex Beauties* calendars (2011–2024)](https://blogs.hrz.tu-freiberg.de/mathekalender/english/), including the [complete 2024 calendar (PDF)](https://www.dropbox.com/scl/fi/w1mi4oqfgcaxztgaheoex/calendar2024Eng_no_margins.pdf?dl=0&rlkey=eifi7vh63t2lgqpxn0e1adfv0).

Move zeros and poles. Watch the phase portrait change. [Video](https://github.com/isomorphismes/wegert/blob/main/rendered_images/add-and-drag-two-zeros-and-two-poles.mp4?raw=1).

[![Wegert demo](https://raw.githubusercontent.com/isomorphismes/wegert/main/rendered_images/add-and-drag-two-zeros-and-two-poles-preview.gif)](https://github.com/isomorphismes/wegert/blob/main/rendered_images/add-and-drag-two-zeros-and-two-poles.mp4?raw=1)

### Algebraic Variety Explorer

<!-- software-release:algebraic-variety-explorer:begin -->
[Source](https://github.com/isomorphismes/algebraic-variety-explorer-mobile)
<!-- software-release:algebraic-variety-explorer:end -->

**Original renderer: Christian Stussak.** This Android adaptation **reuses his Java `jsurf` ray tracer**, written for IMAGINARY's [SURFER](https://www.imaginary.org/program/surfer) at the Mathematisches Forschungsinstitut Oberwolfach. The ray-tracing engine and polynomial rendering were **Stussak's work**; this project supplies a phone interface and packaging, not a new renderer. [Original `jsurf` source](https://github.com/IMAGINARY/jsurf) · [Apache-2.0 attribution](https://github.com/isomorphismes/algebraic-variety-explorer-mobile/blob/surfer/NOTICE).

Graph real zero sets in three variables. [Video](media/algebraic-variety-explorer-demo.mp4).

[![Algebraic Variety Explorer demo](media/algebraic-variety-explorer-demo-preview.gif)](media/algebraic-variety-explorer-demo.mp4)

### Accelerometer

<!-- software-release:accelerometer:begin -->
**Accelerometer native 0.2.0** — [Download APK](https://github.com/Ashtray-Archer/utilities-android-phone-user/releases/download/accelerometer-native-v0.2.0/accelerometer-native-v0.2.0.apk) · [Release notes and provenance](https://github.com/Ashtray-Archer/utilities-android-phone-user/releases/tag/accelerometer-native-v0.2.0) · [Source](https://github.com/Ashtray-Archer/utilities-android-phone-user)
<!-- software-release:accelerometer:end -->

A DEX-free ARMv7/Thumb app. [Sensor code](https://github.com/Ashtray-Archer/utilities-android-phone-user/blob/main/accelerometer/android/android_accelerometer.c) · [Replay](https://github.com/Ashtray-Archer/utilities-android-phone-user/releases/download/accelerometer-native-v0.2.0/accelerometer-native-v0.2.0-replay.mp4).

[![Accelerometer sensor-data replay](https://github.com/Ashtray-Archer/utilities-android-phone-user/releases/download/accelerometer-native-v0.2.0/accelerometer-native-v0.2.0-replay.gif)](https://github.com/Ashtray-Archer/utilities-android-phone-user/releases/download/accelerometer-native-v0.2.0/accelerometer-native-v0.2.0-replay.mp4)

### Pauli

Orbital visualization from spherical harmonics. Thanks to **Dean Dauger** for [Atom in a Box](https://daugerresearch.com/orbitals/mac.shtml). [Source](https://github.com/isomorphismes/pauli).

Turntable of a fixed 2pₓ orbital using Pauli's native CPU renderer (camera motion, not orbital-state rotation). [Video](https://github.com/isomorphismes/pauli/blob/main/media/pauli-2px-turntable.mp4?raw=1).

[![Pauli 2pₓ orbital camera turntable](https://raw.githubusercontent.com/isomorphismes/pauli/main/media/pauli-2px-turntable-preview.gif)](https://github.com/isomorphismes/pauli/blob/main/media/pauli-2px-turntable.mp4?raw=1)

### Fourier Voice / Florence Nightingale

**Writing the simplest programs:** microphone → Fourier mathematics → graphics, exploring the phone's hardware abstraction layer (HAL), tiny native executables, and a **no-libc** target. Today's source uses AAudio and libc—not direct access to the vendor HAL. Florence Nightingale's 1890 voice is a repeatable **offline** movie input, not a live microphone recording. [Movie](https://raw.githubusercontent.com/isomorphismes/Fourier-sound/refs/heads/experiments/nightingale-fourier-movie/media/florence-nightingale-fourier-voice.mp4) · [Source](https://github.com/isomorphismes/Fourier-sound) · [Minimal microphone/HAL experiment](https://github.com/isomorphismes/Fourier-sound/blob/main/docs/minimal-microphone-hal.md).

[![Florence Nightingale Fourier Voice animated preview](https://raw.githubusercontent.com/isomorphismes/Fourier-sound/refs/heads/experiments/nightingale-fourier-movie/media/florence-nightingale-fourier-voice-preview.gif)](https://raw.githubusercontent.com/isomorphismes/Fourier-sound/refs/heads/experiments/nightingale-fourier-movie/media/florence-nightingale-fourier-voice.mp4)

## Projects

**Mathematics:** [Games](mathematics-games.md) · [Coefficient Root Dance](https://github.com/isomorphismes/coefficient-root-dance) · [Coxeter](https://github.com/isomorphismes/coxeter) · [Indra's Pearls](https://github.com/isomorphismes/indras-pearls) · [Subpixel curves](https://github.com/isomorphisms/rough.framebuffer)

**Topology:** [VanKoughnett](https://github.com/isomorphisms/VanKoughnett) · [Goodwillie](https://github.com/isomorphisms/goodwillie) · [Morava](https://github.com/isomorphisms/morava) · [Snaith](https://github.com/isomorphisms/snaith) · [Mapping classes](https://github.com/isomorphisms/mapping-class) · [Kirby calculus](https://github.com/isomorphisms/kirby-calculus) · [Montesinos](https://github.com/isomorphisms/montesinos)

**Languages:** [Icky C](icky-c.md) · [Idriç](https://github.com/isomorphisms/Idric) · [i-thon](https://github.com/dilapidated-shed/ithon) · [IR](https://github.com/isomorphisms/ir) · [Math keyboard](https://github.com/Ashtray-Archer/utilities-android-phone-user/tree/main/math-keyboard-sample)

**Systems:** [IB](https://github.com/isomorphisms/ib) · [Search design](semantic-operating-system.md) · [Grease](https://github.com/dilapidated-shed/grease) · [Android NDK](https://github.com/isomorphisms/android-NDK) · [Cat Food](https://github.com/isomorphisms/catfood) · [FPGA grep](fpga-grep.md) · [Password dots](where-password-dots-live.md)

**AI-built code:** [ai-ci](https://github.com/isomorphisms/ai-ci) · [Cockswain](https://github.com/isomorphisms/coxswain) · [Kitchen](https://github.com/isomorphisms/kitchen) · [mbox](https://github.com/isomorphisms/mbox) · [What I check](reliable-vibe-coding.md)

**Math and error:** [Walnut & Burgundy](applying-highbrow-math.md) · [Fulton](https://github.com/walnut-burgundy/fulton) · [Tymoczko](https://github.com/walnut-burgundy/tymoczko) · [Statistics](statistics-econometrics-and-error-propagation.md) · [Intervals](https://github.com/dilapidated-shed/intervals.idr) · [Precision notes](low-precision-and-honest-error.md)

**Notes:** [Chatbot as build system](chatbot-as-build-system.md) · [Small apps](apps-should-be-smaller-than-the-totality-of-all-russian-literature.md) · [Space age](space-age.md)
