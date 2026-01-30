# Rule: Clear & Testable Acceptance Criteria
| Metadata | Value |
| --- | --- |
| Title | Testable Acceptance Criteria |
| Impact | **CRITICAL** |
| Tags | QA, Definition of Done |

## Rationale
Vague requirements lead to misunderstandings and delivery failures. ACs must be binary (Pass/Fail) and preferably in BDD format.

## Patterns

### ❌ Incorrect
"The login should be fast and secure." (What is fast? What is secure?)

### ✅ Correct
- **Given** the login page is loaded.
- **When** the user enters correct credentials.
- **Then** the user is redirected to the dashboard within 200ms.
