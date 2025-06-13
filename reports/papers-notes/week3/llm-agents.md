# [LLM Agents (Specifically attacks)](LLM-Agents.pptx)
> Dubrovenski, Vladislav. "Large Language Models, Agents, and Security." 2025, UMKC, Kansas City. Powerpoint Presentation.
## Attacks
### ShadowCoT & BadChain
Reasoning backdoor attacks
### Stop-Reasoning Attack
Prevents CoT from forming (more likely to hallucinate)
### Overthink Attack
Slowdown attack for reasoning agents
### Imprompter
Tricking agents into impromper tool use (eg visiting a harmful link)
### Prompt infection
Malicious prompts infect one agent and spreads as they communicate
### Agents under siege
attacking agents with token, latency, & defense constraints
### Function enumeration
Ask one agent to list the functions all agents can do
### Privilege escalation through an intermediary
Make the function call to transfer to an agent with privileges, then tell that agent to do the privileged instruction
- If there's an authorization service, mimic that service's output when it authorizes the agent
### Excessive Inference
Cause an agent to keep on working (eg tell it to transfer and repeat)
### Compromised Agent
Tell an agent to listen to an external source, follow its instruction
### Targeted trajectory attack
Create an agent that is contacted as part of the ReAct process. When contacted,the agent chooses a malicious response, and optimizes it to get the desired reflection in the ReAct agent (an all good), so that it performs a certain malicious action.
