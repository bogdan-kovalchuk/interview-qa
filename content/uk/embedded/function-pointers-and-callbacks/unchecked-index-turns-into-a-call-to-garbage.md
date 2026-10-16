---
id: emb-fnptr-0020
title: "Trap: що не так із dispatch table без перевірки індексу?"
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

## Question code

```c
typedef void (*handler_t)(void);
static handler_t table[4];

table[opcode]();
```

## Short answer

<span class="warn">Якщо `opcode >= 4`, індексація виходить за межі масиву, а поведінка програми стає undefined behavior; адреса виклику не обов’язково буде випадковою.</span>

На Cortex-M наслідком може бути HardFault, некоректний перехід або інша несправність, але стандарт C не гарантує конкретного результату.

Захист: спершу перевіряй індекс, а тоді – що вибраний handler не є null pointer; для технічного обґрунтування див. правила C про індексацію й виклик.[^iso-c-n1570]

## Detailed explanation

Виклик `table[opcode]()` спершу читає елемент масиву за індексом `opcode`, а потім викликає отриманий function pointer. Оскільки в оголошенні є рівно чотири елементи, допустимі індекси – від `0` до `3`; значення `opcode >= 4` не означає «виклик випадкової функції» як гарантований наслідок, а спричиняє undefined behavior через доступ поза межами масиву.[^iso-c-n1570]

Це важливо, бо перевірка лише того, що вказівник не дорівнює null, не виправляє попередній вихід за межі. Прочитане за невалідним індексом значення вже не є коректно вибраним елементом `table`, тож наступна умова також не робить операцію безпечною. Перевірка індексу має відбутися до будь-якого звернення до елемента; лише після неї можна перевірити handler і викликати його.[^iso-c-n1570]

На конкретному MCU помилка може проявитися як fault, перехід у хибний код або інше пошкодження стану. Це залежить від розміщення даних, ABI та реалізації, тому не можна обіцяти саме HardFault чи саме «випадкову адресу». Помилка часто відтворюється лише для певного opcode, а оптимізація змінює симптом; це не робить код коректним.[^iso-c-n1570]

Приклад перевірки:

```c
if (opcode < 4u && table[opcode] != NULL) {
    table[opcode]();
} else {
    handle_invalid_opcode();
}
```

**Типові помилки:**

- Спершу читати `table[opcode]`, а вже потім перевіряти індекс.
- Вважати, що не-null перевірка захищає від out-of-bounds access.
- Називати конкретний апаратний fault гарантованим наслідком undefined behavior.[^iso-c-n1570]
