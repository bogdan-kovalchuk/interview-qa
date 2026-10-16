---
id: emb-dtypes-0052
title: "Скільки пам'яті займає union і як розраховується його розмір?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gcc-attributes-packed
    title: "GCC: Common Attributes"
    url: https://gcc.gnu.org/onlinedocs/gcc/Common-Attributes.html
---

## Short answer

Стандарт C вимагає, щоб `sizeof(union)` було достатнім для найбільшого члена, але точне значення та alignment визначає реалізація; його не слід рахувати як універсальну суму.[^iso-c-n1570]

Всі поля union займають одну і ту ж область пам’яті.

Наприклад, `union { char c; int x; double d; }` має розмір не менший за `sizeof(double)`, але твердження «рівно 8» залежить від ABI.

У кожен момент зберігається значення не більш як одного члена; правила читання іншого члена залежать від мови та конкретного випадку.[^iso-c-n1570]

## Detailed explanation

`union` надає всім членам спільне сховище. На відміну від `struct`, де члени розташовані послідовно, члени union починаються з однієї адреси, а розмір має вмістити найбільший із них.[^iso-c-n1570]

Це не означає, що стандарт задає формулу точного розміру як «найбільший член плюс padding». Для конкретної реалізації `sizeof(union U)` мусить бути принаймні достатнім для кожного члена, а компілятор може врахувати вимоги alignment і ABI. Саме тому однакове оголошення може мати різний `sizeof` на різних платформах; числа з прикладу на одному комп’ютері не є обіцянкою для MCU.[^iso-c-n1570]

**Приклад:**

```c
union Value {
    char bytes[5];
    uint32_t word;
};
```

Розмір має вмістити п’ять байтів і один `uint32_t`, а також узгодитися з вирівнюванням типу union. Щоб перевірити фактичний layout, компілюй для цільового ABI та дивись `sizeof` і `_Alignof`; для wire-format не покладайся на неявний padding або endian порядок.

У union одночасно зберігається значення одного члена. Інтерпретація байтів через інший тип має мовні обмеження; union сам по собі не робить type punning переносимим. У C++ додатково важливе поняття active member та коректне створення об’єкта цього типу.[^iso-c-n1570]
