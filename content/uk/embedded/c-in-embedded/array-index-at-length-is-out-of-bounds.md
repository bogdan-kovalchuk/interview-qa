---
id: emb-cppfound-0030
title: "Trap: що не так?<br><pre class=\"code-block\"><code><span class=\"code-type\">int</span> arr[<span class=\"code-num\">5</span>];<br>arr[<span class=\"code-num\">5</span>] = <span class=\"code-num\">0</span>;</code></pre>"
description: "Why an index equal to the array length is out of bounds."
track: embedded
section: c-in-embedded
level: junior
type: pitfall
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

<span class="warn">Out-of-bounds write -> undefined behavior.</span> Валідні індекси: <code>0..4</code>. <code>arr[5]</code> – за межами масиву.<br><br>У пам'яті <code>arr[5]</code> знаходиться одразу за масивом: це може бути інша локальна змінна, адреса повернення, saved LR.<br><br>Наслідки: тихе пошкодження даних або crash при поверненні з функції (зіпсована адреса повернення);<br><br>Захист: <code>-fsanitize=address</code>, явні перевірки індексів, <code>static_assert(i &lt; ARRAY_SIZE)</code>.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
