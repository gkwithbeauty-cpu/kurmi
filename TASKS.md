# Community task board

The live issue tracker is the source of truth. This page groups work so people can find a useful entry point; tasks are proposals and may change through discussion.

## Start here
- Choose a task with clear acceptance criteria.
- Comment before beginning substantial work.
- Ask for clarification if the task touches architecture or sensitive data.
- Link your pull request to the issue.

## Community and project clarity
- Define the smallest end-to-end demo and acceptance criteria
- Create a community contribution recognition policy
- Write architecture proposal template
- Add issue triage guide and label vocabulary
- Review README and project discoverability

## Evidence and core models
- Create source registry schema
- Design evidence and provenance schema
- Implement JSON serialization for domain models
- Define missing, unknown, stale, and conflicting value semantics
- Add test matrix for model invariants
- Build reproducible pipeline run manifest

## Ingestion and normalization
- Define source adapter interface
- Build deterministic CSV ingestion adapter
- Build deterministic JSON ingestion adapter
- Add normalization utilities with locale-aware tests
- Document public data source review checklist

## Signals and entity resolution
- Implement deterministic field comparison signals
- Add freshness/staleness signal policy
- Define entity-resolution candidate interface
- Prototype exact and normalized entity matching
- Define pluggable signal-engine boundary

## Review, audit, and evaluation
- Add finding review state transitions
- Design append-only audit event schema
- Design appeal and correction workflow
- Create synthetic benchmark fixture
- Define evaluation metrics and error review
- Design human-approved correction export format

## Security and operations
- Threat model ingestion and parser boundaries
- Add dependency and secret hygiene checks
- Add data retention and deletion policy
- Add observability without sensitive-data leakage
- Define permission boundaries for future connectors
- Define backup, restore, and incident-response expectations
- Create a model and automation risk register

## Later research
- Research OCR extraction with provenance
- Document internationalization and jurisdiction boundaries
- Create release and compatibility policy
- Add accessibility and plain-language review guidelines
- Build a reproducible first demo after dataset selection

Browse the [open issues](https://github.com/gkwithbeauty-cpu/kurmi/issues) to claim work and see current status.
