---
id: emb-cppoop-0007
title: "Що таке RAII у контексті конструкторів/деструкторів?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-class-dtor
    title: "C++ working draft: Destructors ([class.dtor])"
    url: https://eel.is/c++draft/class.dtor
  - source_id: cpp-draft-except-ctor
    title: "C++ working draft: Stack unwinding ([except.ctor])"
    url: https://eel.is/c++draft/except.ctor
  - source_id: cpp-draft-support-start-term
    title: "C++ working draft: Start and termination ([support.start.term])"
    url: https://eel.is/c++draft/support.start.term
  - source_id: cppcg-r1-raii
    title: "C++ Core Guidelines: R.1 – Manage resources automatically using resource handles and RAII"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r1-manage-resources-automatically-using-resource-handles-and-raii-resource-acquisition-is-initialization
  - source_id: cppcg-c21-special-members
    title: "C++ Core Guidelines: C.21 – If you define or =delete any copy, move, or destructor function, define or =delete them all"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c21-if-you-define-or-delete-any-copy-move-or-destructor-function-define-or-delete-them-all
---

## Short answer

**RAII (Resource Acquisition Is Initialization): конструктор захоплює/налаштовує ресурс, деструктор автоматично звільняє його, коли об’єкт знищується, – для локального об’єкта при виході з блоку.**[^cpp-draft-class-dtor][^cppcg-r1-raii] Наприклад: ctor вмикає clock і конфігурує периферію, dtor вимикає clock або звільняє DMA (direct memory access) канал. Компілятор сам викликає dtor на кожному шляху виходу з блоку, зокрема й при винятку, тож забути деініціалізацію важче.[^cpp-draft-except-ctor] Але `abort()` деструкторів не виконує, а для static-об’єктів вони спрацьовують лише при нормальному завершенні програми.[^cpp-draft-support-start-term]

## Detailed explanation

Ресурси з парними операціями (`fopen`/`fclose`, `lock`/`unlock`, ввімкнути clock/вимкнути clock) легко залишити «відкритими» на одному з шляхів виходу. Core Guidelines радять обгортати такий ресурс в об’єкт: захоплювати в конструкторі, звільняти в деструкторі, бо мова гарантує цю симетрію.[^cppcg-r1-raii] Приклади там – файли, mutex, пам’ять; те саме працює для периферії, але це застосування ідеї, а не окреме правило.

Механізм простий. Для об’єкта з automatic storage duration деструктор викликається, коли блок, у якому його створено, завершується.[^cpp-draft-class-dtor] Це стосується будь-якого шляху виходу: `return` посередині функції, кінець блоку чи виняток. При винятку automatic-об’єкти, що вже сконструйовані, знищуються у зворотному порядку їх створення.[^cpp-draft-except-ctor] Якщо ж виняток вилетів із самого конструктора, деструктори викликаються для вже ініціалізованих підоб’єктів, а не для об’єкта, що не завершив ініціалізацію.[^cpp-draft-except-ctor] Тому конструктор, який захоплює кілька ресурсів, має тримати кожен у власному RAII-члені.

Ілюстративний приклад (імена регістрів умовні):

```cpp
class ClockGate {
  volatile uint32_t *const en_reg_;
  const uint32_t mask_;
public:
  ClockGate(volatile uint32_t *en, uint32_t mask) : en_reg_{en}, mask_{mask} {
    *en_reg_ |= mask_;               // захопили: увімкнули clock
  }
  ~ClockGate() { *en_reg_ &= ~mask_; }  // звільнили: вимкнули clock
  ClockGate(const ClockGate &) = delete;
  ClockGate &operator=(const ClockGate &) = delete;
};

bool read_adc(uint16_t &out) {
  ClockGate adc_clk{&RCC_ENR, ADC_EN};
  if (!calibrate()) return false;    // dtor вимкне clock і тут
  out = convert();
  return true;                       // і тут
}
```

Копіювання тут заборонено навмисно: копія виконала б звільнення вдруге, а Core Guidelines наголошують, що оголошений деструктор потребує свідомого рішення про копіювання й переміщення.[^cppcg-c21-special-members]

Межі підходу в firmware. Деструктор не виконується, якщо програма завершується через `abort()`; `exit()` не знищує automatic-об’єкти.[^cpp-draft-support-start-term] Глобальні об’єкти зі static storage duration знищуються лише при завершенні програми,[^cpp-draft-class-dtor] а головний цикл firmware зазвичай не завершується. Тому RAII найкорисніший для локальних об’єктів із чітким scope: критична секція, тимчасове ввімкнення clock, захоплений канал DMA. А сам по собі він не забезпечує вимкнення периферії при вимкненні живлення чи reset.

**Типові помилки:**

- Очікувати, що деструктор глобального RAII-об’єкта спрацює в firmware з нескінченним циклом `main`.
- Не забороняти копіювання handle: два об’єкти звільнять той самий ресурс.
- Захоплювати кілька ресурсів у тілі конструктора без RAII-членів: якщо конструктор кине виняток, деструктор цього об’єкта не виконається, і попередні ресурси лишаться захопленими.
- Вважати, що RAII захищає від `abort()`, reset чи апаратного збою.
