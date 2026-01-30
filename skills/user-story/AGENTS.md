# Agent Rules: User Story (v5.0.0)

This document contains procedural rules for AI agents. Loaded automatically for high-precision task execution.

# Rule: Clear & Testable Acceptance Criteria

## Rationale
Vague requirements lead to misunderstandings and delivery failures. ACs must be binary (Pass/Fail) and preferably in BDD format.

## Patterns

### ❌ Incorrect
"The login should be fast and secure." (What is fast? What is secure?)

### ✅ Correct
- **Given** the login page is loaded.
- **When** the user enters correct credentials.
- **Then** the user is redirected to the dashboard within 200ms.

---

# Rule: Adhere to the INVEST Principle

## Rationale
Stories must be Independent, Negotiable, Valuable, Estimable, Small, and Testable to ensure team agility and successful delivery.

## Patterns

### ❌ Incorrect
"Implement the database for the login feature." (Technical task, not a user story; not independently valuable to the user).

### ✅ Correct
"AS A user, I WANT TO log in via email, SO THAT I can access my account." (Provides direct user value, small, and testable).

---
