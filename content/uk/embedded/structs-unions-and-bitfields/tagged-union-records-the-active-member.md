---
id: emb-structs-0018
title: "Чому `union` часто додають тегом-дискримінатором?"
description: "Бо сам union не пам’ятає, який member зараз активний або логічно валідний."
track: embedded
section: structs-unions-and-bitfields
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

**Бо сам union не пам’ятає, який member зараз активний або логічно валідний.**[^iso-c-n1570]

Типовий патерн: `enum kind` поруч із `union payload`. Без discriminator код може прочитати temperature payload як pressure payload або interpret pointer як integer. Це логічна помилка навіть там, де binary access формально можливий.

Правило: для variant data зберігай tag разом із union і перевіряй його перед читанням відповідного члена.[^iso-c-n1570]

## Detailed explanation

Tagged union – це `struct`, що зберігає тег-ознаку та `union` із кількома альтернативними полями. Сам `union` містить спільне сховище, але не має окремого поля, яке повідомляє програмі, який варіант логічно вибраний.[^iso-c-n1570]

Тег зазвичай оголошують як `enum`, а член union читають лише у гілці, що відповідає цьому тегу. Це підтримує інваріант: тег і payload змінюються разом. Якщо оновити payload, але залишити старий tag, код може інтерпретувати байти як інший тип і отримати хибні дані або некоректне представлення.[^iso-c-n1570]

**Приклад:**

```c
enum Kind { INTEGER, REAL };
struct Value {
    enum Kind kind;
    union { int i; float f; } payload;
};

if (value.kind == REAL) {
    use_float(value.payload.f);
}
```

Перевірка `kind` пов’язує вибір поля з тим, як його інтерпретують. На практиці корисно інкапсулювати створення та читання такого значення у функції, які встановлюють tag разом із payload. Це зменшує ризик змінити одне поле і забути відповідно змінити інше.[^iso-c-n1570]

Тег не перевіряє сам себе: він може бути пошкоджений у пам’яті або містити значення поза переліком після отримання некоректного пакета. На межі довіри перевіряйте допустимість tag і довжину вхідних даних до доступу до payload; не покладайтеся на tag як на доказ коректності зовнішнього вводу.[^iso-c-n1570]

**Типова помилка:** читати `payload.f` лише тому, що байти схожі на число з плаваючою комою. Спочатку перевірте tag, а під час додавання варіанта перегляньте всі місця, які розгалужуються за ним.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->
