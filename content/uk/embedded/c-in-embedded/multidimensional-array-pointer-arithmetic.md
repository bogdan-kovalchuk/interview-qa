---
id: emb-cppfound-0060
title: "Що виведе?<br><pre class=\"code-block\"><code>int arr[3][3]={{1,2,3},{4,5,6},{7,8,9}};<br>printf(\"%d\", *(*(arr+1)+2));</code></pre>"
description: "How multidimensional-array pointer arithmetic reaches an element."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 1
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
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? c-in-embedded; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

<code>6</code>.<br><br><code>arr+1</code> -> вказівник на другий рядок <code>arr[1]</code> (тип <code>int(*)[3]</code>). <code>*(arr+1)</code> -> decay до <code>int*</code>, вказує на <code>arr[1][0] = 4</code>. <code>*(arr+1)+2</code> -> вказує на <code>arr[1][2] = 6</code>. <code>*(*(arr+1)+2)</code> -> значення = <code>6</code>.<br><br>Еквівалентно: <code>arr[1][2]</code>.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
