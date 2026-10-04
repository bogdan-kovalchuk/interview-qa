---
id: emb-macros-0031
title: "Trap: чому `inline` без `static` у C може дати linker error?"
description: "У C99+ функція, оголошена просто inline (без static/extern), надає лише inline definition; вона не створює external symbol."
track: embedded
section: inline-and-macros
level: junior
type: pitfall
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

У C99+ визначення функції з external linkage, оголошеної просто `inline`, є inline definition, а не external definition; саме по собі воно не гарантує зовнішнього символу для linker.[^iso-c-n1570]

Якщо виклик потребує зовнішнього визначення, але жодна translation unit його не надає, linker може повідомити про відсутній symbol. Компілятор не зобов’язаний вбудовувати виклик.[^iso-c-n1570]

Для функції, визначеної у header окремо в кожній translation unit, типовий варіант – `static inline`, що надає функції internal linkage у кожній одиниці трансляції.[^iso-c-n1570]

## Detailed explanation

У C99 і пізніших версіях стандарту `inline` є підказкою щодо можливого способу реалізації виклику, а не командою компілятору. Функція з external linkage, визначена без `extern`, утворює inline definition. Стандарт прямо відрізняє її від external definition: компілятор може використати inline definition для викликів у цій translation unit, але сам цей текст не надає обов’язкового зовнішнього визначення для компонування.[^iso-c-n1570]

Тому сам факт наявності тіла функції у `.c` файлі не завжди означає, що linker матиме зовнішній symbol. Якщо виклик не вбудовано і потрібне зовнішнє визначення, його треба надати окремо відповідно до правил C inline linkage. Реалізація може вирішити вбудувати виклик, але програма не повинна покладатися на оптимізацію: рішення залежить від оптимізатора, прапорців і меж translation unit.[^iso-c-n1570]

Приклад заголовка для невеликої функції, тіло якої має бути доступне в кожній translation unit:

```c
static inline int clamp_low(int value, int low)
{
    return value < low ? low : value;
}
```

`static` надає функції internal linkage, тому кожна translation unit, що включає цей header, має власне визначення. Це прибирає вимогу до одного спільного external definition, хоча функція може бути скомпільована як звичайний виклик, якщо компілятор так вирішить.[^iso-c-n1570]

Якщо потрібен один зовнішній symbol, поширений підхід – оголосити функцію у header як `inline` declaration для клієнтів, а в одному `.c` файлі надати відповідне визначення з `extern` згідно з обраною схемою C. Через тонкі відмінності між C99 inline, GNU89 inline та C++ inline потрібно перевіряти мову і режим компілятора; висновок для C++ не можна автоматично переносити на C.[^iso-c-n1570]

**Типова помилка:** стверджувати, що кожна проста `inline` функція завжди викликає linker error. Помилка виникає лише коли згенерований код потребує зовнішнього визначення, а його немає. Інша помилка – вважати `inline` гарантією оптимізації: стандарт такої гарантії не дає.[^iso-c-n1570]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
