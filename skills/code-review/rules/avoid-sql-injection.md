# Rule: Avoid SQL Injection via Parameterized Queries
| Metadata | Value |
| --- | --- |
| Title | Parameterized Queries |
| Impact | **CRITICAL** |
| Tags | Security, Database |

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
