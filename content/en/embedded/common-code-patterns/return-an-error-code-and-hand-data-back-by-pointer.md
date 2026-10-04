---
id: emb-patterns-0018
title: "What does the return-code error handling pattern look like?"
description: "The function returns err_t and passes data through an output pointer."
track: embedded
section: common-code-patterns
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

## Question code

```c
typedef enum {
  ERR_OK = 0, ERR_TIMEOUT, ERR_CRC, ERR_BUSY, ERR_PARAM
} err_t;

err_t sensor_read(uint8_t a, uint16_t *out);
```

## Short answer

**The function returns `err_t` and passes data through an output pointer.**

When the API defines `ERR_OK = 0`, `if (result) { /* error */ }` tests for a non-zero result. Each error branch can return a specific code.[^iso-c-n1570]

Return codes make status explicit, but the caller must still check the result.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
