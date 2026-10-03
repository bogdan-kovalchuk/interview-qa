---
id: emb-volconst-0042
title: "Trap: чому `const` у C не означає compile-time constant для всіх випадків?"
description: "У C const означає read-only object через цей identifier, але не завжди integer constant expression."
track: embedded
section: volatile-and-const
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

<span class="warn">У C `const` обмежує зміну object-а через цей identifier, але саме значення object-а не стає integer constant expression.</span>[^iso-c-n1570]

Наприклад, `const int n = 10;` не є integer constant expression у C і не підходить для розміру звичайного file-scope array, де потрібен такий вираз. У C++ правила відрізняються. Для сталого розміру в C зазвичай використовують integer constant, `enum` або `#define`.

Захист: не плутай обмеження запису через `const` із вимогою мови до integer constant expression.[^iso-c-n1570]

## Detailed explanation

`const` у C кваліфікує тип object-а й забороняє змінювати його через lvalue без `const`; воно не перетворює object на integer constant expression. Це різні властивості: перша описує допустимий доступ до object-а під час виконання, а друга визначає, які вирази дозволені в контекстах, що потребують значення часу трансляції.[^iso-c-n1570]

У прикладі `const int n = 10;` ім’я `n` позначає object. Навіть коли його ініціалізатор записаний числовою константою, звернення до `n` не належить до категорій операндів integer constant expression, перелічених стандартом C. Тому `n` не можна загалом підставити замість integer constant expression у контексті, де він обов’язковий, наприклад у розмірі file-scope array. Слово «загалом» тут суттєве: вимоги залежать від конкретного контексту, а не лише від того, чи змінює програміст значення object-а.[^iso-c-n1570]

**Приклад:**

```c
const int n = 10;
int values[n];       // на file scope це не стандартний fixed-size array у C
enum { COUNT = 10 };
int fixed[COUNT];    // COUNT є integer constant expression
```

Не слід автоматично пояснювати кожне прийняття `const int` компілятором як гарантію переносимості: розширення компілятора можуть дозволяти більше, ніж вимагає стандарт. Так само block-scope оголошення з таким розміром може трактуватися як VLA за підтримки цієї можливості; це інший тип array і не робить `n` integer constant expression. Перевіряй потрібний dialect та прапорці компілятора, особливо для embedded toolchain, де VLA може бути вимкнено.[^iso-c-n1570]

Типова пастка проявляється як прийнятий код, який перестає компілюватися з іншим режимом C або toolchain. Щоб уникнути її, визначай константу способом, дозволеним потрібним контекстом, і перевіряй діагностику в цільовому режимі компіляції. `const` і далі корисний для захисту від випадкового запису; просто не використовуй його як синонім compile-time constant.[^iso-c-n1570]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
