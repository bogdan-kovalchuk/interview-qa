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

## Short answer

Yes. Direct parameter declaration, but a typedef is more readable:

```c
void register_cb(void (*cb)(int));

typedef void (*event_cb_t)(int);
void register_cb(event_cb_t cb);
```

Rule: raw syntax is useful to know for interviews, but in production APIs a typedef makes the contract stable and less error-prone.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
