# Agent Rules: Code Review (v5.0.0)

This document contains procedural rules for AI agents. Loaded automatically for high-precision task execution.

# Rule: Avoid SQL Injection via Parameterized Queries

## Rationale
Dynamically concatenating user input into SQL strings allows attackers to manipulate queries and access unauthorized data.

## Patterns

### ❌ Incorrect
```javascript
const query = "SELECT * FROM users WHERE id = " + req.params.id;
const results = await db.query(query);
```

### ✅ Correct
```javascript
const query = "SELECT * FROM users WHERE id = ?";
const results = await db.query(query, [req.params.id]);
```

---

# Rule: Handle All Errors Explicitly

## Rationale
"Swallowing" errors or leaving promises unhandled makes debugging nearly impossible and can leave the system in an inconsistent state.

## Patterns

### ❌ Incorrect
```javascript
try {
  await someCriticalOperation();
} catch (e) {
  // Silent fail
}
```

### ✅ Correct
```javascript
try {
  await someCriticalOperation();
} catch (e) {
  logger.error("Critical operation failed", { error: e.message, stack: e.stack });
  throw new OperationalError("Could not complete task", 500);
}
```

---
