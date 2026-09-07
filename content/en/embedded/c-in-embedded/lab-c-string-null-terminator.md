---
id: emb-cppfound-0072
title: "How is a C string stored in memory, and what is the role of the null terminator?"
description: "How the null terminator marks the end of a C string."
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
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

A string in C is an array of characters where the last element is **'\0' (null-terminator)**, a byte with value 0. "hello" -> `['h','e','l','l','o','\0']` – 6 bytes in memory. The null-terminator signals to standard functions (`strlen`, `strcpy`, `printf %s`) where the string ends; without '\0' – reading goes out of bounds -> UB. String literals automatically have '\0'; when filling manually: `buf[n] = '\0';` is mandatory.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
