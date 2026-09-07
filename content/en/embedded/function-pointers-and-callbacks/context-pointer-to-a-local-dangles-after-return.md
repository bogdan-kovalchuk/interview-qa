---
id: emb-fnptr-0029
title: "Trap: what is wrong with this context pointer?"
description: "&app becomes a dangling pointer after returning from init."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Question code

```c
void init(void) {
    struct App app;
    timer_register(on_timer, &app);
}
```

## Short answer

<span class="warn">`&app` becomes a dangling pointer after returning from `init`.</span>

If the timer callback fires later, it receives the address of a stack object that no longer exists. On an MCU this can look like random state corruption, a HardFault or a flaky bug.

Protection: make `app` static or global, store it in caller-owned storage, or unregister the callback before the object's lifetime ends.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
