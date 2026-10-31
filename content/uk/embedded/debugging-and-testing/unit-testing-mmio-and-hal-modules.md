---
id: emb-testemb-0006
title: "Як написати unit test для модуля, який працює з MMIO-регістрами або HAL-драйвером?"
track: embedded
section: debugging-and-testing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-testing
    title: "Zephyr Project documentation: Testing"
    url: https://docs.zephyrproject.org/latest/develop/test/index.html
  - source_id: cmsis-core-peripheral-access
    title: "CMSIS-Core (Cortex-M): Peripheral Access"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__peripheral__gr.html
  - source_id: gcc-volatiles
    title: "GCC manual: When is a Volatile Object Accessed?"
    url: https://gcc.gnu.org/onlinedocs/gcc/Volatiles.html
  - source_id: zephyr-ztest
    title: "Zephyr Project documentation: Test Framework (Ztest)"
    url: https://docs.zephyrproject.org/latest/develop/test/ztest.html
---

## Short answer

Винеси доступ до регістрів/HAL за тонкий interface або fake register block, а бізнес-логіку тестуй на host. У тесті перевіряй, які bits записані, у якій послідовності, як обробляються flags, timeout і помилки. <span class="warn">Не тестуй реальний MMIO pointer на host напряму; заміни `volatile` register access контрольованим fake/shim шаром.</span>[^dou-embedded-interview]

## Detailed explanation

Модуль, що звертається до регістрів, на host не запуститься як є: адреса периферії на MCU – фіксована фізична адреса, і розіменування такого вказівника на ПК закінчиться аварією процесу або записом у випадкову пам’ять. Тому головне рішення приймають ще під час проєктування коду: доступ до заліза має проходити через шов (seam), у який тест може підставити контрольовану заміну.

### Підхід 1: передати блок регістрів як параметр

CMSIS описує периферію як `typedef struct` з полями-регістрами, а конкретний екземпляр – як макрос, що приводить базову адресу до вказівника на цю структуру, наприклад `#define LPC_UART2 ((LPC_UART_TypeDef *) LPC_UART2_BASE)`.[^cmsis-core-peripheral-access] Якщо драйвер не звертається до макроса напряму, а отримує вказівник на структуру як параметр (або через контекст драйвера), то у firmware передають справжню адресу, а в тесті – звичайну змінну в RAM.

```c
#include <assert.h>
#include <stdint.h>

typedef struct {
    volatile uint32_t SR;   /* bit 0: READY, set by hardware */
    volatile uint32_t CR;   /* bit 0: START */
    volatile uint32_t DR;   /* 12-bit result */
} adc_regs_t;

#define ADC_SR_READY (1u << 0)
#define ADC_CR_START (1u << 0)

int adc_read(adc_regs_t *regs, uint32_t max_polls, uint16_t *out)
{
    regs->CR = ADC_CR_START;
    while ((regs->SR & ADC_SR_READY) == 0u) {
        if (max_polls == 0u) {
            return -1;                      /* timeout path */
        }
        max_polls--;
    }
    *out = (uint16_t)(regs->DR & 0xFFFu);
    return 0;
}

/* Host test: the register block is ordinary RAM. */
static adc_regs_t fake;

int main(void)
{
    uint16_t value = 0;

    fake.SR = 0u;                           /* READY never comes */
    assert(adc_read(&fake, 10u, &value) == -1);
    assert(fake.CR == ADC_CR_START);        /* conversion was started */

    fake.SR = ADC_SR_READY;                 /* conversion already finished */
    fake.DR = 0xABCDu;
    assert(adc_read(&fake, 10u, &value) == 0);
    assert(value == 0xBCDu);                /* only the low 12 bits */
    return 0;
}
```

У firmware виклик виглядає як `adc_read((adc_regs_t *)ADC1_BASE, 1000u, &v)`. Поля залишаються `volatile`: за документацією GCC, volatile-об’єкти використовують для доступу до hardware, і реалізація не може переставляти чи об’єднувати volatile-доступи через sequence point.[^gcc-volatiles] Там само зазначено, що volatile bit-fields для регістрів використовувати небажано, тому маски бітів надійніші за bit-field структури.

### Обмеження фейкового блоку регістрів

Звичайна пам’ять не відтворює апаратних side effects: прапорець не встановиться сам посеред циклу очікування, біт write-1-to-clear не скинеться записом одиниці, а читання data-регістра не очистить статус. Тест вище обходить це, задаючи стан наперед. Якщо потрібно перевірити саме послідовність доступів (наприклад, «спочатку ввімкнути clock, потім записати конфігурацію, потім enable»), регістровий доступ виносять у функції `reg_read()`/`reg_write()`, а в тесті підставляють реалізацію, яка записує журнал операцій і може змінювати значення після N-го читання. Тоді тест перевіряє не лише кінцевий стан, а й порядок записів.

### Підхід 2: mock на межі HAL

Якщо модуль працює з HAL або драйверним API, шов проходить по функціях: тест підміняє `hal_spi_transfer()` чи `i2c_write()` fake-реалізацією, перевіряє кількість викликів і аргументи та повертає помилку, щоб пройти гілки error handling. У Zephyr для цього інтегровано FFF (Fake Function Framework), а Zephyr містить готові fake-драйвери, які працюють як stubs або як mocks. Pseudo-board `unit_testing` збирає модуль host-toolchain у звичайний виконуваний файл без ядра Zephyr, тож відсутні функції ядра теж доводиться підмінювати stubs.[^zephyr-ztest]

### Що саме перевіряти

- які біти записані в які регістри і в якій послідовності;
- реакцію на прапорці помилок (overrun, NACK, CRC) і на timeout, коли прапорець так і не з’явився;
- граничні значення: маскування результату, переповнення лічильників, максимальна довжина буфера;
- що драйвер не чіпає чужі біти в спільному регістрі.

### Типові помилки

Mock, що повторює реалізацію рядок за рядком, перевіряє сам себе: тест ламається від будь-якого рефакторингу і не ловить нових дефектів. Mock HAL, написаний за уявленням автора, може поводитися інакше за справжній драйвер, тому host-тести доповнюють тестами на target (qid:emb-testemb-0002). І нарешті, гілки timeout неможливо перевірити, якщо цикл очікування не має межі: це сигнал змінити код, а не тест.
