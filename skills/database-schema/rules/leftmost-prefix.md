# Rule: Design Indexes for Leftmost Prefix
| Metadata | Value |
| --- | --- |
| Title | Leftmost Prefix Rule |
| Impact | **HIGH** |
| Tags | Indexing, SQL, MySQL |

## Rationale
Composite indexes (A, B, C) can only be used by the optimizer if the query uses the columns in order starting from the left (A, or AB, or ABC).

## Patterns

### ❌ Incorrect
`Index: (user_id, status)`
`Query: SELECT * FROM orders WHERE status = 'paid';` (Index will not be used efficiently)

### ✅ Correct
`Index: (user_id, status)`
`Query: SELECT * FROM orders WHERE user_id = 1 AND status = 'paid';`
