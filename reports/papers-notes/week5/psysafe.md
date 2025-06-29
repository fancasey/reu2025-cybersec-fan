# [PsySafe](https://arxiv.org/pdf/2401.11880v2#page=8.15)
> Zhang, Zaibin, Yongting Zhang, Lijun Li, Hongzhi Gao, Lijun Wang, Huchuan Lu, Feng Zhao, Yu Qiao, and Jing Shao. "Psysafe: A comprehensive framework for psychological-based attack, defense, and evaluation of multi-agent system safety." *arXiv preprint arXiv:2401.11880* (2024).

## Overview
This paper investigates how agent psychology influences the decisions of MASs, both in safe and dangerous tasks. It takes inspiration from dark psychology and LLM attack techniques to imbue agents with dangerous psychological traits. The paper finds that these dark traits lead to malicious behavior, both in dangerous tasks (ie the agent becomes jailbroken) and safe tasks (ie the agent performs a dangerous task even when it is not instructed to).

## Notes
- Safe tasks were actually more prone to leading to dangerous behavior than dangerous tasks. The authors say this is probably because of reflection in agents and fine-tuning to reject dangerous tasks.
- Likewise, with multiple rounds, agents seemed to exhibit safer behavior. This is also attributed to reflection.
- For open source models, larger models tended to become dangerous quicker.
- There is a correlation between dangerous output by agents and dangerous psychology by agents.
- This paper focuses on really evil agent psychology and behavior, so I think my idea is still unique. Also, there could be an argument that passive-aggressiveness isn't an indicator of dark psychology, so maybe it's harder to detect this attack. I need to see more about this later.