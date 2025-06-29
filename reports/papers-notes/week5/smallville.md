# [Simulating Human Behavior with LLMs](https://dl.acm.org/doi/pdf/10.1145/3586183.3606763#page=12.97)
> Park, Joon Sung, Joseph O'Brien, Carrie Jun Cai, Meredith Ringel Morris, Percy Liang, and Michael S. Bernstein. "Generative agents: Interactive simulacra of human behavior." In *Proceedings of the 36th annual acm symposium on user interface software and technology*, pp. 1-22. 2023.

## Overview
This paper describes a simulation (like the Sims) to see how well LLMs/LLM agents can simulate human behavior. It seems to focus on how LLMs can be used for non-playable characters (NPCs) in videogames, but the results on how the agents interact is still worthwile. It's also worth noting that this paper is relatively old (2023) and used ChatGPT turbo 3.5, so the results may not be the same if reproduced today.

The researchers created 25 agents to interact in a simulatino of a village in 2 days. They unique prompts (personalities, so to speak) for each agent, and told one agent about a Valentine's day party and another agent about an election going on. Agents were equipped with memory, reflection, and planning capabilities. 

## Notes
- Information spread pretty well. After a couple of days of simulation, knowledge about the party and the election both spread to about 50%.
- Agents seem to embellish their memories. It's worth noting that outright hallucinations were rare, but agents would sometime add details that weren't true.
- Making memory larger was a challenge. It seems like the paper didn't use RAG, so this might not be an issue anymore.
- Agents are fine-tuned to be especially nice and formal. This may make it harder to form attacks. Alternatively, I could fine-tune models that are not so nice and create adversarial agents from those. This does seem like a bigger task, so I'll try to defer it as late as I can.
- Agents also sometimes misunderstood–or weren't able to make correct associations between–what certain locations/objects were. For example, they kept on treating (private) dorm bathrooms as if they were for multiple people.