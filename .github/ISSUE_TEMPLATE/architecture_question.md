---
name: Architecture question
about: Discuss a design constraint or component-boundary change
title: "[Architecture]: "
labels: architecture
assignees: ""
---

## What are you trying to build?

Describe the workflow, number of accounts, execution model, and operational constraints.

## Which component are you extending?

Identify the account lifecycle, task queue, scheduler, worker, persistence, workflow, or distributed-execution boundary.

## Why doesn't the current architecture fit?

Explain the mismatch and the invariant or design decision that would need to change.

## Alternatives Considered

What other approaches did you evaluate, and why were they insufficient?

## Persistence and Recovery

Describe state changes, migration needs, retry behavior, and recovery after partial failure.
