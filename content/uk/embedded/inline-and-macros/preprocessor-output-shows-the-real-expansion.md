---
id: emb-macros-0027
title: "Як побачити, у що насправді розгорнувся макрос?"
description: "Подивитися output препроцесора: gcc -E file.c (або arm-none-eabi-gcc -E)."
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
  - source_id: gcc-cpp-invocation
    title: "GCC: Invocation (The C Preprocessor)"
    url: https://gcc.gnu.org/onlinedocs/cpp/Invocation.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Документує запуск препроцесора GCC через -E та його вихід; інші компілятори можуть мати інші параметри."
---

## Short answer

Подивитися output препроцесора: `gcc -E file.c` (або `arm-none-eabi-gcc -E`). Цей прапорець просить GCC зупинитися після preprocessing і вивести перетворений translation unit.[^gcc-cpp-invocation]

Такий перегляд допомагає простежити включені файли та знайти наслідки підстановки макросів, наприклад пропущені дужки або неочікувані токени. Вихід містить також заголовки й службові linemarkers, тому це не лише короткий список макросів.[^gcc-cpp-invocation] [^iso-c-n1570]

## Detailed explanation

Параметр `-E` запускає preprocessing і завершує роботу GCC до компіляції; результат містить оброблений вміст початкового файла разом із включеними файлами, макророзгортаннями та зазвичай linemarkers.[^gcc-cpp-invocation]

У C препроцесор працює з preprocessing tokens. Для object-like макроса кожне наступне входження його імені замінюється списком токенів із `#define`; function-like макрос додатково підставляє токени аргументів у відповідні місця replacement list. Це текстово-токенна трансформація до звичайного аналізу C, а не виклик типізованої функції.[^iso-c-n1570]

Приклад:

```c
#define SQUARE(x) ((x) * (x))
int y = SQUARE(a + 1);
```

Після preprocessing ініціалізатор матиме вигляд `((a + 1) * (a + 1))`. Дужки зберігають групування, але аргумент-вираз усе одно з’являється двічі й обчислюватиметься за правилами C під час виконання. Сам preprocessing output показує структуру підстановки, але сам по собі не доводить, скільки разів виконається кожен вираз і чи є програма коректною.[^iso-c-n1570]

Для embedded-проєкту команда зазвичай має містити той самий `-I`, `-D` і `-std` набір, що й реальна збірка: конфігураційні макроси впливають на результат. Наприклад, можна перенаправити вивід `gcc -E -Iinclude -DSTM32 foo.c` у файл і знайти там потрібну функцію чи директиву. Якщо заголовки дуже великі, це буде великий дамп; опція `-P` прибирає linemarkers, але може ускладнити відстеження джерела рядків.[^gcc-cpp-invocation]

**Типова помилка:** вважати, що `-E` виконує код або виявляє всі проблеми макросів. Він лише показує стадію preprocessing; типи, обчислення, оптимізація та linker errors потребують відповідних наступних етапів компіляції.[^gcc-cpp-invocation]

## Sources

<!-- generated from frontmatter -->
