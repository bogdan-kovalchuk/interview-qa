---
id: emb-cemb-0038
title: "Для чого використовують pointer-to-pointer у драйверах, API виділення ресурсів і linked structures?"
track: embedded
section: pointers-and-arrays
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: armv7m-arm
    title: "ARMv7-M Architecture Reference Manual"
    url: https://developer.arm.com/documentation/ddi0403/e/
---

## Short answer

`T **` потрібен, коли функція має змінити pointer у caller-а: видати handle, додати node в list head або повернути buffer із pool. У драйверах це часто виглядає як `driver_open(dev_t **out)` або queue API, що оновлює head/tail. Важливо документувати ownership: хто після цього звільняє або повертає ресурс.[^dou-embedded-interview]

## Detailed explanation

### Фундаментальна причина використання в мові C

У мові C передача всіх параметрів у функції здійснюється **виключно за значенням** (`pass-by-value`, ISO/IEC 9899:2011, §6.5.2.2)[^iso-c-n1570]. Коли функція приймає одинарний вказівник `T *ptr`, вона отримує локальну копію адреси на стеку. Будь-які модифікації самого вказівника всередині функції (наприклад, `ptr = malloc(...)` або `ptr = next_node`) змінюють лише локальну копію, залишаючи вказівник викликаючої сторони (`caller`) незмінним.

Щоб функція мала змогу перезаписати адресу в самому вказівнику `caller`-а, їй необхідно передати адресу цієї змінної-вказівника – тобто подвійний вказівник (`pointer-to-pointer`, `T **ptr_to_ptr`).

### Застосування у драйверах та API ресурсів

1. **Шаблон вихідного параметра (Out-parameter) та статусні коди:**
   У низькорівневих драйверах (Linux kernel, RTOS, POSIX, CMSIS-Driver) значення, що повертається функцією через `return`, резервується для коду помилки (`status_t` або від’ємне число помилки). Створюваний дескриптор об’єкта повертається через подвійний вказівник:
   ```c
   typedef struct uart_dev uart_dev_t;

   status_t uart_open(uint8_t port_id, uart_dev_t **out_dev) {
       if (out_dev == NULL) return STATUS_INVALID_PARAM;

       uart_dev_t *dev = find_or_allocate_dev(port_id);
       if (!dev) return STATUS_NO_DEVICE;

       *out_dev = dev; // записує адресу дескриптора безпосередньо у змінну caller-а
       return STATUS_OK;
   }
   ```
   Це дозволяє чисто відокремити потік обробки помилок від повернення корисних даних.

2. **Модифікація зв’язаних списків без спеціальних умов:**
   У планувальниках RTOS черги задач часто реалізуються одно- чи двозв’язаними списками. Видалення або додавання елемента в голову списку (`head`) зазвичай вимагає спеціальної перевірки `if (head == target)`. Використання `node_t **` усуває це розгалуження (відомий інженерний підхід Лінуса Торвальдса):
   ```c
   void list_remove(node_t **head, node_t *target) {
       node_t **curr = head;
       while (*curr && *curr != target) {
           curr = &(*curr)->next; // переходимо за адресою поля next
       }
       if (*curr) {
           *curr = target->next; // автоматично оновлює або сам head, або поле next попередника
       }
   }
   ```

3. **Безпечне вивільнення ресурсів (Safe Free Pattern):**
   При звичайному `free(ptr)` вказівник залишається вказувати на звільнену пам’ять (`dangling pointer`). Функція з подвійним вказівником одночасно звільняє пам’ять і обнуляє вказівник користувача:
   ```c
   void safe_free(void **pp) {
       if (pp && *pp) {
           free(*pp);
           *pp = NULL; // запобігає Use-After-Free
       }
   }
   ```

### Робота на рівні асемблера ARM Cortex-M

На рівні системи команд Thumb-2 для ARM Cortex-M доступ через подвійний вказівник генерує два послідовні звернення до пам’яті[^armv7m-arm]:

```assembly
; R0 = out_dev (адреса вказівника користувача), R1 = dev (адреса створеного об’єкта)
STR     R1, [R0]        ; запис адреси об’єкта dev за адресою в R0
```

Якщо ж викликається зчитування через `**pp`, генеруються дві інструкції `LDR`:
```assembly
LDR     R0, [SP, #pp_offset] ; R0 = pp (адреса першого вказівника)
LDR     R1, [R0]             ; R1 = *pp (адреса цільового об’єкта)
LDR     R2, [R1]             ; R2 = **pp (значення цільового об’єкта)
```

### Модель власності (Ownership) та інженерна дисципліна

При проектуванні API з подвійними вказівниками критично важливо чітко документувати модель володіння пам’яттю:
- **Передача власності (`Transfer of Ownership`):** Хто саме відповідає за звільнення або повернення ресурсу в пул? Якщо функція повертає буфер через `get_buffer(uint8_t **buf)`, в документації має бути чітко вказано, чи повинен `caller` викликати `release_buffer(*buf)`.
- **Захист від невалідних покажчиків:** Першим рядком функції обов’язково перевіряйте сам аргумент на нуль (`if (out_ptr == NULL) return ERROR;`), щоб запобігти падінню системи через розіменування нульової адреси.
