# Security Policy

## Reporting a Vulnerability

Do not open a public issue for a security vulnerability. Use GitHub's private vulnerability reporting or security-advisory feature for this repository. Include the affected document or reference file, impact, reproduction details, and a suggested mitigation when available.

Do not send credentials, access tokens, cookies, private session data, or real account identifiers. Use minimal synthetic examples.

Maintainers should acknowledge a complete report within seven days. Resolution timing depends on severity, reproducibility, and whether the issue affects reference code or architectural guidance.

## Scope

Relevant reports include:

- unsafe credential or secret-handling guidance;
- account-state isolation errors;
- retry or lease behavior that could cause unintended duplicate actions;
- examples that expose private data;
- reference code that crosses account boundaries; and
- documentation that encourages insecure platform integration.

SocialFlow is a reference architecture, not a hosted service. It does not process user accounts or operate production infrastructure.

## Responsible Integration

Implementations derived from SocialFlow should use permitted APIs or user-authorized browser sessions, apply least privilege, protect secrets outside task payloads, retain appropriate audit records, and follow applicable platform terms and policies.

The project does not support CAPTCHA bypass, authentication bypass, rate-limit evasion, credential collection, session theft, or automation of unauthorized accounts. Requests to add such functionality are out of scope.

## Disclosure

Please allow maintainers a reasonable opportunity to evaluate and correct a reported issue before public disclosure. Credit will be offered when requested and appropriate.
