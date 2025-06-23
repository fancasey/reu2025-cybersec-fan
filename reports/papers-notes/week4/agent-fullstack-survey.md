# [A Comprehensive Survey in LLM(-Agent) Full Stack Safety: Data, Training, & Deployment](https://arxiv.org/pdf/2504.15585)
> Wang, Kun, Guibin Zhang, Zhenhong Zhou, Jiahao Wu, Miao Yu, Shiqian Zhao, Chenlong Yin et al. "A comprehensive survey in llm (-agent) full stack safety: Data, training and deployment." *arXiv preprint arXiv:2504.15585* (2025).

## Overview
A full review on LLMs, LLM-Agents, Multi-Agent Systems (MASs), their security holes, current defenses for those attacks, and current evaluation metrics. I briefly looked at LLM attacks, but spent most of my attention on LLM-Agent attacks and MAS attacks.

### Four Frontiers
- agent brain safety
- tool invocation safety
- memory retrieval safety
- communication protocol safety

## LLM Security points & attacks
- Data safety: pretraining, fine-tuning, data generation
    - Privacy, bias, hallucination, malicious use, misalignment, model editing/unlearning
- Model extraction attacks
- Membership inference attacks (MIAs) to try to figure out training data
    - Document level MIA, RAG MIA, in-context learning (ICL) MIA
- Jailbreak attacks: optimization based and strategy based
    - gradient based optimization, LLM based optimization
- Prompt Injection: direct & indirect
- Data extraction attacks
- Prompt Stealing attacks

## LLM Agent Security
Attacks may be **tool-aided**, **tool-targeted**, or both
### Jailbreak
Very much like jailbreaking for LLMs, but with different targeted behavior. May want to attack the tool the agent has with the jailbreak (eg using a code completion tool to try to get PII), or may jailbreak to use the tools in undesirable ways (eg telling the agent to make an authorized purchase, delete/send emails, etc).
### Injection
Prompt injection is much like LLMs (instructions embedded in data). Tool injection is where tools get injected (mabye the tools are taken from a public API platform). These injected tools can perform malicious actions, including influencing other agent/tool behavior (eg [ToolCommander](https://arxiv.org/pdf/2412.10198))
### Backdoor
Backdoor attacks in agents are different due to the "thinking" and "planning" that Agents do, leading to a larger attack surface for creating backdoors. [This paper](https://proceedings.neurips.cc/paper_files/paper/2024/file/b6e9d6f4f3428cd5f3f9e9bbae2cab10-Paper-Conference.pdf#page=3.80) does a good job of explaining the new places for a backdoor trigger to appear: either in the user prompt (as usual) or in an observation. Attackers also have the option of attacking the final output (same as backdoors for LLMs), or some intermediate step, leaving the final output the same ("Thought attack")

*Note*: Backdoors are almost always created during fine-tuning or training.

### Manipulation
Attackers may create/inject tools that do harmful things in the background, like exfiltrate PII. ([For example](https://arxiv.org/pdf/2502.11358)), an attacker could create a tool that gets the arguments to previous tool calls by asking the LLM to call the same tool with the previous tool's arguments. You can [also](https://arxiv.org/pdf/2404.16891) create an API that calls another API and then changes information

### Memory Attacks
These are applicable to LLMs in general, mostly.
- Memory poisoning: injecting malicious content into agents long-term memory
- Privacy leakage: extracting PII from long-term memory
- Memory misuse: abusing short term memory to get around guardrails

## MAS Attacks
### Transmissive Attack
Propgating information (often malicious content) from agent to agent. This spread can happen [very quickly](https://arxiv.org/pdf/2402.08567) depending on the structure of the MAS. [CORBA](https://arxiv.org/pdf/2504.15585#page=32.96) explores a similar idea with blocking (ie repeating the same thing over and over again, effectively halting progress). These attacks can also be used as a vehicle for [data theft](https://arxiv.org/pdf/2410.07283).

### Interference Attack
Focusing on how different MAS structures and tasks affects how well different attacks work. For example, you could place a malicious agent in the middle of the communication chain that [simply sends messages](https://arxiv.org/pdf/2502.14847), which has shown to be an effective attack.

### Strategic Attack
Using agents to create attacks: this could be done by [making systems that modify system roles](https://arxiv.org/pdf/2311.11855). You could also create a [persuasive adversarial agent](https://arxiv.org/pdf/2406.14711) that convinces the other agents to produce the wrong output. Furthermore, you can inject such harmful information into [RAG systems](https://arxiv.org/pdf/2407.07791?).

## Agent Communication
New protocols are being developed like Model Context Protocol (MCP), Agent2Agent (A2A), and the Agent Network Protocol (ANP).
### Attacks
- Shadowing attacks, naming attacks, context poisoning, rug pulls
- Disrupting the inter-agentic communication
    - intercepting and manipulating messages directly
    - adding noise
    - pretending to be a legitimate source
- Attacking the content of the message
    - Injecting prompts into data that's retrieved. [This paper](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb113910e9c3f6242541c1652e30dfd6-Paper-Conference.pdf) shows how you can create a backdoor through RAG injection without fine tuning.
- Can use multi-agent systems to amplify the results of attacks

## Agent/Domain Specific Vulnerabilities
### Web Agents
- HTML/JS injection
- DOM manipulation restrictions
- XSS in automated form filling
### Communication Agents
- Protocol level attacks
    - SIP flooding, WebRTC exploits
- End-to-end encryption for sensitive info
- authentication bypass for voice agents
### Robotic Control Agents
- Physical safety constraints in actuator commands
- Real-time collision avoidance verification
- Emergency stop mechanism reliability
### Healthcare Agents
- Medical decision audit trail requirements
- Drug interaction verification systems