---
id: emb-cppfound-0021
title: "Що таке double pointer (`int **pp`) і навіщо він потрібен?"
track: embedded
section: pointers-and-arrays
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**Double pointer** – вказівник, що зберігає адресу іншого вказівника.

Навіщо:
1. **Зміна pointer caller-а**: `void alloc(int **pp){ *pp = malloc(n); }` – без `**` caller не побачить нову адресу;
2. **2D масиви через масиви вказівників**;
3. Просування parse-cursor: `void parse(char **p){ (*p)++; }`.

Читання типу: `int **pp` – "вказівник на вказівник на int"; `*pp` -> вказівник, `**pp` -> значення int.[^embeddedinterviewlab]

## Detailed explanation

### Семантика передачі аргументів за значенням у C та потреба у double pointer

У мові C абсолютно всі аргументи передаються у функції виключно за значенням (pass-by-value). Якщо функція приймає одинарний покажчик `void allocate(int *p)`, створюється локальна копія покажчика `p`. Будь-яке присвоєння всередині функції (наприклад, `p = malloc(sizeof(int));`) змінює лише цю локальну копію в поточному стековому кадрі, тоді як початковий покажчик у викликаючій функції (caller) залишається незмінним.

Щоб функція могла змінити значення змінної сторони виклику (caller), їй необхідно передати адресу цієї змінної. Якщо змінна сама є покажчиком (`int *ptr`), то її адреса `&ptr` має тип «покажчик на покажчик на int» (`int **`):

```c
void allocate_correct(int **pp, size_t size) {
    *pp = malloc(size * sizeof(int)); /* Модифікує початковий покажчик caller-а */
}

/* Виклик */
int *my_buffer = NULL;
allocate_correct(&my_buffer, 128); /* my_buffer тепер вказує на виділену пам’ять */
```

### Практичні патерни в embedded C: алокатори, парсери та списки

У системному програмуванні мікроконтролерів подвійні покажчики використовуються у трьох ключових архітектурних патернах:

1. **Ініціалізація дескрипторів та повернення кодів помилок:**
   У надійних embedded API функції повинні повертати статус виконання (`status_t` або код помилки за стандартом POSIX), а дескриптор створеного ресурсу повертати через вихідний параметр:
   ```c
   status_t ring_buffer_init(ring_buffer_t **out_handle, size_t capacity);
   ```
2. **Зсув курсора потоку під час парсингу пакетів (zero-copy parsing):**
   Під час розбору мережевих протоколів або кадрів зв’язку (UART, CAN, BLE) функція розбору може безпосередньо просувати покажчик на поточний байт у буфері:
   ```c
   uint8_t parse_header(const uint8_t **stream_cursor, size_t *remaining_len) {
       uint8_t packet_id = **stream_cursor;
       (*stream_cursor)++; /* Зсуваємо покажчик сторони виклику на наступний байт */
       (*remaining_len)--;
       return packet_id;
   }
   ```
3. **Елегантне видалення вузлів зі зв’язних списків:**
   Класичний патерн без спеціального розгалуження для голови списку (відомий за реалізацією в ядрі Linux):
   ```c
   void list_remove(node_t **head, node_t *target) {
       for (node_t **curr = head; *curr != NULL; curr = &(*curr)->next) {
           if (*curr == target) {
               *curr = target->next; /* Модифікує head або попередній next без if-else */
               break;
           }
       }
   }
   ```

### Безпека, перевірка NULL та надійність коду

Використання подвійної непрямої адресації несе підвищені ризики збоїв під час розіменування:
- **Перевірка покажчиків перед розіменуванням:** у захисному програмуванні (defensive programming) функція повинна перевіряти як сам подвійний покажчик, так і проміжний одинарний покажчик:
  ```c
  if (pp == NULL || *pp == NULL) {
      return ERR_INVALID_ARG;
  }
  ```
- **Запобігання висячим покажчикам:** функція звільнення пам’яті (deallocator) може приймати подвійний покажчик, щоб самостійно обнулити покажчик caller-а одразу після звільнення ресурсу:
  ```c
  void safe_free(void **pp) {
      if (pp != NULL && *pp != NULL) {
          free(*pp);
          *pp = NULL; /* Захищає від повторного використання звільненої пам’яті */
      }
  }
  ```
Такий підхід виключає виникнення висячих покажчиків (dangling pointers) у прошивці, підвищуючи стабільність системи.
