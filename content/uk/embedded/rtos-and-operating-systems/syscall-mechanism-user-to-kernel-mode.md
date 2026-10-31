---
id: emb-fund-0003
title: "Що таке system call?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: ostep-limited-direct-execution
    title: "Arpaci-Dusseau, Operating Systems: Three Easy Pieces, ch. 6: Mechanism: Limited Direct Execution"
    url: https://pages.cs.wisc.edu/~remzi/OSTEP/cpu-mechanisms.pdf
  - source_id: linux-man-syscall
    title: "Linux manual page: syscall(2)"
    url: https://man7.org/linux/man-pages/man2/syscall.2.html
  - source_id: linux-man-syscalls
    title: "Linux manual page: syscalls(2)"
    url: https://man7.org/linux/man-pages/man2/syscalls.2.html
  - source_id: linux-x86-64-syscall-table
    title: "Linux kernel source: arch/x86/entry/syscalls/syscall_64.tbl"
    url: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/arch/x86/entry/syscalls/syscall_64.tbl
  - source_id: linux-man-vdso
    title: "Linux manual page: vdso(7)"
    url: https://man7.org/linux/man-pages/man7/vdso.7.html
  - source_id: zephyr-usermode-overview
    title: "Zephyr Project documentation: User Mode Overview"
    url: https://docs.zephyrproject.org/latest/kernel/usermode/overview.html
  - source_id: zephyr-syscalls
    title: "Zephyr Project documentation: System Calls"
    url: https://docs.zephyrproject.org/latest/kernel/usermode/syscalls.html
---

## Short answer

**System call (syscall)** – механізм запиту сервісів ядра з user-space.[^dou-embedded-interview] Оскільки user-space не має прямого доступу до апаратури та ресурсів ядра, програма виконує syscall для переходу в kernel mode.

Механізм (x86-64): програма поміщає номер syscall у `rax`, аргументи у `rdi/rsi/rdx...`, виконує інструкцію `syscall`. Ядро переключається в privileged mode, виконує обробник і повертає результат.

Забезпечує ізоляцію: user-space процеси не можуть пошкодити пам’ять ядра або інших процесів.

## Detailed explanation

### Навіщо потрібен окремий механізм

Процесор із підтримкою захисту має щонайменше два режими. Код у user mode обмежений: він не може, наприклад, напряму виконувати введення-виведення, а спроба зробити привілейовану операцію спричиняє виняток, після якого ОС зазвичай завершує процес. У kernel mode працює ядро, і там дозволено все, включно з привілейованими інструкціями. Системний виклик – це контрольований спосіб, яким ядро відкриває прикладним програмам ключові послуги: доступ до файлової системи, створення й знищення процесів, обмін між процесами, виділення пам’яті.[^ostep-limited-direct-execution]

Звичайний виклик функції так зробити не може: якби програма могла стрибнути на довільну адресу в ядрі, вона обійшла б будь-які перевірки прав.

### Що відбувається покроково

1. **Обгортка в C-бібліотеці.** `read()` чи `write()` у програмі – це звичайний виклик функції бібліотеки. Обгортка за домовленою з ядром конвенцією кладе аргументи і номер системного виклику у визначені регістри та виконує спеціальну trap-інструкцію.[^ostep-limited-direct-execution]
2. **Перехід у ядро.** Trap-інструкція одночасно передає керування в ядро і підвищує рівень привілеїв. Апаратура зберігає достатньо стану, щоб потім повернутися: на x86, наприклад, програмний лічильник, прапорці та кілька регістрів потрапляють на kernel stack цього процесу.[^ostep-limited-direct-execution]
3. **Вибір обробника за номером.** Адресу, куди перейти, задає не програма: ядро під час завантаження налаштовує таблицю обробників (trap table), а налаштування цієї таблиці – теж привілейована операція. Обробник перевіряє номер виклику і, якщо він коректний, виконує відповідний код. Саме цей рівень непрямості є захистом: user-код може лише попросити послугу за номером.[^ostep-limited-direct-execution]
4. **Перевірка аргументів і виконання.** Ядро зобов’язане з підозрою ставитися до всього, що передав user space. Якщо `write()` отримала адресу буфера, що вказує в пам’ять ядра, виклик має бути відхилено, інакше процес зміг би прочитати пам’ять ядра, а через неї – пам’ять інших процесів.[^ostep-limited-direct-execution] Під час виконання виклик може й заблокуватися (наприклад, `read()` із порожнього сокета), і тоді планувальник віддає процесор іншому потоку.
5. **Повернення.** Ядро виконує інструкцію повернення з trap, яка відновлює збережені регістри й знижує рівень привілеїв до user mode.[^ostep-limited-direct-execution] На архітектурах без окремого прапорця помилки ядро повертає від’ємний номер помилки; обгортка робить його додатним, записує в `errno` і повертає `-1`.[^linux-man-syscalls]

