# Uncertainty, rigid geometry, and vehicle Jacobians

## Why a car is a good mathematical test

A vehicle has rigid pieces, hinges, curved trajectories, measurements, imperfect surfaces, and uncertain reference frames.

Its geometry is simple enough to write down in parts. Its uncertainties are not simple. A small angular error can turn into a larger position error after a lever arm or near-singular trigonometric calculation. Several errors can cancel, reinforce, or refer to mutually incompatible physical states.

This is an experiment in mathematical representation. It is **not** a validated vehicle-alignment procedure.

The interesting problem is not to compute one answer with an extra decimal place. It is to preserve what is known, what was assumed, and what is still not known.

## An interval is the easiest case, not the foundation

A definite interval $[a,b]$ says an unknown real value lies between known endpoints. An open endpoint changes the membership rule. This is useful and precise.

But "I do not know the value" can be much stronger:

- I may not know the width of the uncertainty.
- I may not know how to resolve it.
- I may not know how many nested regions of uncertainty surround the point.
- I may not know whether two sources of error interact.
- I may not know whether a measurement was reversed or assigned to the wrong side.
- I may not know whether the correct physical model was used.

No single $\pm\varepsilon$ captures all of that.

The notation $(\bullet)$ versus $((\bullet))$ versus $(((\bullet)))$ suggests successive enclosures, but the number and interpretation of layers may themselves be unknown. A family of candidate sets may be nested, overlapping, disjoint, correlated, or not yet comparable.

The type model should therefore allow **unknown structure**, not simply an interval with very wide bounds.

~~~text
PointEstimate
  + SourceOfError(name, status, evidence)
  + PossibleRegion(shape or unknown)
  + Dependence(other source: known / ruled out / unresolved)
  + ResolutionCondition(known / proposed / unknown)
  + RefinementHistory
~~~

These are conceptual fields, not claims that Idriç already implements them.

