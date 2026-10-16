---
id: emb-dtypes-0001
title: "Що таке секція `.text` у пам'яті embedded програми?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: embedded-ld-layout
    title: "GNU ld documentation: linker scripts and output section LMA"
    url: https://sourceware.org/binutils/docs/ld/Output-Section-LMA.html
---

## Short answer

У типовому embedded linker script секція `.text` містить виконувані інструкції; її адресу й доступність визначає компонування для конкретної цілі. Часто код виконується з Flash, але XIP, копіювання до RAM і захист від запису залежать від MCU та налаштувань. Саме ім'я `.text` не гарантує HardFault при спробі запису.[^embedded-ld-layout]

## Detailed explanation

Назви секцій описують домовленість між compiler, object format і linker, а не фізичну властивість мови C. У linker script розробник задає output sections і призначає їм memory regions; отже `.text` може розміщуватися в ROM/Flash, RAM або іншій доступній області залежно від плати й сценарію завантаження.[^embedded-ld-layout]

GNU `ld` окремо розрізняє адресу виконання (VMA) та адресу завантаження (LMA). Це дає змогу, наприклад, зберігати секцію в ROM, але виконувати її з RAM після копіювання startup code; чи підтримує це конкретна система, визначають linker script і код запуску.[^embedded-ld-layout]

Для звичайної прошивки `.text` часто містить машинний код, який CPU читає з memory-mapped Flash. Проте не кожен CPU виконує з Flash безпосередньо, і не кожна Flash read-only: внутрішні механізми захисту, MPU та правила шини залежать від мікроконтролера. Тому помилкове припущення про гарантований HardFault може приховати запис у RAM-копію або невдалу спробу, що має іншу реакцію.

**Типові помилки:**
- Вважати `.text` ключовим словом C із гарантованим розміщенням.
- Робити висновок про поведінку запису лише з назви секції, не перевіривши linker script і memory protection.
