# Security Policy

## Scope
Report vulnerabilities in code, workflows, dependency handling, data ingestion, authorization, evidence storage, and features that could expose sensitive data or trigger unsafe actions.

## Reporting
Do not publish exploitable details in a public issue. Use GitHub's private vulnerability reporting feature if enabled. Otherwise contact a repository owner privately through a verified channel and ask for a secure reporting route. Never include real personal records or credentials in reports.

## Design commitments
- Least privilege and explicit authorization.
- No secrets in source control, fixtures, logs, or examples.
- Treat source content as untrusted input.
- Keep audit trails tamper-evident where practical.
- Separate suggestion, review, approval, and execution.
- Default to no consequential automated changes.
- Minimize retention and access to personal data.

Reports should be acknowledged, triaged, reproduced safely, and fixed with a coordinated disclosure plan. Do not promise response times until a maintainer rotation exists.
