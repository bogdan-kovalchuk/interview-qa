---
id: sd-msgq-0001
title: "Design a payment webhook consumer that is safe under at-least-once delivery"
description: "Deduplicate on the provider event id inside the same transaction that applies the effect."
track: system-design
section: messaging-and-queues
level: senior
type: system-design
tags: [idempotency, at-least-once, webhooks, exactly-once, deduplication]
status: published
updated: 2026-09-08
content_revision: 3
reconciled_with:
  uk: 3
see_also: [db-orm-0001]
applies_to:
  - product: PostgreSQL
    version: "17"
  - product: Stripe webhooks
    version: null
anki:
  export: true
sources:
  - source_id: stripe-webhooks-best-practices
    title: "Stripe documentation: receive Stripe events in your webhook endpoint"
    url: https://docs.stripe.com/webhooks
    accessed: 2026-09-08
    kind: official
    version: null
    applicability: "Delivery guarantees, retry behaviour, event identifiers and signature verification for Stripe webhooks; other providers differ in detail."
  - source_id: postgresql-17-insert-on-conflict
    title: "PostgreSQL 17 documentation: INSERT ... ON CONFLICT"
    url: https://www.postgresql.org/docs/17/sql-insert.html#SQL-ON-CONFLICT
    accessed: 2026-09-03
    kind: official
    version: "17"
    applicability: "Conflict handling against a unique constraint within one transaction, in PostgreSQL 17."
---

## Scale prompt

Peak 300 webhooks per second with bursts to 3000 during provider retry storms, at-least-once delivery
with retries for up to three days, and an availability target of 99.9% for the receiving endpoint.

## Short answer

**Treat delivery as at-least-once and make the effect idempotent, rather than trying to make delivery
exactly-once.** Stripe can automatically retry live-mode delivery for up to three days and does not
guarantee event order.[^stripe-webhooks-best-practices] Verify the signature, then key
everything on the provider event id under a unique constraint: whichever transaction applies the
business effect must commit that event's marker with it, so a retry finds the marker and does
nothing.[^postgresql-17-insert-on-conflict] Acknowledge fast and do the slow work asynchronously
under the same id.

## Detailed explanation

Every design in this space starts from one fact: the provider cannot know whether a lost response
means the effect happened. Its only safe behaviour is to retry, so the consumer receives duplicates by
design, and no amount of care on the sending side removes them.[^stripe-webhooks-best-practices]
"Exactly-once delivery" is therefore the wrong target; exactly-once *effect* is achievable, and it is
achieved on the consumer.

The consumer needs three separable properties. Authenticity: the request really came from the
provider, established by verifying the signature over the raw body before parsing it. Idempotency: a
repeated event produces no second effect. Ordering tolerance: events about one object may arrive in an
order that does not match the order in which they happened, so state transitions must be decided from
the event payload rather than from arrival order.

Idempotency has to be enforced by a store that can refuse a duplicate atomically, which in practice
means a unique constraint. The critical detail is that the deduplication record and the business
effect commit together. If the effect commits first and the record second, a crash between them
duplicates the effect on retry; if the record commits first, a crash loses the effect and the retry is
suppressed. One transaction removes both windows.[^postgresql-17-insert-on-conflict]

The final constraint is the response deadline. Providers time out quickly and treat a slow endpoint as
failed, which turns latency into a retry storm precisely when the system is already struggling. The
endpoint must therefore do the minimum needed to be safe and durable, then acknowledge; anything
expensive is queued under the same event id, so the worker is idempotent for the same reason the
endpoint is.

## Requirements

Functional:

- Accept webhook deliveries, verify their authenticity, and apply each event to the payment state
  machine exactly once in effect.
- Tolerate duplicates, retries and out-of-order arrival for the same object.
- Expose the processing state of an event for support queries and manual replay.

Non-functional:

- Respond within the provider timeout under peak and burst load.
- Lose no accepted event: once acknowledged, the event is durable.
- Keep the deduplication window at least as long as the provider retry window.
- Provide an audit trail: the raw payload of every accepted event is retained.

Out of scope: the payment state machine itself, and the outbound API calls to the provider.

## Scale assumptions

- 300 events per second sustained, bursts to 3000 for minutes at a time when the provider retries a
  backlog.
- Event payload up to 64 KB; median around 4 KB.
- Retry window of three days, so the deduplication table must cover at least that, sized at roughly
  80 million rows for a 3-day window at peak, and retained for 30 days for audit.
- Duplicate rate in normal operation below 1%, rising sharply during an incident.
- One database region; cross-region failover is allowed to lose the in-flight queue but not
  acknowledged events.

## Architecture

Ingress path, synchronous and small:

1. The endpoint reads the raw body, verifies the provider signature over it, and rejects with 400 on
   failure. Verification happens before parsing, because parsing normalises bytes and invalidates the
   signature.[^stripe-webhooks-best-practices]
2. It opens one transaction and inserts `(event_id, provider, received_at, payload)` into
   `webhook_event`, where `event_id` carries a unique constraint. `ON CONFLICT DO NOTHING` reports
   whether the row was new.[^postgresql-17-insert-on-conflict]
3. If the row is new, the same transaction enqueues a processing job by inserting into an outbox
   table keyed by `event_id`.
4. It commits and returns 200. A duplicate reaches step 2, inserts nothing, and returns 200 without a
   job.

