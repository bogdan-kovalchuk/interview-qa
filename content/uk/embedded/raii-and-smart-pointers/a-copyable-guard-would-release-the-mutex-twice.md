---
id: emb-raii-0004
title: "Trap: чому lock guard має забороняти копіювання (`= delete`)?"
description: "Копія guard-а дала б двох власників одного mutex і два `osMutexRelease`: перший деструктор знімає lock, поки інша копія ще вважає його своїм."
track: embedded
section: raii-and-smart-pointers
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-06
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
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-06; це джерело не є доказом тверджень."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C++; freestanding і вендорські тулчейни можуть відрізнятися."
  - source_id: cmsis-rtos2-mutex
    title: "CMSIS-RTOS2: Mutex Management"
    url: https://arm-software.github.io/CMSIS_6/latest/RTOS2/group__CMSIS__RTOS__MutexMgmt.html
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Описує mutex API CMSIS-RTOS2: osMutexRelease повертає osErrorResource, якщо mutex не було взято або потік не власник; рекурсивний mutex (osMutexRecursive) потрібно звільнити стільки разів, скільки його взято. Конкретна RTOS-реалізація поза специфікацією може поводитися інакше."
  - source_id: cpp-draft-class-copy-ctor
    title: "C++ working draft: Copy/move constructors ([class.copy.ctor])"
    url: https://eel.is/c++draft/class.copy.ctor
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що без user-declared copy constructor він неявно оголошується (для класу з user-declared деструктором це deprecated), що неявний move constructor оголошується лише коли, серед інших умов, немає user-declared copy constructor і деструктора, і що неявно визначений move constructor виконує memberwise move. Не стосується оптимізацій."
  - source_id: cpp-draft-class-copy-assign
    title: "C++ working draft: Copy/move assignment operator ([class.copy.assign])"
    url: https://eel.is/c++draft/class.copy.assign
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Пункт 2: якщо в класі немає user-declared copy assignment operator, він неявно оголошується; тому видалення самого лише copy constructor присвоєння не забороняє. Деталі deprecated для цього оператора не розглядаються."
  - source_id: cpp-draft-dcl-fct-def-delete
    title: "C++ working draft: Deleted definitions ([dcl.fct.def.delete])"
    url: https://eel.is/c++draft/dcl.fct.def.delete
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Пункт 2: конструкція, що позначає видалену функцію (виклик, вказівник на неї), ill-formed; приклад 3 показує move-only клас із видаленими copy constructor і copy assignment та defaulted move-операціями. Про поведінку RTOS нічого не каже."
---

## Question code

```c
LockGuard(const LockGuard&) = delete;
LockGuard& operator=(const LockGuard&) = delete;
```

## Short answer

<span class="warn">Копія guard-а дала б двох власників одного mutex і два виклики `osMutexRelease`.</span>

Перший деструктор знімає lock, поки код у scope іншої копії ще вважає, що mutex утримується; другий виклик у CMSIS-RTOS2 повертає `osErrorResource`, якщо mutex не було взято або потік не власник.[^cmsis-rtos2-mutex] Компілятор усе одно згенерує copy constructor для класу з user-declared деструктором (це deprecated),[^cpp-draft-class-copy-ctor] тож заборонити копіювання треба явно.

Захист: клас-обгортка ресурсу має бути non-copyable (`= delete` на copy) або move-only.[^cpp-draft-dcl-fct-def-delete]

## Detailed explanation

Guard із питання qid:emb-raii-0003 оголошує деструктор, але не copy constructor і не copy assignment. Компілятор у такому разі неявно оголошує їх сам: copy constructor – хоча для класу з user-declared деструктором це deprecated,[^cpp-draft-class-copy-ctor] copy assignment – так само, якщо немає власного.[^cpp-draft-class-copy-assign] Обидві виконують memberwise-копію, тож `LockGuard b = a;` чи передавання guard-а за значенням компілюється мовчки й дає два об’єкти з однаковим `m_`. Кожен із них у деструкторі викличе `osMutexRelease(m_)`.

Ось як це ламає критичну секцію (ілюстративний код):

```cpp
void log_state(LockGuard g);   // takes the guard by value

void work(osMutexId_t m) {
    LockGuard lock(m);
    log_state(lock);       // copy: its destructor calls osMutexRelease
    touch_shared_data();   // mutex is already free, but `lock` is still in scope
}                          // second osMutexRelease
```

Деструктор копії-параметра відпрацьовує вже при завершенні виклику `log_state`, тож `touch_shared_data()` виконується без захисту й може гонитися з іншим потоком. Останній `osMutexRelease` наприкінці `work` для звичайного mutex повертає `osErrorResource`: mutex не взято, або, якщо його вже встиг узяти інший потік, цей потік не власник.[^cmsis-rtos2-mutex] Цей код помилки в деструкторі ніхто не бачить. Якщо mutex рекурсивний, надлишковий release не повертає помилку, а зменшує лічильник блокувань, тож може зняти lock зовнішнього guard-а, який цей потік узяв раніше.[^cmsis-rtos2-mutex]

Видалена функція перетворює цей run-time баг на помилку компіляції: будь-яка конструкція, що звертається до видаленої функції (у тому числі неявний виклик copy constructor), ill-formed.[^cpp-draft-dcl-fct-def-delete] Move-операції окремо видаляти не потрібно: user-declared copy constructor, навіть видалений, означає, що неявний move constructor не оголошується, і спроба «перемістити» guard вибере видалений copy constructor.[^cpp-draft-class-copy-ctor] Якщо власність треба передавати (повертати guard із функції, зберігати в контейнері), клас роблять move-only (qid:emb-raii-0009): move constructor пишуть явно й обнуляють джерело, наприклад `o.owns_ = false`.

**Типові помилки:**

- Видалити лише copy constructor і забути copy assignment: присвоєння лишається неявно згенерованим, і `a = b` знову дає двох власників.[^cpp-draft-class-copy-assign]
- Зробити guard move-only через `= default` на move constructor: він виконує memberwise move,[^cpp-draft-class-copy-ctor] а для вказівника чи `bool` це просто копіювання значення, тож джерело лишається власником і release знову виконується двічі.
- Не помітити, що guard передано у функцію за значенням: це теж копія.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
