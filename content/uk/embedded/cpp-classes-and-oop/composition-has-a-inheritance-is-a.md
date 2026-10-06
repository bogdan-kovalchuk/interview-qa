---
id: emb-cppoop-0023
title: "Композиція vs успадкування: у чому різниця?"
description: "Композиція («has-a»): компоненти – це члени-об’єкти, батько делегує їм."
track: embedded
section: cpp-classes-and-oop
level: junior
type: concept
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
  - source_id: cpp-draft-intro-object
    title: "C++ working draft: [intro.object] Object model"
    url: https://eel.is/c++draft/intro.object
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "Каже, що об’єкти можуть містити інші об’єкти (subobjects) і що subobject буває member subobject, base class subobject або елементом масиву. Про якість дизайну чи зчеплення не каже нічого."
  - source_id: cppcg-c120
    title: "C++ Core Guidelines: C.120 – Use class hierarchies to represent concepts with inherent hierarchical structure (only)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c120-use-class-hierarchies-to-represent-concepts-with-inherent-hierarchical-structure-only
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Настанова: ієрархію класів використовувати лише для понять із внутрішньо ієрархічною структурою; ідея в базі має точно відповідати всім нащадкам, а тісне зчеплення успадкування варто обирати, лише коли кращого способу вираження немає; якщо досить data member, успадкування не використовувати (воно потрібне, коли нащадок перевизначає virtual-функцію бази або має доступ до protected-члена). Числових порогів не задає."
  - source_id: cppcg-c121
    title: "C++ Core Guidelines: C.121 – If a base class is used as an interface, make it a pure abstract class"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c121-if-a-base-class-is-used-as-an-interface-make-it-a-pure-abstract-class
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Настанова: клас стабільніший, якщо не містить даних; інтерфейс складається з публічних pure virtual функцій і порожнього або default virtual-деструктора. Це рекомендація стилю, а не вимога мови."
  - source_id: cppcg-c122
    title: "C++ Core Guidelines: C.122 – Use abstract classes as interfaces when complete separation of interface and implementation is needed"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c122-use-abstract-classes-as-interfaces-when-complete-separation-of-interface-and-implementation-is-needed
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Настанова з прикладом Device із write/read: різні реалізації використовуються взаємозамінно через інтерфейс, і їх можна змінювати, поки доступ іде через нього. Це настанова, а не вимога стандарту."
  - source_id: cppcg-c129
    title: "C++ Core Guidelines: C.129 – When designing a class hierarchy, distinguish between implementation inheritance and interface inheritance"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c129-when-designing-a-class-hierarchy-distinguish-between-implementation-inheritance-and-interface-inheritance
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Настанова: розрізняти interface inheritance та implementation inheritance; реалізація й дані в базі роблять інтерфейс крихким (приклад: додавання даних у базу потребує перегляду й перекомпіляції всіх нащадків і користувачів); важливість зростає з розміром ієрархії, її віком і кількістю організацій, що нею користуються. Порогів у цифрах не дає."
---

## Short answer

**Композиція («has-a»)**: клас містить компоненти як члени-об’єкти й делегує їм роботу, користуючись лише їхнім публічним інтерфейсом. **Успадкування («is-a»)**: похідний клас є різновидом бази, а ідея в базі має точно відповідати всім похідним типам; це тісне зчеплення.[^cppcg-c120] Якщо досить data member, успадкування не використовують. Правило: успадкування – для стабільного інтерфейсу (база без даних), усе інше – композиція.[^cppcg-c121]

## Detailed explanation

Композиція й успадкування – два способи збудувати клас з інших класів, і на рівні об’єкта вони схожі: і член-об’єкт, і база – це підоб’єкти (subobjects) всередині більшого об’єкта.[^cpp-draft-intro-object] Різниця в тому, що саме бачить код. При композиції клас тримає компонент як член і викликає лише його публічні методи, тобто делегує. При успадкуванні похідний клас отримує інтерфейс і реалізацію бази та мусить відповідати їй за змістом: Core Guidelines вимагають, щоб ідея в базі точно відповідала всім похідним типам, і прямо називають успадкування тісним зчепленням.[^cppcg-c120]

Звідси практичне правило. Core Guidelines радять не використовувати успадкування, коли досить data member; зазвичай воно потрібне, коли нащадок мусить перевизначити virtual-функцію бази або має доступ до protected-члена.[^cppcg-c120] Успадкування інтерфейсу – інша річ: клас без даних стабільніший,[^cppcg-c121] а різні реалізації за таким інтерфейсом взаємозамінні для користувача.[^cppcg-c122] Натомість успадкування реалізації й дані в базі роблять інтерфейс крихким: після зміни бази доводиться перекомпілювати користувачів і переглядати нащадків.[^cppcg-c129]

Для тестування й підміни це означає можливість, а не автоматичну властивість. Якщо клас залежить від компонента через параметр шаблону чи посилання на інтерфейс, у тесті можна передати фейк, не чіпаючи решти (докладніше в `qid:emb-cppoop-0036`). Але клас, який тримає конкретний тип за значенням, прив’язаний саме до нього.

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
- Сприймати «успадкування лише на один рівень» як закон: це орієнтир (див. `qid:emb-cppoop-0012`), а вирішує стабільність інтерфейсу.

## Sources

<!-- generated from frontmatter -->
