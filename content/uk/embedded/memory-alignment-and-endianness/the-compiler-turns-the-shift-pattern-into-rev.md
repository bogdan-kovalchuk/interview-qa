---
id: emb-align-0019
title: "Чому варто віддати перевагу впізнаваному byte-swap idiom або builtin замість inline assembly?"
description: "Це зберігає семантику й переносність та дає optimizer змогу вибрати цільову byte-swap instruction."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: concept
tags: []
status: published
updated: 2026-09-08
content_revision: 4
reconciled_with:
  en: 4
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання і відповіді; відповідь незалежно не перевірена."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
  - source_id: gcc-byte-swap-builtins
    title: "Byte-Swapping Builtins"
    url: https://gcc.gnu.org/onlinedocs/gcc/Byte-Swapping-Builtins.html
    accessed: 2026-09-08
    kind: official
    version: null
    applicability: "Документує GCC builtins, семантика яких прямо виражає 16-, 32- і 64-бітне розвертання байтів."
  - source_id: learncpp-bitwise
    title: "Bitwise operators"
    url: https://www.learncpp.com/cpp-tutorial/bitwise-operators/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Додаткове пояснення portable shift/mask idiom."
  - source_id: acode-cpp-next
    title: "C++ вивчено – що далі?"
    url: https://acode.com.ua/end-cpp-what-is-next/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Додаткова українська дорожня карта; не є нормативним джерелом щодо compiler optimization."
---

## Short answer

**Зрозумілий unsigned shift/mask idiom або byte-swap builtin робить операцію видимою для optimizer.**

На придатному Arm target optimizing compiler може вибрати `REV` або `REV16`, а на іншій платформі – найкращу послідовність її архітектури. Це поширена оптимізація, але не гарантія для кожної compiler configuration.

Правило: спершу пиши зрозумілий C; до intrinsics/asm вдавайся, лише якщо профіль показав потребу.[^embeddedinterviewlab]

## Detailed explanation

Inline assembly прив'язує source до instruction set, syntax, register constraints та compiler interface. Він також може завадити constant folding або instruction scheduling, якщо constraints неправильно описують хоча б один ефект. Language-level operation зберігає більше інформації для whole-program optimization і водночас має визначену поведінку на targets без спеціальної byte-swap instruction.

Є два вдалі способи виразити намір:

- використати unsigned shifts, masks та OR у відомому idiom;
- використати toolchain builtin за невеликим portability wrapper.

GCC документує `__builtin_bswap16`, `__builtin_bswap32` і `__builtin_bswap64` як операції, що розвертають байти аргументу.[^gcc-byte-swap-builtins] Builtin особливо явно показує намір, а portable idiom працює й там, де цього extension немає. Огляд LearnCpp пояснює bitwise operators у другому варіанті.[^learncpp-bitwise]

Code generation залежить від обраного CPU, ISA features, optimization level, навколишнього коду та compiler version. Наприклад, constant input може бути обчислений без жодної runtime instruction, а старішому target можуть знадобитися кілька shifts. Тому «це стане однією `REV`» – спостереження, яке треба перевірити в optimized disassembly, а не частина контракту C.

Починай із найзрозумілішої коректної форми, компілюй для фактичного MCU з release options і перевіряй або вимірюй hot path. Застосовуй intrinsic чи inline assembly лише тоді, коли виміряний результат і підтримуваний toolchain виправдовують додатковий зв'язок. Дорожня карта aCode є додатковим орієнтиром для ширшого вивчення C і C++.[^acode-cpp-next]

## Sources

<!-- generated from frontmatter -->
