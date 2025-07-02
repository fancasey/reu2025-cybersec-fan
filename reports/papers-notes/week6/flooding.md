# [Flooding Spread of Manipulated Knowledge](https://arxiv.org/pdf/2407.07791?#page=1.94)
> Ju, Tianjie, Yiting Wang, Xinbei Ma, Pengzhou Cheng, Haodong Zhao, Yulong Wang, Lifeng Liu, Jian Xie, Zhuosheng Zhang, and Gongshen Liu. "Flooding spread of manipulated knowledge in llm-based multi-agent communities." *arXiv preprint arXiv:2407.07791* (2024).

## Overview
In this paper, the authors try to attack a multi-agent system through an infected agent. They assume that they do not have access to prompts, but they are able to modify the model behind that infected agent. Their process invovles two steps: the first is persuasion injection, where the model is trained to give more "persuasive" answers–answers that are longer and are backed by (potentially fabricated) evidence. The second stage is manipulating the knowledge of the model: this manipulation was changed to be simply counterfactual in one case and toxic (intentionally harmful) in another. They then tested this infected agent in MASs that went for 3 rounds and found that infected agents were able to influence the answers of the benign agents, both with counterfactual and toxic knowledge. They found that manipulated knowledge stored in RAG databases affects the outcome of MAS interactions.

## Persuasiveness Injection
The researchers note that LLMs have been shown to believe answers that have evidence supporting them, and LLMs aren't necessarily trained to fact check those answers; more likely, they'll just assume the evidence is legitimate and agree. They also note how LLMs, trained on generating the next plausible token, are very good at generating evidence, even if that evidence is made up. They thus believe that they can train a model to be "persuasive" by always generating (real or fake) evidence for their answer.

The researchers use Direct Preference Optimization (DPO) to first train their model to prefer longer, evidence-backed answers: they do this by asking an LLM to generate a short and brief answer and a long answer supported by evidence and tell the DPO to prefer the latter. They then use LoRA to further fine-tune persuasiveness; LoRA is less likely to change the foundational knowledge of the model.

## Manipulated Knowledge Injection
They then use knowledge editing (KE) techniques, like ROME, to inject incorrect information. They gathered this information from CounterFact and zsRE, and then modified these to generate toxic versions of the datasets.

## Experiment Details
- Vicuna (7b), LLaMA Instruct (8b), Gemma Instruct (7b)
- They infect an agent, then have the MAS talk about the specific knowledge
    - In most experiments the infected agent speaks **first**
- The conversations are then stored in RAG
- Measurements are accuracy (acc), rephrase accuracy (rephrase), and locality accuracy (locality)
    - they compare acc (old) and acc (new) for accuracy to pre and post edited knowledge, respectively
    - rephrase is accuracy when answering questions phrased differently
    - locality is accuracy for related questions. The answers here ideally would not change after KE

## Results
- They found that persuasion injection increased counterfactual answers much more (~10%)
- Their models are comparable to asking a SOTA LLM (GPT 4) to come up with evidence
- They found that with more rounds (ie more time for the manipulated knowledge to spread), the MASs adhered more to the modified information (only very slightly though)
    - They only did 3 rounds. I would guess that with more rounds, this could grow way more ([AgentSmith](https://arxiv.org/pdf/2407.07791) showed that the growth is exponential)
- They found that the effect on MMLU (ie general/foundational knowledge) was minimal
- Toxic information spread was still effective (10-20% accuracy), but much worse than counterfactual
    - Likely due to LLM alignment
    - Also seemed to trend toward higher accuracy with more rounds, but not as monotone as counterfactual
- The knowledge persisted through RAG and reappeared in new conversations through knowledge retrieval
- They found that fewer benign agents led to higher accuracies (more effective attack)
- Infected agent placement mattered: random speaking order was the most effective, followed by infected speaking first, then infected speaking last
    - They guess that this introduces variability, and thus makes it harder for the other agents to catch the misinformation

## Mitigation
- Guardian agents to analyze & fact-check answers, supported by trusted knowledge bases
- Prompt engineering to fact check more