---
id: emb-cemb-0040
title: "Які storage classes є у C і як вони пов’язані з linkage та storage duration?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

Основні specifiers: `auto`, `register`, `static`, `extern`, `_Thread_local`. `static` у block scope дає static storage duration, а на file scope дає internal linkage. `extern` зазвичай оголошує object/function з external linkage, але lifetime визначається самим об’єктом, не словом `extern`.[^dou-embedded-interview]

## Detailed explanation

### Специфікатори класу пам’яті у стандарті C

Стандарт ISO/IEC 9899 (пункт 6.7.1) визначає п’ять основних специфікаторів класу пам’яті (storage class specifiers): `auto`, `register`, `static`, `extern` та `_Thread_local` (доданий у C11).[^iso-c-n1570] Специфікатор класу пам’яті у коді визначає поведінку ідентифікатора одночасно у трьох ортогональних вимірах:

1. **Область видимості (scope):** частина тексту програми, де оголошене ім’я є доступним (block scope, file scope або function prototype scope).
2. **Тривалість зберігання (storage duration):** час життя виділеної для об’єкта пам’яті під час виконання програми.
3. **Зв’язування (linkage):** визначає, чи посилається один і той самий ідентифікатор в інших областях видимості або різних одиницях трансляції (translation units) на один і той самий об’єкт.

### Три ортогональні виміри: scope, storage duration і linkage

Стандарт C розрізняє чотири види storage duration:[^iso-c-n1570]
- **Automatic:** пам’ять виділяється під час входу в блок і звільняється під час виходу з нього. Притаманна локальним змінним без специфікатора або з явним `auto` чи `register`.
- **Static:** об’єкт існує протягом усього часу виконання програми, а його ініціалізація виконується один раз до виклику `main()`.
- **Allocated:** пам’ять виділяється та звільняється динамічно під час виконання через функції сімейства `malloc`/`free`.
- **Thread:** час життя об’єкта прив’язаний до життєвого циклу конкретного потоку (актуально для систем із підтримкою потоків у C11).

Для linkage стандарт встановлює три варіанти:[^iso-c-n1570]
- **External linkage:** ідентифікатор позначає об’єкт або функцію, доступну в усіх translation units проєкту (глобальні змінні та функції за замовчуванням або з `extern`).
- **Internal linkage:** ідентифікатор видимий лише в межах поточної translation unit (змінні та функції рівня файлу зі словом `static`).
- **No linkage:** ідентифікатор позначає унікальну локальну сутність (локальні змінні, параметри функцій, типи).

### Семантика static та extern на рівні блоку і файлу

Ключове слово `static` має принципово різний зміст залежно від місця оголошення:[^iso-c-n1570]
- **У block scope (всередині функції або блоку):** `static` змінює storage duration з automatic на static, але не змінює linkage (воно залишається no linkage). Змінна зберігає своє значення між викликами функції, проте залишається недоступною за іменем поза межами цього блоку.
- **У file scope (поза функціями):** `static` змінює linkage з external на internal, не впливаючи на storage duration (який уже є static). Символ не експортується в глобальну таблицю символів об’єктного файлу, захищаючи модуль від колізій імен.

Слово `extern` оголошує ідентифікатор, який зазвичай має external linkage, але сам по собі `extern` не виділяє пам’яті (якщо це не супроводжується ініціалізатором). Тривалість зберігання визначається тим місцем, де об’єкт фактично визначено.

Специфікатор `register` повідомляє оптимізатору компілятора про бажаність розміщення змінної в регістрі процесора, а взяття її адреси оператором `&` заборонено синтаксисом C.[^iso-c-n1570]

### Розміщення у секціях пам’яті мікроконтролера

У вбудованих системах вибір специфікатора безпосередньо впливає на розміщення об’єкта лінкером у фізичній пам’яті MCU:[^gnu-ld-manual]
- Змінні зі static storage duration та ненульовою ініціалізацією потрапляють у секцію `.data` (початкові дані зберігаються у Flash, а під час запуску startup-код копіює їх у RAM).
- Змінні зі static storage duration без ініціалізації або з ініціалізацією нулем потрапляють у секцію `.bss` (startup-код очищує відповідний діапазон RAM нулями перед запуском програми).
- Дані зі специфікатором `const` зазвичай відображаються у секцію `.rodata` і можуть залишатися безпосередньо у Flash, заощаджуючи оперативну пам’ять.
- Змінні з automatic storage duration виділяються компілятором у stack frame поточної функції або тимчасово утримуються у вільних CPU-регістрах.