### Конкретні конвенції Linux

Кожна архітектура має власну інструкцію входу в ядро і власний розподіл регістрів:[^linux-man-syscall]

- **x86-64**: інструкція `syscall`, номер виклику в `eax`, результат у `rax`, аргументи в `rdi`, `rsi`, `rdx`, `r10`, `r8`, `r9`;
- **i386**: `int $0x80`, номер в `eax`, аргументи в `ebx`, `ecx`, `edx`, `esi`, `edi`, `ebp`;
- **arm64**: `svc #0`, номер у `w8`, аргументи в `x0`–`x5`, результат у `x0`;
- **arm/EABI**: `swi 0x0`, номер у `r7`, аргументи в `r0`–`r6`, результат у `r0`;
- **riscv**: `ecall`, номер в `a7`, аргументи в `a0`–`a5`, результат в `a0`.

Ці таблиці не описують конвенцію повністю: деякі архітектури можуть змінювати й інші регістри, не перелічені в них.[^linux-man-syscall] Номери теж залежать від архітектури: на x86-64 `write` має номер 1.[^linux-x86-64-syscall-table] Для виклику без готової обгортки glibc надає функцію `syscall()`; константа `SYS_write` розгортається в номер для тієї архітектури, під яку зібрано програму.

```c
#define _GNU_SOURCE
#include <sys/syscall.h>
#include <unistd.h>

int main(void)
{
    static const char msg[] = "hello\n";

    write(STDOUT_FILENO, msg, sizeof msg - 1);              /* glibc wrapper */
    syscall(SYS_write, STDOUT_FILENO, msg, sizeof msg - 1); /* same call by number */
    return 0;
}
```

### Ціна переходу і vDSO

Перехід між режимами не безкоштовний. Документація Linux прямо зазначає, що для частих викликів накладні витрати на вихід із user space і вхід у ядро можуть домінувати в продуктивності, а старий шлях `int $0x80` на 32-бітному x86 дорогий, бо проходить повну обробку переривання. Тому ядро відображає в кожен процес vDSO – невелику бібліотеку, через яку C-бібліотека виконує, наприклад, `clock_gettime` без входу в ядро.[^linux-man-vdso] Практичний висновок для embedded: не робіть системний виклик на кожен байт; групуйте дані у великі `read()`/`write()`.

### Системні виклики на мікроконтролерах

На платформах без MMU/MPU код ядра RTOS і застосунку виконується в одному спільному адресному просторі[^zephyr-introduction], тож виклик API ядра – це звичайний виклик функції. Якщо ж RTOS підтримує ізоляцію, з’являється той самий механізм. У Zephyr потоки user mode вважаються ненадійними, ізольовані від ядра й один від одного, а повернутися в supervisor mode вони можуть лише через визначені ядром системні виклики та обробники переривань.[^zephyr-usermode-overview] Кожен системний виклик Zephyr має функцію перевірки аргументів, яка обгортає реальну реалізацію; згенерована обгортка викликає реалізацію напряму, якщо код уже працює в supervisor mode, і проходить підвищення привілеїв та перевірку, якщо виклик зроблено з user mode.[^zephyr-syscalls]

### Що хоче почути інтерв’юер

Що системний виклик – це не просто функція, а контрольований перехід через trap-інструкцію з підвищенням привілеїв; що ядро обирає обробник за номером і перевіряє аргументи; що результат і помилка повертаються через регістр і `errno`; що конвенції залежать від архітектури; що перехід має ціну. Перелік основних викликів наведено в qid:emb-fund-0001.
