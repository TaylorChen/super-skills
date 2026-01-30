# Rule: Implement Robust Idempotency
| Metadata | Value |
| --- | --- |
| Title | Implement Robust Idempotency |
| Impact | **CRITICAL** |
| Tags | Safety, Payments, API-Design |

## Rationale
Critical operations (like payments) must produce the same result regardless of how many times the same request is sent. This prevents double-charging and race conditions.

## Patterns

### ❌ Incorrect
```javascript
// No check for existing transaction
app.post('/payments', async (req, res) => {
  const result = await db.createOrder(req.body);
  await stripe.charge(result.amount);
  res.status(201).send(result);
});
```

### ✅ Correct
```javascript
app.post('/payments', async (req, res) => {
  const idempotencyKey = req.headers['idempotency-key'];
  
  // 1. Check if we already processed this key
  const existing = await db.getProcessedRequest(idempotencyKey);
  if (existing) return res.status(200).send(existing);

  // 2. Process within transaction
  const result = await db.transaction(async (tx) => {
    const order = await tx.createOrder(req.body);
    await tx.logIdempotency(idempotencyKey, order);
    return order;
  });
  
  res.status(201).send(result);
});
```
