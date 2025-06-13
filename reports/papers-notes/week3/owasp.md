# [OWASP Top 10](OWASP_TOP_10_LLM.pdf)
> OWASP. *OWASP Top 10 for LLM Applications 2025*. Version 2025, OWASP, 18 Nov. 2024, genai.owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf.

## Vocab
- **Prompt Injection**: A prompt that causes the LLM to perform unexpected behavior. It may tell the LLM to do things that are unsafe (eg reveal PII, generate harmful content, etc)
- **Jailbreaking**: A type of prompt injection that tell the LLM to disregard its safety protocol
- **RAG Triad**: context relevance, groundedness, question/answer relevance
- **Least privilege**: Only grant access to data that is necessary for user
- **Federated learning**: Training models from different servers/devices on different data. Only sends updates to weights from each machine, not the data (ie data remains decentralized)
- **Differential privacy**: adding noise to individual data to make them harder to locate
- **ROME (aka lobotomization)**: a method of modifying certain weights in a model to change general knowledge, not just specific response patterns (see paper for more information)
- **Provenence assurance**: making sure the origin of training data can be traced
- **Low-Rank Adaptation (LoRA)**: a method of fine-tuning by adding only a small number of tunable parameters to a pretrained model
- **Model merging**: combining the parameters of multiple models into a new model
- **Red teaming**: simulation of attacks. "red team" (attackers) attacking "blue team" (organization/defenders)
- **Software Bill of Materials (SBOM)**: an inventory of packages that can be checked for vulnerabilities
- **Code signing**: asymmetric encryption on your code to ensure authenticity
- **Data poisoning**: when training data/embeddings are manipulated to introduce vulnerabilities, backdoors, or biases. Happens during pretraining, fine-tuning, or data embedding
- **Malicious pickling**: malware embedded in software that runs when the program runs
- **Sandbox**: an isolated environment for a system to run unknown programs. A **strict sandbox** is an especially restrictive sandbox.
- **Data version control (DVC)**: a way to keep track of previous versions of data; good way to see changes
- **Cross site scripting (XSS)**: injecting scripts into a legitimate web page that are run by the browser
- **Cross site request forgery (CSRF)**: tricking a user into submitting HTTP requests into somewhere they're already authenticated
- **Server-side request forgery (SSRF)**: manipulating a server to make requests to unintended locations
- **Content Security Policy (CSP)**: mechanism that allows developers to control which resources a page can load
- **Complete mediation principle**: every access to a protected resource should be checked for authorization
- **Side channel attack**: an attack that exploits the side effects of a system instead of the encryption. Can often be used to gather information about encoding/keys/data
- **MLOps**: DevOps for ML; automates ML cycle

## Prompt Injections
### Overview
**Direct Prompt injection** is when the user inputs (on purpose or by accident) a prompt that changes the model's behavior. **Indirect Prompt Injection** is when external content (from visiting a website, for example) is read in and changes the model's behavior. Multimodality of LLMs allows users to embed their prompt injections in forms other than text (an image, for example).
### Mitigation
1. Limit behavior model behavior: have the model only do exactly what it is told
2. Define intput/output formatting
    - check formatting deterministically
3. input/output filtering
    - evaluate with RAG triad. Use semantic filtering & string-checking
4. enforce privilege control and least privilege access
    - Use an extensible API to say who controls what
5. Human in the loop
6. Segregate and identify external content (mark as untrusted)
7. Adversarial testing & attack simulations

## Sensitive information disclosure
### Overview
Confidential data (eg PII, financial documents, secret research, etc) is often shared with LLMs. We need to make sure this data isn't misused/mishandled. The model itself may also reveal proprietary algorithms/training data.
### Mitigation
- Sanitization
    1. scrubbing/masking user data that goes into training model
    2. input validation to filter out bad inputs
- Access Controls
    1. least privilege
    2. Restrict access to external data, make sure that data is controlled during runtime
- Federated learning and Privacy techniques
    1. Federated learning reduces exposure risk (not everything in one place)
    2. Differential privacy
- User education and transparency
    1. Safe LLM usage training
    2. Transparent policies about data usage; allow users to opt out of data collection
- Secure system configuration
    1. Conceal system settings/prompt
    2. Reference Security Misconfiguration Best Practices (eg *OWASP API8:2023 Security Misconfiguration*)
- Advanced techniques
    1. Homomorphic encryption
    2. Tokenization and redaction; you're able to detect patterns of sensitive data & redact them before analyzing

## Supply chain
### Overview
Getting an LLM to a user involves many steps, and often involves running many processes on many different machines. There are opportunities for many of these steps to be "poisoned," causing the model to perform in malicious/unintended ways.
### Risks
- Third party packages that are old/deprecated can be exploited, and then when used, compromise the LLM.
- Different licenses can be confusing and hard to manage
- Old/deprecated models can have security risks
- Using pretrained models that are vulnerable (biases, backdoors, etc). Pretrained models could be attacked by poisoning the dataset or tampering with ROME (aka lobotomization)
- Models do not provide provenence assurance. There is limited information for many models (eg what data they were trained on, how they were trained, etc), and no guarantees on what they claim to be.
- Malicious LoRA adapters can affect pretrained models
- There are vulnerabilities with model merging, and merging is very common. Conversation bots may also introduce malicious code into models.
- If a model is on-device, there are more tools available to an attack (OS, firmware) to tamper with or reverse-engineer the model
- Bad terms and conditions let people train models on sensitive data & copyrighted material

