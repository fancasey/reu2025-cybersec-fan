# [Fuzzing](https://en.wikipedia.org/w/index.php?title=Fuzzing&oldid=1294289036)
> Wikipedia contributors, "Fuzzing," *Wikipedia, The Free Encyclopedia*, https://en.wikipedia.org/w/index.php?title=Fuzzing&oldid=1294289036 (accessed June 17, 2025).
## Vocab
- **Trust boundary**: boundary between two principals of different "trust" or privilege. Can apply to data and execution (eg getting an untrstued file or changing to root).
- **Random testing/monkey testing**: The testing of random inputs
- **Instrumentation**: Modifying software to learn about it.
## Overview
Fuzzing is a testing technique that involves trying to produce invalid inputs (or inputs that result in bugs). Fuzzers often use **code coverage** as a metric of effectiveness.
## Types of fuzzers
- **Mutation-based fuzzers**: Take some given inputs ("seeds") and change them in random/interesting ways to create semi-valid inputs
- **Generation-based fuzzers**: Are not given seeds. They create inputs from scratch
- **Dumb fuzzers**: Do not have any knowledge on input structure
- **Smart fuzzers**: Have knowledge on input structure.
- **Black box fuzzers**: Do not have any knowledge of the program they are trying to break, and hence don't know code coverage. Often only generates "shallow" bugs. There are attempts of developing black box fuzzers that learn. 
- **White box fuzzers**: Use program analysis to develop inputs. Note that analysis takes time.
- **Gray box fuzzers**: Use instrumentation to learn about the program. Instrumentation gives information about code coverage during fuzzing with less of an overhead than white box fuzzing.

## Other Items
[American Fuzzy Lop: SOTA fuzzer](https://en.wikipedia.org/wiki/American_Fuzzy_Lop_(software))