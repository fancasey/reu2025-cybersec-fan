# [OWASP Top 10](OWASP_TOP_10_LLM.pdf)
> OWASP. *OWASP Top 10 for LLM Applications 2025*. Version 2025, OWASP, 18 Nov. 2024, genai.owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf.

## Vocab
- **Prompt Injection**: A prompt that causes the LLM to perform unexpected behavior. It may tell the LLM to do things that are unsafe (eg reveal PII, generate harmful content, etc)
- **Jailbreaking**: A type of prompt injection that tell the LLM to disregard its safety protocol.
- **RAG Triad**: context relevance, groundedness, question/answer relevance
- **Least privilege**: Only grant access to data that is necessary for user
- **Federated learning**: Training models from different servers/devices on different data. Only sends updates to weights from each machine, not the data (ie data remains decentralized)
- **Differential privacy**: adding noise to individual data to make them harder to locate
- **ROME (aka lobotomization)**: 

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
## Data and modeling poisoning
## Improper output handling
## Excessive Agency
## System prompt leakage
## Vector and embedding weaknesses
## Misinformation
## Unbounded consumption