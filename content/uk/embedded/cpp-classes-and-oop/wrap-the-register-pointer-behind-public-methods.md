---
id: emb-cppoop-0004
title: "Як інкапсулювати GPIO-регістр у клас?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-class-access
    title: "C++ working draft: Member access control, general ([class.access.general])"
    url: https://eel.is/c++draft/class.access.general
  - source_id: cpp-draft-class-mfct
    title: "C++ working draft: Member functions ([class.mfct])"
    url: https://eel.is/c++draft/class.mfct
  - source_id: cpp-draft-dcl-inline
    title: "C++ working draft: The inline specifier ([dcl.inline])"
    url: https://eel.is/c++draft/dcl.inline
  - source_id: gcc-optimize-options
    title: "GCC 16.1.0: Options That Control Optimization"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Optimize-Options.html
  - source_id: cpp-draft-dcl-type-cv
    title: "C++ working draft: The cv-qualifiers ([dcl.type.cv])"
    url: https://eel.is/c++draft/dcl.type.cv
  - source_id: cpp-draft-expr-assign
    title: "C++ working draft: Assignment and compound assignment operators ([expr.assign])"
    url: https://eel.is/c++draft/expr.assign
---

## Question code

```cpp
class Gpio {
  volatile uint32_t *const odr_;
  const uint8_t pin_;
public:
  Gpio(volatile uint32_t *odr, uint8_t pin) : odr_{odr}, pin_{pin} {}
  void set() const { *odr_ |= (UINT32_C(1) << pin_); }
  void clear() const { *odr_ &= ~(UINT32_C(1) << pin_); }
};
```

## Short answer

**Приватний вказівник на GPIO (general-purpose input/output) register + публічні методи доступу.** `private`-члени може назвати лише код самого класу (та його friends), тож сирий read-modify-write ззовні через клас не виконається.[^cpp-draft-class-access] Малі методи, визначені в тілі класу, неявно `inline`, і GCC на `-O2` зазвичай підставляє їх у місце виклику, але стандарт цього не вимагає.[^cpp-draft-class-mfct][^gcc-optimize-options] Правило: клас-обгортка дає інкапсуляцію й типобезпеку, а оверхед у release-збірці зазвичай мінімальний – перевіряй асемблер і пам’ятай, що `|=` не стає атомарним.

## Detailed explanation

Клас у питанні тримає адресу регістра (`volatile uint32_t *const odr_`) і номер піна (`pin_`) у `private`-секції. За стандартом такий член можна назвати лише в членах і friends класу,[^cpp-draft-class-access] тому код користувача не може випадково записати в регістр повністю або зіпсувати чужі біти: єдина дорога – `set()` і `clear()`, які самі виставляють і скидають один біт. Це інкапсуляція на рівні мови, а не апаратний захист: до того самого регістра можна дістатися іншим вказівником чи іншим об’єктом `Gpio` з такою самою адресою.

Кваліфікатор `volatile` на тому, на що вказує `odr_`, обов’язковий для регістра. Стандарт називає `volatile` підказкою не оптимізувати агресивно об’єкт, що може змінюватися незалежно від програми, а семантику доступу через volatile glvalue – implementation-defined.[^cpp-draft-dcl-type-cv] Без нього компілятор мав би право злити чи прибрати записи, які для периферії є обов’язковими.

Щодо «нульового оверхеду»: метод, визначений у класі, неявно `inline`,[^cpp-draft-class-mfct] але `inline` лише висловлює перевагу підстановки, а реалізація не зобов’язана її виконувати.[^cpp-draft-dcl-inline] GCC на `-O2` увімкнено `-finline-small-functions`, і така евристика охоплює навіть функції без `inline`, якщо тіло менше за код виклику,[^gcc-optimize-options] тож для `set()` підстановка дуже ймовірна. На `-O0` вона зазвичай відсутня. Крім того, `odr_` і `pin_` – звичайні поля об’єкта: якщо компілятор не бачить, чим їх ініціалізовано (об’єкт передають у функцію з іншого модуля чи тримають у пам’яті), він читатиме їх з об’єкта при кожному виклику, а сам об’єкт займає RAM. Тому остаточну відповідь дає disassembly, а не припущення.

Нарешті, `*odr_ |= mask` – це read-modify-write: за стандартом `E1 op= E2` еквівалентне `E1 = E1 op E2` з одноразовим обчисленням `E1`.[^cpp-draft-expr-assign] Клас ховає цей запис, але не робить його атомарним: якщо ISR змінить той самий регістр між читанням і записом, ця зміна загубиться. Захист від цього – критична секція або регістри, що пишуться без читання, якщо периферія їх надає (дивись datasheet).

**Типові помилки:**

- Вважати, що обгортка завжди компілюється в таку саму інструкцію, і не дивитися асемблер на `-O0` чи на цільовому компіляторі.
- Забути `volatile` у типі вказівника на регістр.
- Вважати `set()` атомарним щодо ISR або DMA, бо метод «один».
- Додати getter, що повертає сирий вказівник на регістр: інкапсуляція втрачається.
