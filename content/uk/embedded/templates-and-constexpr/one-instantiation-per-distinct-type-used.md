---
id: emb-tmplcx-0002
title: "Скільки інстанціацій template опиниться у бінарнику?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-temp-inst
    title: "C++ working draft: Implicit instantiation ([temp.inst])"
    url: https://eel.is/c++draft/temp.inst
---

## Short answer

**Одна інстанціація на кожен різний набір template-аргументів, який реально використано.**

Якщо викликати `max<int>(a, b)` і `max<float>(x, y)`, компілятор створює дві інстанціації функції; шаблон функції, якого ніхто не викликає, не інстанціюється.[^cpp-draft-temp-inst]

Це кількість згенерованих копій коду, а не гарантований розмір прошивки: оптимізатор може вбудувати виклики, тож результат варто перевіряти через `nm -C` або map file.

## Detailed explanation

Шаблон сам по собі не є кодом: компілятор створює інстанціацію лише тоді, коли програма її потребує. Шаблон функції інстанціюється, коли на нього посилаються в контексті, що вимагає наявності визначення, наприклад коли функцію викликають.[^cpp-draft-temp-inst] Для шаблону класу сам клас інстанціюється, коли його повний тип потрібний, а окремі члени – тільки тоді, коли до них звертаються.[^cpp-draft-temp-inst]

Ілюстративний приклад: для коду нижче `nm -C` на об’єктному файлі без оптимізації покаже символи `max_of<int>` і `max_of<float>`, а для `unused_fn` символа немає, бо її ніхто не викликає. З `-O2` у цьому прикладі символів `max_of` у файлі немає взагалі, бо виклики вбудовано.

```cpp
template <typename T>
T max_of(T a, T b) { return a < b ? b : a; }

template <typename T>
T unused_fn(T a) { return a; }

int f(int a, int b, float x, float y) {
  return max_of<int>(a, b) + static_cast<int>(max_of<float>(x, y));
}
```

Правило стосується кількості інстанціацій, а не розміру прошивки. Оптимізатор може вбудувати виклик у місці використання, тому оцінювати витрати за кількістю шаблонних аргументів не варто. Надійніше дивитися на результат збирання: `nm -C` показує символи в об’єктному файлі, а map file – що лишилося в бінарнику після лінкування.

**Типові помилки:**

- Вважати, що кожна інстанціація гарантовано дає окрему копію коду у Flash.
- Рахувати шаблон із заголовка витратою пам’яті, навіть коли його ніхто не викликає.
- Судити про розмір бінарника за кількістю шаблонів, а не за `nm` чи map file.
