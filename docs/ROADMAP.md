# Roadmap

This roadmap is an invitation to debate priorities, not a fixed architecture.

## M0 — Project clarity and community
- [ ] Agree on a concise problem statement and non-goals.
- [ ] Publish governance and contributor expectations.
- [ ] Choose a safe, public, reproducible demonstration dataset.
- [ ] Define threat model and privacy review checklist.
- [ ] Agree on initial success metrics.

## M1 — Evidence primitives
- [ ] Define source, snapshot, observation, evidence reference, finding, and review schemas.
- [ ] Preserve raw and normalized values separately.
- [ ] Add timestamps, provenance, source version, and content hashes.
- [ ] Validate schema invariants and serialization.
- [ ] Document compatibility/versioning strategy.

## M2 — Reproducible ingestion
- [ ] Define a source adapter interface.
- [ ] Build a local-file CSV/JSON adapter first.
- [ ] Add schema mapping and validation errors.
- [ ] Add deterministic fixtures and golden tests.
- [ ] Add safe retries, timeouts, and size limits for network adapters.
- [ ] Document source permission and terms review.

## M3 — Reconciliation signals
- [ ] Define signal taxonomy: conflict, missing, stale, unexpected change, duplicate candidate.
- [ ] Implement deterministic field comparison.
- [ ] Explain why each signal was emitted.
- [ ] Represent unknown and missing separately.
- [ ] Add tests for nulls, units, dates, locale formats, and normalization.
- [ ] Establish a labeled evaluation set with documented limitations.

## M4 — Entity resolution
- [ ] Define candidate generation interface.
- [ ] Compare exact, normalized, and fuzzy matching approaches.
- [ ] Add explainable match features and thresholds.
- [ ] Keep ambiguous links unresolved.
- [ ] Build human correction and merge/split review events.
- [ ] Test false merges and near-duplicate edge cases.

## M5 — Evidence graph and audit
- [ ] Model provenance edges between sources, observations, signals, and decisions.
- [ ] Define append-only audit event schema.
- [ ] Add replayable deterministic pipeline run metadata.
- [ ] Document retention, deletion, and correction semantics.
- [ ] Explore graph storage only after in-memory needs are measured.

## M6 — Review experience
- [ ] Design a finding detail view with supporting and conflicting evidence.
- [ ] Add review states and reviewer rationale.
- [ ] Add dispute, correction, and appeal flows.
- [ ] Track reviewer disagreement and time-to-resolution.
- [ ] Test accessibility and plain-language explanations.

## M7 — Operational readiness
- [ ] Define authorization boundaries for every action.
- [ ] Add observability without leaking sensitive values.
- [ ] Threat-model connectors and third-party dependencies.
- [ ] Add data retention and deletion controls.
- [ ] Publish reproducible benchmark and model card if models are used.
- [ ] Document deployment, backup, rollback, and incident response.
- [ ] Conduct external security and privacy review before real deployment.

## Later, only after evidence
- OCR for document extraction with page/region provenance.
- Permitted APIs or public portals as adapters.
- Human-approved correction export formats.
- Pluggable signal engines and evaluation harness.
- Multi-tenant access controls only if a real use case requires them.

A milestone is complete only when acceptance criteria, tests, documentation, safety review, and known limitations are visible. A large issue count is not progress by itself.
