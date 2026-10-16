---
id: emb-volconst-0043
title: "Що буде з таким кодом у C?"
track: embedded
section: volatile-and-const
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Question code

```c
const int n = 8;
int a[n];
```

## Short answer

У block scope в C це може бути VLA (variable length array), якщо реалізація підтримує VLA; це не обов’язково compile-time fixed array.[^iso-c-n1570]

`const int n` не робить `n` integer constant expression у C так, як багато хто очікує після C++. Для VLA розмір визначається під час виконання; стандарт не вимагає саме stack allocation, а конкретні embedded компілятори можуть не підтримувати або забороняти VLA.

Захист: для compile-time розміру в C використовуй `#define N 8` або `enum { N = 8 }`.[^iso-c-n1570]

## Detailed explanation

У цьому фрагменті `n` є звичайним `const` object-ом типу `int`, а не integer constant expression. Тому в block scope оголошення `int a[n];` задає variable length array (VLA), якщо реалізація підтримує цю умовну можливість стандарту C. Розмір такого array визначається під час виконання, коли виконується оголошення.[^iso-c-n1570]

Кваліфікатор `const` обмежує присвоєння через `n`, але не змінює категорію його значення для правил оголошення array. У C integer constant expression формується з дозволених стандартом константних операндів; ідентифікатор звичайного `const int` object-а до них не належить. Відтак однаковий на вигляд код може мати інший результат у C та C++: не переносіть правила одного dialect-а на інший.[^iso-c-n1570]

**Приклад:**

```c
void process(void) {
    const int n = 8;
    int a[n];       // VLA у C-реалізації з підтримкою VLA
}

enum { N = 8 };
int fixed[N];       // integer constant expression задає сталий розмір
```

VLA є умовною можливістю C: реалізація не зобов’язана її підтримувати, а компілятор або правила проєкту можуть забороняти її окремо. Стандарт визначає runtime розмір, але не каже, що пам’ять обов’язково виділяється саме на `stack`; це деталь реалізації. На MCU неконтрольований розмір може створити ризик перевищення доступної автоматичної пам’яті, тож для фіксованого буфера краще оголосити справжню integer constant expression і перевіряти бюджет пам’яті лінкером та засобами цільового toolchain.[^iso-c-n1570]

Типова помилка – побачити `const` і припустити, що компілятор завжди створить fixed-size array. Ознака проблеми – програма збирається лише з конкретним компілятором або прапорцями. Для фіксованої місткості використовуй `enum { N = 8 }` чи `#define N 8`; залишай VLA лише коли runtime розмір справді потрібен і підтримку перевірено для кожної цілі.[^iso-c-n1570]