A genuine interval arithmetic kernel is still valuable. It is one case in which the endpoints and the set operation are known. [Existing statistics and interval notes](../statistics-econometrics-and-error-propagation.md) and the [Idriç interval work](https://github.com/dilapidated-shed/intervals.idr) belong next to, not in place of, this broader incomplete-knowledge problem.

## Several epsilons must retain their identities

Suppose a result depends on three sources:

$$
y=f(x,\varepsilon_{\text{angle}},
       \varepsilon_{\text{reading}},
       \varepsilon_{\text{calibration}}).
$$

Do not replace them by a single unnamed $\varepsilon$ at the start.

One source may be a bounded position error. Another may be a shared bias affecting every reading. Another may describe a discrete mistake such as confusing a left measurement with a right one.

If the terms have a joint probabilistic model, covariance is useful. Without that model, independent Gaussian addition is not justified. If bounds are known, interval or set propagation may be valid but conservative.

Interactions can matter. A Taylor expansion of a smooth output contains not only separate first-order terms but also mixed terms:

$$
\Delta y\approx
\sum_i\frac{\partial f}{\partial\varepsilon_i}\Delta\varepsilon_i
+\frac12\sum_{i,j}
\frac{\partial^2 f}{\partial\varepsilon_i\partial\varepsilon_j}
\Delta\varepsilon_i\Delta\varepsilon_j.
$$

The mixed derivatives describe one type of interaction. Dependence or correlation between sources is a different one. They must not be conflated.

Also keep apart the numerical uncertainty symbols $\varepsilon_i$ and the *nilpotent* formal quantity in dual-number differentiation ($\epsilon^2=0$). Both may be written "epsilon," but they are different objects.

## A small trigonometric example

Take a point $(x,y)$ in metres and a measured angle $\theta$ in radians. Let the observed projection be

$$
f(x,y,\theta)=x\cos\theta+y\sin\theta.
$$

Its Jacobian is

$$
Df(x,y,\theta)=
\begin{bmatrix}
\cos\theta &
\sin\theta &
-x\sin\theta+y\cos\theta
\end{bmatrix}.
$$

At $x=2\text{ m}$, $y=1\text{ m}$, and $\theta=20^\circ$:

- the projection is about $2.221405\text{ m}$;
- $\partial f/\partial x\approx0.939693$;
- $\partial f/\partial y\approx0.342020$;
- $\partial f/\partial\theta\approx0.255652\text{ m/radian}$.

Suppose the **hypothetical** independent absolute bounds are $|\Delta x|\le0.01\text{ m}$, $|\Delta y|\le0.02\text{ m}$, and $|\Delta\theta|\le0.5^\circ$.

The first-order worst-case absolute bound is approximately

$$
0.939693(0.01)+0.342020(0.02)
+0.255652(0.5\pi/180)
\approx0.018468\text{ m}.
$$

This is a **linearized** bound, not an exact containment theorem. Curvature adds higher-order terms. Joint constraints may make this sum overconservative. A shared calibration error may cause errors to move together instead of varying independently.

Even this simple projection shows why several named uncertainties are more informative than one anonymous error bar.

## Angle amplification

A caster-like geometric sensitivity calculation may contain

$$
m(\theta)=\frac{1}{2\sin\theta}.
$$

For the illustrative angle $\theta=360^\circ/17.4\approx20.689655^\circ$,

$$
m(\theta)\approx1.415204.
$$

Its derivative is

$$
m'(\theta)=-\frac{\cos\theta}{2\sin^2\theta}.
$$

Near zero, this derivative becomes large in magnitude. A seemingly small steering-angle uncertainty can dominate a downstream calculation.

The steering ratio here is an illustrative input. A real vehicle's linkage, compliance, steering geometry, and measurement method can invalidate a fixed-ratio model. A sharp sensitivity result is a reason to check the model, not a reason to trust its nominal output.

## Rigid pieces and curved motion

A rigid-body transform can be written

$$
p_{\mathrm{world}}
=R(\theta)\,p_{\mathrm{body}}+t,\qquad R\in SO(3).
$$

A vehicle is not one rigid body. Steering knuckles, control arms, bushings, springs, and wheels impose constraints and introduce additional degrees of freedom. Some trajectories are curved. Some joints are approximately rigid. Some changes are load-dependent.

Let $x\in\mathbb R^{26}$ represent one chosen set of parameters and let $f(x)\in\mathbb R^{14}$ represent fourteen predicted observations. The particular components and units must be declared for any real fixture.

Then

$$
J(x)=Df(x)\in\mathbb R^{14\times26}.
$$

That is a **364-entry** Jacobian. It describes local sensitivity, not the complete nonlinear geometry.

The finite difference

$$
\frac{f(x+h v)-f(x-h v)}{2h}
$$

should approximate $J(x)v$ for suitable $h$ and a declared direction $v$. Multiple step sizes detect cancellation or truncation error. An automatic-differentiation or symbolic oracle offers an independent second check when practical.

The Jacobian and the underlying geometric relations should be kept side by side.

## The inverse Jacobian is a real mathematical question

A $14\times26$ Jacobian has **no ordinary matrix inverse**. Its rank is at most fourteen. If rank is fourteen, its nullspace still has dimension at least twelve.

An observed change in fourteen outputs therefore need not identify a unique change in twenty-six unconstrained inputs.

There are several different inverse problems:

- **Local inverse:** choose a square, full-rank parameterization or add enough independent constraints. Then the inverse-function theorem may apply locally.
- **Pseudoinverse:** $J^+$ supplies one least-squares/minimum-norm answer under a chosen metric. It does not recover the unknown nullspace components.
- **Constrained inverse:** intersect the possible parameter states with rigid, joint, physical, and observational constraints.
- **Uncertainty inverse:** return the entire admissible input region, not one arbitrary point.

For a linearized measurement $r=y_{\mathrm{observed}}-f(x_0)$, an inverse uncertainty set can be written

$$
\mathcal U_x
=\left\{\delta x:
r-J\delta x\in\mathcal U_y,\
x_0+\delta x\in\mathcal C
\right\}.
$$

Here $\mathcal U_y$ is the permitted output-error set and $\mathcal C$ is the permitted parameter set. Both need explicit meaning.

This expresses an honest inverse question. It may have zero, one, or infinitely many admissible states.

If a locally invertible square submap $g$ is justified, check both round trips, $g^{-1}(g(x))$ and $g(g^{-1}(y))$, within the selected numerical tolerance. For the rectangular case, check the Moore–Penrose identities such as $JJ^+J=J$, and keep the nullspace visible.

## Forward and inverse error bars differ

Forward uncertainty propagates a set of inputs through a map:

$$
\mathcal U_y=f(x_0+\mathcal U_x)-f(x_0).
$$

A linear approximation uses $J\mathcal U_x$. The full nonlinear image need not be an ellipsoid, box, or even convex.

Inverse uncertainty starts from observations. It asks which inputs are compatible with them. It is a *preimage*, usually enlarged by model and measurement error.

Using $\Sigma_y\approx J\Sigma_xJ^\mathsf T$ is valid under a declared local linearization and a covariance interpretation of $\Sigma_x$. It cannot replace set-valued uncertainty, discrete mistakes, or unknown dependencies.

A nonlinear inverse can split into multiple branches. An optimizer reporting one solution should not silently erase the other branches.

## Commutative algebra enters through constraints

Geometry can sometimes be represented by polynomial relations.

For a planar rotation, introduce $c=\cos\theta$ and $s=\sin\theta$ as algebraic variables. Then

$$
c^2+s^2-1=0.
$$

Transforming $(x,y)$ gives

$$
u=cx-sy,\qquad v=sx+cy.
$$

The relations

$$
c^2+s^2-1,\quad u-cx+sy,\quad v-sx-cy
$$

generate an ideal in a polynomial ring over the chosen coefficient field.

Now ask useful algebraic questions:

- Which coordinate combinations are possible after eliminating hidden variables?
- Which components of the solution set are physical?
- Where does the Jacobian rank drop?
- What relations among constraints are redundant?
- Does a singular point correspond to an ambiguous inverse or a modeling artifact?
- Can the ideal or its saturation distinguish an intended geometric branch from an extraneous one?

Elimination, primary decomposition, tangent spaces, syzygies, and rank conditions give precise tools for parts of this task.

This does **not** make a real vehicle a single polynomial variety. Material deformation, friction, measurement noise, backlash, and trigonometric parameterizations may require other models. Introducing sine and cosine with the circle relation can encode a rotation, but not every physical constraint becomes exact merely because it is written as a polynomial.

The algebra is useful when it changes what we can prove, calculate, or rule out.

## Singularities and identifiability

Let $F(x)=0$ describe the constraints. At a regular point where $DF(x)$ has locally constant rank, its kernel describes permitted first-order tangent motions.

At a singular point the rank can drop. An extra tangent direction may appear even when the nearby nonlinear set does not contain a corresponding smooth motion.

This distinction matters for a steering mechanism near a special configuration, a statistical model with nonidentifiable parameters, or a rendering of an algebraic surface.

A numerical optimizer can confuse poor conditioning, genuine nonidentifiability, multiple branches, and a bad starting point. Algebraic and differential checks can separate some of these cases.

## A testing ladder

1. **Definitions:** declare each physical coordinate, unit, frame, constraint, and source of uncertainty.
2. **Forward model:** keep the equations, not only fitted numbers.
3. **Derivatives:** verify directional finite differences, symbolic or automatic derivatives, and chain-rule decompositions.
4. **Adjoint:** verify $u^\mathsf T(Jv)=(J^\mathsf T u)^\mathsf T v$ with independently chosen $u,v$.
5. **Rank:** compute singular values and investigate null directions. Record scale choices before judging conditioning.
6. **Second order:** compare Taylor predictions with nonlinear evaluations as perturbations grow.
7. **Inverse:** test local inverse only where justified; otherwise compare pseudoinverse and full feasible-set answers.
8. **Uncertainty:** keep named epsilon sources, known interactions, unknown interactions, and discrete-error hypotheses.
9. **Precision:** repeat the same 364-entry fixture under Float32, Float16, E4M3, E5M2, E3M2, and permitted E5M3 storage.
10. **Observation:** compare predicted and actually measured quantities. Retain residual = observed − reference and the measurement method.

For signed Jacobians, unsigned storage-only E5M3 is not a drop-in replacement. See [E5M3 and memory costs](e5m3-memory-and-nano-optimization.md).

## Why this reaches beyond the car

The same distinctions arise in econometrics:

- observed quantities versus latent parameters;
- local derivatives versus global model structure;
- rank defects and identifiability;
- multiple plausible explanations for one observation;
- uncertainty about measurement, model, and dependencies;
- algebraic constraints that describe which parameter combinations are possible.

A car makes these distinctions tangible. Its Euclidean dimensions, rotations, hinge constraints, and imperfect measurements put abstract geometry next to a physical object.

[Why Eisenbud changed the questions](eisenbud-econometrics-and-geometry.md) records that longer mathematical thread.

## Credit and reading

- **David Eisenbud**, [*Commutative Algebra with a View Toward Algebraic Geometry*](https://link.springer.com/book/10.1007/978-1-4612-5350-1) (1995). The algebraic tools above are established mathematics, not inventions of this project.
- **Mathias Drton, Bernd Sturmfels, Seth Sullivant**, [*Lectures on Algebraic Statistics*](https://link.springer.com/book/10.1007/978-3-7643-8905-5) (2009). A direct bridge between algebraic geometry and statistical inference.
- **Mathias Drton and Seth Sullivant**, [*Algebraic statistical models*](https://arxiv.org/abs/math/0703609) (2007). Polynomial and semialgebraic statistical model structure.
- [Existing uncertainty notes](../statistics-econometrics-and-error-propagation.md).
- [Rotations, frames, and machine representations](rotations-types-to-assembly.md).

The vehicle application and the proposed uncertainty types remain research sketches until definitions, fixtures, and observed measurements support them.
