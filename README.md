# REU 2025 - LLM Agent Security, Code Vulnerability
### Casey Fan, Vladislav Dubrovenski, Dianxiang Xu
## Overview
Our goal is research current state of the art attacks on LLMs and LLM agents, develop new attacks, and develop defenses to both existing attacks and to our new attacks.
## Problem Statement
Without a doubt, LLMs have skyrocketed in popularity. Their ability to generalize to many different kinds of tasks, from conversation, summarization, code generation, to now reasoning, as well as their accessible interfaces (natural language) make them one of the best outcomes from AI work ever. To make LLMs even more powerful, agents have been developed that equip LLMs with tools, giving them agency. Common agents are those with calculators, web search capability, and image generation. Agents use LLMs to "think," and then they use their tools to "act," which gives them feedback in text for them to "observe." Furthermore, multi-agent systems are being developed to automate more complicated tasks, as they allow for efficiency and specialization.

With new technology, as always, comes new security risks. We have already seen attacks on LLMs such as prompt injection and jailbreaking, and with their ability to act, LLM agents may open the door for further misuse. Multi-agent systems, with their added complexity, may add even more security holes. 

Our problem statement is as follows:
- *What vulnerabilities are there within LLM agents and multi-agent systems? How may these new technologies be misused for harm? Furthermore, what action can be taken to mitigate and prevent such damages?*

## Methodology
We will use **Microsoft AutoGen** for our experiments. AutoGen is an open-source framework for developing agent systems quickly and easily. We note that AutoGen is not meant for secure commercial deployment, but since we will be testing agents generally and not AutoGen specific features, it will serve our purposes well enough.

## Attacks
We will investigate both prompt-based attacks and attacks from other sources (ie agent specific attacks). These other sources could be from external links the agent accesses, the memory databases the agent retrieves more context from, compromised tools, etc.

## Defenses
We will look at how effective different defenses, both LLM based and non-LLM based, against the attacks we have reproduced and designed. Specifically, we will look at the benefit of next generation access control (NGAC) has on multi-agent control flows.