---
id: emb-structs-0024
title: "Trap: чому bit-fields небезпечні для memory-mapped registers?"
description: "Layout bit-field-ів implementation-defined, а доступ часто генерує read-modify-write."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-04
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
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; це джерело не є доказом тверджень."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
  - source_id: stm32-w1c-manual
    title: "SR5E1x 32-bit Arm Cortex-M7 architecture microcontroller reference manual"
    url: https://www.st.com/resource/en/reference_manual/rm0483-sr5e1x-32bit-arm-cortexm7-architecture-microcontroller-for-electrical-vehicle-applications-stmicroelectronics.pdf
    accessed: 2026-10-04
    kind: official
    version: "RM0483 Rev 6"
    applicability: "Приклад визначення W1C у документації виробника; фактичну семантику треба перевіряти в manual конкретного пристрою."
---

## Short answer

<span class="warn">Layout bit-field-ів implementation-defined, а доступ часто генерує read-modify-write.</span>

Порядок розміщення бітів у storage unit, signedness plain `int` bit-fields і padding між ними залежать від компілятора/ABI. Крім того, запис одного bit-field може прочитати весь register і записати назад, що небезпечно для write-one-to-clear або read-to-clear bits.

Захист: для hardware registers часто краще використовувати masks/shifts і атомарні set/clear registers. Якщо bit-fields дозволені, прив’язуйся до конкретного compiler ABI і тестуй generated code.[^iso-c-n1570]

## Detailed explanation

Bit-fields are a poor default for memory-mapped registers because the C language does not promise a hardware register layout, and a source-level field assignment may not correspond to a single hardware write.[^iso-c-n1570]

Реалізація визначає порядок розміщення бітів у одиниці зберігання, можливість переходу поля через її межу та деякі властивості самої одиниці. Тому compiler і ABI визначають відповідність оголошень бітам; лише з `error : 1` не можна зробити висновок, що це саме біт ERROR із документації мікросхеми.[^iso-c-n1570]

Окрема проблема – спосіб доступу. Щоб змінити одне поле, згенерований код може прочитати ширше значення register, змінити вибрані біти в CPU register, а потім записати ціле значення назад. Така послідовність може конфліктувати з поведінкою периферії: читання може скидати flag, запис одиниці може скидати W1C flag, а hardware може змінити інший status bit між читанням і записом. Це залежить від периферії та compiler, тому перевіряй datasheet і згенеровані інструкції.[^iso-c-n1570]

Наприклад, якщо status register має W1C flag поруч зі звичайними бітами стану, присвоєння нуля полю C саме по собі не гарантує, що інші біти збережуться під час транзакції з периферією. Використовуй спосіб запису з reference manual – наприклад, окремий clear register або запис mask – і перевір його для цільового пристрою.[^stm32-w1c-manual]

**Типові помилки:**

- Вважати, що порядок полів у `struct` задає порядок апаратних бітів.
- Вважати, що `volatile` робить операцію атомарною або безпечною для W1C.
- Переносити перевірену розкладку на інший compiler чи ABI без перевірки.

Для звичайного внутрішнього представлення даних bit-fields можуть бути доречними, якщо ABI зафіксовано. Для периферії важливі і layout, і побічні ефекти доступу; маски та явно документовані операції зазвичай легше звірити з datasheet.[^iso-c-n1570]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
