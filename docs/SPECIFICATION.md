# Working specification

Status: exploratory; all interfaces are provisional.

## Problem space
Public and institutional information is fragmented across documents, portals, tables, registries, and APIs. Values may disagree, be stale, refer to different entities, or lack enough evidence to compare. Kurmi explores a transparent workflow for collecting permitted observations, linking entities cautiously, surfacing candidate discrepancies, and supporting human review.

## Conceptual pipeline
1. Source registry: record owner, access method, terms, jurisdiction, update cadence, schema, and risk classification.
2. Acquisition: fetch only permitted data with rate limits, bounded retries, provenance, and safe parsing.
3. Normalization: preserve raw values and source context while producing typed normalized observations.
4. Entity resolution: propose links with explainable features and uncertainty; never silently collapse ambiguous entities.
5. Signal generation: identify contradictions, missing values, stale records, unusual changes, and cross-source mismatch.
6. Evidence graph: connect source snapshots, observations, entities, transformations, signals, reviews, and decisions.
7. Human review: show supporting and conflicting evidence, confidence limits, and a clear path to challenge a finding.
8. Resolution workflow: track outcomes and authorized corrections; do not write back to source systems by default.
9. Evaluation: measure precision, recall where labels exist, reviewer burden, drift, and subgroup error patterns.

## Initial non-goals
- A universal source of truth.
- Automated accusations or individual risk scoring.
- Unreviewed enforcement, benefit denial, or changes to official records.
- Circumventing access controls, CAPTCHAs, terms, or privacy protections.
- Treating model confidence as proof.

## Required invariants
- Every finding links to evidence and transformation versions.
- Unknown, stale, conflicting, and missing values remain distinct.
- Provenance and timestamps survive normalization.
- Corrections are append-only or versioned, with actor and rationale.
- Automated outputs are recommendations until authorized human action.
- Sensitive data is minimized, access-controlled, and excluded from public fixtures.
- A finding can be disputed and reviewed.

## Open questions
- What is the smallest useful end-to-end demonstration?
- Which source and jurisdiction can be used lawfully for a public fixture?
- How should source reliability and freshness be represented?
- Which graph representation provides value before adding infrastructure?
- What are acceptable false-positive and review-burden thresholds?
- How should users appeal an incorrect entity match?
- Which functions need deterministic logic versus probabilistic models?
