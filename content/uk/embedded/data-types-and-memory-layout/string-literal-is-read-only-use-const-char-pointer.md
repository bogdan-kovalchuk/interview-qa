---
id: emb-dtypes-0006
title: "Чому для рядкового літерала краще використовувати `const char*`, а не `char*`?"
description: "Стандарт забороняє змінювати масив рядкового літерала, але не визначає, де саме реалізація його зберігає."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
tags: []
status: published
updated: 2026-10-04
content_revision: 3
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
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; це джерело не є доказом тверджень."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
  - source_id: cpp-draft-string-literals
    title: "C++ working draft, [lex.string]"
    url: https://eel.is/c++draft/lex.string
    accessed: 2026-10-04
    kind: spec
    version: "current"
    applicability: "Тип звичайного C++ string literal і заборона модифікації його об’єкта; це working draft стандарту C++."
  - source_id: gcc-write-strings
    title: "GCC 16.1 Warning Options: -Wwrite-strings"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Warning-Options.html
    accessed: 2026-10-04
    kind: official
    version: "GCC 16.1"
    applicability: "Поведінка GCC прапорця -Wwrite-strings; це діагностика компілятора, а не правило мови."
---

## Short answer

У C літерал рядка `"hello"` має тип `char[6]`, але стандарт забороняє змінювати його масив: така спроба має <span class="warn">undefined behavior</span>; де саме реалізація зберігає літерал, стандарт не визначає. У C++ тип літерала – `const char[6]`, тому `const char *p = "hello";` зберігає цю заборону в системі типів. У C `char *p = "hello";` дозволено для сумісності, але запис через такий вказівник усе одно має undefined behavior.[^iso-c-n1570] [^cpp-draft-string-literals]

## Detailed explanation

Літерали рядків мають статичну тривалість зберігання, однак стандарт C не вимагає розміщувати їх у фізично доступній лише для читання пам’яті. Він вимагає іншого: спроба змінити масив, який відповідає літералу, має undefined behavior. Через це програму не можна вважати безпечною лише тому, що на конкретній платі запис випадково не спричинив fault.[^iso-c-n1570]

У C тип звичайного літерала – масив `char`, а не `const char`; несумісний на вигляд тип історично зберігся для сумісності. У C++ елементи масиву літерала мають `const char`, а перетворення літерала на `char *` не є коректним стандартним кодом. Тому `const char *p` доречний в обох мовах: він не дозволяє модифікувати символи через цей вказівник, хоча інші вказівники на той самий об’єкт не стають від цього const.[^iso-c-n1570] [^cpp-draft-string-literals]

Якщо потрібен змінюваний буфер, оголосіть власний масив, ініціалізований літералом: `char text[] = "hello";`. Це окремий масив із копією початкових символів, а не сам літерал. У C `-Wwrite-strings` у GCC змінює тип літералів для діагностики й попереджає про присвоєння `char *`; це поведінка конкретного компілятора, а не зміна правил мови.[^gcc-write-strings]

Різницю видно за часом життя й можливістю запису: `text[0] = 'H';` змінює елемент локального масиву, тоді як `p[0] = 'H';` для `p`, що вказує на літерал, має undefined behavior. Сам тип `const char *` забороняє запис саме через `p`, але не створює копію й не змінює властивості об’єкта, на який він вказує.[^iso-c-n1570] [^cpp-draft-string-literals]

У C передавання літерала функції з параметром `char *` може пройти перевірку типів, бо літерал має тип масиву `char`, але функція все одно не повинна його змінювати. Для інтерфейсу, який лише читає текст, параметр `const char *` виражає цей контракт; для функції, яка редагує текст, передайте окремий змінюваний масив.[^iso-c-n1570]

**Типова помилка:** плутати фізичне розміщення з гарантією мови й вважати, що відсутність апаратної помилки робить запис допустимим. Використовуйте `const char *` для читання літерала, а змінювану копію зберігайте у `char` масиві.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
