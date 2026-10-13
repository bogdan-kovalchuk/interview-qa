---
id: emb-raii-0027
title: "Чому RAII-guard роблять `explicit` у конструкторі?"
description: "Щоб заборонити неявне перетворення з handle у guard."
track: embedded
section: raii-and-smart-pointers
level: junior
type: concept
tags: []
status: published
updated: 2026-10-13
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
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-13; це джерело не є доказом тверджень."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C++; freestanding і вендорські тулчейни можуть відрізнятися."
  - source_id: cpp-draft-class-conv-ctor
    title: "C++ working draft: [class.conv.ctor]"
    url: https://eel.is/c++draft/class.conv.ctor
    accessed: 2026-10-13
    kind: spec
    version: null
    applicability: "Точний пункт стандарту: explicit-конструктор використовується лише при direct-initialization або явному cast, а не для неявних перетворень. Не описує поведінку конкретних RTOS-handle."
  - source_id: cpp-core-guidelines-c46
    title: "C++ Core Guidelines, C.46: By default, declare single-argument constructors explicit"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c46-by-default-declare-single-argument-constructors-explicit
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Правило C.46 керівних принципів C++ Core Guidelines: за замовчуванням конструктори з одним аргументом роби explicit, щоб уникнути неочікуваних перетворень; у правилі є виняток для навмисного неявного перетворення. Не доводить поведінку RTOS."
---

## Short answer

**Щоб заборонити неявне перетворення з handle у guard.**

`explicit LockGuard(osMutexId_t)` не дає випадково створити тимчасовий guard через неявне перетворення, наприклад коли м’ютекс передають у функцію, що приймає guard за значенням; такий тимчасовий guard захопив би lock у місці виклику.[^cpp-draft-class-conv-ctor]

За замовчуванням конструктори з одним аргументом роби `explicit`; виняток – випадок, коли неявне перетворення є свідомою частиною типу.[^cpp-core-guidelines-c46]

## Detailed explanation

Конструктор із одним аргументом без `explicit` задає неявне перетворення з типу аргумента в тип класу. Стандарт C++ каже, що explicit-конструктор створює об’єкти лише там, де явно записано direct-initialization або cast, а не при неявних перетвореннях.[^cpp-draft-class-conv-ctor] Для RAII-guard це важливо: конструктор захоплює ресурс, тож тимчасовий guard, створений мимоволі, означає захоплення lock у місці, якого програміст не бачив.

Приклад показує обидві ситуації. Рядок `LockGuard g{m};` дійсний, бо це direct-initialization. Рядок `process(m);` із `explicit` не компілюється: параметр-значення типу `LockGuard` потребує неявного перетворення з `osMutexId_t`, а його немає. Без `explicit` той самий рядок компілюється і захоплює м’ютекс у місці виклику.

```cpp
// Illustrative: osMutexId_t stands in for an RTOS mutex handle.
using osMutexId_t = void*;
void osMutexAcquire(osMutexId_t m);
void osMutexRelease(osMutexId_t m);

class LockGuard {
public:
    explicit LockGuard(osMutexId_t m) : m_(m) { osMutexAcquire(m_); }
    ~LockGuard() { osMutexRelease(m_); }
    LockGuard(const LockGuard&) = delete;
    LockGuard& operator=(const LockGuard&) = delete;
private:
    osMutexId_t m_;
};

void process(LockGuard) {}

void run(osMutexId_t m) {
    LockGuard g{m};        // direct-initialization: allowed
    process(m);            // error: no implicit conversion from osMutexId_t
}
```

Правило C.46 робить explicit типовим вибором, щоб уникнути неочікуваних перетворень.[^cpp-core-guidelines-c46] Для guard це означає, що захоплення ресурсу з’являється лише як явний виклик типу, а не як побічний ефект передачі аргумента.

**Типові помилки:**

- Вважати, що `explicit` забороняє створювати об’єкт взагалі; `LockGuard g{m};` і `LockGuard g(m);` залишаються дійсними.
- Вважати, що `explicit` сам по собі забороняє копіювання; для цього потрібен `= delete`.
- Ставити `explicit` там, де неявне перетворення є змістом типу, наприклад у `Complex(double)` з того самого правила C.46.

## Sources

<!-- generated from frontmatter -->
