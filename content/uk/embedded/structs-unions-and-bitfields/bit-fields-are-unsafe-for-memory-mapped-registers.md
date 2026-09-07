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
updated: 2026-09-07
content_revision: 1
reconciled_with:
  en: 1
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
---

## Short answer

<span class="warn">Layout bit-field-ів implementation-defined, а доступ часто генерує read-modify-write.</span>

Порядок розміщення бітів у storage unit, signedness plain `int` bit-fields і padding між ними залежать від компілятора/ABI. Крім того, запис одного bit-field може прочитати весь register і записати назад, що небезпечно для write-one-to-clear або read-to-clear bits.

Захист: для hardware registers часто краще використовувати masks/shifts і атомарні set/clear registers. Якщо bit-fields дозволені, прив'язуйся до конкретного compiler ABI і тестуй generated code.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
