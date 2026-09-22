# Small useful software

Some software should simply be cheap enough to give away.

A flashlight. A spirit level. A Unicode picker. A text pad. A tiny statistics program. A price lookup. A shopper app for a neighborhood store.

None of these needs to become a venture-backed platform.

If the program is small, understandable, and cheap to produce, the natural price floor is often zero.

That matters for users.

It also matters for small businesses.

## Give the small shop some of the software advantage

A large company can afford an internal software team, custom mobile apps, data analysis, inventory systems, customer-facing interfaces, and integrations.

A pizza place, independent auto garage, hardware store, corner store, produce market, or food truck usually cannot.

That difference has nothing to do with whether the small business is good at making pizza, repairing cars, stocking bolts, or selling vegetables.

It is a software-capital advantage.

Cheap software can narrow that gap.

The goal is not to build one enormous "small business platform."

It is to make ordinary capabilities cheap enough that a small operator can use them without needing a software department.

That might mean:

- a simple customer catalog;
- a cart;
- current prices and availability;
- a mobile-friendly menu;
- a tiny appointment or queue tool;
- a useful diagnostic record;
- a small reporting program;
- a command-line import/export tool;
- or one narrowly useful phone utility.

The application can be specific because the cost of producing another application is falling.

## Green Grocer

The current Green Grocer work lives on the `green-grocer` line of [Ashtray-Archer/utilities-android-phone-user](https://github.com/Ashtray-Archer/utilities-android-phone-user).

Its current specimen is deliberately small:

~~~text
browse
    → inspect product
    → add to cart
    → view cart
    → change quantity
    → remove
    → continue shopping
~~~

At this stage it is a shopper-flow and rendering/type-design specimen, not a claim of finished production retail software.

That narrowness is useful.

It gives us a concrete place to work out what a product is, what a cart is, which values are fundamental, which values are derived, how state changes, how the phone rerenders, and how a high-level domain description survives into an actual application.

The broader economic motivation remains straightforward:

**a small independent store should not need Kroger's software budget to have a competent customer-facing phone experience.**

The same architecture can later be tested against a hardware store, a garage, a restaurant, or another small seller without pretending they all have the same business model.

## Tiny phone utilities

[utilities-android-phone-user](https://github.com/Ashtray-Archer/utilities-android-phone-user) contains another useful class of specimens: small Android programs that do one understandable thing.

Examples include:

- accelerometer viewing;
- a spirit level;
- mathematical-character entry;
- clipboard access;
- hardware/sensor experiments;
- and small text-oriented utilities.

These programs are valuable even when the feature itself is ordinary.

Everybody already understands what a level or clipboard tool is supposed to do.

That makes them unusually good tests for a programming language.

There is nowhere for the implementation to hide behind novelty.

If the language makes a simple tool difficult to understand, difficult to package, or difficult to connect to the phone, that is evidence against the language.

## Cheap data analysis

[Econometrician](https://github.com/bl4ckb4ll/econometrician) follows the same principle in statistics.

It does not try to be a universal statistics environment.

Its first programs are narrow, deterministic procedures with explicit input contracts and inspectable output.

That is useful to somebody who needs the calculation.

It is also a strong language test.

A statistics program forces us to care about:

- numeric representation;
- dimensions and shapes;
- validation;
- exact versus approximate calculation;
- named assumptions;
- structured input and output;
- failure conditions;
- and whether the source still looks like the statistical procedure being performed.

Those are precisely the boundaries a readable systems language should handle well.

## Small command-line programs

[Idriç CLI](https://github.com/isomorphisms/idric-cli) collects small command-line programs around real services and data sources.

A tiny CLI client is another excellent specimen because very little application framework is needed to obscure the language.

A program may only need to:

~~~text
read request
    → validate values
    → call one service
    → decode response
    → select useful fields
    → print a result
~~~

That path exercises text, bytes, networking, errors, structured data, authentication boundaries, and process behavior without requiring a large application.

A language that claims to be practical should make these small programs pleasant.

## The apps are also tests for the language

This is the second purpose of all of this work.

The goal is not merely to produce a large pile of applications.

Each application should force the language through another real boundary.

A useful test portfolio might include:

- sensor input;
- touch input;
- graphics;
- ordinary forms and state;
- lists and scrolling;
- local files;
- networking;
- APIs;
- structured data;
- numerical analysis;
- exact money;
- compact binary representation;
- text editing;
- process execution;
- command-line composition;
- Android packaging;
- direct machine code;
- DEX;
- GPU code;
- and constrained embedded targets.

If Idriç works beautifully for one mathematical demonstration but becomes ugly as soon as it has to display a grocery cart, that is a problem.

If it handles Android sensors but needs a giant foreign-language wrapper to parse a small web response, that is a problem.

If high-level source looks clear but the route to the machine destroys its meaning, that is a problem.

The little programs keep exposing those failures.

## High level and low level should meet cleanly

The language project is trying to reject an old tradeoff.

We should be able to write:

~~~text
add product to cart
read acceleration from sensor
calculate chi-square statistic
write response to connection
~~~

and still retain precise control over:

- representation;
- allocation;
- numeric width;
- bytes;
- system calls;
- device interfaces;
- executable format;
- and target-specific lowering.

The high-level description should not merely be a pleasant wrapper around an unrelated implementation.

The transformations between the high-level operation and the low-level machine work should themselves be inspectable.

Small programs are ideal for testing that claim because the whole path can still fit in a person's head.

## Zero price is part of the experiment

If software becomes dramatically cheaper to produce, some existing prices should be pushed downward.

For small, reproducible utilities, the endpoint may simply be free software.

That creates several useful pressures:

- remove unnecessary dependencies;
- reduce hosting requirements;
- avoid subscriptions where no ongoing service is needed;
- make local/offline operation normal where practical;
- let another person inspect and modify the source;
- and make deployment cheap enough that a tiny organization can actually use it.

A free program is not automatically a good program.

But when the cost of distribution is nearly zero and the software does not require an expensive continuing service, zero is a real competitive price.

## Not an app factory

The target is not "generate ten thousand apps."

Most possible apps are useless.

The useful loop is narrower:

~~~text
find a small thing that should exist
    → build the smallest coherent program
    → make it useful
    → make it inspectable
    → test it on real hardware or real data
    → learn what the language still does badly
    → improve the language
    → make the next program cheaper
~~~

That loop can produce public goods and language research at the same time.

The small business gets software.

The phone user gets a useful tool.

The language gets another hostile real-world test.

And every time the language improves, the cost of producing the next useful little program falls again.
