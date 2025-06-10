## bugs
- If you do parallel tool calls, you get a scenario when the pi transfers to multiple departments at once and then only one of them approves (bug)?
    - If you don't, it works as it should (pi goes to someone, they report back, pi goes to next, etc)
- Since you can't transfer back to the user, there's a bug where the pi asks the user for more input but then since they can't transfer they just repeat the question
- The pi_agent never seems to handoff to the user. This would make sense at first, since user wasn't listed in handoffs, but even when i switched it so that user was listed, the pi_agent still didn't hand off control.
- Look at test_just_id: 
    - The pi_agent eventually sent it to the cs_chair_agent, and the cs_chair_agent approved it with the reason that "The proposal aligns well with our departmental goals and actively involves computer science elements." 
    - The pi_agent then sends it to the math_chair_agent, who approves it with the reason "The proposal does not specifically focus on math, hence it can be approved." This goes against what the system prompt for the math_chair_agent says. I think this is due to the double negative in the system prompt, which can be hard to understand.


## Thoughts for improvements
- Ask agents to break things down, analyze each part, and think things through before handing off (a la CoT).
- Use simple language in system prompts. No double negatives (unless it's linguistically very common), all (or mostly) commands, specific metrics, etc.
- The pi_agent has to be able to defer to the user for more than just asking for clarification. What if the user is unclear as to what the task is? There are many inputs that might not look like PDSs and would confuse the pi_agent, but its only option to terminate is once the would-be PDS reaches the research administrator.
    - see test_ask_for_help
- Maybe we could make an LM to detect malicious prompts? Or we could make an optimizer to develop bad prompts?
- For an "attack agent" $M_a$, we could prompt it to get us some resource. $M_a$ comes up with a prompt, tries it on the agent system, and gets feedback upon termination (ie if it was able to successfully get it).
    - must find out how to optimize, however (could use something like they did in Imprompter)