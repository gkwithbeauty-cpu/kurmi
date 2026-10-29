from datetime import datetime

import pytest

from kurmi.models import EvidenceRef, Finding, FindingStatus, Observation


def evidence() -> EvidenceRef:
    return EvidenceRef("registry", "snapshot-1", "row:4", "sha256:abc")


def test_evidence_requires_provenance_fields() -> None:
    with pytest.raises(ValueError):
        EvidenceRef("", "snapshot-1", "row:4", "sha256:abc")


def test_observation_requires_timezone_aware_timestamp() -> None:
    with pytest.raises(ValueError):
        Observation("entity-1", "address", "A", "A", datetime(2025, 1, 1), evidence())


def test_finding_score_must_be_bounded() -> None:
    with pytest.raises(ValueError):
        Finding("conflict", "Address differs", (evidence(),), score=1.1)


def test_confirmed_finding_requires_evidence() -> None:
    with pytest.raises(ValueError):
        Finding("conflict", "Address differs", (), status=FindingStatus.CONFIRMED)


def test_candidate_finding_can_be_unscored() -> None:
    finding = Finding("missing", "Field absent", ())
    assert finding.score is None
    assert finding.status is FindingStatus.CANDIDATE
