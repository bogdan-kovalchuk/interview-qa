---
id: emb-testemb-0001
title: "Як code review для firmware відрізняється від code review звичайного application-коду?"
track: embedded
section: debugging-and-testing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-testing
    title: "Zephyr Project documentation: Testing"
    url: https://docs.zephyrproject.org/latest/develop/test/index.html
  - source_id: gcc-volatiles
    title: "GCC manual: When is a Volatile Object Accessed?"
    url: https://gcc.gnu.org/onlinedocs/gcc/Volatiles.html
  - source_id: cmsis-core-dcache
    title: "CMSIS-Core (Cortex-M): D-Cache Functions"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__Dcache__functions__m7.html
  - source_id: gcc-developer-options
    title: "GCC manual: GCC Developer Options (-fstack-usage)"
    url: https://gcc.gnu.org/onlinedocs/gcc/Developer-Options.html
  - source_id: zephyr-coding-guidelines
    title: "Zephyr Project documentation: Coding Guidelines"
    url: https://docs.zephyrproject.org/latest/contribute/coding_guidelines/index.html
  - source_id: misra-compliance-2020
    title: "MISRA Compliance:2020 – Achieving compliance with MISRA Coding Guidelines"
    url: https://misra.org.uk/app/uploads/2021/06/MISRA-Compliance-2020.pdf
---

## Short answer

**Firmware review** перевіряє не лише логіку, а й взаємодію з MCU: регістри, ISR, DMA, clock/reset, timing, memory layout і power states. Окремо дивляться на undefined behavior, volatile/MMIO, concurrency між ISR і tasks, stack/heap budget, error paths і fail-safe стани. <span class="warn">Код, який виглядає коректно як application logic, може ламати hardware через race, неправильний register sequence або timing.</span>[^dou-embedded-interview]

## Detailed explanation

Review звичайного application-коду здебільшого перевіряє логіку, API, читабельність і тести. У firmware до цього додається контракт із фізичним світом: код пише в регістри, ділить дані з ISR і DMA, працює в обмеженій пам’яті без MMU і мусить залишати hardware в безпечному стані, коли щось пішло не так. Помилки цього класу часто не видно ані в unit tests на PC, ані в нормальному сценарії на столі, тому reviewer свідомо шукає їх за окремим чеклистом.

### Доступ до регістрів: volatile, послідовність, side effects

`volatile` потрібен для об’єктів, що змінюються поза програмою, але він не робить з доступу бар’єр пам’яті. Документація GCC прямо каже, що доступи до non-volatile об’єктів не впорядковані відносно volatile-доступів, тож запис у звичайний буфер може ще не відбутися на момент запису в volatile-регістр; для такої гарантії потрібен явний memory barrier. Там же сказано, що volatile bit-fields небажано використовувати для hardware, бо такі поля можуть неявно читатися під час запису або під час доступу до сусідніх полів.[^gcc-volatiles]

Типові знахідки review в цьому блоці:

- регістр використовують до ввімкнення його clock або до виходу периферії з reset;
- порушено порядок кроків із reference manual (unlock, конфігурація, enable);
- read-modify-write регістра, у якому є біти write-1-to-clear: усі прапорці, що читалися як 1, будуть записані назад одиницями й скинуться разом із потрібним.

```c
#define UART_SR_ORE (1u << 3)   /* status bits are write-1-to-clear */

UART->SR |= UART_SR_ORE;        /* wrong: writes back and clears every pending flag */
UART->SR  = UART_SR_ORE;        /* right: clears only the overrun flag */
```

### Concurrency: ISR, tasks, DMA і cache

`volatile` не дає атомарності. Інкремент лічильника, який змінюють і task, і ISR, – це read-modify-write; якщо переривання стається між читанням і записом, одне оновлення губиться. Reviewer шукає кожну змінну, спільну для ISR і task, і питає, чим захищено доступ: critical section, atomic-операція або передача через чергу або кільцевий буфер з одним writer.

DMA додає ще одного «автора» пам’яті. На ядрах із data cache (наприклад, Cortex-M7) буфер перед передачею через DMA треба очистити з cache (clean), а після прийому інвалідувати. CMSIS-функції `SCB_CleanDCache_by_Addr()` і `SCB_InvalidateDCache_by_Addr()` працюють з адресою, вирівняною на межу 32 байтів,[^cmsis-core-dcache] тому reviewer перевіряє вирівнювання й розмір DMA-буферів: якщо буфер ділить рядок cache з іншими змінними, інвалідація може стерти їхні свіжі записи.

### Ресурси: stack, heap, час

Без MMU переповнення stack мовчки псує сусідню пам’ять. GCC з `-fstack-usage` видає розмір кадру stack для кожної функції окремо;[^gcc-developer-options] щоб оцінити найгірший випадок, ці числа складають уздовж call graph і додають запас на вкладені переривання. У review звертають увагу на великі локальні масиви, рекурсію, `printf` у глибокому стеку викликів і динамічне виділення пам’яті після старту (фрагментація heap проявляється через дні роботи).

Щодо часу: чи немає блокувальних викликів або довгих циклів в ISR, чи кожне очікування апаратного прапорця має timeout і гілку помилки, чи не залежить коректність від швидкості CPU.

### Error paths і безпечний стан

Для кожної апаратної помилки (timeout шини, NACK, CRC, brown-out) має бути відповідь на питання «що робить система далі». Виходи, що керують навантаженням, мають переходити в безпечний стан, а watchdog годують лише після перевірки стану системи, а не з таймерного переривання (див. qid:emb-safety-0001).

### Правила та інструменти

Багато firmware-команд фіксують підмножину MISRA C; наприклад, правила кодування Zephyr базуються на MISRA C:2012 і обов’язкові для нового коду.[^zephyr-coding-guidelines] Механічні правила перевіряє static analysis у CI (qid:emb-testemb-0007), а людина на review зосереджується на тому, чого інструмент не вирішить. MISRA Compliance:2020 пояснює, що частина правил є undecidable: якщо порушення залежить від значень під час виконання, інструмент може відповісти лише «можливо», а відсутність diagnostic не означає відповідності.[^misra-compliance-2020]

### Що хоче почути інтерв’юер

Що firmware review – це не лише стиль і логіка, а перевірка взаємодії з hardware: послідовність і семантика регістрів, гонки з ISR і DMA, межі пам’яті й часу, поведінка при відмовах. Сильна відповідь показує розподіл праці: компілятор і аналізатори ловлять механічні порушення, review – архітектурні рішення, timing і safety-наслідки, а тести на target підтверджують те, що неможливо побачити в коді.
