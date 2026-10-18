# Engineering and GitHub Copilot Instructions

Repository: `x4-runtime`. Treat source, README, manifests, tests, and CI as authoritative; repository names and roadmap items do not prove implementation.

## Safe engineering
- Inspect relevant source, tests, configuration, dependency manifests, and workflows before editing. Preserve architecture, public interfaces, and unrelated work.
- Prefer small, reviewable patches; avoid speculative abstractions, broad rewrites, and lockfile churn.
- Validate external input at trust boundaries. Use least privilege, safe defaults, parameterized queries, and context-appropriate output encoding. Never commit credentials, tokens, private keys, or production secrets.
- Use explicit timeouts, bounded retries, idempotency where applicable, cancellation, and safe failure behavior for network, subprocess, model, and storage operations.
- Add deterministic regression tests for behavior changes, edge cases, failure paths, and security boundaries. Do not weaken/delete tests to make CI pass.

## Model-assisted completion
1. Read acceptance criteria, relevant implementation/tests, and existing instructions before changing code.
2. Treat generated code and commands as untrusted proposals. Inspect commands before execution; do not auto-run deployments, migrations, destructive operations, or privilege changes.
3. Reuse established APIs and project patterns. Keep the diff focused and avoid replacing whole files unnecessarily.
4. Validate syntax, types, schemas, authorization, injection surfaces, dependency changes, resource bounds, and error handling.
5. Run documented checks, inspect the final diff, and report each check as PASS, FAIL, NOT RUN, or BLOCKED with command and evidence. Never fabricate tests, coverage, benchmarks, security findings, or deployments.
6. Bound repair attempts; if uncertainty remains, state UNKNOWN — HUMAN REVIEW REQUIRED.
7. No merge, deployment, destructive data operation, permission/visibility change, or default-branch write without explicit task-specific authorization.

## Build, tests, workflows
- Derive commands from README, CONTRIBUTING, project manifests, lockfiles, package scripts, Makefile, and existing CI; do not guess.
- Prefer reproducible lockfile-respecting installs. Run available formatting/lint, static/type checks, tests, and build/package validation.
- CI should default to `contents: read`, use timeouts/concurrency, and never hide failures with `|| true`, swallowed exit codes, or unconditional success fallbacks.
- Add workflow steps only for detected tooling and supported commands. Pin actions to reviewed immutable SHAs where practical.
- Codecov is opt-in: add an uploader or badge only when CI generates coverage and the Codecov project/token/public-upload configuration is verified. Otherwise omit it and report the gap.

## Review and reporting
- Use a dedicated branch and reviewable PR; never merge automatically.
- Separate OBSERVED, VALIDATED, CORRELATED, and HYPOTHESIS. Report branch, PR, commit SHA, changed paths, exact checks/results, and unknowns.
- Unexecuted checks must be marked `NOT RUN — HUMAN REVIEW REQUIRED`.
