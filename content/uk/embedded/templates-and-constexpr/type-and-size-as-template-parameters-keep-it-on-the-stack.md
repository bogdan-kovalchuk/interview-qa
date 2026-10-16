---
id: emb-tmplcx-0003
title: "Як виглядає class template для буфера фіксованого розміру?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-temp-arg-nontype
    title: "C++ working draft: Constant template arguments ([temp.arg.nontype])"
    url: https://eel.is/c++draft/temp.arg.nontype
  - source_id: cpp-draft-basic-stc-auto
    title: "C++ working draft: [basic.stc.auto]"
    url: https://eel.is/c++draft/basic.stc.auto
  - source_id: cpp-draft-basic-stc-static
    title: "C++ working draft: Static storage duration ([basic.stc.static])"
    url: https://eel.is/c++draft/basic.stc.static
---

## Question code

```cpp
template<typename T, size_t N>
class CircularBuffer {
  T buf_[N];
  size_t head_ = 0, tail_ = 0;
};
CircularBuffer<uint8_t, 64> uart_rx;
```

## Short answer

**Тип і розмір – template-параметри, тому масив `buf_[N]` є частиною самого об’єкта, без `new` і `malloc`.**

Значення `N` має бути константою часу компіляції.[^cpp-draft-temp-arg-nontype] Де живе сам об’єкт, визначає місце оголошення: локальний об’єкт має automatic storage,[^cpp-draft-basic-stc-auto] а `uart_rx` на рівні простору імен – static storage.[^cpp-draft-basic-stc-static]

## Detailed explanation

Шаблон `CircularBuffer<T, N>` сам нічого не виділяє. Для `CircularBuffer<uint8_t, 64> uart_rx;` масив `buf_` є частиною самого об’єкта, а два індекси `head_` і `tail_` додають ще два `size_t`. На x86-64 з GCC 13 розмір такого об’єкта дорівнює 80 байтам: 64 байти буфера і 16 байтів індексів. У цьому коді немає жодного виклику `new` чи `malloc`.

Шаблон визначає розмір, а не місце в пам’яті. Локальна змінна у функції має automatic storage duration і зазвичай лежить на стеку, поки не вийде з блоку.[^cpp-draft-basic-stc-auto] `uart_rx` оголошено на рівні простору імен, тому вона має static storage duration і живе весь час роботи програми.[^cpp-draft-basic-stc-static] Отже великий глобальний `CircularBuffer` не займає стек, а як локальний об’єкт в ISR чи у функції з малим стеком може його переповнити.

Значення `N` має бути константним виразом: `CircularBuffer<uint8_t, 64>` правильний, а розмір, прочитаний з конфігурації під час роботи, компілятор відхилить.[^cpp-draft-temp-arg-nontype] Для змінного розміру потрібен інший дизайн, наприклад фіксований максимум із лічильником фактичного розміру або динамічний буфер.

**Типові помилки:**

- Вважати, що сам шаблон визначає місце об’єкта: глобальний `CircularBuffer` не лежить на стеку.
- Оголошувати великий буфер локально в ISR чи у функції з малим стеком.
- Очікувати змінного розміру в runtime: `N` має бути константою часу компіляції.
