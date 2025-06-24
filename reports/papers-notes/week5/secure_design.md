# [Secure Design Principles](Secure%20Design%20Principles.pptx)
> Xu, Dianxiang. "Secure Design Principles." Presentation, Software Security, Kansas City, MO.
## Design
![Waterfall](waterfall.png)
Design is the creative process of transforming a problem into a solution. The solution's description is also known as a design.

## Secure Design Principles
### Minimal Attack Surface
Reducing attack surface means reducing risks.
- Reduce the amount of code running
- Reduce entry points for untrusted users
- Turn off unnecessary functionality
- Reduce privileges to limit damage potential
- In Object oriented design (OOD), minimum visibility should be given to classes & class members

### Least Privilege
- User given least privileges that are necessary to do the task
- Chain of trust/privileges

### Defense-in-Depth
- Manage security risks w/ layers of defense
- Preventitive, detective, and protective measures to stop and mitigate intrusion
- Preventative techniques aren't perfect, always expect malicious traffic
- Need containment procedures to mitigate damage

### Fail-Safe Stance
- If the system fails, make sure that it fails in a safe state (hard to exploit)
- Expect & plan for failure and exception
    - Deny instead of grant access
    - Shouldn't show error messages that could inform attackers

### Secure by Default
- Default configuration uses the most secure settings possible
- "Hardening" a system
    - Turn off all unnecessary features by default (less exploitability)

### Separation of Duties
- Prevent fraud/error by disseminating a task & associated privileges among multiple users (checks and balances)

### Security Through Obfuscation (STO)
- Make code hard to decompile/disassemble or hard for humans to read/understand
    - Name obfuscation: random variable names
    - Control flow obfuscation: modify logical structure to make less predictable and harder to trace
    - Arithmetic obfuscation: convert simple math to complex expressions
    - Code virtualization: code → instructions for randomly generated virtual machines
- Indistinguishable obfuscation: cryptographically hard
- Obscurity should never be the only security mechanism of software

### Robust Resource Management
- Good for performance and protects against malicious resource consumption
- Remove temporary files
- Ensure resources are closed when not needed
- Cleanup at program termination
- Avoid memory/resource leaks during serialization (tranforming from data to a stream of bytes)
- Thread pools to enable graceful degradation of service

### Forensic Readiness
Digital forensics: identify, preserve, recover, analyze, and present digital evidence in a forensically sound manner.
- Montoring and logging
    - Critical events & related data
    - Secure access & cannot be tampered with by adversary
    - To facilitate investigation. Might be different from normal output

### Security Features ≠ Security
- You cannot solve all problems
- Can only provide a *risk assessment*
- Attacker needs to find one flaw, but you need to find all
- Security features won't stop bugs