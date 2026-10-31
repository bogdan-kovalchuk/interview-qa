---
id: emb-rtos-0013
title: "Що таке task в RTOS і як він відрізняється від interrupt handler та bare-metal superloop?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: freertos-kernel-book
    title: "FreeRTOS Kernel Book and Reference Manual"
    url: https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book
---

## Short answer

**RTOS task** має власний stack, priority і scheduler-managed state. Interrupt handler виконується асинхронно в interrupt context, має бути коротким і не поводиться як звичайна task. Bare-metal superloop - один головний цикл без scheduler-а; concurrency там зазвичай будується на flags, ISR і state machines.[^dou-embedded-interview]

## Detailed explanation

Три поняття відповідають на одне питання – хто і коли виконує код, що реагує на події, – але з різними гарантіями щодо стеку, блокування й часу відгуку. Приклади нижче наведено для FreeRTOS на одноядерному MCU.

### RTOS task

Task у FreeRTOS – звичайна C-функція `void f(void *pvParameters)`, яка зазвичай містить нескінченний цикл і ніколи не повертається: вихід за межі функції заборонений, непотрібну задачу видаляють явно. З однієї функції можна створити кілька задач, і кожен екземпляр має **власний стек**, а отже й власні копії локальних змінних.[^freertos-kernel-book] Задача має пріоритет, призначений програмістом, і стан (Running, Ready, Blocked, Suspended), яким керує scheduler; детально – у qid:emb-rtos-0012. Головна властивість задачі – вона може **блокуватися**: чекати queue, semaphore чи таймаут, не витрачаючи CPU, і її може витіснити задача вищого пріоритету.

### Interrupt handler (ISR)

ISR хоч і написаний у програмному коді, але є апаратною сутністю: яка ISR і коли запуститься, вирішує апаратура, а не scheduler. Задачі виконуються лише тоді, коли не виконується жодна ISR, тож навіть переривання найнижчого пріоритету перериває задачу найвищого пріоритету, а задача не може витіснити ISR.[^freertos-kernel-book] Пріоритет задачі і пріоритет переривання – різні шкали, які не можна порівнювати напряму.

З цього випливають обмеження:

- ISR не може заблокуватися, бо немає задачі, яку можна перевести в Blocked. Тому з ISR можна викликати лише функції FreeRTOS із суфіксом `FromISR`.[^freertos-kernel-book]
- ISR має бути коротким: поки він виконується, задачі стоять, він вносить jitter у час старту й виконання задач, а залежно від архітектури нові переривання можуть бути частково чи повністю заблоковані.[^freertos-kernel-book]
- Типовий шаблон – **deferred interrupt processing**: ISR фіксує причину переривання, знімає прапорець і будить задачу, а основна обробка виконується в задачі, де доступний увесь API і пріоритет можна вибирати відносно інших задач. Якщо пріоритет цієї задачі найвищий, обробка почнеться одразу після виходу з ISR, ніби вона виконувалася в самому ISR.[^freertos-kernel-book]

```c
static TaskHandle_t rx_task;

void USART1_IRQHandler(void)
{
    BaseType_t woken = pdFALSE;

    /* read the status, clear the flag, push the byte into a buffer */
    vTaskNotifyGiveFromISR(rx_task, &woken);
    portYIELD_FROM_ISR(woken);       /* switch now if rx_task outranks the interrupted task */
}

static void rx_task_fn(void *arg)
{
    for (;;) {
        ulTaskNotifyTake(pdTRUE, portMAX_DELAY);   /* Blocked, no CPU used */
        handle_rx();
    }
}
```

`vTaskNotifyGiveFromISR()` і `ulTaskNotifyTake()` – легший за binary semaphore спосіб розбудити одну задачу з ISR.[^freertos-kernel-book] Способи безпечно передати дані з ISR у задачу – у qid:emb-irq-0009.

### Bare-metal superloop

Superloop – один нескінченний цикл у `main()` без scheduler-а. Події приходять через ISR, які виставляють прапорці або кладуть дані в буфер, а цикл по черзі опитує прапорці й викликає обробники; складну поведінку будують на state machines.

```c
static volatile bool rx_ready;

void USART1_IRQHandler(void)
{
    /* read the status, clear the flag, push the byte into a ring buffer */
    rx_ready = true;
}

int main(void)
{
    init_hardware();
    for (;;) {
        if (rx_ready) {
            rx_ready = false;     /* clear first: a new IRQ during handling is not lost */
            handle_rx();
        }
        update_display();         /* every step adds to the worst-case reaction time */
        poll_buttons();
    }
}
```

Прапорець тут означає лише «є нові дані», а самі байти лежать у ring buffer, тож кілька переривань між перевірками не губляться (шаблон SPSC-буфера – qid:emb-patterns-0007). Ключова властивість superloop: найгірший час реакції на подію приблизно дорівнює сумі найгірших часів виконання всіх кроків циклу. Довгий `update_display()` затримує обробку `rx_ready`, і виправити це можна лише перебудовою коду (розбити роботу на короткі кроки state machine), а не зміною пріоритету.

### Порівняння

- **Стек:** у кожної задачі власний стек, розмір якого треба оцінити; у superloop один стек; ISR використовує стек перерваного коду або окремий стек обробників, залежно від архітектури й порту RTOS, і це треба врахувати, оцінюючи запас стеку.
- **Блокування:** задача може чекати подію без витрати CPU; ISR не може блокуватися взагалі; superloop не блокується, а опитує.
- **Хто вирішує, що виконується:** для ISR – контролер переривань і апаратні пріоритети; для задач – scheduler і програмні пріоритети; у superloop – порядок рядків у циклі.
- **Час реакції:** ISR – найменший; задача високого пріоритету – час ISR плюс context switch; superloop – залежить від тривалості всього циклу.
- **Спільні дані:** у всіх трьох моделях дані, які ділять ISR і решта коду, потребують захисту (критична секція, атомарний доступ, lock-free буфер).

### Коли що доречно

Книга FreeRTOS прямо визнає, що для простих систем добре відомі техніки без багатозадачного ядра можуть бути найкращим рішенням, а межа, де RTOS стає вигіднішим, суб’єктивна. Аргументи на користь RTOS: повністю подієво-кероване виконання без опитування, абстракція часу через API, модульність задач, Idle task для енергозбереження і можливість змішувати періодичну, безперервну та подієву обробку з різними пріоритетами. Ціна – обробка tick, перемикання контексту, пам’ять під стеки задач.[^freertos-kernel-book] На співбесіді сильна відповідь пов’язує вибір з вимогами до latency, кількістю незалежних активностей і обсягом RAM, а не з тим, що RTOS «сучасніший».
