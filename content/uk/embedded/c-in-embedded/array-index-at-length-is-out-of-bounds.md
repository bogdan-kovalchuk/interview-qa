---
id: emb-cppfound-0030
title: "Trap: що не так?"
track: embedded
section: c-in-embedded
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
int arr[5];
arr[5] = 0;
```

## Short answer

<span class="warn">Out-of-bounds write -> undefined behavior.</span> Валідні індекси: `0..4`, а `arr[5]` – за межами масиву.

У пам'яті `arr[5]` знаходиться одразу за масивом: це може бути інша локальна змінна, адреса повернення, saved LR, тож наслідки – тихе пошкодження даних або crash при поверненні з функції (зіпсована адреса повернення).

Захист: `-fsanitize=address`, явні перевірки індексів, `static_assert(i < ARRAY_SIZE)`.[^embeddedinterviewlab]

## Detailed explanation

TODO
