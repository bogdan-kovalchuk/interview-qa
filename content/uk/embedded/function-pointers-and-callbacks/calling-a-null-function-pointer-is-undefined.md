---
id: emb-fnptr-0009
title: "Trap: що станеться при виклику null function pointer?"
description: "Виклик null function pointer у C має undefined behavior; стандарт не визначає наслідку, а симптом залежить від платформи."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-04
content_revision: 3
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

## Question code

```c
void (*cb)(void) = NULL;
cb();
```

## Short answer

<span class="warn">Undefined behavior.</span>

Стандарт C не визначає результат такого виклику: це `undefined behavior`, а конкретна реакція залежить від реалізації та платформи.[^iso-c-n1570]

Захист: перевіряй `cb != NULL` перед необов’язковим викликом або задай API гарантований no-op callback.

## Detailed explanation

Викликати null function pointer не можна: у C це `undefined behavior`, отже стандарт не вимагає конкретного результату.[^iso-c-n1570] Програма може аварійно завершитися, зависнути, здаватися працездатною або поводитися інакше; жоден із цих проявів не є гарантованим. Зокрема, не можна виводити точну адресу переходу чи тип exception лише з правил мови.

Проблема часто з’являється в optional callback API: покажчик ініціалізовано як null, реєстрацію не виконано або її скасовано, але шлях обробки події все одно безумовно викликає `cb()`. На MCU наслідок визначають компілятор, ABI, карта пам’яті та ядро. Можлива апаратна fault, але стандарт C цього не обіцяє й не задає поведінку Cortex-M.

Перед викликом перевіряй стан покажчика або зроби контракт API таким, що завжди містить допустиму функцію. У першому варіанті guard має оточувати саме виклик, а стан реєстрації не повинен змінюватися паралельно без належної синхронізації. У другому варіанті no-op функція може спростити dispatch, але лише якщо її сигнатура точно відповідає callback type.

Приклад:

```c
if (cb != NULL) {
    cb();
}
```

Типова помилка – вважати, що null означає «нічого не робити». Null pointer лише позначає відсутність функції; він не є викличним no-op. Перевірка перед викликом запобігає цьому конкретному дефекту, але не виправляє інші помилки на кшталт dangling pointer чи несумісної сигнатури.

**Як уникнути помилки:** узгодь, чи дозволено null після ініціалізації та скасування реєстрації, і забезпеч guard або default handler на всіх шляхах диспетчеризації.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
