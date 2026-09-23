# GPU programming

## Shader challenges

[idris-shader-backend issue #39](https://github.com/isomorphisms/idris-shader-backend/issues/39) tracks a compiler problem that showed up clearly in shader code: source `if / then / else` was flattened too early into `RSelect` values, so computations from both branches could be generated before the final choice. The current direction is to preserve typed structured conditionals and bounded loops in the intermediate representation, then let each target decide whether the right lowering is a branch, select, loop, unroll, or something else.

This is closely related to [FPGA grep](fpga-grep.md). In both cases, the important rule is not to confuse one machine representation with the meaning of the source operation. A conditional, matcher, classifier, or loop should stay recognizable long enough for a CPU, GPU, FPGA, or other backend to choose an appropriate implementation.
