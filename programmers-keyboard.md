# Programmer's keyboard

Programming languages were designed under input constraints.

QWERTY keyboards, typewriters, ASCII-era character sets, teletypes, terminal conventions, and the desire to type everything with a small familiar set of keys all shaped programming notation.

Those constraints produced some durable conventions.

They also produced a lot of overloaded punctuation.

There is no reason the input device itself has to remain frozen.

[programmers-keyboard](https://github.com/isomorphisms/programmers-keyboard) starts from the opposite direction:

> what operations does a programmer actually perform, and what keys should exist for them?

## Organize keys by function

The current design groups keys into semantic families:

- cursor and page movement;
- process signals and control;
- mathematics;
- classic programming notation;
- regular-expression concepts;
- concept separation;
- command/incantation assistance;
- paste buffers;
- paired delimiters and quotes.

That is already a different design method from "take QWERTY and add a few symbols around the edges."

The keyboard is allowed to be a professional tool designed around the work.

## Stop making one glyph do five jobs

Programming notation repeatedly overloads scarce punctuation.

The existing keyboard notes make the problem concrete.

For example, `*` may mean:

~~~text
multiply
dereference
pointer type
splat / unpack
wildcard
~~~

depending on language and context.

Quotes and apostrophe-like marks have similarly accumulated roles across languages: strings, characters, primes, lifetimes, quoting, shell syntax, contractions inside text, and more.

Square, round, angle, and curly delimiters are overloaded too.

Some of this ambiguity is useful local convention.

Some of it exists because designers were rationing convenient keyboard characters.

A better keyboard does not force a language to keep doing that.

## Use the notation that expresses the idea

If multiplication means multiplication, `×` is available.

If division means division, `÷` is available.

If the relation is `≤`, type `≤`.

If the operation is composition, `∘` is available.

If a definition is being made, `≝` can say so.

If a language distinguishes assignment from equality, it can use different symbols rather than relying entirely on context.

If a paired construct is common, one key action can insert both delimiters and leave the cursor between them:

~~~text
⟦|⟧
“|”
«|»
~~~

The question should be "what notation communicates the operation?" before "which ASCII punctuation is easiest to reach on a U.S. typewriter layout?"

## This does not require changing ASCII

The point is not to redefine byte values.

The keyboard can emit ordinary Unicode text, existing control sequences, or conventional ASCII where compatibility requires it.

Programs, files, terminals, and protocols can continue to exchange standardized encodings.

The input layer can still be better.

That is an important distinction:

~~~text
better human input device
        ≠
invent a private character encoding
~~~

## Regular expressions deserve conceptual keys too

Regular expressions are a good example of an interface that became an incantation language.

The current keyboard notes identify operations such as:

- start of line;
- end of line;
- any character from a class;
- ordered group;
- greedy capture;
- non-greedy capture;
- letter;
- number;
- control character.

Those concepts can be surfaced directly.

An expert can still see or edit the underlying regex notation.

But the physical interface does not need to pretend that remembering punctuation is the essence of regular-expression work.

## Completion is part of the keyboard

The keyboard is not only glyph entry.

The current categories include:

- complete;
- finish the current incantation;
- search command history.

That is important.

A programming keyboard can participate in the language environment.

It can know that the user is completing a name, inserting a paired form, searching previous commands, moving structurally, or operating on a paste buffer.

Physical keys, editor actions, language services, and shell completion can be designed together instead of as unrelated historical layers.

## The keyboard and the language can co-design each other

Idriç deliberately uses notation such as:

- `←`;
- `→`;
- `⇒`;
- `=`;
- `≠`;
- `≟`;
- `≝`;
- `∘`;
- mathematical minus.

A language is much easier to design around meaningful notation when typing that notation is not a nuisance.

The reverse is also true.

A keyboard becomes easier to design when the language can say which operations actually deserve direct representation.

That makes the keyboard another part of the app/language factory: language design exposes missing input operations, and the input device makes better language notation practical.

## Hardware should be allowed to improve

The repository already contains a routed twelve-key movement-keypad prototype with RP2040 and USB-C hardware.

That is deliberately small.

The point is to test the physical path instead of treating the keyboard as a permanently hypothetical layout.

Switch feel, matrix design, firmware, enclosure geometry, key grouping, legends, modifiers, and host integration can all be tested.

There is no requirement that one prototype be the final keyboard.

Trying several designs is cheaper than spending another generation assuming the inherited one is optimal.

## The broader principle

Computing has a tendency to fossilize successful accidents.

Unix was successful.

ASCII was successful.

QWERTY was successful.

C was successful.

That does not make every interface decision around them optimal forever.

Compatibility matters.

So does improvement.

The useful approach is conservative at the machine boundary and aggressive at the human boundary:

~~~text
keep interoperable encodings and protocols
        +
redesign the interface people actually have to use
~~~

A programmer uses the keyboard every day.

It is worth designing one for programming.
