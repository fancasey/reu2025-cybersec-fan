# [Imprompter](https://arxiv.org/pdf/2410.14923)
[Demo website](https://imprompter.ai/)
## Synopsis
Imprompter is an attack method that involves attackers invoking tool-usage in LLM agents to reveal personally identifying information (PII), under the guise of an ambiguous prompt advertised with some other function (eg CV review). It uses gradient-based optimization techniques to make sure the syntax for tool invocation is correct, as well as make sure the prompt is hard to recognize. They define loss functions based on previous context, the prompt, and desired output. They also use perplexity to define the level of obfuscation. The prompt can also be a purposefully distorted image, which the authors note as naturally obfuscated in the image encoding. Results show ~80% effectiveness in revealing PII. 
## Vs Prompt Injection & Jailbreaking
### Prompt Injection
Prompt injection is a technique in which attackers create prompts that users give to the LLM that lead to the attacker's desired behavior. Imprompter is similar to prompt injection, in that the attacker creates a prompt to be used by the user, but Imprompter obfuscates the prompt, arousing less suspicion. 
### Jailbreaking
Jailbreaking is when an attacker manages to get an LLM to break its own rules for safety & conduct. An advantage of jailbreaking is that people have found ways to jailbreak LLMs without knowing model weights. Imprompter, on the other hand, requires model weights (though the authors believe their work can be extended to closed-weight models), and doesn't force the model to do anything against the safety conduct; instead, the attacker tricks *the user* into revealing their own information.
## Questions/notes
- This paper's focus (along with prompt injection) seem to be weaker to me than jailbreaking, as it requires users to put in the prompt themselves.
- In the paper, the LLM replies to the malicious prompt with an invisible 1x1 image. This, clearly, could raise suspicion, though the paper says users will likely note this is strange but move on. I bet it'll be less suspicious (and probably not so difficult) to have the prompt do as it's advertised as well. This increases its likelihood to be shared and will let people be less suspicious of it.
- For the same reasons the paper states, adversial images seem to better at not raising suspicion compared to prompts, as they don't reveal anything as to what's going on behind the scenes (in the prompt) at all. You could even distort an image that looks like it's supposed to do the right thing (eg an image with text telling the LLM what to do).
- What would be the best way to prevent this? The paper proposes some ideas, but none of them seem very good (ie they're all restrictive). Maybe there's a way to encrypt/hide tool invocation tokens (in code and in output), making it so users cannot force the LLM to make those invocations. 

## Related Work/future reading list
- [greedy coordinate gradient](https://arxiv.org/pdf/2307.15043)