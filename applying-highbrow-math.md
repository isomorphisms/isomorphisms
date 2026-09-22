# Applying highbrow math

[Walnut & Burgundy](https://github.com/walnut-burgundy) is where abstract mathematics gets treated as working material rather than decoration.

The point is not to attach impressive vocabulary to ordinary software. The point is to take mathematical structure seriously enough that it changes the program.

That can mean using representation theory to decide what the data really is, using geometry to choose a representation, using topology to understand a transformation, or using a mathematical invariant as a test oracle instead of merely checking a few example outputs.

Some of the current threads include:

- rotations, unit directions, and coordinate changes;
- accelerometer measurements and phone orientation;
- compact representations of points on a sphere;
- separating hyperplanes and geometric classification;
- complex functions and phase portraits;
- analytic continuation;
- representation theory of the symmetric group and Young tableaux;
- music theory expressed with types and geometry.

The repositories are deliberately allowed to cross-pollinate. A rotation problem that begins in an accelerometer can become a test case for compact encoding, language design, visualization, or separating-hyperplane experiments. A mathematical representation should not have to be rediscovered independently inside every program that needs it.

The standard is stronger than “math inspired.” Whenever possible, the program should preserve the actual mathematical structure far enough down that a person can still recognize it and tests can still check it.

A useful example is a unit direction. It is easy to bury the computation inside arithmetic. It is better to expose the sequence of maps:

```text
physical direction
    → normalized direction
    → geometric representation
    → quantized representation
    → bytes
```

Now the code has something intelligible to correspond to. Each stage can have a name, an invariant, and a test.

That is the general idea of Walnut & Burgundy: take subjects that are usually left in books, papers, or blackboards and make them operational without flattening away the interesting structure.

Current homes include [fulton](https://github.com/walnut-burgundy/fulton) for representation-theoretic work, [tymoczko](https://github.com/walnut-burgundy/tymoczko) for music theory with dependent types, and the surrounding Walnut & Burgundy repositories for geometry, statistics, visualization, and related experiments.
