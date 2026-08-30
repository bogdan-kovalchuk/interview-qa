---
id: emb-cppfound-0090
title: "Знайдіть помилку: чи переміститься зовнішній pointer?<br><pre class=\"code-block\"><code><span class=\"code-type\">void</span> advance(<span class=\"code-type\">char</span> *p, <span class=\"code-type\">int</span> n){<br>  p += n;<br>}</code></pre>"
description: "Why changing a pointer parameter does not change the caller's pointer."
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

<span class="warn">НІ.</span> У C параметри передаються <span class="key">за значенням</span>. Функція отримує копію вказівника <code>p</code>. <code>p += n</code> змінює локальну копію, але не оригінальний вказівник у caller-і.<br><br>Для зміни caller-ського pointer: потрібен double pointer:<br><code>void advance(char **p, int n){ *p += n; }</code><br>Виклик: <code>advance(&amp;cursor, 5);</code><br><br>Класична помилка при реалізації парсерів і потокових обробників.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
