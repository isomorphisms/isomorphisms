# Readable notation is usable now

Input design and parser design can move together. If a symbol says what the operation means, there is no need to make a person hunt-and-peck an ASCII spelling merely because older parsers were designed around it.

- [i-thon](https://github.com/dilapidated-shed/ithon) is a Python experiment with assignment arrows.
- [IR](https://github.com/isomorphisms/ir) is an R adaptation that accepts `←`, `→`, `λ`, `≟`, `÷`, and `⊗` while keeping ordinary R spellings available.
- [Compact Math Keyboard](https://github.com/Ashtray-Archer/utilities-android-phone-user/tree/main/math-keyboard-sample) is the matching Android input experiment: put the useful symbols on keys instead of making the user reconstruct them from punctuation.

This is especially practical with AI-assisted coding. An agent can emit the intended spelling directly, while a human can type the same notation from a purpose-built keyboard. The experiment does not require persuading upstream Python or R to adopt the syntax first.

The real architectural cost is fork proliferation: every parser fork can drift from its upstream language and from editor/tooling assumptions. The useful discipline is therefore to keep the syntax delta small, explicit, tested, and easy to rebase instead of turning each experiment into a new language ecosystem.

Search can use the same layered approach. Exact text, BM25 ranking, vector similarity, learned hyperplanes, graph links, and task context answer different questions and can coexist. [Contextual find and replace](contextual-find-and-replace.md) sketches how to combine them without letting a fuzzy retrieval result silently authorize an edit.
