---
id: emb-raii-0016
title: "Що таке static RAII singleton і коли запускаються його ctor/dtor?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-stmt-dcl
    title: "C++ working draft: Declaration statement ([stmt.dcl])"
    url: https://eel.is/c++draft/stmt.dcl
  - source_id: cpp-draft-basic-start-term
    title: "C++ working draft: Termination ([basic.start.term])"
    url: https://eel.is/c++draft/basic.start.term
  - source_id: cpp-draft-support-start-term
    title: "C++ working draft: Start and termination ([support.start.term])"
    url: https://eel.is/c++draft/support.start.term
  - source_id: gcc-cxx-threadsafe-statics
    title: "GCC: C++ Dialect Options, -fno-threadsafe-statics"
    url: https://gcc.gnu.org/onlinedocs/gcc/C_002b_002b-Dialect-Options.html#index-fthreadsafe-statics
---

## Question code

```c
Driver& instance() {
  static Driver d; // ctor - при 1-му виклику
  return d;
}
```

## Short answer

**Function-local static: конструктор виконується один раз, при першому проходженні декларації; деструктор викликається при exit, зокрема при return з main.**[^cpp-draft-basic-start-term]

Об’єкт створюється при першому проходженні декларації, а не на старті програми, тож це lazy init, що обходить static initialization order fiasco між translation units.[^cpp-draft-stmt-dcl] Але GCC за замовчуванням додає код потокобезпечної ініціалізації; `-fno-threadsafe-statics` його прибирає, і тоді паралельний перший вхід не синхронізується кодом компілятора.[^gcc-cxx-threadsafe-statics]

Правило: Meyers' singleton – heap-free, але не завжди runtime-free; перевіряй generated code на своєму toolchain.

## Detailed explanation

Локальна `static`-змінна з динамічною ініціалізацією не створюється під час старту програми. Її конструктор виконується при першому проходженні керування через декларацію, і ініціалізація вважається завершеною після конструктора.[^cpp-draft-stmt-dcl] Якщо конструктор кинув виняток, ініціалізація не завершилася і буде повторена, коли керування знову дійде до декларації. Тому `instance()` у прикладі створює `Driver` один раз і повертає посилання на той самий об’єкт при кожному наступному виклику.

У багатопотоковому коді паралельний вхід у декларацію, поки триває ініціалізація, має чекати її завершення.[^cpp-draft-stmt-dcl] GCC реалізує це додатковим кодом потокобезпечної ініціалізації за C++ ABI, який за замовчуванням є в згенерованому коді. `-fno-threadsafe-statics` прибирає цей код і трохи зменшує розмір, але вимикати його варто лише там, де ініціалізація точно не може бути паралельною.[^gcc-cxx-threadsafe-statics] Перевірити, чи код є, можна в асемблері: шукай виклики `__cxa_guard_acquire` і `__cxa_atexit`.

Деструктор викликається як частина `std::exit`, а повернення з `main` викликає `std::exit`.[^cpp-draft-basic-start-term] У firmware, де `main` не повертається (типовий нескінченний цикл), деструктор function-local static не виконується взагалі. `std::abort` і `_Exit` завершують програму без деструкторів для об’єктів зі static storage duration.[^cpp-draft-support-start-term] Тож ресурс, який такий об’єкт тримає (периферія, mutex), треба звільнити явно, а не покладатися на dtor.

Ціна static-підходу: перший виклик оплачує конструктор і guard. Якщо функція вперше викликається з ISR, конструктор виконується всередині переривання, тому він має бути коротким і неблокуючим.

**Типові помилки:**

- Вважати, що конструктор виконується на старті програми: якщо функцію ніхто не викликав, об’єкта не існує.
- Очікувати, що деструктор спрацює при `abort()`, `_Exit()` або коли `main` не повертається.
- Вимикати `-fno-threadsafe-statics` у коді, де ініціалізація може виконуватися з кількох потоків.
- Вважати static-об’єкт безкоштовним: перевіряй асемблер на guard-виклики.
