"""Reference data contracts described by the SocialFlow documentation."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any
from uuid import uuid4


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class AccountStatus(str, Enum):
    ACTIVE = "active"
    PAUSED = "paused"
    NEEDS_ATTENTION = "needs_attention"
    DISABLED = "disabled"


class TaskStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    RETRY = "retry"
    FAILED = "failed"
    PAUSED = "paused"


ACCOUNT_TRANSITIONS: dict[AccountStatus, set[AccountStatus]] = {
    AccountStatus.ACTIVE: {
        AccountStatus.PAUSED,
        AccountStatus.NEEDS_ATTENTION,
        AccountStatus.DISABLED,
    },
    AccountStatus.PAUSED: {AccountStatus.ACTIVE, AccountStatus.DISABLED},
    AccountStatus.NEEDS_ATTENTION: {
        AccountStatus.ACTIVE,
        AccountStatus.PAUSED,
        AccountStatus.DISABLED,
    },
    AccountStatus.DISABLED: set(),
}


@dataclass
class Account:
    id: str
    name: str = ""
    status: AccountStatus = AccountStatus.ACTIVE
    last_success: datetime | None = None
    last_failure: datetime | None = None
    failed_tasks: int = 0
    metadata: dict[str, Any] = field(default_factory=dict)

    def transition_to(self, new_status: AccountStatus) -> None:
        """Apply one documented account-lifecycle transition."""
        if new_status == self.status:
            return
        if new_status not in ACCOUNT_TRANSITIONS[self.status]:
            raise ValueError(
                f"invalid account transition: {self.status.value} -> "
                f"{new_status.value}"
            )
        self.status = new_status


@dataclass
class Task:
    account_id: str
    name: str
    priority: int = 100
    scheduled_at: datetime = field(default_factory=utc_now)
    status: TaskStatus = TaskStatus.PENDING
    attempts: int = 0
    max_retries: int = 2
    created_at: datetime = field(default_factory=utc_now)
    workflow_run_id: str | None = None
    step_id: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
    id: str = field(default_factory=lambda: str(uuid4()))


@dataclass(frozen=True)
class ExecutionResult:
    success: bool
    retryable: bool = False
    error: str | None = None
    duration_seconds: float = 0.0
    metadata: dict[str, Any] = field(default_factory=dict)
