---
id: emb-fnptr-0016
title: "Trap: що не так із викликом callback із несумісною сигнатурою?"
description: "Виклик через function pointer несумісного типу має undefined behavior."
track: embedded
section: function-pointers-and-callbacks
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
---

## Question code

```c
void f(int x);
void (*cb)(void) = (void (*)(void))f;
cb();
```

## Short answer

<span class="warn">Виклик через function pointer несумісного типу має undefined behavior.</span>

Навіть якщо адреса функції фізично правильна, calling convention очікує інші аргументи, return value або register usage. На embedded ABI це може пошкодити stack/registers або передати випадкові значення.

Захист: не виправляй warning `-Wincompatible-pointer-types` cast-ом. Зроби adapter function із правильною сигнатурою.[^embeddedinterviewlab] [^iso-c-n1570]

## Detailed explanation

Виклик через pointer to function, тип якого несумісний із типом визначеної функції, має undefined behavior у C. Перетворення адреси між типами function pointer саме по собі дозволене, але стандарт гарантує коректний виклик лише тоді, коли перетворений pointer повернути до початкового сумісного типу; викликати функцію через несумісний тип не можна. [^iso-c-n1570]

У прикладі `f` має тип `void (int)`, а `cb` – `void (void)`. Через `cb()` викликач не передає аргумент, тоді як визначення `f` очікує `int`. Це не просто питання того, чи «правильно лежить адреса»: контракт виклику включає типи аргументів і результату. Реальна поведінка може відрізнятися між компіляторами й ABI, тому не можна обґрунтовувати такий код тим, що на одній платі він нібито працює. [^iso-c-n1570]

Наприклад, callback API може очікувати `void (*)(void *)`, а наявна функція – `void handler(int)`. Передача її адреси через cast не робить параметри сумісними. Якщо значення справді треба перетворити, зробіть окрему функцію з точною сигнатурою, яка дістає контекст, перевіряє його й викликає `handler` із коректно отриманим `int`. [^iso-c-n1570]

**Типові помилки:**

- Вважати, що однакова адреса функції означає однакову сигнатуру.
- Прибирати діагностику компілятора cast-ом і залишати несумісний виклик.
- Приписувати збій лише embedded-платформі: порушення контракту виклику вже є undefined behavior мовою C.

Щоб уникнути проблеми, зберігайте один typedef callback-типу на межі API й передавайте функції саме цього типу. Адаптер має виконувати явне перетворення аргументів на рівні значень; сам cast function pointer не є адаптером. [^iso-c-n1570]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
