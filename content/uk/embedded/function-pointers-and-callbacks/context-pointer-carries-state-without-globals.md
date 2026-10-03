---
id: emb-fnptr-0005
title: "Чому в callback API часто є параметр `void *context`?"
description: "context передає стан користувача callback-а без глобальних змінних."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: concept
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

**`context` дає callback-у доступ до стану конкретного екземпляра.**

C function pointer і data pointer – різні типи; `void *` тут переносить адресу об’єкта, наприклад структури стану, а не адресу callback-функції.[^iso-c-n1570]

Driver зберігає callback разом із цим data pointer і передає його при виклику. Той самий код callback-а тоді може обслуговувати кілька незалежних пристроїв без окремих глобальних змінних.

## Detailed explanation

Параметр `void *context` у callback API дає callback-у доступ до стану того об’єкта або операції, для яких сталася подія. Сам function pointer і data pointer виконують різні ролі: перший визначає код для виклику, а другий переносить адресу даних, які callback має обробити. У C `void *` є універсальним покажчиком на об’єкт, з якого можна перетворитися назад на сумісний object pointer; це не загальний контейнер для function pointer-ів.[^iso-c-n1570]

API зазвичай зберігає обидва значення в об’єкті driver-а. Коли, наприклад, надходить байт UART, driver викликає callback і передає збережений `context`. Реалізація callback-а знає справжній тип даних, приводить покажчик до нього й оновлює відповідний стан. Це розділяє загальний механізм driver-а та специфічну логіку застосунку.

Такий підхід корисний, коли один callback-код працює з кількома UART-ами чи таймерами: кожна реєстрація має власну структуру стану, тому обробники не перезаписують спільну глобальну змінну. Контракт API має також визначати, чи може callback бути відсутнім, де саме його викликають, чи дозволено з нього блокуватися та як довго мають жити дані `context`. Це вимоги до конкретного API, а не гарантії, які задає мова C.

Приклад:

```c
struct RxState { unsigned count; };
void on_byte(void *context, uint8_t byte) {
    struct RxState *state = context;
    state->count += byte != 0;
}
```

Тут `context` має вказувати на живий об’єкт `struct RxState` протягом усіх викликів; передавання покажчика на локальну змінну після завершення її lifetime зробило б його непридатним. Тип і lifetime слід погодити між кодом, що реєструє callback, та driver-ом.

## Sources

<!-- generated from frontmatter -->
