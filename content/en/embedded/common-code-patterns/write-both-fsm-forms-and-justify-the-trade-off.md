---
id: emb-patterns-0042
title: "What should a candidate be able to do on embedded code pattern questions?"
description: "Write FSMs in both forms, explain trade-offs, build a power-of-two ring buffer, and do unsigned mask-and-shift bit ops."
track: embedded
section: common-code-patterns
level: junior
type: concept
tags: []
status: published
updated: 2026-10-06
content_revision: 3
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-06; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Confirms the rules for shifts and unsigned arithmetic (6.5.7, 6.2.5 para. 9), the semantics of `volatile` (6.7.3 para. 7), a data race as undefined behavior (5.1.2.4 para. 25) and that `malloc` can return null (7.22.3); specific devices and toolchains can differ."
  - source_id: holzmann-power-of-ten
    title: "The Power of Ten – Rules for Developing Safety Critical Code (G. J. Holzmann, NASA/JPL)"
    url: https://spinroot.com/gerard/pdf/P10.pdf
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Paper by a NASA/JPL author, hosted on his site: rule 3 forbids dynamic memory allocation after initialization because allocators such as malloc, and garbage collectors, often have unpredictable behavior that can significantly impact performance. It is a guideline, not the requirement of a specific safety standard; the paper does not discuss heap fragmentation directly."
  - source_id: linux-circular-buffers
    title: "Circular Buffers (Linux kernel documentation)"
    url: https://www.kernel.org/doc/html/latest/core-api/circular-buffers.html
    accessed: 2026-10-06
    kind: official
    version: "7.3.0-rc6"
    applicability: "Confirms that for a power-of-two buffer size the index wraps with a bitwise AND instead of a division, and that the one-producer one-consumer scheme needs no shared lock. It is Linux kernel (SMP) documentation, not bare-metal MCU documentation."
---

## Short answer

**Write an FSM (finite state machine) in both forms – switch and table; explain the trade-offs; build a power-of-two ring buffer and know why a shared `count` causes a race; perform bit operations via unsigned mask-and-shift.**

Plus: consistent return codes with every result checked, `volatile` for registers (but not as synchronization with an ISR), guard clauses for null/range.[^iso-c-n1570]

Rule: for every pattern have answers for "when to apply", "is it ISR-safe (interrupt service routine safe)" and "why no heap".

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
