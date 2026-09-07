---
id: emb-patterns-0018
title: "What does the return-code error handling pattern look like?"
description: "The function returns errt and passes data through an output pointer"
track: embedded
section: common-code-patterns
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

## Question code

```c
typedef enum {
  ERR_OK = 0, ERR_TIMEOUT, ERR_CRC, ERR_BUSY, ERR_PARAM
} err_t;

err_t sensor_read(uint8_t a, uint16_t *out);
```

## Short answer

**The function returns `err_t` and passes data through an output pointer.**

`ERR_OK = 0` is always zero, so `if (result) { /* error */ }` is readable. Each error branch returns a specific code.

Rule: return codes are the default pattern because they force the caller to check the result.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
