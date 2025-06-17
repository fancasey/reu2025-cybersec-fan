# [A2A Protocol](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/)
> Surapaneni, Rao, Mika Jhu, Michael Vakoc, and Todd Segal. “Announcing the Agent2Agent Protocol (A2A).” Google for Developers, April 9, 2025. https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/. 

## Vocab
- **Security Service Edge (SSE)**: a cloud-based security framework that secures user access online.
- **Remote Procedure Call (RPC)**: A call from a user to a server that is meant to act like a local call.
- **Artifact**: The output of a task
## Overview
Open protocol for agent to agent communicate that is meant to complement MCP. 
## Design Principles
- **Embracing agents**: allowing agents to be unstructured & interact with each other without a shared state.
- **Build on exisiting standards**: Protocols like HTTP, SSE, JSON-RPC; easy to integrate
- **Secure**: Comparable to OpenAI's security spec
- **Long running tasks**: A2A can complete short and long tasks; support for HITL with notifications & updates
- **Multimodality**: Audio, video, text

## How it works
There's a **client agent** and a **remote agent**. The client agent asks the remote agent to complete tasks.
- **Agent cards**: each remote agent has a JSON-formatted card advertising its capability
- **Tasks**: Agents work to complete tasks, which eventually are supposed to lead to the completion of end-user requests. Tasks have lifecycles (can be instant or many days). The result is called an artifact
- **Collaboration**: Agents have the option to talk with one another and share context, memory, state, artifacts, etc.
- **UX Negotiation**: A message has parts. Each part is a specific type, and users can ask for the format change so much.

[Full specification](https://github.com/google-a2a/A2A)