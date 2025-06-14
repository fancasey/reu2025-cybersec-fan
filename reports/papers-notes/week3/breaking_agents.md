# [Breaking Agents](Breaking-Agents-Compromising-Autonomous-LLM-Agents-Through-Malfunction-Amplification.pdf)
> Zhang, Boyang, et al. "Breaking agents: Compromising autonomous llm agents through malfunction amplification." *arXiv preprint arXiv:2407.20859* (2024).
## Vocab terms
- **Evasion attack**: A type of adversarial example that is specifically made to avoid detection by LLM security systems.
- **Adversarial demonstration**: Purposefully providing incorrect examples to change LLM behavior.
- **Attack surface**: All possible entry points for an attacker.
- **Agent emulator**: use an LLM to create a virtual environment that simulates agent actions
- **Adversarial ratio**: A measure of "disturbance" of an attack. The ratio of the attack prompt to the instruction prompt.
- **Self-examination**: A type of defense where the LLM asks itself a prompt could be harmful.

## Overview
Many LLM agent attacks focus on extracting information or performing harmful action. The authors of this paper state that this is realistically handled, as many systems that require sensitive information or impactful action require more confirmation, and LLMs can be very good at detecting these kinds of malicious behavior. They instead propose a type of attack meant to deny service, either through an infinite loop or incorrect function call.

## Attacks
There are two attacks: one that is meant to cause an infinite loop, and one that is meant to lead to an incorrect function. Both are meant to cause the agent to malfunction.
### Basic vs advanced attack
The authors first launch these attacks on a single agent. They use an agent emulator for their attacks. They then go on to attempt the same attack on a multi-agent system, using a compromised agent to spread their attack to the other agents in a viral manner.
### Attacks
The authors consider multiple different attack strategies: prompt injection, adversarial perturbation, and adversarial demonstration. For adversarial perturbation, they tried SCPN (a paraphraser), VIPER (replacing characters with similar looking ones; eg s with $), and GCG (a gradient based prompt optimizer; they used an open-source model to optimize GCG and transferred the results to their tests).
### Attack Surfaces
The authors placed their attacks as user input, through intermediate outputs (eg email for email agent, within a file for a CSV agent), and in memory. When placing in memory, the authors considered the scenario in which previous successful attacks were in memory and when the attacker had control of the memory and would place their attacks into the memory.

## Results
Prompt injection was the most effective attack strategy. As for malfunctions, infinite loops were sometimes more effective, and incorrect function calls were sometimes more effective. Intermediate outputs were mostly less effective than direct user input, and memory was also relatively uneffective. The authors found very good results on multi-agent systems, especially when testing with agents of different types. They also considered varying number of toolkits, but didn't find many differences. They also found the core model affected results, with more sophisticated models better at fending off against attacks of all types.

## Defenses
Self-examination is a common defense mechanism against the more studied types of attacks against LLMs (eg performing harmful actions, getting/using PII, etc), but these attacks manage to get past classical self-examination techniques. The authors propose a modified self-examination prompt specifically to detect whether a prompt might lead to malfunction, and found it was able to perform better than the standard self-examination, but still with relatively poor results.