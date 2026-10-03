---
id: emb-fnptr-0039
title: "Чим pointer to member function у C++ відрізняється від звичайного function pointer?"
description: "Pointer to member function потребує object instance для виклику."
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
  - source_id: cpp-member-pointer
    title: "C++ working draft: Pointers to members and pointer-to-member operators"
    url: https://eel.is/c++draft/dcl.mptr
    accessed: 2026-10-04
    kind: spec
    version: "current working draft"
    applicability: "Визначає окремий тип pointer-to-member та синтаксис застосування до об’єкта; не визначає фізичне представлення на конкретній платформі."
---

## Short answer

**Pointer to member function потребує object instance для виклику.**

`void (Class::*pmf)()` має окремий тип від `void (*)()`: перший є pointer to member, а другий – pointer to function. Для виклику pointer to member застосовують до об’єкта через `.*` або `->*`, після чого викликають результат.[^cpp-member-pointer]

Для C callback із C++ class використовуй static member function wrapper і передавай `this` через context pointer; static member function може мати звичайний function pointer type.[^cpp-member-pointer]

## Detailed explanation

Pointer to member function позначає функцію-член певного класу, але сам по собі не містить об’єкт, для якого цю функцію треба виконати. Його тип записують із назвою класу, наприклад `void (Device::*pmf)()`. Це окремий тип, не сумісний зі звичайним `void (*)()` function pointer.[^cpp-member-pointer]

Щоб викликати функцію-член через такий покажчик, потрібні і покажчик, і відповідний об’єкт: `(device.*pmf)()` або `(device_ptr->*pmf)()`. Об’єкт надає конкретний стан екземпляра, а member pointer вказує, яку функцію цього класу викликати. Саме тому передавання одного `pmf` у C API, що приймає лише адресу вільної функції, не може передати потрібний екземпляр.[^cpp-member-pointer]

Це не твердження про фізичне представлення покажчика: стандарт не вимагає, щоб pointer to member function був просто машинною адресою чи мав той самий розмір, що й function pointer. Програма має покладатися на типову систему та оператори мови, а не на перетворення через cast.[^cpp-member-pointer]

**Типова помилка:** намагатися передати `&Device::on_event` у callback параметр типу `void (*)(void)`. Для C API зазвичай створюють static member wrapper із сумісною сигнатурою й передають `this` у `void *context`; wrapper відновлює тип об’єкта та викликає його метод. Об’єкт має залишатися живим до завершення всіх callback-викликів.[^cpp-member-pointer]

Приклад застосування покажчика-члена в C++:

```cpp
struct Device { void on_event() {} };
Device device;
void (Device::*pmf)() = &Device::on_event;
(device.*pmf)();
```

Тут `device` – конкретний екземпляр `Device`; без нього цей виклик не визначений синтаксисом pointer-to-member operator.[^cpp-member-pointer]

## Sources

<!-- generated from frontmatter -->
