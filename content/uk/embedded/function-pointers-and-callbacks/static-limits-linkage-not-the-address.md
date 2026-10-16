---
id: emb-fnptr-0035
title: "Чи може callback бути `static` функцією?"
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

**Так.**

`static` у file scope надає функції internal linkage, але її адресу можна передати як callback у межах того самого translation unit. Інша одиниця трансляції не може посилатися на її ім’я, однак callback, якому вже передали адресу, може викликати функцію.[^iso-c-n1570]

Наприклад, file-scope `static` handler можна передати локальному драйверу чи scheduler-у без експорту імені в інші translation units. `static` тут не змінює тип функції або тип її вказівника – обмежується саме linkage імені.[^iso-c-n1570]

## Detailed explanation

Функція з `static` на file scope має internal linkage: її ім’я позначає ту саму функцію лише всередині поточного translation unit. У звичайній збірці це файл після препроцесингу, а не обов’язково один фізичний `.c` файл, бо `#include` вставляє текст у нього.[^iso-c-n1570]

Linkage і адреса – різні речі. У відповідному контексті вираз `handler` перетворюється на function pointer; його можна записати в callback-поле чи передати функції, оголошеній у цьому translation unit. Одержувачеві не потрібно знати ім’я `handler`, щоб викликати адресу. Прототип callback має бути сумісним за типом повернення та параметрами.[^iso-c-n1570]

Це корисно, коли реалізація драйвера має прихований handler, а публічний інтерфейс лише реєструє callback. Зовнішнє ім’я потрібне іншому translation unit лише тоді, коли той має звернутися до функції за її ім’ям через декларацію з external linkage.[^iso-c-n1570]

**Типова помилка:** вважати, що `static` означає «функцію неможливо передати». Воно забороняє зовнішнє зв’язування імені, а не передавання значення-вказівника.

Приклад:

```c
typedef void (*callback_fn)(int);
static void on_event(int code) { (void)code; }
static void register_callback(callback_fn fn) { fn(1); }
void register_local_handler(void) {
    register_callback(on_event); /* address is usable here */
}
```

Цей приклад коректний, якщо `register_callback` приймає сумісний тип callback. Одержувач може зберегти адресу для подальших викликів: обмеження internal linkage стосується видимості імені, а не можливості викликати функцію через збережений function pointer.[^iso-c-n1570]
