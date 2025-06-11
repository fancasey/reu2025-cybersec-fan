# [Peronsal LLM Agents (Security section)](https://arxiv.org/pdf/2401.05459#page=30.36)
> Li, Yuanchun, et al. "Personal llm agents: Insights and survey about the capability, efficiency and security." *arXiv preprint arXiv:2401.05459* (2024).

![Overview](CIR_LLM.png)

## Vocab Terms
- **Homomorphic encryption (HE)**: an encryption scheme that allows calculations to be done on it without decryption being necessary.
- **Personally Identifiable Information (PII)**: personal information that the user may not want revealed. It could be used in things such as identity theft (eg SSN, full name, address, etc)
- **Adversarial Example (AE)**: An input that is very similar (often by $L_p$ norm) to another, but is misclassified as different.
## Confidentiality
### Local processing
Obviously, we don't want sensitive data being sent to servers. One way to get around this is to have all LLM inference be done locally. This would be slower, though
### Secure Remote Processing
Use homomorphic encryption to be able to compute on the server while keeping information secure. This is slower than sending plaintext data, and not all operations in LLM computations are supported in currently known HE schemes
### Data Masking
Mask out personally identifiable information. This is a hard task to do securely. Another idea is to hide the information when you embed into vectors, but that could be less efficient. There are methods being developed to measure obfuscation/anonymization and increase those as well.
### Information Flow Control
Making sure output is controlled (eg make sure you don't send PII to other tools). Transparency (who, what when, where how) lets users make more informed decisions about what PII they'd like to disclose. You can also explicitly ask the LLM to not reveal PII (not provably safe).

## Integrity
### Common attacks
- changing model parameters
- theft (i don't know what they mean by this)
- tampering with local data

These can be addressed with encryption, permissions, hardware isolation, and other measures.
### Adversarial attack
