# Agent Rules: Technical Design (v5.0.0)

This document contains procedural rules for AI agents. Loaded automatically for high-precision task execution.

# Rule: Implement Circuit Breakers for Downstream Services

## Rationale
If a downstream service is slow or failing, repeated requests will exhaust the upstream service's resources (threads/memory), leading to a cascading failure.

## Patterns

### ❌ Incorrect
```javascript
// Direct call without protection
async function getOrderDetails(id) {
  return await axios.get(`http://order-service/orders/${id}`);
}
```

### ✅ Correct
```javascript
// Using Hystrix/Resilience4j concept
const breaker = new CircuitBreaker(getOrderDetails);
breaker.on('open', () => fallbackResponse());

async function getProtectedOrderDetails(id) {
  return await breaker.fire(id);
}
```

---

# Rule: Design for Zero Single Points of Failure

## Rationale
Any component that lacks a redundant backup will cause the entire system to fail if it goes down. This applies to servers, databases, and network paths.

## Patterns

### ❌ Incorrect
- Placing all application servers in a single Availability Zone (AZ).
- Using a single database instance without a failover replica.

### ✅ Correct
- Deploying application instances across at least two AZs.
- Implementing a Multi-AZ database setup with automatic failover.
- Using a global Load Balancer with health checks.

---
