---
id: emb-macros-0001
title: "Що таке препроцесор C і коли він виконує свою роботу?"
description: "Препроцесор – це текстова фаза, яка виконується до компіляції і обробляє директиви #include, #define, #if."
track: embedded
section: inline-and-macros
level: junior
type: concept
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
  - source_id: gcc-cpp-overview
    title: "GCC manual: The C Preprocessor, Overview"
    url: https://gcc.gnu.org/onlinedocs/cpp/Overview.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Описує роль і межі GNU CPP перед компіляцією; деталі реалізації можуть відрізнятися в інших препроцесорах."
  - source_id: gcc-cpp-invocation
    title: "GCC manual: The C Preprocessor, Invocation"
    url: https://gcc.gnu.org/onlinedocs/cpp/Invocation.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Підтверджує, що gcc -E зупиняється після preprocessing; це інструкція саме для GCC."
---

## Short answer

**Препроцесор** – це текстова фаза, яка виконується до компіляції і обробляє директиви `#include`, `#define`, `#if`.

Він обробляє preprocessing directives і розгортає macros, але не перевіряє типи чи звичайну семантику C/C++. Тому помилка може стати видимою лише після розгортання, під час подальшого розбору або перевірки типів.[^gcc-cpp-overview]

Щоб побачити результат GCC preprocessing, дивись output `gcc -E file.c`.[^gcc-cpp-invocation]

## Detailed explanation

Препроцесор виконує попередню обробку вихідного тексту C: обробляє директиви на кшталт `#include` і `#if`, а також розгортає макроси до власне компіляції.[^gcc-cpp-overview]

На цій стадії препроцесор може вставляти вміст header-файлів, включати або виключати ділянки за умовою та замінювати виклики макросів їхніми розгортаннями. Він працює з preprocessing tokens і правилами директив, а не є довільною операцією пошуку й заміни рядків. Наприклад, параметризований macro може формувати різний текст залежно від аргументів, а `#` і `##` мають окреме значення в його визначенні.[^gcc-cpp-overview]

Після preprocessing результат передається наступним стадіям компілятора. Вони розбирають синтаксис C і перевіряють типи та правила мови. Отже, макрос може породити фрагмент, який не є коректним C, або текстово повторити аргумент кілька разів; помилка проявиться вже в отриманому результаті. Сам препроцесор не виконує повну перевірку типів і не розуміє, чи безпечний задуманий вираз.

Приклад: якщо `#define TWICE(x) ((x) + (x))`, виклик `TWICE(i++)` розгортається у вираз із двома інкрементами. Зовнішній код треба аналізувати після розгортання, а не оцінювати лише короткий запис макросу. Щоб дослідити GCC output без компіляції, команда `gcc -E file.c` зупиняє драйвер після preprocessing.[^gcc-cpp-invocation]

**Типова помилка:** називати препроцесор простим text substitution і очікувати, що він знайде помилкові типи. Використовуй його для директив і розгортання, а для діагностики перевіряй preprocess output та повідомлення компілятора.

## Sources

<!-- generated from frontmatter -->
