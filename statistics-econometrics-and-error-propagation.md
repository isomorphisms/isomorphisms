# Statistics, econometrics, and error propagation

There are several different experiments here. They should not be collapsed into one claim that there is a new statistical method.

The common question is:

> can mathematical structure, type systems, and better representations make statistical work more explicit, more inspectable, and harder to misuse?

## Start with practical statistics

[walnut-burgundy/statistics](https://github.com/walnut-burgundy/statistics) begins from ordinary statistical work as it is actually done:

~~~text
get data
    → inspect it
    → clean it
    → understand how it was defined
    → transform it
    → visualize it
    → fit something
    → check whether the result means what we think it means
~~~

That matters because statistical software is often taught as though the interesting problem begins after a clean rectangular dataset has already appeared.

[Econometrician](https://github.com/bl4ckb4ll/econometrician) takes a narrower executable approach. Its current slices implement small deterministic statistical procedures with explicit contracts, including Pearson chi-square procedures and a bounded bootstrap reference.

The program is deliberately willing to refuse unsupported assumptions rather than silently generalize from one implemented case.

**Make the assumptions and the boundary executable.**

## Ask whether commutative algebra actually helps

Another line is more speculative.

There is a substantial algebraic-statistics literature around toric ideals, Markov bases, Gröbner bases and related machinery.

The experiment is not to say that commutative algebra is sophisticated, therefore statistics should use more of it. The question is whether an existing algebraic result removes, simplifies, or reorganizes a real statistical computation we actually care about.

So far, that line has not been especially productive. That is useful evidence too.

The system should be able to explore a mathematically plausible transfer and conclude that the machinery is not earning its cost for the current problem.

The wider [Idriç higher-mathematics constraint work](https://github.com/isomorphisms/Idric/issues/42) and [Computer Science theorem/planning work](https://github.com/walnut-burgundy/computer-science/issues/56) provide one possible future route: mathematical facts can be typed, versioned, and supplied as inspectable constraints rather than hard-coded folklore.

But algebra should have to prove that it helps.

## Do not collapse every uncertainty into one number

A more immediately useful direction is to treat **sources of error as first-class values**.

A calculation might contain several different uncertainties:

~~~text
measurement error
calibration error
quantization error
sampling error
model error
input-position error
numerical approximation error
unknown nuisance effect
~~~

Those do not necessarily mean the same thing. They may not combine by the same rule.

Some may be bounded intervals. Some may be approximately Gaussian. Some may be correlated. Some may be directional or geometric. Some may only be known as a conservative bound. Some may have no useful numerical interaction with one another except that all remain relevant to the final result.

The first rule is simple:

**do not forget where an error came from merely because a calculation produced a new number.**

## Error terms as something like a formal sum

A useful mental model is closer to a formal sum than one anonymous error bar:

~~~text
result
    + sensor_error
    + calibration_error
    + steering_angle_error
    + model_error
~~~

The terms do not have to be numerically combined immediately. They can retain their identities while the computation transforms them.

A later operation may discover that two sources interact and need a joint model. Another may be able to bound them independently. Another may merely carry both forward.

This is attractive for a type system because forgetting a term can become a visible operation rather than an accidental omission.

## Transform the uncertainty with the value

If a value is transformed by a map, the associated uncertainty should also be transformed.

For a scalar interval, that may mean interval arithmetic or another conservative enclosure.

For a direction on a sphere, uncertainty may be a region around that direction rather than a scalar plus/minus value. A rotation should rotate the uncertainty region with the direction. A deformation of a sphere may deform the associated region.

If the program transforms only the central estimate and leaves the error model behind, it has lost part of the computation.

This connects naturally to the rotations, spheres, projective spaces, and hyperplane work.

## Intervals are the deliberately simple kernel

The current Idriç interval experiment is intentionally much smaller than a general uncertainty framework.

The research branch [examples/units-time-intervals](https://github.com/isomorphisms/Idric/tree/examples/units-time-intervals/_/examples/units-time-intervals) contains a small executable kernel with exact rational values, units and dimensional structure, signed durations and instants, open and closed one-dimensional intervals, interval addition, explicit endpoint membership, and a deliberate distinction between interval openness and nilpotent dual-number epsilon.

The tests explicitly say that probability, Gaussian inference, correlated uncertainty, and interval multiplication/division are **not** part of that first slice.

That is a good boundary. Intervals are useful before they become a theory of statistics.

## Intervals are also a planning primitive

An interval is not only an error bar. It is also a compact statement about what is possible.

If a planner can establish

~~~text
possible result ∈ [a, b]
~~~

it may be able to prove that a branch can never be taken, an object cannot intersect a region, a threshold cannot be crossed, a rendering block can be skipped, a candidate algorithm is impossible, or a more expensive calculation is unnecessary.

This belongs with the broader [ask mathematics before registers](https://github.com/walnut-burgundy/computer-science/issues/54) planning work.

The planner should exploit a cheap symbolic bound before paying for a lower-level computation when the bound already answers the question.

That is a straightforward computer-science use of the same interval machinery.

## Nested bounds can stay nested

Sometimes one approximation sits inside another. There is no requirement to flatten nested bounds immediately into one final radius or tolerance.

Keeping nested regions can preserve provenance:

~~~text
physical tolerance
    contains measurement uncertainty
        contains numerical approximation
~~~

Other problems may have independent overlapping regions rather than containment. The representation should follow the actual relationship instead of forcing every uncertainty into one scalar convention.

## Statistics can benefit from richer types without becoming type theory

The goal is not to turn every statistical analysis into a proof-assistant exercise.

A type can simply preserve distinctions the analyst is already reasoning about:

- this quantity has units;
- this value is bounded by this interval;
- this estimate assumes IID sampling;
- this uncertainty came from calibration;
- these two terms are correlated;
- this result is exact;
- this result is numerical;
- this bound is conservative;
- this interval is open at one endpoint;
- this quantity lives on a sphere rather than a line.

Those distinctions already exist in the reasoning. The question is whether the program can preserve them instead of asking a comment or variable name to carry all of the meaning.

## Several lines can coexist

~~~text
practical statistics and econometrics
    → make ordinary analysis inspectable

algebraic statistics / commutative algebra
    → test whether existing deeper mathematics actually earns its cost

typed intervals and error sources
    → preserve uncertainty through transformations

symbolic planning
    → use bounds and mathematical structure to avoid unnecessary computation
~~~

Some of these may become powerful. Some may remain small utilities. Some may fail.

The important part is that the computer can help test the ideas against real statistical and computational problems instead of leaving them as vague mathematical enthusiasm.