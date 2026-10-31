---
id: emb-irq-0012
title: "Що таке interrupt vector і як він відрізняється між MCU startup code та Linux kernel?"
track: embedded
section: interrupts-and-timing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: cmsis-core-nvic
    title: "CMSIS-Core (Cortex-M): Interrupts and Exceptions (NVIC)"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__NVIC__gr.html
  - source_id: armv7m-arm
    title: "ARMv7-M Architecture Reference Manual"
    url: https://developer.arm.com/documentation/ddi0403/latest/
  - source_id: linux-kernel-irq
    title: "Linux Kernel IRQ Handling"
    url: https://docs.kernel.org/core-api/genericirq.html
  - source_id: linux-x86-irq-vectors
    title: "Linux kernel source: arch/x86/include/asm/irq_vectors.h"
    url: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/arch/x86/include/asm/irq_vectors.h
  - source_id: linux-kernel-hacking
    title: "Linux kernel documentation: Unreliable Guide To Hacking The Linux Kernel"
    url: https://docs.kernel.org/kernel-hacking/hacking.html
---

## Short answer

На MCU **interrupt vector table** зазвичай лежить за фіксованою адресою і містить initial stack pointer та addresses handlers. Startup code задає weak default handlers, а firmware замінює потрібні ISR. У Linux hardware interrupt routing прихований за architecture/kernel IRQ subsystem: driver реєструє handler через kernel API, а не редагує startup vector table напряму.[^dou-embedded-interview]

## Detailed explanation

Вектор переривання (Interrupt Vector) – це адреса точки входу функції-обробника (ISR) або інструкція безумовного переходу, яку процесор апаратно завантажує під час виникнення винятку або сигналу переривання. Таблиця векторів (Vector Table) формує єдиний реєстр, що пов’язує апаратні та системні події з їхнім програмним кодом обробки.

Хоча призначення вектора є спільним для всіх обчислювальних платформ, підходи до його конфігурації кардинально відрізняються між мікроконтролерами (bare-metal) та операційними системами загального призначення (наприклад, Linux).

### Організація векторів у MCU: статичне зв’язування та startup-файл

У мікроконтролерах із ядром ARM Cortex-M контролер переривань (NVIC) тісно інтегрований у ядро, а таблиця векторів формується статично на етапі компіляції та лінкування:[^armv7m-arm]
1. **Структура в пам’яті:** таблиця векторів розміщується за фіксованою фізичною адресою пам’яті (за замовчуванням `0x00000000` або `0x08000000` у Flash-пам’яті). Перший 32-бітний елемент – початкове значення stack pointer, далі йдуть 32-бітні адреси обробників винятків ядра, а після них – обробників переривань конкретного чипа.[^cmsis-core-nvic]
2. **Асемблерний startup-файл (`startup_*.s` або `.c`):**
   - У startup-файлі таблиця векторів описується як послідовний масив адрес у виділеній секції компонувальника (наприклад, `.isr_vector`).
   - Усі обробники оголошуються зі слабким атрибутом (`[WEAK]`), що вказує на спільний обробник за замовчуванням (`Default_Handler` – зазвичай порожній нескінченний цикл):
     ```c
     void Default_Handler(void) { while (1); }
     void USART1_IRQHandler(void) __attribute__((weak, alias("Default_Handler")));
     ```
   - Якщо розробник реалізує у своєму коді функцію `void USART1_IRQHandler(void)`, компонувальник замінює адресу слабкої заглушки в таблиці векторів на адресу користувацької функції.
3. **Релокація через VTOR:** ядра ARMv7-M (Cortex-M3/M4/M7) дозволяють під час виконання змінити базову адресу таблиці за допомогою регістра `SCB->VTOR`. Це використовується при переході з bootloader у головну програму або для перенесення таблиці в SRAM для усунення Flash wait states.[^armv7m-arm] В ARMv6-M це не гарантовано: CMSIS-функція `NVIC_SetVector()`, що змінює вектор у таблиці, позначена як недоступна для Cortex-M0[^cmsis-core-nvic], а в Cortex-M0+ регістр VTOR опційний і його наявність у конкретному чипі задає макрос `__VTOR_PRESENT`.

