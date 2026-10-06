---
id: emb-cppoop-0001
title: "Що означає «zero-overhead abstraction» для C++ класу?"
description: "Non-virtual клас може компілюватися у такий самий машинний код, як C-struct із вільними функціями, якщо оптимізатор бачить тіло методів."
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
  - source_id: cpp-draft-expr-prim-this
    title: "C++ working draft: [expr.prim.this] The keyword this"
    url: https://eel.is/c++draft/expr.prim.this
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "Підтверджує, що `this` є вказівником на об’єкт, для якого викликано нестатичну member-функцію; не визначає, як саме його передає ABI."
  - source_id: cpp-draft-class-prop
    title: "C++ working draft: [class.prop] Properties of classes"
    url: https://eel.is/c++draft/class.prop
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "Визначає standard-layout класи (без virtual-функцій і virtual-баз, з однаковим access control нестатичних даних, зі standard-layout членами й базами та за низки інших умов) і зазначає, що такі класи придатні для обміну з кодом іншими мовами; нічого не обіцяє про машинний код."
  - source_id: cpp-draft-intro-abstract
    title: "C++ working draft: [intro.abstract] Abstract machine"
    url: https://eel.is/c++draft/intro.abstract
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "Підтверджує, що реалізація не зобов’язана копіювати структуру abstract machine, а лише її observable behavior; саме це дозволяє компілятору інлайнити методи. Не гарантує, що він це зробить."
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "Визначає dynamic class (з virtual-функціями чи virtual-базами) як клас, що потребує virtual table pointer; отже клас без них його не має. Це ABI, а не стандарт мови: інші ABI можуть відрізнятися в деталях."
  - source_id: gcc-optimize-options
    title: "GCC 16.1.0: Optimize Options"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Optimize-Options.html
    accessed: 2026-10-06
    kind: official
    version: "16.1.0"
    applicability: "Документує, що без оптимізації GCC не розгортає функції inline (-fno-inline за замовчуванням), що -finline-small-functions вмикається на -O2, -O3 і -Os, і що -flto дозволяє інлайнити між об’єктними файлами; конкретні рішення евристик залежать від коду."
  - source_id: cpp-core-guidelines
    title: "C++ Core Guidelines: In.aims"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#ss-aims
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Формулює zero-overhead principle: що не використовуєш, за те не платиш, а правильно використана абстракція не гірша за ручний низькорівневий код. Це принцип проєктування, а не гарантія для кожного компілятора й коду."
---

## Short answer

**Non-virtual клас може компілюватися у такий самий машинний код, як C-struct із вільними функціями, якщо оптимізатор бачить тіло методів.**

Нестатична member-функція отримує неявний `this`;[^cpp-draft-expr-prim-this] у типових ABI клас без `virtual` не має vptr/vtable,[^itanium-cxx-abi] а прості методи зазвичай інлайняться. На `-O0` або через окремі translation units (без LTO) виклик може лишитися звичайним call.[^gcc-optimize-options]

Правило: інкапсуляція через клас у embedded зазвичай безкоштовна в release-збірці, поки немає virtual і зайвого стану.[^cpp-core-guidelines]

## Detailed explanation

«Zero-overhead» – це принцип, а не обіцянка нульового коду: те, чим не користуєшся, нічого не коштує, а те, чим користуєшся, не гірше за ручну реалізацію нижчого рівня.[^cpp-core-guidelines] Для non-virtual класу це означає, що `led.toggle()` по суті є викликом вільної функції `led_toggle(&led)`: нестатична member-функція працює над об’єктом, на який вказує `this`.[^cpp-draft-expr-prim-this] Модифікатори `private` і `public` – це правила доступу до імен під час компіляції, у машинному коді їх немає.

Дані теж лежать як у C-структурі. Щоб клас був standard-layout, він, окрім відсутності virtual-функцій і virtual-баз та однакового access control усіх нестатичних даних, має мати лише standard-layout члени й бази та виконувати решту умов [class.prop]; стандарт прямо каже, що такі класи придатні для обміну з кодом інших мов.[^cpp-draft-class-prop] Стандарт не вимагає від реалізації певної структури, лише відтворення observable behavior abstract machine,[^cpp-draft-intro-abstract] тому vptr – деталь конкретного ABI. У Itanium C++ ABI vptr потрібен лише dynamic class, тобто класу з virtual-функціями або virtual-базами; один `virtual` додає вказівник у кожен об’єкт і непрямий виклик.[^itanium-cxx-abi]

Умова «оптимізатор бачить тіло» суттєва. Без оптимізації GCC не інлайнить функції, а `-finline-small-functions` вмикається лише на `-O2`, `-O3` і `-Os`; метод, оголошений в одному `.cpp` і викликаний в іншому, інлайниться тільки з LTO.[^gcc-optimize-options] Тому зручно писати короткі методи в заголовку. Конструктори й деструктори, як і ініціалізація та очищення в C, виконують код – «нуль» стосується абстракції, а не роботи.

```cpp
class Led {
public:
    Led(volatile std::uint32_t* odr, std::uint32_t mask) : odr_(odr), mask_(mask) {}
    void toggle() { *odr_ = *odr_ ^ mask_; }
private:
    volatile std::uint32_t* odr_;
    std::uint32_t mask_;
};

/* C-еквівалент (ілюстративно): той самий розмір даних і той самий виклик */
struct led { volatile uint32_t* odr; uint32_t mask; };
static inline void led_toggle(struct led* self) { *self->odr = *self->odr ^ self->mask; }
```

**Типові помилки:**

- Вважати будь-який клас безкоштовним: один `virtual` додає vptr в об’єкт і vtable-виклик.
- Порівнювати розмір чи швидкість на `-O0`: методи не інлайняться, і C++ здається повільнішим, ніж у release.
- Ховати тіла маленьких методів у `.cpp` без LTO і чекати інлайнінгу.
- Плутати «zero overhead» зі «zero code»: конструктор і деструктор усе одно виконують роботу.

## Sources

<!-- generated from frontmatter -->
