# Agent Rules: Deployment Guide (v5.0.0)

Rules for zero-downtime, safe deployment automation.

## [dep-001] Immutable Infrastructure
Deployment scripts must use fixed versions/SHAs, not `latest` tags.

### Patterns
- **Incorrect**: `image: myapp:latest`
- **Correct**: `image: myapp:v1.2.3@sha256:abc...`

## [dep-002] Health Check Mandatory
Every service deployment must define `liveness` and `readiness` probes.

## [dep-003] Rollback First
Every "Apply" action must be preceded by a "Dry-run/Plan" and include a rollback command.
