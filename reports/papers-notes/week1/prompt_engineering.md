# [Prompt Engineering](https://www.promptingguide.ai/techniques)
## Settings
**Temperature:** how creative you want the LLM to be. Higher means selects more creative (lower chance) tokens, lower means less creative.

**Top P:** Tightens the token pool. p is the total percent you want to pool from. Lower value means less creative, higher value means more creative

**Top K:**
Chooses from the top K tokens.

*Note:* It's recommended you use temperature, top p, and top k disjointly.

**Max length:**
control output of the model

**Stop sequences:**
Tell the model to stop output when it outputs a specific phrase

**Frequency penalty:**
Repeated tokens are discouraged (more tokens $\implies$ less consideration)

**Presence penalty:**
Repeated tokens are discouraged; doesn't change if there are more than 2 repeats.

*Note:* It's recommended you use frequency penalty and presence penalty disjointly

## Elements
Prompts can be broken up into 4 sections: **instruction, context, input, and output.** These are all self-explanatory.

## Techniques
### Zero-shot vs Few-shot
"shots" are how many examples you provide. These go in the context. Few shot improves the response of the model, even if the examples are wrong (think of it as improving the structure, which improves the output)

### Chain of Thought (CoT)
Tell the model to "think step-by-step." Basically creates a chain of reasoning within the model, allowing it solve reasoning questions better. The context window is basically all the model has to work off of, so if it can give itself more context, that helps with reasoning. 

**Automatic Chain of Thought** is when the LLM clusters questions that are similar, and when answer its CoT, samples from clusters. Reduces chance of choosing bad responses.

### Meta Prompting
Force the model to follow a specific structure. Can be zero shot (just provide template) or few shot. Structure allows the model to give more preditable, desired answers.

### Self-consistency (SC)
Ask the LLM to do CoT multiple times. Choose the answer that appears the majority of the time from the thought processes.

### Generated knowledge
Before giving its response, ask the model to come up with its knowledge on the subject first. Allows the model to work with more context/knowledge. Can be zero shot or few shot

### Prompt chaining
Break your prompt into multiple prompts. Feed the output of one as part of the input of the other

### Tree of Thoughts
Tell the model to generate multiple reasoning paths, and continue with the ones that look most promising. Involves intermediate step in which model (can be same or different) evaluates responses as possible, likely, impossible, etc. Shown to be better than CoT and CoT with SC.

### Retrieval Augmented Generation (RAG)
The model grabs more information (either from a database, search, etc) before making its response. Reduces hallucinations

### Automatic Reasoning and Tool-Use (ART)
Puts tools into CoT. Follows examples from a *task library*.

### Automatic Prompt Engineer (APE)
Ask a model to give a prompt that produces desired output for given input. Run those prompts through an LLM to see which ones generate the expected output with highest probability. Ask LLM to generate prompts with the same sentiment. Test again

### Active-Prompt
Asks model to use CoT to solve questions from a dataset. Those with most uncertainty (eg most conflicting answers) are sent for human annotation to improve the model.

### Directional Stimulus Prompting
Make a LM that generates hints for the LLM to generate better responses

### Progam Aided Language Models (PAL Models)
Use a code interpreter with the model, and ask the LLM to generate & run code to solve problems where it can be solved with an algorithm/calculation

### ReAct
A loop of thinking, acting (using a tool), observing the results of that action, then (optionally) repeating.

### Reflexion
ReAct with another step where an LM (same or different) says whether the results are good or not to help the actor behave better.

### Multimodal CoT Prompting
Tells the model to analyze each object, effectively putting them both in the context window, before asking the LLM what to do.

### GraphPrompts
Prompting for graphs