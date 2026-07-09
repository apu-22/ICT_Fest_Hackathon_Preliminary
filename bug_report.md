Bug Fix Summary
1. auth.py
Bug 1: Access Token Expiry
Issue: ACCESS_TOKEN_EXPIRE_MINUTES was multiplied by 60, making the access token valid for 15 hours instead of 15 minutes.
Fix: Removed the unnecessary multiplication and used the configured expiration time directly.
Bug 2: Logout / Token Revocation
Issue: Revoked tokens were stored using jti, but validation checked sub, allowing revoked tokens to remain usable.
Fix: Updated the validation logic to check the token's jti instead.

2. routers/bookings.py
Bug 1: Refund Policy
Issue: Last-minute cancellations incorrectly received a 50% refund, and the 48-hour boundary condition was incorrect.
Fix: Updated the refund rules to:
≥ 48 hours: 100%
≥ 24 hours: 50%
< 24 hours: 0%
Bug 2: Pagination
Issue: Pagination offset was calculated incorrectly, and the limit value was hardcoded.
Fix: Corrected the offset calculation using (page - 1) * limit and respected the user-provided limit.
Bug 3: Booking Details
Issue: start_time was accidentally overwritten with created_at in the booking details response.
Fix: Removed the incorrect overwrite.
Bug 4: Minimum Booking Duration Validation
Issue: No validation existed for the minimum booking duration.
Fix: Added validation to enforce the minimum booking duration.
Bug 5: Availability Cache
Issue: Availability cache was not invalidated after a booking cancellation, causing stale availability data.
Fix: Invalidated the availability cache when a booking is cancelled.
Bug 6: Usage Report Cache
Issue: Usage report cache was not refreshed after creating a new booking.
Fix: Added cache invalidation after successful booking creation.

3. services/refunds.py
Bug: Refund Amount Calculation
Issue: Refund amounts were calculated using int(), which could produce values different from the API response.
Fix: Replaced int() with round() to ensure consistent refund calculations.

4. services/stats.py
Bug: Race Condition
Issue: Concurrent requests could overwrite statistics due to a read-modify-write race condition.
Fix: Protected the critical section with threading.Lock() to make updates atomic.

5. services/reference.py
Bug: Duplicate Reference Codes
Issue: Concurrent booking requests could generate duplicate booking reference codes.
Fix: Added a lock around the reference code generation process.

6. services/ratelimit.py
Bug: Rate Limiter Race Condition
Issue: Simultaneous requests could bypass or incorrectly update the rate limiter.
Fix: Used a lock to ensure thread-safe rate limit updates.

7. notifications.py
Bug: Deadlock Risk
Issue: Different lock acquisition orders in notification functions could cause deadlocks.
Fix: Standardized the lock acquisition order across all notification operations.

8. services/export.py
Bug: Organization Isolation Bypass
Issue: CSV export did not verify the organization, allowing users to export bookings from other organizations.
Fix: Added org_id filtering to enforce organization-level data isolation.
Overall Summary

The following issues were successfully resolved:

✅ Access Token Expiry
✅ Logout / Token Revocation
✅ Refund Policy
✅ Refund Amount Calculation
✅ Pagination Logic
✅ Booking Detail Response
✅ Minimum Booking Duration Validation
✅ Availability Cache Invalidation
✅ Usage Report Cache Invalidation
✅ Statistics Race Condition
✅ Reference Code Race Condition
✅ Rate Limiter Race Condition
✅ Notification Deadlock Risk
✅ Organization Data Isolation (CSV Export)

Total: 14 bug fixes across 8 files.