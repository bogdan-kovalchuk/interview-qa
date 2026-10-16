---
id: emb-fnptr-0008
title: "Чи потрібен оператор `&` при присвоєнні функції у function pointer?"
track: embedded
section: function-pointers-and-callbacks
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**Для звичайного присвоєння function pointer оператор `&` не обов’язковий.**

`cb = foo;` і `cb = &foo;` мають однаковий ефект для сумісної функції: function designator перетворюється на pointer to function, а `&foo` явно бере адресу функції.[^iso-c-n1570] Так само `cb()` і `(*cb)()` є дозволеними формами виклику.

## Detailed explanation

У виразі `cb = foo` ім’я `foo` є function designator. У C воно зазвичай перетворюється на pointer to function потрібного типу, тому явний унарний `&` не потрібен. `&foo` теж утворює адресу цієї функції, тож обидві форми сумісні з відповідним function pointer за умови, що сигнатура функції відповідає типу покажчика.[^iso-c-n1570]

Наприклад, якщо `cb` оголошено як `int (*cb)(int)`, то `foo` має бути функцією з сумісним типом на кшталт `int foo(int)`. Наявність `&` не виправляє несумісність типів і не виконує функцію: для виклику потрібні аргументи в дужках, наприклад `cb(5)`. Без них присвоєння лише зберігає адресу для пізнішого виклику.

Це перетворення має винятки: наприклад, `sizeof foo` не перетворює function designator, а `&foo` якраз застосовує address operator без цього перетворення.[^iso-c-n1570] Для звичайного callback-коду достатньо запам’ятати, що `cb = foo` та `cb = &foo` ведуть до того самого призначення, тоді як `cb()` виконує виклик через покажчик.

Приклад:

```c
int foo(int value) { return value + 1; }
int (*cb)(int) = foo;
int result = cb(4);  /* result is 5 */
```

Такий короткий запис не є вимогою стилю або гарантією для будь-якого довільного типу; це правило мови C для function designator і сумісного покажчика на функцію.
