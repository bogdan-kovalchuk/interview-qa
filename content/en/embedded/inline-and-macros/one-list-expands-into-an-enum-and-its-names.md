---
id: emb-macros-0022
title: "How does an X-macro keep an `enum` and a string array in sync?"
description: "A single ERR_LIST is expanded twice with different X so the enum and string array stay in sync."
track: embedded
section: inline-and-macros
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
#define ERR_LIST(X) \
  X(ERR_NONE, "OK") \
  X(ERR_TIMEOUT, "Timeout")
```

## Short answer

The same list is expanded twice with different `X`:

```c
#define AS_ENUM(n, s) n,
typedef enum { ERR_LIST(AS_ENUM) } err_t;

#define AS_STR(n, s) [n] = s,
static const char *const names[] = { ERR_LIST(AS_STR) };
```

One list – two generated objects. A new error code is added in one place, and both `enum` and `names[]` are updated together.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
