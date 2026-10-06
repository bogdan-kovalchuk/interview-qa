---
id: emb-raii-0003
title: "Як виглядає RAII lock guard для RTOS-мьютекса?"
description: "Ctor захоплює мьютекс, dtor звільняє його при виході зі scope."
track: embedded
section: raii-and-smart-pointers
level: junior
type: mechanism
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
    applicability: "Описує mutex API CMSIS-RTOS2: osMutexAcquire і osMutexRelease (блокування потоку до отримання mutex, коди повернення, зокрема osErrorResource при release без acquire чи не власником; недоступні з ISR), атрибут osMutexRecursive. Конкретна RTOS-реалізація поза специфікацією може поводитися інакше."
  - source_id: cpp-draft-stmt-dcl
    title: "C++ working draft: Declaration statement ([stmt.dcl])"
    url: https://eel.is/c++draft/stmt.dcl
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Пункт 2: при кожній передачі керування в межах функції (зокрема при поверненні з неї) automatic-змінні блоку, активні в точці відправлення й неактивні в точці призначення, знищуються у зворотному порядку конструювання. Не охоплює завершення програми через exit чи abort і не описує винятки."
  - source_id: cpp-draft-basic-stc-auto
    title: "C++ working draft: Automatic storage duration ([basic.stc.auto])"
    url: https://eel.is/c++draft/basic.stc.auto
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Пункт 2: automatic-змінну з ініціалізацією чи деструктором із побічними ефектами не можна знищити раніше кінця блоку чи прибрати як оптимізацію, навіть якщо вона виглядає невикористаною (окрім copy/move elision). Не стосується змінних із тривіальним деструктором."
  - source_id: cpp-draft-except-ctor
    title: "C++ working draft: Stack unwinding ([except.ctor])"
    url: https://eel.is/c++draft/except.ctor
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Описує знищення automatic-об’єктів у зворотному порядку при винятку та те, що при винятку з конструктора деструктори викликаються для вже ініціалізованих підоб’єктів; не діє, якщо винятки вимкнено компілятором."
  - source_id: cppcg-r1-raii
    title: "C++ Core Guidelines: R.1 – Manage resources automatically using resource handles and RAII"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r1-manage-resources-automatically-using-resource-handles-and-raii-resource-acquisition-is-initialization
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Настанова: обгортати ресурс із парними acquire/release в об’єкт, що захоплює в конструкторі й звільняє в деструкторі; приклади – файли, mutex, пам’ять, не апаратна периферія."
  - source_id: cppcg-cp20
    title: "C++ Core Guidelines: CP.20 – Use RAII, never plain lock()/unlock()"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#cp20-use-raii-never-plain-lockunlock
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Настанова CP.20: брати й віддавати lock через RAII-об’єкт, а не прямими lock()/unlock(), бо хтось забуде unlock, додасть return чи кине exception. Приклад – std::mutex, а не RTOS API."
  - source_id: cppcg-cp44
    title: "C++ Core Guidelines: CP.44 – Remember to name your lock_guards and unique_locks"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#cp44-remember-to-name-your-lock_guards-and-unique_locks
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Настанова CP.44: безіменний локальний об’єкт – це temporary, що одразу виходить зі scope, тож lock не утримується до кінця критичної секції. Приклади – std::lock_guard і std::unique_lock, а не RTOS guard."
---

## Question code

```cpp
class LockGuard {
  osMutexId_t m_;
public:
  explicit LockGuard(osMutexId_t m) : m_(m) {
    osMutexAcquire(m_, osWaitForever);
  }
  ~LockGuard() { osMutexRelease(m_); }
};
```

## Short answer

**Ctor захоплює mutex, dtor звільняє його при виході зі scope.**

RTOS означає real-time operating system. Кожен вихід із блоку (кінець, early `return`, `break`) викликає деструктор, а отже `osMutexRelease`,[^cpp-draft-stmt-dcl] тож на error-шляхах не лишається забутого unlock;[^cppcg-cp20] з увімкненими exceptions те саме відбувається при unwinding до handler.[^cpp-draft-except-ctor] Guard придатний лише для thread context, а статус `osMutexAcquire` треба перевіряти.[^cmsis-rtos2-mutex]

