---
id: emb-tmplcx-0015
title: "Які є стратегії боротьби з template code bloat?"
description: "Thin wrapper над `void*`; обмеження кількості інстанціацій; extern template; винесення T-незалежного коду у non-template base; LTO (link-time optimization)."
track: embedded
section: templates-and-constexpr
level: junior
type: concept
tags: []
status: published
updated: 2026-10-13
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
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-13; це джерело не є доказом тверджень."
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
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що специфікація шаблону функції чи member-функції інстанціюється, коли її визначення потрібне; неявна інстанціація класового шаблону інстанціює лише оголошення членів. Про розмір коду не йдеться."
  - source_id: cpp-draft-temp-explicit
    title: "C++ working draft: Explicit instantiation ([temp.explicit])"
    url: https://eel.is/c++draft/temp.explicit
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що для entity з явною декларацією інстанціації, яку використано так, що інакше була б неявна інстанціація, у програмі має бути явна інстанціація-визначення; явна інстанціація класу інстанціює його прямі не-шаблонні члени. Не описує, як компілятор уникає копій."
  - source_id: gcc-optimize-options
    title: "GCC 16.1.0: Optimize Options"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Optimize-Options.html
    accessed: 2026-10-13
    kind: official
    version: "16.1.0"
    applicability: "Описує -fipa-icf: identical code folding для функцій, що зменшує розмір коду, краще працює з увімкненим LTO і за замовчуванням увімкнено на -O2. Не каже, які саме тіла злито в конкретній програмі."
---

## Short answer

**Thin wrapper над `void*`; обмеження кількості інстанціацій; `extern template`; винесення T-незалежного коду у non-template base; LTO (link-time optimization).**

Кожна інстанціація з іншим `T` дає окремі визначення використаних функцій,[^cpp-draft-temp-inst] тож спільну реалізацію варто винести поза шаблон. Ідея: у шаблоні лишається тонкий типобезпечний шар, а логіка працює через `void*` і розмір елемента або через базовий клас.

Правило: винось усе, що не залежить від `T`, у non-template код.[^embeddedinterviewlab]

## Detailed explanation

Копії шаблонного коду з’являються тому, що кожен набір аргументів створює власні визначення використаних функцій.[^cpp-draft-temp-inst] Стратегії зменшують або кількість різних наборів аргументів, або обсяг коду, який повторюється в кожному з них. Кожна з них має ціну: типобезпеку, гнучкість або складність збірки.

Thin wrapper тримає в шаблоні лише перетворення типів, а логіку виносить у не-шаблонну функцію, яка приймає `void*` і розмір елемента. Ілюстративний приклад (компілюється, але `ring_push_bytes` лишається без визначення):

```cpp
#include <cstddef>

struct RingCore;                                                          // defined once, in ring.cpp
void ring_push_bytes(RingCore* core, const void* item, std::size_t size); // one copy for all T

template <typename T>
class Ring {
public:
    explicit Ring(RingCore* core) : core_(core) {}
    void push(const T& value) { ring_push_bytes(core_, &value, sizeof(T)); }  // thin, per-T
private:
    RingCore* core_;
};
```

Ціна такого рішення в тому, що спільний код бачить лише байти й розмір. Він не викликає конструкторів копіювання чи переміщення `T`. Для не-trivially-copyable `T` побайтове копіювання не дає гарантованого значення, бо стандарт гарантує його лише для trivially copyable типів; тонкий шар має це відсікти через `static_assert(std::is_trivially_copyable_v<T>)`.[^iso-cpp-n4861]

Винесення T-незалежної логіки в non-template базовий клас дає ту саму економію без `void*`: спільна частина компілюється один раз, а шаблон містить лише залежне від `T`. Обмеження кількості інстанціацій – рішення на рівні API: менше різних типів у прошивці означає менше копій. LTO разом з `-fipa-icf` може злити функції з ідентичним тілом, але лише ті, що справді збіглися; на це не слід розраховувати замість проєктування.[^gcc-optimize-options]

`extern template` (докладніше qid:emb-tmplcx-0016) не зменшує код самого шаблону. Він дозволяє не інстанціювати його в інших translation units, якщо явна інстанціація є в одному місці.[^cpp-draft-temp-explicit]

**Типові помилки:**

- Винести в спільний код щось, що залежить від `T`, і отримати неправильну поведінку для окремих типів.
- Розраховувати на LTO як на заміну проєктування: він зливає лише ідентичні функції.
- Залишити `void*`-обгортку без перевірок типів у тонкому шарі.

## Sources

<!-- generated from frontmatter -->
