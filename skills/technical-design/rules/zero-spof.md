# Rule: Design for Zero Single Points of Failure
| Metadata | Value |
| --- | --- |
| Title | Zero Single Points of Failure |
| Impact | **CRITICAL** |
| Tags | HA, Reliability, Infra |

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
