---
id: emb-volconst-0020
title: "Як прочитати декларацію `int * const p`?"
description: "p є const pointer to int."
track: embedded
section: volatile-and-const
level: junior
type: mechanism
tags: []
status: published
updated: 2026-10-04
content_revision: 2
reconciled_with:
  en: 3
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; це джерело не є доказом тверджень."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
---

## Short answer

**`p` є const pointer to `int`**.

`p = &other` заборонено, але `*p = 5` дозволено, якщо об’єкт не const. Це часто плутають із `const int *p`, де const стосується даних, а не адреси.

Embedded-приклад: pointer на fixed RAM cell або writable register address, який не має змінюватися після ініціалізації.[^iso-c-n1570]

## Detailed explanation

У декларації `int * const p` слово `const` стоїть після зірочки, тому воно кваліфікує сам pointer `p`, а не об’єкт `int`, на який він вказує. Якщо `p` ініціалізовано адресою змінного `int`, це значення pointer не можна перепризначити, але запис через `*p` дозволений. Це протилежний розподіл обмеження порівняно з `const int *p`, де pointer можна змінити, але запис через нього заборонений.[^iso-c-n1570]

Зручний спосіб перевірити тип – уявно взяти дужки навколо декларатора: `int * const p` означає, що `p` є const pointer, який вказує на `int`. Ініціалізація має надати йому адресу одразу; оголошення локальної змінної без ініціалізатора залишає її значення невизначеним, а подальше читання такого pointer є помилкою. Після коректної ініціалізації компілятор діагностує спробу `p = &other`, але не забороняє `*p = 5`, якщо об’єкт доступний для запису.[^iso-c-n1570]

У вбудованому коді це може фіксувати локальний alias на конкретну RAM-комірку, але сама адреса не стає безпечною чи валідною від того, що pointer const. Для memory-mapped register зазвичай потрібен тип на кшталт `volatile uint32_t * const reg`: `const` утримує адресу, а `volatile` описує спеціальні правила оптимізації доступів до об’єкта. Кваліфікатори мають відповідати апаратному контракту; `const` не замінює `volatile`, а `volatile` не гарантує атомарності чи міжпотокової синхронізації.[^iso-c-n1570]

**Приклад:** `int value = 1; int * const p = &value;` дозволяє `*p = 5`, тож `value` стане 5, але `p = &other` є помилкою. Якщо об’єкт оголошений `const int`, його не можна змінювати лише через те, що сам pointer не має `const` на цільовому типі: така ініціалізація типово несумісна без явного небезпечного приведення.

**Типові помилки:**
- вважати, що `const` після `*` захищає значення за адресою;
- забути ініціалізувати const pointer;
- вважати const pointer еквівалентом `volatile` pointer для MMIO.

## Sources

<!-- generated from frontmatter -->
