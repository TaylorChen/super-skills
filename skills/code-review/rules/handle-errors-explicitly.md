# Rule: Handle All Errors Explicitly
| Metadata | Value |
| --- | --- |
| Title | Explicit Error Handling |
| Impact | **HIGH** |
| Tags | Robustness, Debugging |

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
