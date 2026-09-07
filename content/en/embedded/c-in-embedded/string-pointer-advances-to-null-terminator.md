---
id: emb-cppfound-0037
title: "What does this print?"
description: "How pointer iteration reaches the string null terminator."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 4
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
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Question code

```c
char str[] = "hello";
char *p = str;
while(*p) p++;
printf("%td", p-str);
```

## Short answer

`5`.

`str` decays to `char*`, so the loop runs until `'\0'`: after `'h','e','l','l','o'` – `*p = '\0'` (false) -> stop. `p` points to the null terminator.

`p - str` = 5 elements = `strlen("hello")`. This is the standard way to implement `strlen` via pointer arithmetic, using `%td` for `ptrdiff_t`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
