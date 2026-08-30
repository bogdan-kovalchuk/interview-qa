---
id: emb-cemb-0028
title: "Які існують бітові операції?"
description: "Побітові AND, OR, XOR, NOT і зсуви використовують для перевірки, встановлення, скидання та перемикання бітів у регістрах."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження цього питання й відповіді; текст відповіді не перевірений незалежно від оригінальної Anki-колоди спільноти."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? c-in-embedded; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

<code>&amp;</code> AND – скидання біта: <code>reg &amp;= ~(1&lt;&lt;n)</code><br><code>|</code> OR – встановлення біта: <code>reg |= (1&lt;&lt;n)</code><br><code>^</code> XOR – інвертування: <code>reg ^= (1&lt;&lt;n)</code><br><code>~</code> NOT – побітова інверсія<br><code>&lt;&lt;</code> зсув вліво: <code>x &lt;&lt; 3</code> = x × 8<br><code>&gt;&gt;</code> зсув вправо: <code>x &gt;&gt; 1</code> = x / 2.<br><br>Типові патерни в Embedded:<br>Перевірити біт: <code>if (reg &amp; (1&lt;&lt;n))</code><br>Встановити: <code>reg |= (1&lt;&lt;n)</code><br>Скинути: <code>reg &amp;= ~(1&lt;&lt;n)</code><br>Перемкнути: <code>reg ^= (1&lt;&lt;n)</code>.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
