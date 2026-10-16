---
id: emb-build-0013
title: "How do make and Makefiles work in a firmware project?"
track: embedded
section: toolchain-and-build
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gcc-overall-options
    title: "GCC manual: Options Controlling the Kind of Output"
    url: https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html
---

## Short answer

`make` reads targets, dependencies, and recipes from the `Makefile`. If a source is newer than its object or binary, the required compile, link, or post-build command runs. In firmware, a Makefile typically defines MCU flags, include paths, a linker script, `.elf/.hex/.bin` outputs, and flash/debug targets.[^dou-embedded-interview]

## Detailed explanation

`make` is a build automation tool that reads a `Makefile` and executes commands to build targets.[^gcc-overall-options]

**Makefile structure**:
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

**How make works**:
1. Reads a target (e.g., `firmware.elf`)
2. Checks dependencies (`main.o`, `utils.o`)
3. For each dependency, recursively checks its dependencies
4. Compares timestamps: if a source is newer than the object, it runs the recipe
5. Executes the recipe (commands starting with `\t`)

**Variables in Makefile**:
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

**Pattern rules** (`%.o: %.c`) allow you to define a rule for all `.c` files.

**Phony targets** (not files, but actions):
```makefile
.PHONY: clean flash debug

clean:
\trm -f *.o firmware.elf firmware.hex

flash: firmware.hex
\tst-flash write firmware.hex 0x8000000

debug: firmware.elf
\tarm-none-eabi-gdb firmware.elf
```

**Including other Makefiles**:
```makefile
include common.mk
include $(wildcard modules/*.mk)
```

**Automatic dependencies** (generated with `-MMD -MP`):
```makefile
-include $(OBJS:.o=.d)
```

### Expected signals

- Understands Makefile structure (target, dependencies, recipe)
- Knows how make determines what needs to be rebuilt
- Can explain variables and pattern rules
- Understands phony targets and their use

### Red flags

- Does not know the difference between target and dependency
- Does not understand how make compares timestamps
- Cannot write a simple Makefile
- Does not know what phony targets are

### Level-up follow-up

- How to automatically generate dependencies for header files?
- How to organize a multi-directory project with Makefile?
- How to integrate CMake with Makefile?
