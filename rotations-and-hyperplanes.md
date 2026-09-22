# Rotations and hyperplanes

Rotations and hyperplanes keep turning up across these projects because they are not merely convenient formulas. They are a small set of geometric ideas that connect sensors, representation theory, machine learning, compact storage, graphics, and programming-language design.

The useful thing is that the same mathematics can appear at several levels without being the same representation.

## Directions are not rotations

An accelerometer measurement is a vector in (mathbb R^3).

Its magnitude and its direction are different information.

After normalization, the direction lies on the sphere

[
S^2.
]

That direction can be stored as a unit 3-vector, a point in an octahedral encoding, or a unit pure quaternion.

None of those is yet a phone orientation.

A full orientation is an element of

[
SO(3).
]

One convenient representation is a unit quaternion in (S^3), with the antipodal identification

[
q sim -q.
]

So already there is a useful chain of related but distinct objects:

~~~text
measurement in R³
    → magnitude + direction
    → direction in S²

orientation
    → SO(3)
    ← double-covered by S³ unit quaternions
~~~

Keeping those distinctions visible is both mathematics and language design.

## Rotations are transformations, not coordinates

A rotation can be represented in several ways:

- a matrix;
- a unit quaternion;
- a product of reflections;
- a sequence of Givens rotations;
- a Coxeter word;
- another factorization chosen for a particular workload.

Those carriers are not interchangeable arrays of numbers.

They have different redundancy, different numerical behavior, different storage costs, and different invariants.

The interesting language-design question is whether the source can say **rotation** while still letting the implementation choose the right concrete carrier.

## Hyperplanes

An affine hyperplane in (mathbb R^n) can be written

[
ncdot x + b = 0.
]

That simple equation turns up everywhere.

It can be:

- a geometric boundary;
- a separating classifier;
- a decision surface in an embedding space;
- the mirror defining a reflection;
- a local linear approximation;
- a constraint;
- or part of a coordinate construction.

But the representation has structure.

Multiplying ((n,b)) by a nonzero scalar gives the same unoriented geometric hyperplane.

If the hyperplane is being used as an oriented classifier, however, multiplying by a negative number swaps the positive and negative sides.

That distinction matters.

## Reflections are the bridge

For a unit normal (v), the Householder reflection

[
H(v)=I-2vv^T
]

reflects across the hyperplane perpendicular to (v).

The signs (v) and (-v) produce the same reflector.

So the normal direction for an unoriented reflecting hyperplane naturally has a projective identification.

Two reflections compose to a rotation.

That gives a compact conceptual bridge:

~~~text
hyperplane
    → reflection
    → product of reflections
    → rotation
~~~

This is one reason the Coxeter work, sensor work, projective-space work, and high-dimensional alignment work keep meeting each other.

They are not accidental neighbors.

## The accelerometer is a real geometric instrument

The Android accelerometer work gives the geometry a physical test.

A sensor produces three measured components.

From those we can extract a direction, transform between coordinate conventions, compare that direction with gravity or another reference, and turn the result into something visible on the screen.

The compact direction codec is particularly useful because it forces us to state the maps explicitly:

~~~text
vector
    → direction
    → normalized geometric representative
    → octahedral map
    → quantization
    → bytes
~~~

Decoding follows the maps back in the other direction, except that quantization prevents it from being an exact inverse.

That is a good programming-language example because the mathematical structure is clear enough that the source can be judged against it.

## Hyperplanes in model activations

The same geometry appears in machine-learning experiments.

A model activation is a vector in a high-dimensional real space.

If an experiment fits a separating hyperplane, several questions immediately matter:

- Which activation layer produced the vector?
- What is its dimension?
- Was it normalized?
- Was it centered, whitened, or projected?
- What metric defines distance or margin?
- Is the hyperplane oriented?
- Which side corresponds to which label?
- Does a rotation merely change coordinates, or does preprocessing change the actual supervised problem?

A model producing an activation vector does not by itself establish anything about supervisor quality.

A fitted hyperplane does not establish that the categories are meaningful.

The geometry should make the experiment more inspectable, not make weak conclusions look mathematical.

This is part of the Cockswain and Pensieve/IB work.

## Spheres, projective spaces, and quotients

These examples also force useful distinctions among spaces that programmers routinely collapse into "vectors."

A normalized direction lies on (S^{n-1}).

An unoriented line through the origin identifies opposite points and belongs naturally to real projective space

[
mathbb{RP}^{n-1}.
]

A unit quaternion representing a rotation lies on (S^3), but opposite quaternions represent the same element of (SO(3)).

A hyperplane normal may or may not forget its sign depending on whether orientation matters.

These are small examples of a larger rule:

**the quotient relation is part of the data model.**

If the source language erases that distinction, the programmer has to remember it manually.

## Representation theory

The Fulton work reaches the same territory from the opposite direction.

An abstract group representation may eventually be realized by matrices acting on a real or complex vector space.

Then questions appear about:

- the chosen basis;
- orthogonal versus general linear realizations;
- invariant subspaces;
- normalization;
- projective quotients;
- exact algebraic identities versus floating-point evidence.

The abstract representation should not disappear merely because a matrix has been chosen for computation.

## RHS and semantic honesty

This geometry is also a good test for the RHS idea that programs should do what they say they do.

If something is named

~~~text
unit_direction
rotation
orientation
reflecting_hyperplane
normalized_embedding
~~~

those words should carry more weight than decorative variable names.

Tests and types can check some of the associated claims:

- unit norm;
- determinant;
- orthogonality;
- quotient equivalence;
- dimensionality;
- orientation/sign convention;
- round-trip or approximation bounds;
- preservation of inner products or distances.

The deeper language-design goal is to make these semantic distinctions harder to violate accidentally.

## Why this is exciting

There is a rare amount of reuse here.

The same few objects connect:

- a phone lying on a table;
- compact sensor storage;
- quaternions;
- (S^2), (S^3), (SO(3)), and projective space;
- Householder reflections;
- Coxeter groups;
- representation theory;
- high-dimensional embeddings;
- separating classifiers;
- GPU and visualization work;
- and the design of Idriç.

That gives us something better than a collection of demos.

It gives us a family of concrete problems where abstract mathematics can directly determine better representations, better names, better tests, and better language structure.

The goal is not to force every project onto one representation.

The goal is to know exactly which mathematical object we have, which carrier we chose, which equivalence relations are present, and what information each conversion preserves or destroys.

That is the kind of structure a programming language ought to help us keep.
