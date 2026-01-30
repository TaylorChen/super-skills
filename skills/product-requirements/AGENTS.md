# Agent Rules: Product Requirements (v5.0.0)

This document contains procedural rules for AI agents. Loaded automatically for high-precision PRD and requirement definition.

## [req-001] User Story Format
Standardize all requirements into active voice user stories.

### Rationale
Ensures clarity on who benefits and why.

### Patterns
- **Incorrect**: The system should support user login.
- **Correct**: As a registered user, I want to login securely so that I can access my private dashboard.

## [req-002] BDD Acceptance Criteria
All functional requirements must have at least 3 ACs in Given-When-Then format.

### Rationale
Reduces ambiguity and provides direct input for testing.

### Patterns
- **Incorrect**: ❌ Add AC: Verify login works.
- **Correct**: ✅ **AC 1: Successful Login**
  - **Given**: A registered user is on the login page.
  - **When**: They enter valid credentials and click "Submit".
  - **Then**: They are redirected to the dashboard.

## [req-003] KPI Definition
Every PRD feature must include at least one measurable KPI.

### Rationale
Links feature delivery to business outcome.

### Patterns
- **Pattern**: `Feature: [Name] -> Measurement: [e.g. Conversion Rate +5%, Latency < 200ms]`