### Організація переривань у Linux Kernel: динамічна диспетчеризація

В архітектурах прикладного рівня з блоком керування пам’яттю MMU (наприклад, ARM Cortex-A або x86_64) драйвери периферії ніколи не взаємодіють із апаратною таблицею векторів безпосередньо:[^linux-kernel-irq]
1. **Архітектурна таблиця винятків:** у 32-бітному ARM апаратна таблиця процесора містить лише кілька фіксованих точок входу (Reset, Undefined Instruction, Supervisor Call/SVC, Prefetch Abort, Data Abort, IRQ, FIQ). Усі периферійні переривання надходять на одну спільну точку входу процесора – вектор `IRQ`. На x86-64 устрій інший: IDT має 256 входів, вектори 0–31 відведено під винятки, а переривання пристроїв отримують окремі вектори, починаючи з 32.[^linux-x86-irq-vectors] Але й там драйвер не записує нічого в IDT сам, а реєструє обробник через загальну підсистему IRQ.
2. **Підсистема Generic IRQ:**
   - Коли процесор отримує сигнал `IRQ`, він переходить у режим ядра і викликає центральний низькорівневий асемблерний диспетчер.
   - Диспетчер звертається до зовнішнього контролера переривань (наприклад, ARM GIC – Generic Interrupt Controller), вичитує апаратний номер лінії переривання (Hardware IRQ number, `hwirq`) і транслює його у віртуальний номер переривання ядра (`irq`) за допомогою підсистеми доменів переривань (`irq_domain`).
3. **Динамічна реєстрація драйверами:**
   - Драйвер пристрою під час завантаження або зв’язування з деревом пристроїв (Device Tree) викликає функцію `request_irq()` або її керований варіант `devm_request_irq()` (для threaded IRQ – `request_threaded_irq()` чи `devm_request_threaded_irq()`):[^linux-kernel-irq]
     ```c
     int devm_request_irq(struct device *dev, unsigned int irq,
                          irq_handler_t handler, unsigned long irqflags,
                          const char *devname, void *dev_id);
     ```
   - Ядро тримає для кожного номера дескриптор `struct irq_desc`, а зареєстровані обробники – ланцюжком `struct irqaction` (поле `next` вказує на наступний обробник для shared interrupts), що дозволяє кільком пристроям розділяти одну фізичну лінію переривання (прапорець `IRQF_SHARED`).[^linux-kernel-irq]
4. **Розділена модель обробки (Top-half / Bottom-half):**
   - Обробку переривання в Linux зазвичай ділять на первинний обробник (Hard IRQ / Top-half), який виконується з вимкненими перериваннями і тому має бути швидким (часто лише підтверджує переривання і планує подальшу роботу), та відкладену обробку.[^linux-kernel-hacking] Softirq і tasklet виконуються в контексті software interrupt, а не в контексті потоку, і засинати там не можна.[^linux-kernel-hacking] Workqueue і threaded IRQ виконуються в потоках ядра, де засинати дозволено: для threaded IRQ первинний обробник лише повертає `IRQ_WAKE_THREAD`, і ядро будить окремий handler thread.[^linux-kernel-irq]

### Ключові відмінності

- **Фіксація точки входу:** У MCU кожна периферійна лінія має індивідуальний вектор безпосередньо в апаратній таблиці, і процесор апаратно викликає функцію без програмної диспетчеризації. У Linux на ARM апаратний вектор IRQ спільний, а конкретний драйвер визначається програмно ядром за номером з контролера GIC.
- **Момент зв’язування:** На MCU адреса закріплюється на етапі лінкування (link-time), тоді як у Linux прив’язка відбувається динамічно під час завантаження модуля або ініціалізації драйвера (runtime).
