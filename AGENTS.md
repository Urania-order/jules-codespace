# Jules Co-SMOS — Agent Instructions

## 1. Project identity

Repository:

Urania-order/jules-codespace

Project role:

This repository is an experimental AI development environment
where GitHub Codespaces acts as the workspace and Jules acts
as an autonomous software engineering agent.

The long-term goal is to evolve this environment toward
Co-SMOS — a cooperative multi-agent development system.

---

# 2. Core principle

Jules is an autonomous implementation agent.

Codespace is the controlled development environment.

GitHub is the persistent source of truth.

Never treat temporary workspace state as the authoritative
project state.

---

# 3. Safety rules

Never modify `main` directly.

Every implementation task must work on a dedicated branch.

Never delete existing functionality unless explicitly requested.

Never replace an existing architecture merely because another
architecture appears simpler.

Preserve backward compatibility whenever reasonably possible.

Do not introduce secrets into source code.

Do not commit:

- API keys
- passwords
- tokens
- private credentials
- `.env` files containing secrets

---

# 4. Required workflow

For every non-trivial task use:

    ANALYZE
       ↓
    PLAN
       ↓
    IMPLEMENT
       ↓
    TEST
       ↓
    REVIEW
       ↓
    REPORT

Do not immediately start changing files before understanding
the existing project.

---

# 5. Analysis

Before modifying the project:

1. Inspect repository structure.
2. Inspect package configuration.
3. Inspect existing scripts.
4. Inspect existing tests.
5. Identify dependencies.
6. Identify possible compatibility problems.
7. Identify files that will be modified.

For non-trivial tasks create an analysis record in:

    .jules/tasks/

---

# 6. Planning

Before implementation describe:

- objective
- affected files
- architecture changes
- dependencies
- risks
- testing strategy

Avoid unnecessary dependencies.

Prefer existing project dependencies.

---

# 7. Implementation

Make the smallest coherent change that solves the task.

Keep modules focused.

Do not duplicate existing functionality.

Prefer reusable functions over large monolithic scripts.

Use clear names.

Add comments only where the reason is not obvious from code.

---

# 8. Testing

Before reporting completion:

1. Run existing tests.
2. Run linting if available.
3. Run build if available.
4. Test the modified functionality.

If a test cannot be executed, explicitly report why.

Never claim a test passed if it was not actually executed.

---

# 9. Failure handling

If implementation fails:

DO NOT hide the failure.

Record:

- error
- probable cause
- attempted solution
- current state
- recommended next action

Store the record in:

    .jules/results/

---

# 10. Git discipline

Use descriptive commits.

Preferred format:

    feat:
    fix:
    refactor:
    test:
    docs:
    chore:

Example:

    feat: add Jules task orchestration

Never rewrite history unless explicitly requested.

Never force-push.

---

# 11. Co-SMOS state

The file:

    .co-smos/state.json

contains the current orchestration state.

When an autonomous task starts, update:

    active_task

When it finishes:

    active_task = null
    last_task = completed task

Important decisions should be recorded in:

    .jules/history/

---

# 12. Task reproducibility

Every important task must be reproducible.

A task record should contain:

- task ID
- date/time
- original request
- branch
- files changed
- tests executed
- result
- important decisions

The goal is that a future agent can reconstruct
WHY a change was made, not merely WHAT was changed.

---

# 13. Autonomous behavior

Jules may:

- inspect files
- analyze architecture
- modify code
- add tests
- run tests
- create commits
- prepare pull requests

Jules must NOT:

- expose secrets
- destroy unrelated code
- silently change project goals
- claim success without verification

---

# 14. Communication style

Reports should be concise but technically precise.

Use:

    STATUS
    CHANGES
    TESTS
    RISKS
    NEXT STEP

---

# 15. Long-term architecture

The project is expected to evolve toward:

    Human
       ↓
    Co-SMOS
       ↓
    Task Router
       ↓
    ┌─────────────┬─────────────┐
    ↓             ↓             ↓
   Jules        other AI      tools
    ↓             ↓             ↓
    └─────────────┴─────────────┘
                  ↓
               GitHub
                  ↓
               Review

Do not prematurely implement the entire architecture.

Build it incrementally.
