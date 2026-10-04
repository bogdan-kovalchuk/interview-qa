---
id: emb-macros-0018
title: "Що означає `##` перед `__VA_ARGS__` у variadic-макросі?"
description: "##__VA_ARGS__ прибирає зайву кому, коли variadic-аргументів немає."
track: embedded
section: inline-and-macros
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
  - source_id: gcc-cpp-variadic-macros
    title: "GCC CPP: Variadic Macros"
    url: https://gcc.gnu.org/onlinedocs/cpp/Variadic-Macros.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Описує GNU-розширення для коми перед __VA_ARGS__ та портативний __VA_OPT__; поведінка залежить від режиму стандарту й препроцесора."
---

## Question code

```c
#define DBG(fmt, ...) printf(fmt, ##__VA_ARGS__)
```

## Short answer

**`##__VA_ARGS__` прибирає зайву кому**, коли variadic-аргументів немає.

У GNU-препроцесорі виклик `DBG("hi")` без додаткового механізму лишив би кому перед порожнім variadic argument; GNU-форма видаляє цю кому, отримуючи `printf("hi")`.

Це розширення GNU, а не загальнопортативний синтаксис; для C23 і C++20 передбачено `__VA_OPT__(,)`.[^gcc-cpp-variadic-macros]

## Detailed explanation

Variadic-макрос має параметри після `...`, доступні в replacement list через `__VA_ARGS__`. У звичайному стандартному записі кома перед цим параметром не зникає автоматично, коли додаткових аргументів немає. GNU C додає спеціальне значення для послідовності кома, `##` і `__VA_ARGS__`: за відсутності variadic arguments ця кома разом із маркером вилучається; за наявності аргументів зберігається їхній список.[^gcc-cpp-variadic-macros]

У фрагменті `DBG(fmt, ...)` перший аргумент формату є обов’язковим, а решта передаються `printf`. За виклику `DBG("ready")` GNU-препроцесор прибирає кому, що стоїть безпосередньо перед порожнім `__VA_ARGS__`, і виходить коректний виклик `printf("ready")`. За `DBG("value=%d", value)` зайвого роздільника немає: comma та аргумент залишаються, тож виклик стає `printf("value=%d", value)`.

Не називайте цей прийом правилом `##` загалом: оператор token-pasting зазвичай склеює preprocessing tokens, але цей особливий випадок перед `__VA_ARGS__` визначений як GNU extension. Сумісні режими GCC та Clang підтримують його, та суворий портативний код має спиратися на потрібну версію мови й перевіряти підтримку компілятором. У C23 та C++20 `__VA_OPT__` умовно додає роздільник тільки тоді, коли variadic частина непорожня.[^iso-c-n1570] [^gcc-cpp-variadic-macros]

Наприклад, стандартний за задумом шаблон може мати вигляд `#define DBG(fmt, ...) printf(fmt __VA_OPT__(,) __VA_ARGS__)`; він зберігає кому між `fmt` та додатковими аргументами лише коли вони є. Саме роздільник у дужках `__VA_OPT__(,)` не слід механічно переносити до старішого C або C++ режиму.

**Типові помилки:**

- Вважати, що GNU-форма `, ##__VA_ARGS__` підтримується кожним стандартним препроцесором.
- Плутати порожню variadic частину з аргументом, що сам розгортається в порожню послідовність токенів.
- Не перевірити режим мови та діагностику цільового compiler.

## Sources

<!-- generated from frontmatter -->
