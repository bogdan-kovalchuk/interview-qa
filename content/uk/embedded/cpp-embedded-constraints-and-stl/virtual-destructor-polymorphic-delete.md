---
id: emb-cppemb-0001
title: "Для чого потрібен virtual destructor у C++ і коли це актуально для embedded C++?"
track: embedded
section: cpp-embedded-constraints-and-stl
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
---

## Short answer

Virtual destructor потрібен, якщо об’єкт видаляють через pointer/reference на base class: тоді викликається destructor derived class. Без нього `delete basePtr` для polymorphic object має undefined behavior. В embedded C++ це актуально для driver interfaces, HAL abstractions або state machines, але dynamic allocation часто замінюють static lifetime чи placement new.[^dou-embedded-interview]

## Detailed explanation

### Вимога стандарту C++ та undefined behavior

Згідно зі стандартом C++ ([expr.delete]), якщо об’єкт поліморфного класу знищується за допомогою виразу `delete ptr`, де статичний тип вказівника `ptr` є базовим класом (`Base*`), а динамічний тип – похідним (`Derived*`), деструктор базового класу зобов’язаний бути віртуальним (`virtual`). Якщо деструктор базового класу невіртуальний, така операція спричиняє невизначену поведінку (`undefined behavior`) [^iso-cpp-n4861].

На практиці відсутність `virtual` веде до двох серйозних проблем:
1. **Пропуск деструктора нащадка**: компілятор генерує прямий статичний виклик `Base::~Base()`, оминаючи `Derived::~Derived()`. Якщо похідний клас керував апаратними ресурсами (завершення транзакцій DMA, звільнення буферів, опускання ліній chip select, вимикання тактування периферії або семафори RTOS), деструктор нащадка не виконається, спричиняючи витік ресурсів або некоректний стан периферії.
2. **Некоректне звільнення пам’яті**: у разі множинного чи віртуального успадкування адреса об’єкта `Derived` може не збігатися з адресою підоб’єкта `Base` (зсув `this pointer adjustment`). Оператор `operator delete(void*, std::size_t)` отримає зміщений вказівник або некоректний розмір об’єкта, що призводить до пошкодження купи (`heap corruption`).

### Робота на рівні vtable та накладні витрати на мікроконтролерах

Додавання хоча б однієї віртуальної функції (включно з віртуальним деструктором) змінює внутрішнє представлення класу:
- **Збільшення розміру об’єкта**: компілятор додає до структури приховане поле `vptr` (вказівник на таблицю віртуальних методів `vtable`). На 32-розрядних ядрах (наприклад, ARM Cortex-M0/M3/M4/M7) це збільшує розмір кожного екземпляра класу на 4 байти (або на 8 байтів на 64-бітних архітектурах на кшталт AArch64), що може додатково збільшити структуру через правила вирівнювання (`padding`).
- **Пам’ять Flash/ROM для vtable**: у таблицю методів додаються слоти (в ABI Itanium C++ генеруються два варіанти деструктора: повний `complete object destructor` та `deleting destructor`).
- **Накладні витрати на виклик**: замість прямої інструкції переходу `BL` компілятор генерує непрямий перехід (на ARM це `LDR` з таблиці та `BLX rX`), що унеможливлює вбудовування коду (`inlining`) і скидає конвеєр процесора.

### Специфіка використання в embedded C++

У вбудованих системах динамічне виділення пам’яті (`heap`, `malloc`, `new`) здебільшого заборонене або суворо обмежене стандартами безпеки (MISRA C++, AUTOSAR, DO-178C) через недетермінованість часу виконання та ризик фрагментації RAM. Більшість драйверів, черг та об’єктів периферії створюються статично (`static lifetime`) або через `placement new` у фіксованих буферах пулу пам’яті.

Якщо об’єкт живе протягом усього часу роботи прошивки або ніколи не видаляється через вказівник на базовий тип `delete base_ptr`, потреба у віртуальному деструкторі відпадає.

### Патерни проєктування та альтернативи

У коді вбудованих систем доцільно дотримуватися правила Core Guidelines C.35: деструктор базового класу повинен бути або відкритим і віртуальним (`public virtual`), або захищеним і невіртуальним (`protected non-virtual`):

```cpp
// Варіант 1: Захищений невіртуальний деструктор (нульові накладні витрати)
class IDriver {
public:
    virtual void init() = 0;
    virtual void transmit(const uint8_t* data, size_t len) = 0;
protected:
    ~IDriver() = default; // Забороняє delete driver_ptr ззовні
};

// Варіант 2: Статичний поліморфізм через CRTP (без vtable та vptr)
template <typename Derived>
class HardwareTimer {
public:
    void start() { static_cast<Derived*>(this)->start_impl(); }
    void stop()  { static_cast<Derived*>(this)->stop_impl(); }
};
```

Використання `protected ~IDriver() = default;` на етапі компіляції запобігає спробі викликати `delete` через базовий вказівник (заощаджуючи Flash-пам’ять на генерацію deleting destructor). Якщо ж повністю усунути динамічний поліморфізм через CRTP, клас взагалі не містить `vptr`, що заощаджує 4 байти оперативної пам’яті на кожен екземпляр та виключає накладні витрати на виклики через `vtable`. Концепції C++20 та CRTP забезпечують повний інлайнінг викликів (`zero-cost abstraction`).
