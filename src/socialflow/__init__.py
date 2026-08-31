"""Small reference contracts for the SocialFlow architecture.

The documentation is the primary project artifact. These modules illustrate the
models and selection policy; they are not a production automation package.
"""

from .models import Account, AccountStatus, ExecutionResult, Task, TaskStatus
from .reference_scheduler import select_eligible_tasks

__all__ = [
    "Account",
    "AccountStatus",
    "ExecutionResult",
    "Task",
    "TaskStatus",
    "select_eligible_tasks",
]