Processing path, asynchronous:

5. Workers claim outbox rows and apply the effect inside a transaction that also marks the row done.
   The effect is written under the same `event_id`, so a worker that dies after the effect and before
   the mark is retried without a second effect.
6. Failed jobs retry with exponential backoff and land in a dead-letter table after a bounded number
   of attempts, with the raw payload available for replay.

The deduplication table is partitioned by `received_at` so that expiry is a partition drop rather than
a bulk delete, which matters at 80 million rows. Reading the payload for an audit query is a separate
path and must not compete with ingest: this is the same lazy-relation trap described in
[N+1 queries from lazy relation access](qid:db-orm-0001) at a different layer.

## Alternatives

**Deduplicate in the broker instead of the database.** Push events onto a log with a per-key
deduplication window and let the broker discard repeats. This removes a write from the ingress path,
but the broker window is time-bounded and usually far shorter than a three-day provider retry window,
and it cannot make the deduplication atomic with the effect.

**Make every handler naturally idempotent and skip the dedupe table.** Where the effect is a pure
state assignment derived from the payload, replaying it is harmless, and this is the cheapest design
when it applies. It fails for anything that accumulates: appending a ledger entry, incrementing a
counter, sending a notification.

**Idempotency key passed downstream.** Where the effect is an external call, the same event id can be
forwarded as the downstream idempotency key. This is complementary rather than an alternative: it
extends the guarantee across a boundary the consumer does not control.

**Store and forward with a synchronous 200 before durability.** Acknowledge immediately from memory
and persist afterwards. It gives the best latency and violates the requirement that an acknowledged
event is never lost, so it is only acceptable when the provider offers a long replay window and the
consumer is willing to depend on it.

## Trade-offs

| Decision | Bought | Paid |
|---|---|---|
| At-least-once plus idempotent effect | A guarantee that holds without provider cooperation | Every handler must be written with replay in mind |
| Dedupe insert in the effect transaction | No window in which the two can diverge | The effect is tied to the database that holds the dedupe table |
| Fast acknowledgement, async processing | Endpoint latency independent of the work | Processing state is eventually consistent, and support tooling must show it |
| Dedupe window covering the full retry window | Duplicates cannot slip in late | A large partitioned table and its maintenance |
| Deduplicating on provider event id | Stable across payload changes | Depends on the provider issuing one stable id per event |

## Failure modes

- **Provider retry storm.** A backlog is delivered in a burst; ingest must stay within timeout or the
  storm feeds itself. Mitigation: keep the ingress path to two writes, autoscale on queue depth rather
  than on CPU, and shed load with 429 rather than with a slow 200.
- **Duplicate arriving concurrently.** Two identical deliveries race on the same `event_id`. The
  unique constraint serialises them: one inserts, the other conflicts. Both return
  200.[^postgresql-17-insert-on-conflict]
- **Worker dies mid-effect.** The transaction rolls back, the outbox row stays claimable, and the
  retry reapplies the effect once. No compensating logic is needed.
- **Out-of-order arrival.** A `payment.failed` arrives after a `payment.succeeded` for the same
  object. Do not impose a total order using Stripe's event timestamp. Compare a reliable
  domain-monotonic version when the object exposes one; otherwise retrieve current provider state
  and reconcile the transition, as Stripe recommends for missing or out-of-order objects.[^stripe-webhooks-best-practices]
- **Signature key rotation.** Verification fails for legitimate events during a rotation window.
  Mitigation: accept both the current and previous secret while rotating, and alert on verification
  failures instead of dropping them silently.
- **Dedupe table exhausted or partition maintenance missed.** Ingest starts failing on insert, which
  is the correct direction: the endpoint returns 5xx and the provider retries, rather than the effect
  being applied twice.
- **Poison event.** A payload that always fails processing blocks nothing, because it is claimed
  individually and dead-lettered after bounded retries; the ingress path is unaffected.

## Evaluation guide

### Expected signals

- Rejects exactly-once delivery as unattainable and moves the guarantee to the effect.
- Commits the business effect together with its idempotency marker, and can name the two atomic
  boundaries in this design: the dedup row with the outbox row at ingress, the effect with the done
  mark in the worker.
- Can say what breaks in each of the two orderings if the effect and the marker are not committed
  together.
- Separates fast acknowledgement from slow processing, and keeps the event id as the idempotency key
  across that boundary.
- Treats out-of-order arrival as normal and uses a domain ordering key or current provider state,
  not arrival sequence or the event timestamp alone.
- Verifies the signature on the raw body before parsing.

### Red flags

- "Check whether we have seen this id, then process it" as two statements, with no transaction and no
  unique constraint.
- Relies on a queue that claims exactly-once semantics and stops thinking there.
- Does all the work synchronously inside the webhook request, and does not connect a slow endpoint to
  a retry storm.
- Deduplicates on a hash of the body, so a provider adding a field silently reprocesses everything.

### Level-up follow-up

Ask what happens when the effect is not in a database the consumer controls: sending an email,
charging a card, calling a third-party API. A senior answer separates the durable record of intent
from the external call, passes an idempotency key to the downstream provider where one is supported,
and accepts at-least-once for effects that cannot be made idempotent, with reconciliation to catch the
difference.

## Sources

<!-- generated from frontmatter -->
