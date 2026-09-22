# Making agents smarter about things

Large language models know a little about an enormous number of subjects. That is useful, but it also means they are often surprisingly bad at the concrete details of a particular domain.

Cars are a good example. A model can explain what a control arm is and still give poor diagnostic advice because it does not preserve the sequence of measurements, what each measurement rules out, the difference between a suspected fault and a confirmed fault, or the exact geometry of a suspension adjustment.

The human body has the same problem. A model can repeat anatomy vocabulary while mixing together tissue mechanics, whole-body models, pain, posture, motor control, and claims made by different schools of treatment.

Color is another example. RGB numbers are easy. Color perception, color spaces, local deformations, display behavior, and Josef Albers-style interaction are much less reliably represented.

It is not necessary to train a new model every time this happens.

A much cheaper intervention is to build a small public information store that an agent can retrieve from.

The useful pattern is:

~~~text
good sources
    → inspected notes
    → explicit claims and boundaries
    → reusable examples
    → retrieval
    → a better answer
~~~

The store does not need to contain everything about a subject. It needs to contain the things models repeatedly get wrong, with enough structure that an agent can recover the relevant evidence instead of improvising from memory.

## Automotive diagnosis

[the-twin-pines/ASE](https://github.com/the-twin-pines/ASE) is an automotive diagnosis corpus.

It is organized around the questions that actually matter during diagnosis:

- What does this measurement establish?
- What does it fail to establish?
- What should be tested next?
- Why did replacing the obvious part not fix the problem?
- Is the fault mechanical, electrical, hydraulic, control-side, or load-side?
- Was the suspected fault actually confirmed after repair?

The important unit is not a pile of automotive facts. It is a diagnostic trace:

~~~text
complaint
    → observation
    → discriminating test
    → inference
    → next test
    → confirmed fault
    → repair
    → verification
~~~

That structure gives an agent something much better than a generic summary of an ASE chapter.

Suspension geometry is especially useful because the answer has to remain connected to measurements and physical geometry. The Dodge Dakota camber/caster work is an example of turning messy real measurements into an inspectable model instead of asking a language model to guess what an eccentric cam probably did.

## Musculoskeletal mechanics

[isomorphisms/osteopathy](https://github.com/isomorphisms/osteopathy) is a mechanics-first evidence corpus for reasoning about the musculoskeletal system.

The point is not to collect generic back-pain advice. It is to keep claims attached to the conditions under which they were actually supported:

- species;
- tissue versus whole-body model;
- loading direction;
- load magnitude;
- duration;
- posture;
- measured outcome;
- and the difference between a proposed mechanism and demonstrated evidence.

This matters because language models are very good at blending plausible-sounding explanations together. A retrieval store can instead preserve who claimed what, what mechanism was proposed, what evidence bears on it, and where the evidence stops.

## Color and perception

[walnut-burgundy/albers](https://github.com/walnut-burgundy/albers) collects research and experiments around Josef Albers, color interaction, perception, and computational color models.

Color is a useful case because a model can know the vocabulary while still being weak at the actual relationships among physical display values, color-space coordinates, perceptual context, and mathematical transformations.

Small exact experiments — even one pixel or two adjacent colors — give the agent concrete objects to reason from instead of asking it to synthesize a vague theory of color from pretrained memory.

## Evidence that should not come from model memory

[bl4ckb4ll/blackball](https://github.com/bl4ckb4ll/blackball) applies the same general idea to social, institutional, historical, educational, labor, and economic questions.

Its retrieval path is explicit:

~~~text
question
    → candidate claims
    → evidence
    → source owner
    → scope and time
    → disagreement
    → answer
~~~

For these questions, the failure mode is often not lack of fluency. It is that a fluent model can produce an answer whose provenance and scope are impossible to inspect.

A public evidence corpus makes later answers less dependent on whatever associations happened to be encoded in the model.

## This is deliberately cheap

These projects are not attempts to build a better foundation model.

I am not being paid to retrain a model to understand every subject it handles badly, and there would be little reason for me to attempt that.

The cheaper idea is to notice repeated failures and preserve the missing information in a form that any capable agent can retrieve.

Sometimes that means twenty carefully selected sources. Sometimes it means one diagnostic case with the measurements in the right order. Sometimes it means a small collection of mathematical examples. Sometimes it means a claim ledger that prevents a model from turning a search result or a remembered slogan into evidence.

The marginal cost can be very small compared with model training.

It can also compound. Once the information is public and structured, different models and agents can use the same store. A better future model does not make the work useless; it can simply make better use of the same evidence.

## What makes a useful agent knowledge store

The store should not optimize for volume.

Useful material tends to have one or more of these properties:

- the model repeatedly gets the subject wrong;
- the distinction is easy to lose in ordinary prose;
- the answer depends on measurements or sequence;
- provenance matters;
- competing claims need to remain separate;
- a source has been inspected rather than merely discovered;
- there is a concrete example that can serve as an oracle;
- or the model needs to know when it does not have enough evidence.

The result is intentionally modest.

Do not try to make the model omniscient.

Make it less dumb about the particular thing that matters.
