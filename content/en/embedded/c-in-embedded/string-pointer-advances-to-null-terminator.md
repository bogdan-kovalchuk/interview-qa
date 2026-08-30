---
id: emb-cppfound-0037
title: "What does this print?<br><pre class=\"code-block\"><code><span class=\"code-type\">char</span> str[] = \"hello\";<br><span class=\"code-type\">char</span> *p = str;<br><span class=\"code-kw\">while</span>(*p) p++;<br><span class=\"code-fn\">printf</span>(\"%td\", p-str);</code></pre>"
description: "How pointer iteration reaches the string null terminator."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-06
content_revision: 1
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
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
