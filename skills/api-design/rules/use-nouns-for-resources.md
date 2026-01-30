# Rule: Use Nouns for Resources
| Metadata | Value |
| --- | --- |
| Title | Use Nouns for Resources |
| Impact | **HIGH** |
| Tags | REST, Naming, Semantics |

## Rationale
Endpoints should represent resources, not actions. HTTP methods (GET, POST, etc.) should define the action.

## Patterns

### ❌ Incorrect
`POST /getUsers`
`GET /deleteOrder?id=123`

### ✅ Correct
`GET /users`
`DELETE /orders/123`
