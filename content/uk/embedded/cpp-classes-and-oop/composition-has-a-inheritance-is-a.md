---
id: emb-cppoop-0023
title: "Композиція vs успадкування: у чому різниця?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-intro-object
    title: "C++ working draft: [intro.object] Object model"
    url: https://eel.is/c++draft/intro.object
  - source_id: cppcg-c120
    title: "C++ Core Guidelines: C.120 – Use class hierarchies to represent concepts with inherent hierarchical structure (only)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c120-use-class-hierarchies-to-represent-concepts-with-inherent-hierarchical-structure-only
  - source_id: cppcg-c121
    title: "C++ Core Guidelines: C.121 – If a base class is used as an interface, make it a pure abstract class"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c121-if-a-base-class-is-used-as-an-interface-make-it-a-pure-abstract-class
  - source_id: cppcg-c122
    title: "C++ Core Guidelines: C.122 – Use abstract classes as interfaces when complete separation of interface and implementation is needed"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c122-use-abstract-classes-as-interfaces-when-complete-separation-of-interface-and-implementation-is-needed
  - source_id: cppcg-c129
    title: "C++ Core Guidelines: C.129 – When designing a class hierarchy, distinguish between implementation inheritance and interface inheritance"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c129-when-designing-a-class-hierarchy-distinguish-between-implementation-inheritance-and-interface-inheritance
---

## Short answer

**Композиція («has-a»)**: клас містить компоненти як члени-об’єкти й делегує їм роботу, користуючись лише їхнім публічним інтерфейсом. **Успадкування («is-a»)**: похідний клас є різновидом бази, а ідея в базі має точно відповідати всім похідним типам; це тісне зчеплення.[^cppcg-c120] Якщо досить data member, успадкування не використовують. Правило: успадкування – для стабільного інтерфейсу (база без даних), усе інше – композиція.[^cppcg-c121]

## Detailed explanation

Композиція й успадкування – два способи збудувати клас з інших класів, і на рівні об’єкта вони схожі: і член-об’єкт, і база – це підоб’єкти (subobjects) всередині більшого об’єкта.[^cpp-draft-intro-object] Різниця в тому, що саме бачить код. При композиції клас тримає компонент як член і викликає лише його публічні методи, тобто делегує. При успадкуванні похідний клас отримує інтерфейс і реалізацію бази та мусить відповідати їй за змістом: Core Guidelines вимагають, щоб ідея в базі точно відповідала всім похідним типам, і прямо називають успадкування тісним зчепленням.[^cppcg-c120]

Звідси практичне правило. Core Guidelines радять не використовувати успадкування, коли досить data member; зазвичай воно потрібне, коли нащадок мусить перевизначити virtual-функцію бази або має доступ до protected-члена.[^cppcg-c120] Успадкування інтерфейсу – інша річ: клас без даних стабільніший,[^cppcg-c121] а різні реалізації за таким інтерфейсом взаємозамінні для користувача.[^cppcg-c122] Натомість успадкування реалізації й дані в базі роблять інтерфейс крихким: після зміни бази доводиться перекомпілювати користувачів і переглядати нащадків.[^cppcg-c129]

Для тестування й підміни це означає можливість, а не автоматичну властивість. Якщо клас залежить від компонента через параметр шаблону чи посилання на інтерфейс, у тесті можна передати фейк, не чіпаючи решти (докладніше в qid:emb-cppoop-0036). Але клас, який тримає конкретний тип за значенням, прив’язаний саме до нього.

```cpp
// Ілюстративний фрагмент.
struct Spi { std::uint8_t transfer(std::uint8_t byte); };   // конкретний драйвер шини

template <class Bus>              // компонент підміняється на етапі компіляції
class Imu {
public:
    explicit Imu(Bus& bus) : bus_(bus) {}                   // has-a: лише посилання на шину
    std::uint8_t who_am_i() { bus_.transfer(0x8F); return bus_.transfer(0); }
private:
    Bus& bus_;
};
```

**Типові помилки:**

- Успадковувати заради повторного використання коду (`Imu : Spi`), хоча IMU не є шиною: тут досить члена.
- Тримати дані й `protected`-поля в базі: нащадки стають залежними від її реалізації.
- Вважати композицію автоматично слабко зв’язаною: залежність від конкретного типу лишається, доки між ними немає інтерфейсу чи параметра шаблону.
- Сприймати «успадкування лише на один рівень» як закон: це орієнтир (див. qid:emb-cppoop-0012), а вирішує стабільність інтерфейсу.
