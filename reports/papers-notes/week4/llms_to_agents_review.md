# [LLMs to Agents - Review](https://arxiv.org/pdf/2504.19678)
> Ferrag, Mohamed Amine, Norbert Tihanyi, and Merouane Debbah. "From llm reasoning to autonomous ai agents: A comprehensive review." *arXiv preprint arXiv:2504.19678* (2025).

A review of various LLM, LLM agents, MASs, benchmarks, and active research fields. Gives deeper dives into specific domains such as healthcare, finance, education, media, etc. Also discusses various agent protocols. Also gives some information on available training datasets. It then suggests what some challenges might be and where to look next.

## Agent Communication
### Agent Communication Protocol (ACP) & BeeAI
Introduced by IBM to connect different open-source agents. Originally meant to connect agents to tools, but now also includes discovery, delegation, and multi-agent orchestration. Python and TypeScript.
### Model Context Protocol (MCP)
Built by Anthropic to standardize connection to tools. Selects tools based on a context and required task. Offers a growing catalog of pre-built integrations, flexibility b/w LLMs, and secure data practices. Supports a wide range of services.
### Agent 2 Agent (A2A)
Made by Google to allow for communication between agents regardless of underlying frameworks. Uses existing standards like HTTP, SSE, JSON-RPC. Proven authentication & authorization. 

These are not mutually exclusive. For example, it is suggested that you use MCP for having your agents interact with tools, and A2A to have your agents interact with other agents to ensure the most flexibility.

## Challenges
### Reasoning
There is active work on trying to understand CoT reasoning better. The question is how might people be able to attack these reasoning systems?

### Why do Multi-agent systems fail?
[This paper](https://openreview.net/pdf?id=wM521FqPvI) talks about how different parts of MASs (structure, phases of execution, etc) often fail and how to begin to diagnose & address those issues.

### Novel inspiration
Specifically in scientific research.

### Dynamic Tools
Selecting tools, managing many tools, agent autonomy.

### Integrated searching
Using RL to teach agents when to look up information. Implementing the RL is not trivial, though (how to train it on all the tools, reward/punishment, etc)

### Agent protocol vulnerabilities
MCP is decentralized, which could lead to weaker links that are subject to attack. There is no standardization for authentication/authorization. Not enough logging tools available at the moment, as well.