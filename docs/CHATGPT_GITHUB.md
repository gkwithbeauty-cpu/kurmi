# Working with ChatGPT and GitHub

ChatGPT can help explore code, draft tests, summarize issues, propose implementation plans, and prepare pull requests when the GitHub connector has the necessary permissions. It is not an independent maintainer or a substitute for human review.

## Suggested loop
1. Open the repository and select a specific issue.
2. Ask ChatGPT to inspect relevant files and restate acceptance criteria.
3. Request a small implementation plan before changing cross-cutting code.
4. Implement on a feature branch, add tests, and explain trade-offs.
5. Inspect the diff and run CI.
6. Open a pull request linked to the issue.
7. A human reviews correctness, security, privacy, licensing, and scope before merge.

If the connector cannot write, create a branch locally, make changes, run tests, and push a pull request using GitHub's interface. Never paste secrets, credentials, private datasets, or sensitive personal records into prompts or issues.

Useful prompts:
- Read issue #N and relevant files. Give me a plan and risks before editing.
- Implement only acceptance criteria 1 and 2. Add regression tests.
- Review this diff for data loss, privacy leakage, unsafe automation, and unhandled uncertainty.
- Explain behavior and limitations in plain language.

A useful PR includes a linked issue, focused diff, tests, documentation, failure-mode discussion, and explicit limitations. AI-generated code must be understood and reviewed by the submitting contributor.
