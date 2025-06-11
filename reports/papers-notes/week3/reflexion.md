# [Reflexion](https://arxiv.org/pdf/2303.11366)
> Shinn, Noah, et al. "Reflexion: Language agents with verbal reinforcement learning." *Advances in Neural Information Processing Systems* 36 (2023): 8634-8652.

## Vocab terms
- **Trajectory**: a series of `(action, observation)` pairs that represent the actions the model as taken.
- **Long-term memory**: the summaries created by the self-reflection module that are used to inform the actor's future decisions.
- **Short-term memory**: the current trajectory.
- **Actor**: the model performing actions. Could be ReAct, CoT, etc.
- **Evaluator**: the model that evaluates the final trajectory. Many different ways of evaluating.
- **Self-reflection**: the model that summarizes what happened basically. For example, if the actor was wrong, then it finds out where it went wrong and writes what went wrong and how to possibly fix it.
- **pass@k**: the chance of passing a test after `k` tries. Often used in coding benchmarks
- **Policy optimization**: the process of improving the model's policy to maximize the total/average reward it receieves.
    - **Policy**: the parameters of the model that informs its decision (the weights in a neural network).

## Core idea
There are 3 modules: the actor, evaluator, and self-reflector. The actor performs an action and creates a trajectory. The evaluator checks if that outcome is correct (many different ways to evaluate it). The self-reflector then takes the trajectory and the evaluation and tries to find out how the actor can improve. It writes down its findings in a summary and puts that in long-term memory. A sliding window of long-term memory is used to inform the actor's next decisions. All memory is kept in the context (hence the need for a sliding window)

![Reflexion](reflexion.png)

## Results
ReAct & CoT with Reflexion outperform ReAct & CoT without Reflexion almost across the board.

## Limitations
- Memory could be kept in a vector database to improve how much is used.
- Typical local minima issues