# Rule: Prevent N+1 Query Problems
| Metadata | Value |
| --- | --- |
| Title | Prevent N+1 Queries |
| Impact | **CRITICAL** |
| Tags | Performance, SQL, ORM |

## Rationale
Issuing a separate database query for each item in a collection causes massive latency and DB load.

## Patterns

### ❌ Incorrect
```javascript
// Loops inside query
const posts = await db.posts.findMany();
for (let post of posts) {
  post.author = await db.users.findUnique({ where: { id: post.authorId } });
}
```

### ✅ Correct
```javascript
// Use JOIN or Batch loading
const posts = await db.posts.findMany({
  include: { author: true }
});
```
