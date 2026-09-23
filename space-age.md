# Space age

AI just changed the economics of making software.

A large part of programming used to be the cost of turning an idea into an implementation: writing the boilerplate, learning another API, wiring together another framework, chasing another build system, translating the same intention through layer after layer until a machine finally did the thing.

That cost has dropped hard.

My reaction is not: great, now I can make ordinary software faster.

My reaction is: **how much of the accumulated compromise in computing can we go back and fix?**

I want to bring software back to the space age.

Not as nostalgia. The 1960s were not a lost paradise of perfect software. The point is the attitude: the computer is an astonishing machine, the problem is worth understanding all the way down, and the program should be made as good as we know how to make it.

Don Eyles's *[Sunburst and Luminary](https://www.sunburstandluminary.com/SLhome.html)* is one picture of that attitude. The Apollo lunar-landing software was not an interchangeable corporate application sitting on top of an indefinite pile of machinery. The mathematics, the guidance problem, the representation, the hardware, the timing, the user interface, the failure modes, and the actual mission were connected. The labels mattered because somebody had to understand the program. The machine mattered because there was a real machine at the other end.

Jack Ganssle's *[Embedded Muse](https://www.ganssle.com/tem-back.htm)* comes from a later part of the same engineering tradition: bits are real, timing is real, hardware is real, failures are real, and abstractions do not repeal physics.

That is the spirit I want now, with a new advantage they did not have.

## The new lever arm

AI gives one person an absurd amount of implementation leverage.

That changes what is worth attempting.

If implementation is expensive, you accept the API. You accept the framework. You accept the language. You accept the build system. You accept the browser. You accept the filesystem. You accept 150 MB for a program that conceptually needs almost nothing. You accept that the source says one thing while the machine does another because fixing the whole stack is too much work.

If implementation becomes cheap enough, those compromises become negotiable again.

So use the leverage.

Smash the API if the API is wrong.

Write the direct backend if the intermediate toolchain adds nothing.

Make the phone utility small.

Make the mathematical object look like the mathematical object.

Keep the names and labels that let the next person understand the program.

Make the programming language express intention instead of hiding it behind punctuation and convention.

Make the tests hostile enough that an AI cannot pass by producing something that merely looks plausible.

Make the artifact traceable to the source that produced it.

Make the browser remember what the user was actually doing.

Make the shell know that arguments have roles.

Make the filesystem serve the organization of information instead of forcing one historical tree onto everything.

If a layer earns its place, keep it. If it exists only because everybody inherited it, it is fair game.

## Top to bottom

I do not want "good" to mean polished at the surface and incomprehensible underneath.

I want the chain to make sense all the way down:

```text
human intention
    → readable source
    → explicit mathematical and semantic structure
    → inspectable lowering
    → appropriate representation
    → exact artifact
    → real machine
    → observed behavior
```

Every arrow is part of the program.

That is why apparently different projects here keep running into one another.

[Idriç](https://github.com/isomorphisms/Idric) asks what a programming language should look like if readability and intention are first-class design constraints.

[Making programs smaller and faster](smaller-faster-programs.md) asks why a simple program should drag an unnecessary software civilization behind it.

[Applying highbrow math](applying-highbrow-math.md) asks what happens when mathematics is treated as working structure instead of decoration.

[RHS](programming-languages-do-what-they-say.md) asks whether the visible meaning of a program can have consequences instead of being an unenforced comment.

[IB, Pensieve, Grease, and the semantic operating system](semantic-operating-system.md) ask which old operating-system and interface assumptions are still useful and which ones we can finally replace.

[Cat Food, ai-ci, and Cockswain](reliable-vibe-coding.md) ask how AI can move very fast without requiring the human to trust vibes.

These are not separate hobbies to me.

They are different places to apply the same pressure.

## AI should raise the standard

The depressing use of AI would be to generate mediocre software at much higher volume.

The interesting use is to raise the standard because we can finally afford to.

More tests.

More targets.

More readable names.

More exact representations.

More experiments.

More independent checks.

More documentation at the point where the reasoning happened.

More direct inspection of the machine.

More attempts at the version we actually wanted instead of stopping at the version that was cheap enough to implement.

AI can produce enormous quantities of code. That makes code itself less precious.

Intent, structure, evidence, taste, mathematical correctness, physical reality, and the ability to tell whether the thing actually works become more important.

So the goal is not maximum code generation.

The goal is maximum leverage applied to making the whole thing right.

## Make coding enjoyable again

There is another part of this that is less grand and just as important.

Computers are fun.

Languages can be beautiful.

Machine instructions are interesting.

A good name is satisfying.

A tiny program that does exactly what it says is satisfying.

A mathematical structure surviving intact from the idea into the implementation is satisfying.

Seeing the exact artifact run on the exact machine is satisfying.

Somewhere along the way a lot of software culture learned to treat enormous dependency graphs, inscrutable build systems, bad interfaces, unnecessary abstraction, and perpetual compromise as the price of being serious.

I do not accept that price as a law of nature.

We have a new machine for making machines.

I want to find out what happens if we point it at all the things that have bothered us for decades and stop assuming they are too expensive to fix.

Bring software back to the space age.

Then push forward.
