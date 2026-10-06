---
id: emb-cppoop-0022
title: "Trap: який головний недолік CRTP?"
description: "Base-код дублюється для кожного похідного типу (окрема інстанціація шаблону)."
track: embedded
section: cpp-classes-and-oop
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
  - source_id: cpp-draft-temp-inst
    title: "C++ working draft: Implicit instantiation ([temp.inst])"
    url: https://eel.is/c++draft/temp.inst
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що неявна інстанціація специфікації класового шаблону інстанціює оголошення, але не визначення member-функцій, а специфікація member-функції інстанціюється, коли її визначення потрібне. Про розмір машинного коду не йдеться."
  - source_id: cpp-draft-conv-ptr
    title: "C++ working draft: Pointer conversions ([conv.ptr])"
    url: https://eel.is/c++draft/conv.ptr
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Визначає, що вказівник на похідний клас можна перетворити на вказівник на його базовий клас; про те, які класи є базами, стандарт каже в інших розділах. Про virtual dispatch не йдеться."
  - source_id: gcc-optimize-options
    title: "GCC 16.1.0: Optimize Options"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Optimize-Options.html
    accessed: 2026-10-06
    kind: official
    version: "16.1.0"
    applicability: "Документує -finline-small-functions (підстановка функцій, чиє тіло менше за код виклику; вмикається на -O2, -O3 і -Os) та -fipa-icf (злиття ідентичних функцій; вмикається на -O2 і -Os, ефективніше з LTO). Не гарантує результату для конкретного коду."
---

## Short answer

<span class="warn">Base-код дублюється для кожного похідного типу</span> (окрема інстанціація кожної використаної member-функції).[^cpp-draft-temp-inst]

При багатьох похідних типах і великих base-методах це може <span class="warn">роздути ROM</span>, хоча інлайнінг і злиття ідентичного коду можуть це компенсувати.[^gcc-optimize-options] Також не можна тримати різні CRTP-типи в одному масиві: `SensorBase<A>` не є базою `B`, тож спільного типу вказівника немає.[^cpp-draft-conv-ptr]

Захист: CRTP – для невеликої кількості типів; тримай base-методи дрібними, а важку логіку виноси в non-template код.

## Detailed explanation

Основний недолік CRTP – ціна compile-time dispatch. База є шаблоном, а `SensorBase<Temp>` і `SensorBase<Pressure>` – різні специфікації. Для кожної компілятор інстанціює ті member-функції, чиє визначення потрібне, і кожна така інстанціація – окрема функція.[^cpp-draft-temp-inst] Якщо `read()` у базі робить масштабування, фільтрацію й логування, це тіло з’явиться в образі стільки разів, скільки є похідних типів, що його використовують. У virtual-варіанті той самий код існував би в одній копії, а плата була б іншою: vptr і vtable (див. `qid:emb-cppoop-0013`).

Це не закон природи. Якщо метод малий, компілятор може підставити його в місце виклику: GCC інлайнить функції, чиє тіло менше за код виклику, на `-O2`, `-O3` і `-Os`, і тоді розмір програми навіть зменшується.[^gcc-optimize-options] Ідентичні функції GCC може злити (`-fipa-icf`, на `-O2` і `-Os`; з LTO ефективніше),[^gcc-optimize-options] але копії CRTP-методів, що викликають різні `read_impl`, зазвичай не ідентичні, тож покладатися на це не варто. Тому розмір треба міряти: map file або `size` на цільовій збірці. Умовні числа: якщо base-метод займає 120 байт і без інлайнінгу використовується 8 похідними типами, це 8 × 120 = 960 байт проти 120 байт в одній копії. Для одного методу різниця 840 байт – близько 1,3 % від 64 КіБ flash, а десять таких методів дадуть уже близько 13 %.

Друга вада – тип. Вказівник на похідний клас можна перетворити на вказівник на його базовий клас,[^cpp-draft-conv-ptr] але `SensorBase<A>` не є базою `B`, тож спільного типу вказівника для масиву немає. Гетерогенному контейнеру потрібен спільний non-template base, тобто знову virtual або інша форма type erasure (див. `qid:emb-cppoop-0019`).

Звичайний захист – тонка шаблонна обгортка над non-template кодом (ілюстративно):

```cpp
void scale_and_log(std::int16_t raw);          // не шаблон: одна копія в ROM

template <typename D>
class SensorBase {
public:
    std::int16_t read() {
        std::int16_t raw = static_cast<D*>(this)->read_impl();
        scale_and_log(raw);                    // важка логіка поза шаблоном
        return raw;
    }
};
```

**Типові помилки:**

- Вважати, що CRTP завжди роздуває код або що завжди компактніший за virtual: це залежить від розміру методів, інлайнінгу й кількості типів, тож міряй.
- Класти великі методи в CRTP-базу й інстанціювати її для десятка типів.
- Очікувати масив чи контейнер вказівників на спільну CRTP-базу різних похідних типів.
- Думати, що інстанціюється весь клас: за стандартом визначення member-функцій інстанціюються, лише коли потрібні.[^cpp-draft-temp-inst]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
