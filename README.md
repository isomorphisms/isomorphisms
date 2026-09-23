Installable releases:

### Wegert

<!-- software-release:wegert:begin -->
[APK — release 0.1.50](https://github.com/isomorphismes/wegert/releases/download/v0.1.50/wegert-0.1.50.apk) · [source](https://github.com/isomorphismes/wegert) · [demo](https://github.com/isomorphismes/wegert/blob/main/rendered_images/add-and-drag-two-zeros-and-two-poles.mp4?raw=1) — Phase portraits of rational functions in the complex plane, rendered live on your phone. Add and drag zeros and poles and immediately see the function change.
<!-- software-release:wegert:end -->

<video controls muted loop src="https://raw.githubusercontent.com/isomorphismes/wegert/main/rendered_images/add-and-drag-two-zeros-and-two-poles.mp4"></video>

[![Wegert Android interaction demo](https://raw.githubusercontent.com/isomorphismes/wegert/main/rendered_images/add-and-drag-two-zeros-and-two-poles-preview.gif)](https://github.com/isomorphismes/wegert/blob/main/rendered_images/add-and-drag-two-zeros-and-two-poles.mp4?raw=1)


### Accelerometer

<!-- software-release:accelerometer:begin -->
[APK — release 0.2.0](https://github.com/Ashtray-Archer/utilities-android-phone-user/releases/download/accelerometer-native-v0.2.0/accelerometer-native-v0.2.0.apk) · [source](https://github.com/Ashtray-Archer/utilities-android-phone-user/tree/main/accelerometer) · [native sensor path](https://github.com/Ashtray-Archer/utilities-android-phone-user/blob/main/accelerometer/android/android_accelerometer.c) — Access the accelerometer through Android's native `ASensorManager` / `ASensorEventQueue` path, bypassing `android.hardware.SensorManager`, `SensorEventListener`, and application-side JNI glue. The APK is DEX-free and the ARMv7 build runs as Thumb code. The compact geometric state and related machine representations are part of a broader [ARM/Thumb compiler](https://github.com/isomorphisms/idric-arm-thumb) experiment in [representing](https://github.com/isomorphisms/Idric/pull/110) complex numbers, rotations, quaternions, and related geometry more tightly.
<!-- software-release:accelerometer:end -->

<video controls muted loop src="https://github.com/Ashtray-Archer/utilities-android-phone-user/releases/download/accelerometer-native-v0.2.0/accelerometer-native-v0.2.0-replay.mp4"></video>

[![Accelerometer recorded replay](https://github.com/Ashtray-Archer/utilities-android-phone-user/releases/download/accelerometer-native-v0.2.0/accelerometer-native-v0.2.0-replay.gif)](https://github.com/Ashtray-Archer/utilities-android-phone-user/releases/download/accelerometer-native-v0.2.0/accelerometer-native-v0.2.0-replay.mp4)


### Algebraic Variety Explorer

<!-- software-release:algebraic-variety-explorer:begin -->
[source](https://github.com/isomorphismes/algebraic-variety-explorer-mobile) · [build and F-Droid notes](https://github.com/isomorphismes/algebraic-variety-explorer-mobile#f-droid-submission) — Type any polynomial in `x`, `y`, and `z`, with arbitrary powers and products, and immediately see its real zero set as a surface. Ray tracer by Christian Stussak for IMAGINARY's SURFER; Android adaptation produced with ChatGPT 5.6.
<!-- software-release:algebraic-variety-explorer:end -->

![Algebraic Variety Explorer interaction demo](https://github.com/isomorphisms/isomorphisms/raw/refs/heads/main/media/algebraic-variety-explorer-demo-preview.gif)


---

What is all this work aiming at?

Much of the low-level representation work is being co-designed with guidance from ChatGPT 5.6 Sol, which is teaching me some very cool register tricks for complex numbers, rotations, quaternions, and other geometry. I believe this will have further applications to DOM walking, grep, and biological data search. Watch this space over the next few months and see what we discover.

### Larger goals / what I'm excited about

[Space age](space-age.md) · [Readable notation is usable now](readable-notation.md) · [Making programming languages do what they say they do](programming-languages-do-what-they-say.md) · [Writing an easy to read programming language](easy-to-read-programming-language.md) · [Programmer's keyboard](programmers-keyboard.md) · [Making programs smaller and faster](smaller-faster-programs.md) · [My filesystem, my way](my-filesystem-my-way.md) · [Apps should be smaller than the totality of all Russian literature](apps-should-be-smaller-than-the-totality-of-all-russian-literature.md) · [Reliable vibe coding](reliable-vibe-coding.md) · [Lots of useful command-line utilities, lots of useful phone utilities — all free](lots-of-useful-command-line-utilities-lots-of-useful-phone-utilities-all-free.md) · [Trying not to melt the polar ice caps](trying-not-to-melt-the-polar-ice-caps.md) · [Making agents smarter about things](making-agents-smarter-about-things.md) · [Literature on your phone](literature.md) · [Mathematics games](mathematics-games.md) · [Pursuing color with stacks](pursuing-color-with-stacks.md) · [GPU programming](gpu-programming.md) · [FPGA grep](fpga-grep.md) · [Rotations and hyperplanes](rotations-and-hyperplanes.md) · [Statistics, econometrics, and error propagation](statistics-econometrics-and-error-propagation.md) · [iBrowser, Pensieve, Grease, and the semantic operating system](semantic-operating-system.md) · [Contextual find and replace](contextual-find-and-replace.md) · [Forms should work on a $60 phone](forms-should-work-on-a-60-dollar-phone.md) · [What I'm excited about](what-im-excited-about.md)

## Getting AI to behave

- push forward ([cockswain](https://github.com/isomorphisms/cockswain))
- push back (deterministic tests)
- factor through (strongly typed programs)
- anchor to exact references (store local copies of API definitions and useful good/bad sample code; translate in several directions and compare the translations)
