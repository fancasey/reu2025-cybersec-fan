# [Testing Different MASs' Resilences](https://arxiv.org/pdf/2408.00989#page=3.95)
> Huang, Jen-tse, Jiaxu Zhou, Tailin Jin, Xuhui Zhou, Zixi Chen, Wenxuan Wang, Youliang Yuan, Maarten Sap, and Michael R. Lyu. "On the resilience of multi-agent systems with malicious agents." *arXiv preprint arXiv:2408.00989* (2024).

## Overview
This paper looks at how faulty agents affect different MASs on different downstream tasks. It looks at two different types of faulty agents, **AutoTransform** and **AutoInject**, and tested them on different system types (hierarchy, linear, flat), as well as different downstream tasks (math, coding, MMLU, etc). They found that hierarchical structures are the most resilient against attacks. There are also many details of the paper that are worth mentioning.

## Background

### AutoTransform
AutoTransform works by transforming the profile of agents (through their system prompt), telling the agents to subtly introduce errors. This attack method is hard to control/manage explicitly.

### AutoInject
AutoInject intercepts agent messages and directly introduces errors. The researchers use 2 metrics: 
- $P_m$ describes the proportion of messages that are faulty
- $P_e$ describes the proportion of faultiness within each message (eg number of faulty lines of code over total number of lines)

### Error Types
The paper also distinguishes between syntactic errors (invalid logical structure) and semantic errors (valid logical structure, but invalid meaning).

## Results
- Hierarchical was the most resilient to faulty agents, followed by flat, and finally followed by linear.
    - The researchers suggest that centralized decision making allows for better error correction
    - They also found that faulty 'lead' agents led to more errors than faulty 'assistant' agents
- AutoInject does better than AutoTransform on ChatGPT 3.5, other way around for ChatGPT 4o.
    - The researchers attribute AutoTransform's worse behavior to limits on context length. They believe the original prompt to subtly introduce errors gets lost after multiple instructions afterward.
    - The researchers also claim that since AutoTransform does not have strict error implementation requirements and is required to make its errors stealthy, it ends up produce fewer errors.
    - When the LLM is better, these two issues are mitigated for AutoTransform
- Tasks that require formalization are less resilient.
- MASs often outperform single agents, but underperform when agents are faulty
    - Sometimes, faulty agents actually improve performance in MASs due to [divergent thinking](https://arxiv.org/pdf/2305.19118) and because 
    - Subjective tasks see less improvement, as errors are not as explicitly defined (and harder to catch)?
- \# of faulty messages drops performance more than \# of errors within a single message
- Syntactic errors lead to greater performance drop than semantic errors
    - The researchers say that this is probably because models are trained on things that are almost always syntacticly correct, and that semantic meaning is harder to extract/analyze
- Comments can create (false) trust
    - Erroneous lines of code with comments saying they are correct/fixed do not get detected as much as the same lines without the comment
- Number of rounds does not necessarily lead to improved performance

## Defense
They propose a "challenger," which is a 'good' version of AutoTransform (urges agents to look at what thye are given from other agents more critically), as well as an "inspector," which is a 'good' version of AutoInject (intercepts messages and checks them for errors). They found these two defenses lead to recovering 96.4% of performance.
