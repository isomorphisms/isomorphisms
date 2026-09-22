# Software

Current software and installable releases.

## Wegert

<!-- software-release:wegert:begin -->
**Wegert Android test 0.1.50** — prerelease

- [Download APK](https://github.com/isomorphismes/wegert/releases/download/v0.1.50/wegert-0.1.50.apk)
- [Release notes and checksum](https://github.com/isomorphismes/wegert/releases/tag/v0.1.50)
- [Source](https://github.com/isomorphismes/wegert)
<!-- software-release:wegert:end -->

<video controls muted loop src="https://raw.githubusercontent.com/isomorphismes/wegert/main/rendered_images/add-and-drag-two-zeros-and-two-poles.mp4"></video>

[![Wegert Android interaction demo](https://raw.githubusercontent.com/isomorphismes/wegert/main/rendered_images/add-and-drag-two-zeros-and-two-poles-preview.gif)](https://github.com/isomorphismes/wegert/blob/main/rendered_images/add-and-drag-two-zeros-and-two-poles.mp4?raw=1)

[Watch Android demo](https://github.com/isomorphismes/wegert/blob/main/rendered_images/add-and-drag-two-zeros-and-two-poles.mp4?raw=1)


## Accelerometer

<!-- software-release:accelerometer:begin -->
**Accelerometer native 0.2.0**

- [Download APK](https://github.com/Ashtray-Archer/utilities-android-phone-user/releases/download/accelerometer-native-v0.2.0/accelerometer-native-v0.2.0.apk)
- [Release notes and provenance](https://github.com/Ashtray-Archer/utilities-android-phone-user/releases/tag/accelerometer-native-v0.2.0)
- [Source](https://github.com/Ashtray-Archer/utilities-android-phone-user)
<!-- software-release:accelerometer:end -->

<video controls muted loop src="https://github.com/Ashtray-Archer/utilities-android-phone-user/releases/download/accelerometer-native-v0.2.0/accelerometer-native-v0.2.0-replay.mp4"></video>

[![Accelerometer recorded replay](https://github.com/Ashtray-Archer/utilities-android-phone-user/releases/download/accelerometer-native-v0.2.0/accelerometer-native-v0.2.0-replay.gif)](https://github.com/Ashtray-Archer/utilities-android-phone-user/releases/download/accelerometer-native-v0.2.0/accelerometer-native-v0.2.0-replay.mp4)

[Watch MP4 replay](https://github.com/Ashtray-Archer/utilities-android-phone-user/releases/download/accelerometer-native-v0.2.0/accelerometer-native-v0.2.0-replay.mp4)


## Algebraic Variety Explorer

<!-- software-release:algebraic-variety-explorer:begin -->
**SURFER Android port — experimental**

- [Source](https://github.com/isomorphismes/algebraic-variety-explorer-mobile)
<!-- software-release:algebraic-variety-explorer:end -->
- [Build and F-Droid notes](https://github.com/isomorphismes/algebraic-variety-explorer-mobile#f-droid-submission)

<video controls muted loop playsinline src="https://raw.githubusercontent.com/isomorphisms/software/my/media/algebraic-variety-explorer-demo.mp4"></video>

[![Algebraic Variety Explorer interaction demo](https://raw.githubusercontent.com/isomorphisms/software/my/media/algebraic-variety-explorer-demo-preview.gif)](https://github.com/isomorphisms/software/blob/my/media/algebraic-variety-explorer-demo.mp4?raw=1)

[Watch demo](https://github.com/isomorphisms/software/blob/my/media/algebraic-variety-explorer-demo.mp4?raw=1)

Rendered interaction preview using the current app layout and shipped Torus, Cayley cubic, and Heart examples.


## Readable notation is usable now

Input design and parser design can move together. If a symbol says what the operation means, there is no need to make a person hunt-and-peck an ASCII spelling merely because older parsers were designed around it.

- [i-thon](https://github.com/dilapidated-shed/ithon) is a Python experiment with assignment arrows.
- [IR](https://github.com/isomorphisms/ir) is an R adaptation that accepts `←`, `→`, `λ`, `≟`, `÷`, and `⊗` while keeping ordinary R spellings available.
- [Compact Math Keyboard](https://github.com/Ashtray-Archer/utilities-android-phone-user/tree/main/math-keyboard-sample) is the matching Android input experiment: put the useful symbols on keys instead of making the user reconstruct them from punctuation.

This is especially practical with AI-assisted coding. An agent can emit the intended spelling directly, while a human can type the same notation from a purpose-built keyboard. The experiment does not require persuading upstream Python or R to adopt the syntax first.

The real architectural cost is fork proliferation: every parser fork can drift from its upstream language and from editor/tooling assumptions. The useful discipline is therefore to keep the syntax delta small, explicit, tested, and easy to rebase instead of turning each experiment into a new language ecosystem.

Search can use the same layered approach. Exact text, BM25 ranking, vector similarity, learned hyperplanes, graph links, and task context answer different questions and can coexist. [Contextual find and replace](contextual-find-and-replace.md) sketches how to combine them without letting a fuzzy retrieval result silently authorize an edit.

The release artifacts remain attached to their source repositories; this repository is the public software index for now.

---

**More:** [Applying highbrow math](applying-highbrow-math.md) · [Making programming languages do what they say they do](programming-languages-do-what-they-say.md) · [Writing an easy to read programming language](easy-to-read-programming-language.md) · [Programmer's keyboard](programmers-keyboard.md) · [Making programs smaller and faster](smaller-faster-programs.md) · [Reliable vibe coding](reliable-vibe-coding.md) · [Lots of useful command-line utilities, lots of useful phone utilities — all free](lots-of-useful-command-line-utilities-lots-of-useful-phone-utilities-all-free.md) · [Trying not to melt the polar ice caps](trying-not-to-melt-the-polar-ice-caps.md) · [Making agents smarter about things](making-agents-smarter-about-things.md) · [Great literature on your phone](great-literature-on-your-phone.md) · [Mathematics games](mathematics-games.md) · [Pursuing color with stacks](pursuing-color-with-stacks.md) · [Hyperbolic geometry](hyperbolic-geometry.md) · [Rotations and hyperplanes](rotations-and-hyperplanes.md) · [Statistics, econometrics, and error propagation](statistics-econometrics-and-error-propagation.md) · [Browser, Pensieve, Grease, and semantic operating system](semantic-operating-system.md) · [Contextual find and replace](contextual-find-and-replace.md)
