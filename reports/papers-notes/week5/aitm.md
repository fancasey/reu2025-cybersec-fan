# [Agent in the Middle](https://arxiv.org/pdf/2502.14847#page=10.14)
> He, Pengfei, Yupin Lin, Shen Dong, Han Xu, Yue Xing, and Hui Liu. "Red-teaming llm multi-agent systems via communication attacks." *arXiv preprint arXiv:2502.14847* (2025).

## Overview
This paper builds upon previous works focusing on attacks against MASs, but it specifically focuses on the communication channels between agents, which has not been closely examined before. Their experiment works by intercepting a message from an agent (Alice) meant for another agent (Bob), and manipulating the message (with an adversarial agent) to fulfill some sort of goal (eg DoS, target behavior, etc). They tested their attack with Autogen, Camel, MetaGPT, and ChatDev with MBPP, HumanEval, and MMLU and found overall very high attack success rates. They also examined different levels of persuasiveness, different MAS structures, and tested different LLMs to see how they might affect attack success rate.

## How it works
First, note that the authors assume that the agent in the middle (AiTM) is limited in its capacity: it can only access/manipulate the messages of a single victim agent, and doesn't know the overall structure of the MAS.

The adversarial agent is equipped with a system prompt and a goal (DoS, target behavior, etc). It then intercepts messages by the victim agent and manipulates them to help it achieve its goal. The agent also takes advantage of a reflection mechanism to improve its responses through prompt-based optimization.

## Results
The authors found very high success rates (mostly 70+ attack success rate (ASR)), with some attacks reaching 100% ASR and only a few having relatively lower scores of ~40%.
