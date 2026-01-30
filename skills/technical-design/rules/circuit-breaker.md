# Rule: Implement Circuit Breakers for Downstream Services
| Metadata | Value |
| --- | --- |
| Title | Circuit Breaker Pattern |
| Impact | **HIGH** |
| Tags | Resilience, Microservices |

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
