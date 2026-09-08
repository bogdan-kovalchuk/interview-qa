---
id: emb-build-0013
title: "Як працюють make і Makefile у firmware-проекті?"
description: "make порівнює targets і dependencies у Makefile та виконує лише потрібні кроки компіляції, link і post-build."
track: embedded
section: toolchain-and-build
level: middle
type: concept
tags: []
status: published
updated: 2026-09-08
content_revision: 4
reconciled_with:
  en: 4
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження цього питання й відповіді; текст відповіді не перевірений незалежно від оригінальної Anki-колоди спільноти."
  - source_id: gcc-overall-options
    title: "GCC manual: Options Controlling the Kind of Output"
    url: https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Авторитетне джерело рівня секції для понять розділу toolchain-and-build; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

`make` читає targets, dependencies і recipes з `Makefile`. Якщо source новіший за object або binary, виконується потрібна команда компіляції, link чи post-build. У firmware Makefile часто задає MCU flags, include paths, linker script, output `.elf/.hex/.bin` і flash/debug targets.[^dou-embedded-interview]

## Detailed explanation

`make` – це build automation tool, який читає `Makefile` і виконує команди для побудови target-ів.[^gcc-overall-options]

**Структура Makefile**:
```makefile
# target: dependencies
# \trecipe (command)
firmware.elf: main.o utils.o
\tarm-none-eabi-gcc -T linker.ld -o firmware.elf main.o utils.o

main.o: main.c main.h
\tarm-none-eabi-gcc -c -mcpu=cortex-m4 main.c -o main.o

utils.o: utils.c utils.h
\tarm-none-eabi-gcc -c -mcpu=cortex-m4 utils.c -o utils.o
```

**Як працює make**:
1. Читає target (наприклад, `firmware.elf`)
2. Перевіряє dependencies (`main.o`, `utils.o`)
3. Для кожної dependency рекурсивно перевіряє її dependencies
4. Порівнює timestamps: якщо source новіший за object, виконує recipe
5. Виконує recipe (команди з `\t` на початку)

**Variables у Makefile**:
```makefile
CC = arm-none-eabi-gcc
CFLAGS = -mcpu=cortex-m4 -mthumb -O2
LDFLAGS = -T linker.ld
SRCS = main.c utils.c
OBJS = $(SRCS:.c=.o)

firmware.elf: $(OBJS)
\t$(CC) $(LDFLAGS) -o $@ $^

%.o: %.c
\t$(CC) $(CFLAGS) -c $< -o $@
```

**Pattern rules** (`%.o: %.c`) дозволяють задати правило для всіх `.c` файлів.

**Phony targets** (не файли, а дії):
```makefile
.PHONY: clean flash debug

clean:
\trm -f *.o firmware.elf firmware.hex

flash: firmware.hex
\tst-flash write firmware.hex 0x8000000

debug: firmware.elf
\tarm-none-eabi-gdb firmware.elf
```

**Включення інших Makefile**:
```makefile
include common.mk
include $(wildcard modules/*.mk)
```

**Автоматичні dependencies** (генерується з `-MMD -MP`):
```makefile
-include $(OBJS:.o=.d)
```

## Evaluation guide

### Expected signals
- Розуміє структуру Makefile (target, dependencies, recipe)
- Знає, як make визначає, що потрібно переробити
- Може пояснити variables і pattern rules
- Розуміє phony targets і їх використання

### Red flags
- Не знає різниці між target і dependency
- Не розуміє, як make порівнює timestamps
- Не може написати простий Makefile
- Не знає, що таке phony targets

### Level-up follow-up
- Як автоматично генерувати dependencies для header files?
- Як організувати multi-directory проект з Makefile?
- Як інтегрувати CMake з Makefile?

## Sources

<!-- generated from frontmatter -->
