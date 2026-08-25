---
id: cpp-tooling-0001
title: "A worker crashes once every few thousand requests: how do you find the use-after-free?"
description: "An asynchronous callback captured a reference that outlived the object; a sanitizer turns the crash into a stack trace."
track: cpp
section: tooling-and-diagnostics
level: senior
type: debugging
tags: [use-after-free, sanitizers, lifetime, asynchronous, undefined-behavior]
status: published
updated: 2026-09-03
content_revision: 1
reconciled_with:
  uk: 1
see_also: [cpp-ptrref-0001]
applies_to:
  - product: ISO C++
    version: "C++20"
anki:
  export: true
sources:
  - source_id: clang-address-sanitizer
    title: "Clang documentation: AddressSanitizer"
    url: https://clang.llvm.org/docs/AddressSanitizer.html
    accessed: 2026-09-03
    kind: official
    version: null
    applicability: "Flags, report format and quarantine behaviour of AddressSanitizer as documented by Clang; GCC implements the same interface."
  - source_id: cppreference-object-lifetime
    title: "cppreference: Lifetime"
    url: https://en.cppreference.com/w/cpp/language/lifetime
    accessed: 2026-09-03
    kind: spec
    version: "C++20"
    applicability: "When the lifetime of an object ends and what access after that point means, through C++20."
---

## Short answer

**Stop reproducing the crash and start detecting the access instead: rebuild the service with
AddressSanitizer and run the ordinary load.** The sanitizer reports the freed allocation, the stack
that freed it and the stack that touched it afterwards, which turns an intermittent crash into one
readable report.[^clang-address-sanitizer] The pattern behind almost all of these is an asynchronous
callback holding a reference to an object whose owner returned; access after the lifetime ends is
undefined, so a crash is the lucky outcome.[^cppreference-object-lifetime]

## Detailed explanation

An intermittent crash under load is a scheduling question before it is a memory question. The failure
appears only when two operations interleave in a particular order, so the first instinct, running it
again under a debugger, mostly reproduces the ordering that works.

Reasoning about which pointer is stale is also the slow path. The efficient move is to make the
program detect the bad access itself. AddressSanitizer replaces the allocator, marks freed memory as
poisoned, keeps it in quarantine instead of handing it straight back, and reports the allocation, the
deallocation and the offending access with all three stacks.[^clang-address-sanitizer] That converts a
crash whose stack points at innocent code into a report that names the guilty pair directly.

The reason a use-after-free is so rarely a clean crash is that freed memory usually remains mapped.
Reading it returns whatever the allocator has put there since, so the program continues with a
plausible-looking value and fails somewhere else entirely. Nothing in the language promises otherwise:
once the lifetime has ended, any access is undefined behaviour, and "it worked in staging" is a
statement about the allocator, not about correctness.[^cppreference-object-lifetime]

## Symptom

A request-handling service crashes roughly once every few thousand requests, only under concurrent
load, and never in a single-threaded test. The stack trace differs from crash to crash and usually
points into standard library code such as `std::string` destruction rather than into service code.
Some occurrences produce garbled log output instead of a crash.

## Observations

- The crash rate scales with concurrency, not with request count: two workers crash far less often
  than sixteen at the same total volume.
- Every trace involves the completion path of an asynchronous operation.
- The corrupted values are readable text belonging to a different, already finished request.
- A debug build with a checked allocator crashes at a different point but no less often.
- Reverting the change that moved response serialisation into the thread pool removes the crash.

## Reproduction

Build the service with `-fsanitize=address -fno-omit-frame-pointer -g -O1` and run the load generator
at sixteen concurrent connections against an endpoint that returns a session-derived body. The report
appears within a few hundred requests, well before the unsanitised build would have
crashed.[^clang-address-sanitizer] The minimal form is a session destroyed by its owner while a pool
task still holds a reference to it:

```cpp
void submit(ThreadPool& pool, Session& session) {
    pool.post([&session] { session.write_response(); });   // captures a reference
}                                                          // owner destroys the session on return
```

## Hypotheses

1. Two threads write to one shared buffer without synchronisation, and the data race corrupts it.
2. A callback outlives the object it refers to, and the completion path touches freed memory.
3. The allocator or an interposing library is at fault.
4. The container holding sessions reallocates while another thread holds a pointer into it.

Hypothesis 3 is last on evidence: a fault in a widely used allocator is far less likely than a fault
in the code that changed last week. Hypotheses 2 and 4 are both lifetime bugs, and the sanitizer
distinguishes them, because it reports the allocation that was freed.

## Diagnosis

AddressSanitizer reports `heap-use-after-free`, an eight-byte read inside `Session::write_response`.
The three stacks settle it: the allocation stack is the request accept path, the free stack is the
handler returning and destroying the session, and the access stack is the pool worker running the
posted lambda.[^clang-address-sanitizer] Hypothesis 2 is confirmed and the others are ruled out; the
report names one object rather than a range, so it is not container reallocation.

The lambda captured the session by reference and was posted to a pool that runs it later. The handler
returns as soon as the task is queued, and the session is a local of that handler, so its lifetime
ends before the task runs. Whether the worker reaches the object before or after that happens is
decided by the scheduler, which is exactly why load and concurrency change the failure rate.

## Fix

Give the task shared ownership of what it uses, so that the lifetime cannot end while the task is
pending. The choice between exclusive and shared ownership is the one described in
[unique_ptr against shared_ptr](qid:cpp-ptrref-0001); here the number of owners genuinely is not known
in advance, because the pool may still hold the task after the handler has returned.

```cpp
void submit(ThreadPool& pool, std::shared_ptr<Session> session) {
    pool.post([session = std::move(session)] { session->write_response(); });
}
```

Capturing by value moves the ownership into the task, and the session is destroyed when the task
finishes, on whichever thread that turns out to be. Do not fix this by making the handler wait for the
task: that removes the crash and removes the point of the thread pool with it.

## Prevention

- Keep the sanitizer build in CI and run the integration suite under it, not only the unit tests. This
  particular defect is only reachable with concurrency, so the suite has to exercise it.
- Treat capture by reference in anything posted, deferred or detached as a review rule: the capture
  list must not contain a bare reference unless the callback provably finishes first.
- Make ownership explicit in the API. A `post` that takes a `shared_ptr` cannot be handed a dangling
  reference; one that takes an arbitrary callable can.
- When a crash is intermittent, record the concurrency at which it appears. It is the cheapest signal
  that the defect is an ordering one, and it belongs in the ticket.

## Evaluation guide

### Expected signals

- Reaches for a sanitizer or an equivalent detector before reaching for a debugger or for added
  logging.
- Explains why the crash location is misleading: the corruption and the symptom are separated in time.
- Identifies capture by reference in an asynchronous callback as the lifetime bug, not the thread pool.
- Proposes a fix that changes ownership rather than one that changes timing.

### Red flags

- Adds a sleep, a retry or a lock and calls the problem fixed once the crash rate drops.
- Concludes "memory corruption, probably the allocator" and stops there.
- Says undefined behaviour is acceptable because the field values look correct in practice.

### Level-up follow-up

Ask what they would do if the sanitizer build is too slow to carry the production load. A senior
answer covers running it against replayed traffic, on a canary instance, or in a targeted stress test,
and mentions that a use-after-free can also be surfaced by an allocator that does not reuse memory
quickly.

## Sources

<!-- generated from frontmatter -->