### Mitigation
- Keep careful track of sources
- follow mitigation strategies (like in OWASP's *A06:2021 – Vulnerable and Outdated Components*)
- Lots of testing of model & data: red teaming, trustworthy benchmarks (eg Decoding Trust)
- keep track of packages, licenses, & environments with the corresponding tools (eg SBOM, 3rd party tools, *HuggingFace SF_Convertbot Scanner*)
- use verified sources, 3rd party integrity checks (signing, file hashing)
- encrypt models deployed on edge (ie closer to local devices)

## Data and modeling poisoning
### Overview
Data poisoning is an integrity attack and should be considered especially when using external sources. Attackers can also pickle models. You can also poison data to create a "sleeper agent" that leads to a backdoor upon a certain trigger. Data poisoning can happen on purpose ("Split-view Data Poisoning" and "Frontrunning poisoning"), by accessing external data sources, or by unaware users. Poison could be harmful content or sensitive content.
### Mitigation
- Track and test data and model outputs (data version control, red teaming)
- Use sandboxing when interacting with external sources.
- Fine tune for specific tasks when possible
- Use RAG & grounding

## Improper output handling
### Overview
Insufficient data validation, sanitization, and handling of outputs (ie giving users additional functionality). Can lead to XSS, CSRF, SSRF, privilege escalation, remote code execution. These kinds of attacks often depend on the environment in which the LLM is running, which can cause certain output to run code (eg shell, browser, etc).
### Mitigation
- treat model as a user (0-trust approach, strict CSP), check inputs/outputs
- follow OWASP ASVS (Application Security Verification Standard)
- encode output to prevent code execution
    - consider environment & perform encoding based on that
- prepare/fill in args for database queries
- robust logging/monitoring

## Excessive Agency
### Overview
Damaging actions from an agent in response to unexpected, ambiguous, or manipulated outputs from an LLM. Could be from hallucination or prompt injection. Often due to:
- excessive functionality
    - access to unnecessary functions/tools
    - open-ended functionality
- excessive permissions
    - eg an agent that needs to access a specific user's information is given the ability to see all information
- excessive autonomy
    - doesn't verify/approve high-impact actions (eg deleting)

### Mitigation
- minimize extensions and extension functionality; avoid open-ended extensions
- minimize extension permissions, stay in user's context
- require user approval (HITL); complete mediation
- sanitize inputs/outputs: OWASP's ASVS (Application Security Verification Standard), Static Application Security Testing (SAST), and Dynamic and Interactive application testing (DAST, IAST)
- Log extension activity
- Implement rate limiting

## System prompt leakage
### Overview
System prompts should not be considered secret/a security control. Don't put sensitive data in your system prompt. There are always strong (ie deterministic) or safe ways to this instead. The problem isn't that the system prompt is revealed, it's that information that shouldn't be in the system prompt will then be revealed (even if not the exact words).
### Mitigation
- externalize information to the systems the model doesn't directly access
- use external guardrails and systems to ensure model behavior
- security controls should be independent of the LLM
    - want them to be deterministic and auditable

## Vector and embedding weaknesses
### Overview
Since RAG uses vector embedding, LLMs that use it are especially prone to having vulnerable embeddings being manipulated.
### Risks
- poor embedding can lead to unauthorized/sensitive information being retrieved from vectors
- if different systems share the same vector database, there may be leakage. Different data sources can contradct (eg two systems in federated learning or RAG with old data LLM was trained on)
- vulnerable embeddings can be reverted to retrieve lots of information
- vectors can be poisoned
- RAG can change behavior (eg reduce emotional intelligence)
### Mitigation
- permission/access control & strict partitioning
- validate & monitor data from RAG & data from multiple sources

## Misinformation
### Overview
Misinformation comes from hallucinations, which are a result of statistically probable outputs without real understandig behind those outputs, and biases in the data. Users might also overrely on LLM outputs, aggravating the issue. Some examples of misinformation are:
- stating incorrect facts, baseless claims, and coming up with fake evidence
- giving the illusion of expertise, leading to users trusting an incorrect statement
- unsafe code, pulling from libraries that are deprecated or don't exist anymore

### Mitigation
- RAG to verify, other automatic validation
- fine tune (eg parameter efficient tuning (PET), CoT)
- encourage cross checking & tell users risks of LLM outputs
- establish secure coding practices

## Unbounded consumption
### Overview
Unbounded consumption happens when an LLM generates too much output. This can lead to denial of service, economic losses, model theft, & service degradation. Since LLMs are often on the cloud & are computationally expensive, they are more prone to resource abuses.
### Attacks
- variable length input flood: sending many requests of different lengths, abusing slow processing
- Denial of Wallet (DoW): submitting many many requests, draining the provider's wallet (due to cost-per-use model of cloud AI services)
- continuous input overflow: input that exceeds the context window can slow things down
- complex queries can slow the system down
- use the API to collect information (w/ prompt injection) about the model. Then make a partial model or a shadow model
- use a model's response to train a functional copy of it
- exploit input filtering techniques of the model to execute side-channel attacks, gathering weights
### Mitigation
- Check inputs
- Reduce information (eg logbits, logprobs) in API output
- rate limiting, timeouts/throttling
- monitor and manage resources dynamically
- restrict LLM's access to resources (network, internal, API) with a sandbox
- watermarking to find unauthorized use of outputs
- graceful degradation: degrade under heavy load gradually
- train against adversarial prompts
- check for known glitch tokens
- strong access control (eg RBAC) & least privilege
- use a centralized ML model inventory/registry
- MLOps w/ governance, tracking, & approval workflows