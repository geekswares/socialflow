"""Readable scheduler-selection reference, intentionally without I/O."""

from __future__ import annotations

from collections.abc import Iterable
from datetime import datetime

from .models import Account, AccountStatus, Task, TaskStatus


def select_eligible_tasks(
    tasks: Iterable[Task],
    accounts: dict[str, Account],
    *,
    now: datetime,
    capacity: int,
    in_flight_accounts: set[str] | None = None,
) -> list[Task]:
    """Select a priority-ordered batch containing at most one task per account.

    A real scheduler must claim tasks and account leases transactionally before
    dispatch. This pure function exists only to make the selection policy easy to
    discuss and test in an implementation derived from the reference design.
    """
    if capacity < 0:
        raise ValueError("capacity must be non-negative")

    busy = set(in_flight_accounts or ())
    selected: list[Task] = []
    candidates = sorted(
        tasks,
        key=lambda task: (
            task.priority,
            task.scheduled_at,
            task.created_at,
            task.id,
        ),
    )

    for task in candidates:
        if len(selected) >= capacity:
            break
        if task.status not in {TaskStatus.PENDING, TaskStatus.RETRY}:
            continue
        if task.scheduled_at > now or task.account_id in busy:
            continue

        account = accounts.get(task.account_id)
        if account is None or account.status is not AccountStatus.ACTIVE:
            continue

        selected.append(task)
        busy.add(task.account_id)

    return selected
