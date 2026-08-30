---
id: emb-cppfound-0013
title: "Розберіть?<br><pre class=\"code-block\"><code>int arr[3] = {1,2,3};<br>printf(\"%d %d\", arr[2], *(arr+2));</code></pre>"
description: "Why array indexing and pointer dereferencing are equivalent."
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

Обидва вирази виводять <span class="key">3</span> і є повністю еквівалентними за стандартом C.<br><br><code>arr[2]</code> -> стандарт визначає як <code>*(arr+2)</code>: до адреси <code>arr</code> додається <code>2 * sizeof(int) = 8</code> байт, потім розіменовується.<br><br>Тому навіть <code>2[arr]</code> -> <code>*(2+arr)</code> -> 3 – теж коректно (через комутативність додавання, хоча й нечитабельно).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
