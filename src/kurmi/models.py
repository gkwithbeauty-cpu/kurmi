"""Small provisional domain models with conservative validation."""
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import StrEnum


class FindingStatus(StrEnum):
    CANDIDATE = "candidate"
    NEEDS_REVIEW = "needs_review"
    CONFIRMED = "confirmed"
    DISMISSED = "dismissed"
    DISPUTED = "disputed"


@dataclass(frozen=True, slots=True)
class EvidenceRef:
    source_id: str
    snapshot_id: str
    locator: str
    content_hash: str

    def __post_init__(self) -> None:
        for name in ("source_id", "snapshot_id", "locator", "content_hash"):
            if not getattr(self, name).strip():
                raise ValueError(f"{name} must not be empty")


@dataclass(frozen=True, slots=True)
class Observation:
    entity_key: str
    field_name: str
    raw_value: str | None
    normalized_value: str | None
    observed_at: datetime
    evidence: EvidenceRef
    schema_version: str = "1"

    def __post_init__(self) -> None:
        if not self.entity_key.strip() or not self.field_name.strip():
            raise ValueError("entity_key and field_name must not be empty")
        if self.observed_at.tzinfo is None:
            raise ValueError("observed_at must be timezone-aware")
        if not self.schema_version.strip():
            raise ValueError("schema_version must not be empty")


@dataclass(frozen=True, slots=True)
class Finding:
    signal_type: str
    summary: str
    evidence: tuple[EvidenceRef, ...]
    score: float | None = None
    status: FindingStatus = FindingStatus.CANDIDATE
    rationale: str = ""
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def __post_init__(self) -> None:
        if not self.signal_type.strip() or not self.summary.strip():
            raise ValueError("signal_type and summary must not be empty")
        if self.score is not None and not 0.0 <= self.score <= 1.0:
            raise ValueError("score must be between 0 and 1")
        if self.created_at.tzinfo is None:
            raise ValueError("created_at must be timezone-aware")
        if self.status == FindingStatus.CONFIRMED and not self.evidence:
            raise ValueError("confirmed findings require supporting evidence")
