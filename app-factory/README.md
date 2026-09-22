# App factory

The project is to build a **factory for software**.

The individual applications matter, but they are not the deepest object being built.

The deeper object is a system that can repeatedly turn a small, well-stated need into a real program while keeping the result easy to understand, easy to inspect, easy to test, easy to diagnose, and cheap to reproduce.

Speed matters.

But speed comes after architecture.

A factory that produces wrong software quickly is not a good factory.

## The target

The desired path is something like:

~~~text
human intention
    → explicit domain model
    → readable program
    → checked transformations
    → target-specific lowering
    → executable artifact
    → behavioral evidence
~~~

Every arrow should be inspectable.

When something goes wrong, it should be possible to tell **where** it went wrong.

Was the request misunderstood?

Was the domain model wrong?

Was a semantic distinction erased?

Did lowering change the meaning?

Did the target backend mishandle a representation?

Did packaging fail?

Did the program run correctly but fail to satisfy the actual user need?

The factory should make those questions easier, not hide them behind another layer of automation.

## Correctly, not merely quickly

Current AI systems make it easy to generate a lot of code.

That is not the same thing as making software cheap.

Wrong code is expensive.

A misunderstood feature is expensive.

A plausible-looking implementation that cannot be inspected is expensive.

A change that requires five more model turns, three more builds, and another round of debugging is expensive.

So the useful production rate is not:

~~~text
applications generated per hour
~~~

It is closer to:

~~~text
accepted useful applications
----------------------------
total human and machine work
~~~

The factory should optimize that quantity.

## Inspectability is factory infrastructure

Readable source is not a cosmetic feature of the output.

It is part of the production machinery.

A factory is easier to improve when the generated or authored program visibly states:

- what objects exist;
- what operations mean;
- which values are fundamental;
- which are derived;
- what invariants hold;
- which conversions lose information;
- where the operating-system boundary is;
- where storage begins;
- where a target-specific representation appears;
- and what evidence establishes that the program works.

That is why the Idriç, RHS, direct-backend, testing, and acceptance work belongs inside the app-factory project rather than beside it.

## High level to low level without losing the plot

The factory should be able to start with a statement such as:

~~~text
add product to cart
~~~

and eventually emit machine behavior without turning the intervening layers into an archaeological dig.

Likewise:

~~~text
read acceleration from sensor
calculate chi-square statistic
copy text to clipboard
fetch delivered price
show current queue
~~~

The source should retain the high-level meaning.

The backend should retain low-level control.

The path between them should be explicit enough that a person or an agent can follow it.

That is the architectural problem.

## A growing acceptance suite made of real programs

The applications produced along the way are the factory's acceptance suite.

Different programs force different capabilities into existence.

For example:

- a spirit level exercises sensors, geometry, state, and rendering;
- Programmer's Unicode Picker exercises text, glyphs, clipboard integration, and native Android UI;
- Green Grocer exercises lists, touch, scrolling, money, derived totals, ordinary business state, and rendering;
- Econometrician exercises mathematical procedures, contracts, structured input, numerical behavior, and deterministic output;
- API clients exercise networking, authentication boundaries, structured data, and command-line composition;
- graphics experiments exercise GPU paths;
- tiny hardware programs exercise direct machine and device boundaries;
- browser work exercises durable state, indexing, sessions, and large persistent corpora.

A capability is much more convincing when several unrelated applications use it successfully.

## The factory should generalize

A bad app generator solves each new program with a new pile of exceptions.

A good factory discovers reusable structure.

If Green Grocer needs a list, that list machinery should help the next app.

If the accelerometer needs a compact direction representation, the same geometry should be reusable wherever the semantic object is actually a direction.

If several programs need structured command-line roles, the shell and language should learn that abstraction instead of copying parsers.

If several Android programs need the same clipboard or sensor boundary, that boundary should become a small reusable facility.

The applications should pull common structure into the factory.

They should not all become one framework.

## Assume apps themselves are worth zero

The factory is being designed under a strong economic assumption:

**ordinary applications should be treated as commodities whose sale price tends toward zero.**

That does not mean every service in the world is free.

Servers, scarce compute, physical goods, payment processing, human labor, support, logistics, and specialized continuing operations still cost money.

But merely possessing a small executable should not be presumed to support a business model.

Designing under that assumption is useful even if reality is messier.

It forces the production system to become cheap.

It encourages local and offline operation where possible.

It discourages unnecessary recurring infrastructure.

It makes free distribution a normal outcome rather than a special charitable case.

And it makes software capability available to people and small organizations that cannot buy custom development.

## The economic output is the factory

If one app is free, that is useful.

If a factory can produce the next hundred useful apps at very low marginal cost, that is more important.

A neighborhood grocer does not need to become a software company.

A mechanic does not need a mobile development team.

A teacher should not need venture funding for one interactive mathematical diagram.

A person who wants a better spirit level should not need a subscription.

The factory absorbs the software complexity so the application can stay small.

## Do not hide failures behind generation

The factory should fail in informative ways.

Unsupported language behavior should be rejected clearly.

A failed backend should not silently fall back to another compiler.

A model suggestion should not become accepted state without evidence.

A test should claim only the boundary it actually exercised.

Generated artifacts should retain enough provenance to reconstruct how they were produced.

If an application is wrong, the system should help answer why.

That matters more than how impressive the generation demo looked.

## The compounding loop

The long-term loop is:

~~~text
build factory
    → emit useful app
    → expose missing capability
    → improve language / runtime / tools
    → emit broader class of apps
    → expose deeper structural problem
    → improve factory again
~~~

The point of the early applications is partly that they are obvious.

Everybody knows roughly what a text pad, spirit level, store cart, command-line client, or small statistics program should do.

That makes them good calibration instruments.

Once the factory can produce ordinary software cleanly, correctly, and inspectably, making more things becomes the easy part.
