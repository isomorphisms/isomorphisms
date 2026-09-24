# Icky, functorial C

[ICK](https://github.com/dilapidated-shed/ick) is a GCC-derived C compiler.

By **Icky C** I mean C compiled by ICK. It does not prescribe a coding style. Write short names, long names, procedural C, function-heavy C, or whatever else is appropriate. The important part is that the compiler is open to a larger programming alphabet than historical ASCII C.

By **functorial C** I mean my own preferred style: named functions calling named functions, explicit data flow, composition where it helps, and long descriptive names when they make the program easier to inspect. That style is independent of ICK.

**Icky, functorial C** is simply the combination: that function-oriented style, written through ICK's less artificially restricted source notation.

## Stop spelling obvious symbols indirectly

Some notation questions are genuinely design questions. Others are not very mysterious.

We have written these symbols on paper for a long time:

```text
λ   ≟   ≠   →   −   ²   √   ×
```

There is no good reason for a modern programming language interface to force all of them back through ASCII approximations.

- `λ` can mean the lambda-calculus lambda directly.
- `≟` can ask whether two things are equal.
- `≠` can mean not equal.
- `→` can be an arrow instead of the two-character drawing `->`.
- `−` can be a minus sign rather than a hyphen pressed into mathematical service.
- `²` and other useful superscripts can express powers directly where that notation is appropriate.
- `√` can say square root directly.
- `×` can say multiplication directly.

This is not a claim that every piece of mathematical notation belongs in source code. It is a claim that when programmers already mean one of these ordinary things, the source should be allowed to say it.

## One character should not have to do every job

The ordinary C `*` is a simple example.

It is used for multiplication:

```c
a * b
```

It participates in pointer declarations:

```c
thing *p
```

and it dereferences a pointer:

```c
*p
```

Elsewhere in programming, repeated stars such as `**` are also used for exponentiation.

We do not need to keep piling unrelated meanings onto the same small ASCII inventory. Multiplication can be `×`. Powers can use superscripts where that is clear. That leaves room to improve pointer and dereference notation later instead of pretending the current punctuation is the final design.

The same principle applies more broadly: the fact that an ASCII workaround became conventional is not evidence that it was the best notation.

## The narrow claim comes first

ICK can also be a place to try more experimental ideas. Definition notation, pointer notation, parentheses, commas, semicolons, tildes, backticks, richer mathematical alphabets, and numeric notation all have real design choices in them. I do not need to pretend those questions are settled.

For example, a definition spelling such as `=def` can be made available experimentally without claiming that everybody should trust it immediately or that it belongs in every program.

That uncertainty is different from the easy cases.

Using `≠` for not equal is not a radical language-design thesis. Using `≟` for an equality question is not a radical thesis. Using `λ` where the source means lambda is not a radical thesis. Using an actual arrow when the source means an arrow is not a radical thesis.

We should have stopped writing some of these ASCII approximations years ago. ICK makes it cheap to stop now.

## Typing is not the bottleneck anymore

A special keyboard is useful, but it is not required.

The [programmer's keyboard](https://github.com/isomorphisms/programmers-keyboard) is an attempt to give frequently used programming and mathematical symbols physical keys. A software keyboard can do the same thing. Editors can insert Unicode. A small input method can do it.

And with vibe coding, an assistant can simply write the characters into the source.

That changes the tradeoff. The important question is less often "how many keystrokes does this character take on a stock QWERTY keyboard?" and more often "is the resulting program easier to inspect?"

Readable source is valuable even when a human did not type every character manually.

## Related experiments

The same general idea is being explored outside C:

- [IR](https://github.com/isomorphisms/ir) allows notation including `←`, `→`, `λ`, and `≟` in R.
- [i-thon](https://github.com/dilapidated-shed/ithon) experiments with readable assignment-arrow syntax in Python.
- [ICK](https://github.com/dilapidated-shed/ick) is the GCC-derived compiler line for doing this work in C.

These projects do not need to converge on one grand notation theory before the obvious improvements are useful.

The immediate proposal is much smaller:

**stop hamstringing source code with an obsolete character budget when the intended symbol is already clear.**
