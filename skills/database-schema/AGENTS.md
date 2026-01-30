# Agent Rules: Database Schema (v5.0.0)

This document contains procedural rules for AI agents. Loaded automatically for high-precision task execution.

# Rule: Design Indexes for Leftmost Prefix

## Rationale
Composite indexes (A, B, C) can only be used by the optimizer if the query uses the columns in order starting from the left (A, or AB, or ABC).

## Patterns

### ❌ Incorrect
`Index: (user_id, status)`
`Query: SELECT * FROM orders WHERE status = 'paid';` (Index will not be used efficiently)

### ✅ Correct
`Index: (user_id, status)`
`Query: SELECT * FROM orders WHERE user_id = 1 AND status = 'paid';`

---

# Rule: Prevent N+1 Query Problems

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

---