Правило: кожна пара acquire/release у C API (application programming interface) – кандидат на lock guard.[^cppcg-r1-raii]

## Detailed explanation

Конструктор `LockGuard` викликає `osMutexAcquire(m_, osWaitForever)`: потік переходить у стан BLOCKED, доки mutex не стане доступним, і повертається вже як власник.[^cmsis-rtos2-mutex] Деструктор викликає `osMutexRelease`, після чого потоки, що чекали, стають READY. Локальний об’єкт `LockGuard lock(bus);` тому задає критичну секцію: вона триває від рядка з оголошенням до закриваючої дужки блоку, і цю межу видно в самому коді.

Перевага над ручними `acquire`/`release` – у кількості виходів. Кожен новий `return`, `break` чи (з exceptions) `throw` у ручній схемі – ще один шанс забути unlock, тоді як деструктор виконується на всіх шляхах, якими керування залишає блок.[^cpp-draft-stmt-dcl] Core Guidelines описують саме цей сценарій: рано чи пізно хтось забуде unlock, додасть `return` чи кине exception.[^cppcg-cp20] Компілятор не може вилучити змінну-guard як «невикористану», бо деструктор має побічні ефекти.[^cpp-draft-basic-stc-auto]

Код із питання – мінімальна ілюстрація, і в реальному драйвері до нього є зауваження. По-перше, статус `osMutexAcquire` ігнорується, а він може бути не `osOK`: наприклад, `osErrorParameter` для невалідного mutex, `osErrorISR` при виклику з переривання або `osErrorTimeout`, якщо замість `osWaitForever` задано скінченний timeout. Guard, що mutex не отримав, усе одно викличе `osMutexRelease`; для валідного mutex, який цей потік не взяв, це `osErrorResource`, а код помилки в деструкторі ніхто не перевіряє.[^cmsis-rtos2-mutex] По-друге, за замовчуванням mutex не рекурсивний: потік не може взяти його повторно, тож другий guard на тому самому mutex в тому самому потоці з `osWaitForever` заблокує потік на самому собі, якщо mutex не створено з `osMutexRecursive`.[^cmsis-rtos2-mutex] По-третє, цей guard копійований (див. qid:emb-raii-0004). Варіант, що це враховує (ілюстративний):

```cpp
class LockGuard {
    osMutexId_t m_;
    bool owns_;
public:
    explicit LockGuard(osMutexId_t m)
        : m_(m), owns_(osMutexAcquire(m, osWaitForever) == osOK) {}
    ~LockGuard() { if (owns_) osMutexRelease(m_); }
    LockGuard(const LockGuard&) = delete;
    LockGuard& operator=(const LockGuard&) = delete;
    bool owns() const { return owns_; }
};

int read_sensor(osMutexId_t bus, int* out) {
    LockGuard lock(bus);
    if (!lock.owns()) return -1;
    if (!sensor_start()) return -2;   // lock is released here
    if (!sensor_read(out)) return -3; // and here
    return 0;                         // and here
}
```

**Типові помилки:**

- Безіменний temporary: `LockGuard{bus};` знищується в кінці виразу, тож mutex звільняється одразу, а не в кінці блоку. Core Guidelines наводять таку саму пастку для `lock_guard`.[^cppcg-cp44]
- Ігнорувати статус `osMutexAcquire`: guard, який не отримав mutex, усе одно викличе `osMutexRelease`.
- Використовувати guard в ISR: mutex API CMSIS-RTOS2 звідти недоступний.[^cmsis-rtos2-mutex]
- Тримати guard довше, ніж потрібно (довгі операції чи затримки під lock): усі інші потоки, що чекають на mutex, стоять увесь цей час.

## Sources

<!-- generated from frontmatter -->
