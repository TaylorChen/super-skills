# Agent Rules: Refactoring Guide (v5.0.0)

Procedural rules for safe code transformation and technical debt reduction.

## [ref-001] Small Commits Rule
Never perform more than 3 distinct refactorings in a single output.

### Rationale
Reduces review complexity and regression risk.

## [ref-002] Test-Driven Reflow
Always ask for current test coverage before suggesting structural changes.

### Rationale
Safeguards against breaking existing functionality.

## [ref-003] Pattern Selection
Prioritize SOLID principles and Design Patterns over ad-hoc optimizations.
- Use **Strategy** for logic branching.
- Use **Decorator** for feature wrapping.
- Use **Factory** for complex creation.
