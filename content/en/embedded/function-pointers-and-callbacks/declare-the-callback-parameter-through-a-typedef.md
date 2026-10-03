---
id: emb-fnptr-0014
title: "How do you declare a function that takes a callback `void cb(int)`?"
description: "Declare the parameter directly as a function pointer, or use a typedef for readability."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: mechanism
tags: []
status: published
updated: 2026-10-04
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Short answer

Yes. Direct parameter declaration, but a typedef is more readable:

```c
void register_cb(void (*cb)(int));

typedef void (*event_cb_t)(int);
void register_cb(event_cb_t cb);
```

Both declarations specify the same parameter type; a typedef only gives it a reusable name and makes the signature easier to read. It adds no checks or guarantees by itself.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
