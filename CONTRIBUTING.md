# Contributing to SocialFlow

SocialFlow welcomes corrections, failure scenarios, design alternatives, diagrams, and small reference implementations. The documentation is the primary artifact, so clarity and architectural consequences matter more than feature count.

## Before You Start

- Use a bug report for an incorrect statement, broken link, or reference-code defect.
- Use a feature request for a new documented capability.
- Use an architecture question when a proposal changes component responsibilities, state, concurrency, or recovery semantics.
- Do not include credentials, tokens, cookies, private sessions, or real account data.

Large architectural changes should begin with an issue so assumptions can be reviewed before substantial writing or code changes.

## Design Expectations

Contributions should preserve these boundaries unless the proposal explicitly revises a recorded design decision:

1. Accounts remain the default isolation boundary.
2. Workers execute tasks and return results; schedulers own global policy.
3. Retry budgets are finite and persisted.
4. Durable state is sufficient to explain scheduling eligibility.
5. Platform-specific behavior remains behind adapters.
6. Distributed execution assumes at-least-once delivery.

When proposing a different approach, explain the problem, alternatives, consequences, migration path, and effect on failure recovery. Update [`docs/design-decisions.md`](docs/design-decisions.md) when a recorded choice changes.

## Documentation Style

- Prefer precise terms over promotional language.
- Distinguish current design from roadmap work.
- Do not invent benchmarks, adoption numbers, deployments, or guarantees.
- Make diagrams readable in GitHub's Mermaid renderer.
- Link to related documents rather than copying large sections.
- Use synthetic account IDs and redacted error examples.

## Reference Code

Reference code should stay small, use the Python standard library where practical, and illustrate a documented contract. It should not introduce a framework, platform client, credential store, or production-service dependency without prior discussion.

Run this basic check after changing Python files:

```bash
python -m compileall -q src
```

## Pull Requests

A pull request should have one coherent purpose. Include:

- the problem being solved;
- the chosen approach and alternatives considered;
- affected invariants or design decisions;
- persistence and compatibility impact;
- failure and recovery behavior; and
- verification performed.

By contributing, you agree that your contribution is licensed under the MIT License.
