# Agent Rules: Testing Strategy (v5.0.0)

Rules for high-coverage, low-flake testing implementations.

## [test-001] Pyramid Priority
Enforce the testing pyramid: Unit > Integration > E2E.

### Patterns
- **Correct**: 70% Unit, 20% Integration, 10% E2E.

## [test-002] No Mocks in Logic
Avoid mocking internal business logic; only mock IO/External APIs.

### Rationale
Prevents brittle tests that pass even when logic is broken.

## [test-003] Edge Case Requirement
Every test suite must include:
- Null/Empty values
- Out of bound values
- Rapid concurrent requests (if applicable)
