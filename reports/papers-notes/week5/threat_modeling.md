# [Threat modeling](Secure%20Design%20Principles.pptx)
> Xu, Dianxiang. "Threat Modeling." Powerpoint, CS 483/5583 Software Security, Kansas City, MO.

## Tools
- [MS Threat Modeling Tool](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool)
- [OWASP Threat Dragon](https://owasp.org/www-project-threat-dragon/ )
- [AWS ThreatComposer](https://awslabs.github.io/threat-composer/workspaces/default/dashboard)
- [Threagile](https://threagile.io/)
- etc.

## Modeling
Modeling is the process of creating an abstraction to gain valuable insights/learn how something works.
- Data Flow Diagrams (DFDs)
- Finite State Machines (FSMs)
- Unified Modeling Language (UML)
- Petri nets
### Data Flow Diagrams
Decomposition of data through systems and subsystems. Allows for better intuitive understanding, but can sometimes be ambiguous
![DFD](dfd.png)
#### Rules
- A process must have at least one data flow entering/exiting
- Data flows start/stop at a process
- Data stores connect process with data flow
- Data stores cannot connect together
- Process names: verbs and nouns, verb phrases
- Data flow names: nouns/noun phrases
- Interactor names: nouns
- Data store names: nouns

### Finite State Machines

## Threat Modeling
**Work flow**: model functions → determine threats → rank threats → mitigate threats

Helps find bugs, helps people understand the program faster, and helps testers develop test cases.

### MS Threat Modeling
- Model functions: application decomposition & DFD
- Determine threats: STRIDE & threat trees
- Rank threats: DREAD
- Mitigate threats: Mark threat tree

#### Decomposition
Decompose enough to find threats; it is OK to allow for abstraction to help understand better.

#### STRIDE: Spoofing, Tampering with data/process, Repudiation, Information disclosure, Denial of Service, and Elevation of Privilege
- **Spoofing**: process, file, machine, person, role
    - Authentication
- **Tampering**: file, memory, network
    - Integrity, authorization
- **Repudiation**: action, attacking the logs
- **Information disclosure**: process, data store, data flow
    - Confidentiality
- **DoS**: process, data store, data flow
    - Availability
- **EoP**: corrupting the process, skipping checks, buggy checks, data tampering
    - Authorization
    - EoP card game to demonstrate threats

Threats may be interrelated, but STRIDE categorizes by the cause of the vulnerability.

CMU SEI: OCTAVE also is another form of threat analysis

#### Threat Trees
![Threat tree](threat%20tree.png)
- Root: ultimate attack goal
- Internal nodes: sub-goals of parent, may be AND/OR related
- Leaf nodes: primitive attack conditions/actions
- Attack path: sequence of leaves that achieve the attack goal
- Dotted lines for least likely paths
- Solid lines for most likely paths
- Circles below least likely paths to explain how/why the threat is mitigated

#### DREAD: Damage Potential, Reproducibility, Exploitability, Affected Users
- Each category gets rated 1-10: 1 least severe, 10 most
- DREAD rating is average of the categories
- Sort threats in descending order
- Response options include
    - Do nothing
    - Inform user
    - Remove problem
    - Fix problem

## Issues
- Are functions correct?
- Are threats correct?
- Are threats absent? Are mitigations correct?