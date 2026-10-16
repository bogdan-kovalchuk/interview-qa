---
id: emb-raii-0003
title: "Як виглядає RAII lock guard для RTOS-мьютекса?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cmsis-rtos2-mutex
    title: "CMSIS-RTOS2: Mutex Management"
    url: https://arm-software.github.io/CMSIS_6/latest/RTOS2/group__CMSIS__RTOS__MutexMgmt.html
  - source_id: cpp-draft-stmt-dcl
    title: "C++ working draft: Declaration statement ([stmt.dcl])"
    url: https://eel.is/c++draft/stmt.dcl
  - source_id: cpp-draft-basic-stc-auto
    title: "C++ working draft: Automatic storage duration ([basic.stc.auto])"
    url: https://eel.is/c++draft/basic.stc.auto
  - source_id: cpp-draft-except-ctor
    title: "C++ working draft: Stack unwinding ([except.ctor])"
    url: https://eel.is/c++draft/except.ctor
  - source_id: cppcg-r1-raii
    title: "C++ Core Guidelines: R.1 – Manage resources automatically using resource handles and RAII"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r1-manage-resources-automatically-using-resource-handles-and-raii-resource-acquisition-is-initialization
  - source_id: cppcg-cp20
    title: "C++ Core Guidelines: CP.20 – Use RAII, never plain lock()/unlock()"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#cp20-use-raii-never-plain-lockunlock
  - source_id: cppcg-cp44
    title: "C++ Core Guidelines: CP.44 – Remember to name your lock_guards and unique_locks"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#cp44-remember-to-name-your-lock_guards-and-unique_locks
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
