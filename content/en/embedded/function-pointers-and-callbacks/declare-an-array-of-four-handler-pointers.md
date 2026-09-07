---
id: emb-fnptr-0047
title: "How do you declare an array of four `void handler(void)` handlers?"
description: "Declare the array as void (handlers[4])(void), or more readably through a typedef handlert handlers[4]."
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

Yes. Direct array declaration, or more readably through a typedef:

```c
void (*handlers[4])(void);

typedef void (*handler_t)(void);
handler_t handlers[4];
```

Rule: in complex declarations of a function pointer array, using a typedef is almost always worthwhile.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
