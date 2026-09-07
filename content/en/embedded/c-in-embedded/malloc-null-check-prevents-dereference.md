---
id: emb-cppfound-0084
title: "Why should malloc always be checked for NULL?"
description: "Why failed allocation must be handled before dereferencing the result."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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
    applicability: "Origin of the question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

`malloc` returns **NULL** on allocation failure (no memory, heap fragmentation). If not checked and NULL is dereferenced -> <span class="warn">HardFault on MCU</span>.

```c
int *p = malloc(n * sizeof(int));
if(p == NULL) { error_handler(); return; }
// Тепер безпечно використовувати
```

In embedded: malloc can fail even for small requests due to fragmentation; safety-critical standards forbid malloc altogether – but if you use it, the check is mandatory.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
