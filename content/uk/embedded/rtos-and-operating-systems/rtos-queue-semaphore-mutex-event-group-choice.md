---
id: emb-rtos-0014
title: "Які synchronization primitives є в RTOS і коли використовувати queue, semaphore, mutex або event group?"
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

**Queue** передає дані між ISR/tasks або tasks, **semaphore** сигналізує подію чи рахує ресурси. **Mutex** захищає shared resource і бажано має пріоритетне успадкування (priority inheritance). **Event group** зручний для набору flags, коли task чекає одну або кілька умов.[^dou-embedded-interview]

## Detailed explanation

Вибір примітиву визначається тим, **що саме** передається між задачами: дані, факт події, кількість, право доступу до ресурсу чи комбінація умов. Нижче – на прикладі FreeRTOS; в інших RTOS назви й деталі відрізняються, але розподіл ролей той самий.

### Queue – передати дані

Queue зберігає скінченну кількість елементів фіксованого розміру; і довжину, і розмір елемента задають при створенні. Зазвичай це FIFO, але можна писати й у голову черги. FreeRTOS копіює дані в чергу байт за байтом, тож відправник може одразу повторно використати змінну, навіть локальну на стеку, а відправник і отримувач не мусять домовлятися, хто володіє даними.[^freertos-kernel-book]

- Писати в чергу й читати з неї можуть будь-які задачі та ISR; на практиці часто буває кілька писачів і один читач.[^freertos-kernel-book]
- Читач може заблокуватися з таймаутом, поки черга порожня, а писач – поки вона повна. Якщо на черзі чекають кілька задач, розблоковується задача з найвищим пріоритетом, а серед рівних – та, що чекає найдовше.[^freertos-kernel-book]
- Для великих даних передають указівник, але тоді треба чітко визначити власника пам’яті й гарантувати, що вона лишається дійсною; указівник на дані зі стеку задачі передавати не можна.[^freertos-kernel-book]

### Binary semaphore – повідомити про подію

Binary semaphore можна уявити як чергу довжиною 1 без даних: вона або порожня, або повна. Класичне застосування – синхронізація задачі з перериванням: задача блокується на `xSemaphoreTake()`, ISR робить `xSemaphoreGiveFromISR()`, і основна обробка переходить у задачу.[^freertos-kernel-book] Семафор, використаний для синхронізації, зазвичай не повертають: той, хто «дає», і той, хто «бере», – різні сторони.

### Counting semaphore – рахувати

Counting semaphore – черга довжиною більше одиниці, де важлива лише кількість елементів. Два типові застосування: **підрахунок подій** (початкове значення 0, кожна подія збільшує лічильник, кожна обробка зменшує, тож події не губляться, якщо приходять швидше, ніж їх обробляють) і **керування пулом ресурсів** (початкове значення дорівнює кількості ресурсів, наприклад буферів DMA).[^freertos-kernel-book]

### Mutex – захистити спільний ресурс

Mutex – особливий binary semaphore для взаємного виключення: задача бере «токен», працює з ресурсом і обов’язково повертає його. Ключова відмінність від binary semaphore – вбудований базовий механізм **priority inheritance**: власник mutex-а тимчасово отримує пріоритет найвищої задачі, що на нього чекає. Це обмежує тривалість priority inversion, але не усуває її і ускладнює аналіз таймінгів.[^freertos-kernel-book] Через вплив на пріоритети задач mutex не можна використовувати з ISR.[^freertos-kernel-book]

```c
static SemaphoreHandle_t i2c_lock;   /* created once with xSemaphoreCreateMutex() */

bool sensor_read(uint8_t reg, uint8_t *val)
{
    if (xSemaphoreTake(i2c_lock, pdMS_TO_TICKS(20)) != pdTRUE)
        return false;                /* timeout: report it, it may be a deadlock */
    bool ok = i2c_read_reg(SENSOR_ADDR, reg, val);
    xSemaphoreGive(i2c_lock);        /* the task that took it gives it back */
    return ok;
}
```

Таймаут тут свідомий: FreeRTOS радить не чекати mutex безкінечно, а брати таймаут трохи довший за очікуваний максимум, щоб неотримання mutex-а сигналізувало про помилку дизайну, зокрема deadlock (qid:emb-rtos-0004).[^freertos-kernel-book] Якщо та сама задача може повторно взяти mutex (наприклад, через бібліотечну функцію), потрібен recursive mutex, інакше задача заблокує сама себе. Альтернатива mutex-у – **gatekeeper task**, єдина задача, яка володіє ресурсом, а решта звертаються до неї через чергу; так зникають і priority inversion, і deadlock.[^freertos-kernel-book] Для дуже коротких операцій (кілька інструкцій над регістром) замість mutex використовують критичну секцію.

### Event group – дочекатися комбінації умов

Event group – набір бітів-прапорців, значення яких визначає застосунок. На відміну від queue і semaphore, задача може чекати будь-який або всі з кількох бітів, а коли умову виконано, розблоковуються **всі** задачі, що на неї чекали. Звідси типові застосування: broadcast події кільком задачам, очікування кількох незалежних готовностей, синхронізація групи задач, а також заміна кількох binary semaphores однією event group для економії RAM.[^freertos-kernel-book] Кількість бітів залежить від ширини типу tick: 24 біти при 32-бітному tick, 8 – при 16-бітному, 56 – при 64-бітному.[^freertos-kernel-book]

```c
#define WIFI_UP   (1u << 0)
#define TIME_SYNC (1u << 1)

EventBits_t bits = xEventGroupWaitBits(sys_events, WIFI_UP | TIME_SYNC,
                                       pdFALSE,  /* keep the bits set on exit */
                                       pdTRUE,   /* wait for all of them */
                                       portMAX_DELAY);
```

Важлива пастка: встановлення бітів – недетермінована операція, бо невідомо, скільки задач розблокується. Тому `xEventGroupSetBitsFromISR()` не встановлює біти в самому ISR, а передає команду RTOS daemon task через чергу таймерів, і реакція залежить від пріоритету цієї задачі.[^freertos-kernel-book]

### Task notifications – легша альтернатива

Для зв’язку «одна подія чи значення – одна відома задача» FreeRTOS пропонує task notifications: вони значно швидші й потребують значно менше RAM, ніж queue, semaphore чи event group. Обмеження: отримувач лише один, з задачі в ISR повідомлення не передати, буферизується лише одне значення, broadcast неможливий, а відправник не може блокуватися в очікуванні, поки отримувач звільнить слот.[^freertos-kernel-book]

### Як обирати

- Передати дані або команду – queue (або task notification для одного 32-бітного значення).
- Повідомити одну задачу про подію з ISR – task notification або binary semaphore.
- Рахувати події чи вільні ресурси – counting semaphore.
- Захистити спільний ресурс між задачами – mutex з таймаутом, gatekeeper task або коротка критична секція.
- Чекати комбінацію умов або розбудити кілька задач – event group.

### Типові помилки

- Binary semaphore замість mutex-а для захисту ресурсу: немає priority inheritance, і semaphore може «повернути» інша задача.
- Mutex у ISR.
- Передача через queue указівника на стекову змінну або буфер без визначеного власника.
- Очікування без таймауту там, де відсутність події – ознака збою.
- Event group з ISR там, де потрібна мінімальна й детермінована затримка реакції.
