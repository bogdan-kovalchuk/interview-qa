---
id: emb-dtypes-0070
title: "Який результат `sizeof(struct { char a; char b; int c; })` на типовому 32-bit ABI з 4-byte int alignment?"
description: "За вказаного ABI два байти padding вирівнюють int, а sizeof структури дорівнює 8 байтам."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  en: 3
anki:
  export: true
sources:
  - source_id: gnu-c-struct-layout
    title: "GNU C Introduction and Reference Manual: Structure Layout"
    url: https://www.gnu.org/software/c-intro-and-ref/manual/html_node/Structure-Layout.html
    accessed: 2026-10-04
    kind: book
    version: "current"
    applicability: "Ілюструє типове вирівнювання й padding у структурах; точний layout залежить від реалізації та ABI."
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
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

За вказаного ABI результат – **8 байтів**: `a` і `b` мають offsets 0 і 1, два байти padding вирівнюють `c` на offset 4, trailing padding немає.[^gnu-c-struct-layout] За іншим порядком `char`, `int`, `char` типовий layout дорівнює 12 байтам через padding до й після `int`.[^gnu-c-struct-layout]

C не гарантує такий самий layout для всіх систем: розмір і alignment залежать від ABI, packing options та атрибутів. Упорядкування за спаданням alignment часто скорочує padding, але offsets і `sizeof` треба перевіряти компілятором цільової системи.[^iso-c-n1570][^gnu-c-struct-layout]

## Detailed explanation

На поширеному ABI з 8-bit byte, `sizeof(int) == 4` та alignment `int` у чотири байти, `char` займає один байт і має byte alignment. Перші два поля мають offsets 0 і 1. Далі компілятор додає два байти padding, щоб вирівняти `c` на offset 4; його чотири байти завершують об’єкт на offset 8 без trailing padding. Підрахунок спирається на заданий розмір і alignment `int`.[^gnu-c-struct-layout]

Сам напис «32-bit» у запитанні недостатній, щоб гарантувати результат. C вимагає збереження порядку членів і дозволяє padding, але alignment членів є implementation-defined. Розмір `int`, packing flags, ABI та явні alignment attributes впливають на offsets і `sizeof`; для іншого компілятора або опцій відповідь може відрізнятися.[^iso-c-n1570]

Зміна порядку на `char`, `int`, `char` за цих самих припущень дає offset-и 0, 4 і 8. Після першого поля потрібні три байти, щоб вирівняти `int`; після останнього поля структура округлюється до кратної чотирьом довжини, додаючи ще три байти. Підсумок – 12 байтів. Такий порядок полів часто дозволяє зменшити обсяг padding, але це не універсальна оптимізація для всіх ABI.[^gnu-c-struct-layout]

**Приклад перевірки:**

```c
struct S { char a; char b; int c; };
_Static_assert(sizeof(struct S) == 8, "unexpected ABI layout");
```

У production коді, що серіалізує байти або описує hardware registers, не покладайся на візуальний підрахунок: перевіряй `_Alignof`, `offsetof` і `sizeof` для toolchain та прапорців цілі. Padding bytes не є полями протоколу й можуть мати значення, непридатні для wire format.[^iso-c-n1570]

Після зміни compiler flags або ABI повтори перевірку, бо offsets можуть змінитися. Це особливо важливо, коли структура входить до binary interface між firmware модулями.[^iso-c-n1570]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
