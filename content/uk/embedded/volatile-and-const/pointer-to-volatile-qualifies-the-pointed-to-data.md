---
id: emb-volconst-0009
title: "Що означає декларація `volatile uint32_t *p`?"
track: embedded
section: volatile-and-const
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**`p` є вказівником на volatile `uint32_t`**.

Сам вказівник `p` можна змінювати: він може вказувати на іншу адресу. Але кожне `*p` повинно бути реальним volatile-доступом до об’єкта. Це нормальна форма для доступу до hardware register, якщо адреса може вибиратися runtime.

Правило читання: починай від імені `p`: `p` is pointer to volatile `uint32_t`.[^iso-c-n1570]

## Detailed explanation

У декларації `volatile uint32_t *p` оператор `*` належить до декларатора і показує, що `p` є вказівником; `volatile` кваліфікує тип об’єкта, на який він вказує. Отже, сам `p` можна перепризначити, але вираз `*p` має volatile-qualified type. Розташування кваліфікатора важливе, бо C застосовує кваліфіковані типи до lvalue-виразів, які позначають об’єкт.[^iso-c-n1570]

Для memory-mapped I/O такий тип дозволяє позначити дані за адресою як volatile. Кожне читання або запис через `*p` тоді має зберігати семантику volatile-доступу абстрактної машини. Водночас стандарт C визначає сам критерій доступу як implementation-defined, а hardware mapping встановлюють toolchain і платформа. Тому декларація не гарантує сама по собі ні конкретної інструкції CPU, ні правильності адреси периферії.[^iso-c-n1570]

**Приклад:**

```c
volatile uint32_t *p = (volatile uint32_t *)0x40020014u;
uint32_t value = *p; // volatile read of the pointed-to object
p = another_address; // the pointer itself can be reassigned
```

Перше присвоєння ініціалізує вказівник, а читання `*p` звертається до кваліфікованого об’єкта. Саме перепризначення `p` не є volatile-доступом до об’єкта за адресою. Якщо потрібні обидві властивості – volatile-вказівник і volatile-дані – декларація має бути `volatile uint32_t * volatile p`.[^iso-c-n1570]

Не плутайте цю форму з `uint32_t * volatile p`: там кваліфіковане значення самого pointer variable, тоді як тип даних за адресою лишається звичайним. Для hardware register саме кваліфікація pointed-to data зазвичай є потрібною. Розмір і атомарність доступу залишаються питанням конкретної платформи, їх слід перевірити окремо.[^iso-c-n1570]
