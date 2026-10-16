---
id: emb-build-0005
title: "Що буде, якщо у двох файлах зробити функцію з однаковим ім'ям і параметрами? На якому етапі виникне помилка?"
track: embedded
section: toolchain-and-build
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gcc-overall-options
    title: "GCC manual: Options Controlling the Kind of Output"
    url: https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html
---

## Short answer

Якщо у двох `.c`/`.cpp` файлах визначити не-`static` функцію з однаковим ім'ям і external linkage, компіляція окремих файлів може пройти успішно, бо кожен translation unit компілюється окремо.[^dou-embedded-interview]

Помилка зазвичай виникне на етапі **linking**: linker побачить два global symbols з однаковим іменем і видасть multiple definition / duplicate symbol. Якщо зробити функції `static`, кожна матиме internal linkage і конфлікту між файлами не буде. У C++ overload можливий тільки якщо сигнатури різні; однакова сигнатура все одно порушує ODR.

## Detailed explanation

Коли компілятор обробляє `.c` або `.cpp` файл, він створює object file (`.o` або `.obj`) з символами. Кожен non-`static` функція або глобальна змінна стає global symbol у object file. На етапі компіляції кожного файлу окремо компілятор не знає про інші translation units, тому він не може перевірити, чи є конфлікти імен.[^gcc-overall-options]

Linker збирає всі object files разом і будує symbol table. Якщо він бачить два global symbols з однаковим іменем (наприклад, `void process_data()` визначена в `file1.c` і `file2.c`), він не може вирішити, яку версію використовувати, і видає помилку:

```
file2.o: In function `process_data':
file2.c:(.text+0x0): multiple definition of `process_data'
file1.o:file1.c:(.text+0x0): first defined here
```

Якщо зробити функції `static`, кожна матиме internal linkage і буде видима тільки в межах свого translation unit. Linker не побачить конфлікту, бо internal symbols не експортуються.

У C++ ситуація складніша через name mangling. Компілятор додає інформацію про тип до імені функції, тому `void process(int)` і `void process(double)` мають різні mangled names. Але якщо сигнатури однакові, ODR (One Definition Rule) порушується, і linker все одно видасть duplicate symbol.

У C є виняток для `inline` функцій у header files: якщо `inline` функція визначена в header і включена в кілька translation units, linker обере одну визначення (зазвичай з найбільш оптимізованим кодом). Але це працює тільки для `inline`, не для звичайних функцій.

### Симптом

Linker error: `multiple definition of 'function_name'` або `duplicate symbol: _function_name`.

### Чому це стається

Два translation units визначають non-`static` функцію з однаковим ім'ям. Компілятор не перевіряє це на етапі компіляції окремого файлу, але linker бачить два global symbols і не може вирішити, який використовувати.

### Як цього уникнути

- Використовуйте `static` для функцій, які потрібні тільки в одному файлі
- Для header-only бібліотек використовуйте `inline` або `static inline`
- У C++ використовуйте anonymous namespaces замість `static` для internal linkage
- Перевіряйте, чи не визначаєте функцію в header file без `inline`
