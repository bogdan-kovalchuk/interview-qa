---
id: emb-raii-0007
title: "Як використати `unique_ptr` з custom deleter для HAL-ресурсу?"
description: "unique_ptr з stateless лямбдою-deleter автоматично викликає HAL teardown при виході зі scope."
track: embedded
section: raii-and-smart-pointers
level: junior
type: mechanism
tags: []
status: published
updated: 2026-10-06
content_revision: 2
reconciled_with:
  en: 3
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-06; це джерело не є доказом тверджень."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C++; freestanding і вендорські тулчейни можуть відрізнятися."
  - source_id: cpp-draft-unique-ptr-general
    title: "C++ working draft: Unique-ownership pointers, General ([unique.ptr.general])"
    url: https://eel.is/c++draft/unique.ptr.general
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Визначає unique pointer як об’єкт, що зберігає вказівник і розпоряджається ним через associated deleter при власному знищенні; unique_ptr не копіюється, але переміщується. Не каже нічого про розмір unique_ptr."
  - source_id: cpp-draft-unique-ptr-single
    title: "C++ working draft: unique_ptr for single objects ([unique.ptr.single])"
    url: https://eel.is/c++draft/unique.ptr.single
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Визначає конструктори з deleter, деструктор (`if (get()) get_deleter()(get());`, поведінка undefined, якщо виклик кидає виняток), `release()` і `reset()`, а також вимоги до типу deleter. Розмір unique_ptr і inlining не регулює."
  - source_id: cpp-draft-unique-ptr-dltr-dflt
    title: "C++ working draft: default_delete ([unique.ptr.dltr.dflt])"
    url: https://eel.is/c++draft/unique.ptr.dltr.dflt
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що `default_delete::operator()` викликає `delete` на вказівнику; про інші deleter нічого не каже."
  - source_id: cpp-draft-expr-delete
    title: "C++ working draft: Delete ([expr.delete])"
    url: https://eel.is/c++draft/expr.delete
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що операнд single-object delete має бути нульовим, результатом попереднього non-array new або вказівником на базовий підоб’єкт такого об’єкта, інакше поведінка undefined. Не описує, що станеться на конкретній платформі."
  - source_id: cpp-draft-lambda-capture
    title: "C++ working draft: Lambda captures ([expr.prim.lambda.capture])"
    url: https://eel.is/c++draft/expr.prim.lambda.capture
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що для кожної сутності, захопленої за копією, у closure type оголошується безіменний нестатичний член, а для захоплених за посиланням це unspecified. Не визначає sizeof closure type чи unique_ptr."
---

## Question code

```cpp
auto del = [](UART_HandleTypeDef* h) {
  HAL_UART_DeInit(h);
};
std::unique_ptr<UART_HandleTypeDef, decltype(del)>
  uart(&huart1, del);
```

## Short answer

**`unique_ptr` з лямбдою-deleter викликає HAL teardown при знищенні, тобто при виході зі scope.** HAL означає hardware abstraction layer. Тут `unique_ptr` не алокує `huart1`: він лише керує teardown-викликом для вже існуючого handle, викликаючи deleter тільки якщо вказівник не нульовий.[^cpp-draft-unique-ptr-single] Немає control block і reference counting. Правило: тримай deleter stateless (лямбда без capture або empty functor), тоді `unique_ptr` зазвичай лишається розміром із вказівник; function pointer deleter зазвичай збільшує його.

## Detailed explanation

`unique_ptr` – це не лише власник пам’яті з heap. Стандарт описує його як об’єкт, що зберігає вказівник і при власному знищенні розпоряджається тим, на що той вказує, через associated deleter – function object, правильний виклик якого і є «звільненням» ресурсу.[^cpp-draft-unique-ptr-general] `delete` – лише deleter за замовчуванням: `default_delete` просто викликає `delete`.[^cpp-draft-unique-ptr-dltr-dflt] Власний deleter дозволяє описати RAII для будь-якої пари «взяти/віддати», зокрема `HAL_UART_Init` і `HAL_UART_DeInit`. Handle `huart1` при цьому статичний: `unique_ptr` його не створює й нічого не звільняє в heap, а лише гарантує виклик teardown.

Деструктор еквівалентний `if (get()) get_deleter()(get());`, тож teardown виконується, лише коли вказівник не нульовий.[^cpp-draft-unique-ptr-single] Звідси поведінка інших операцій: `reset()` викликає deleter одразу для старого значення, `release()` віддає вказівник без виклику deleter (відповідальність за teardown переходить до коду, який викликав `release()`), а move в інший `unique_ptr` передає і вказівник, і цей обов’язок. Якщо виклик deleter кидає виняток, поведінка undefined, тож teardown у deleter не повинен кидати.[^cpp-draft-unique-ptr-single]

Тип deleter входить у тип `unique_ptr`, тому конкретний виклик відомий на етапі компіляції. Лямбда без capture не додає стану: нестатичні члени в closure type з’являються для захоплених сутностей, за копією завжди, а за посиланням це unspecified.[^cpp-draft-lambda-capture] Тому `unique_ptr` з такою лямбдою чи empty functor у типових реалізаціях займає стільки ж, скільки вказівник, хоча стандарт цього не гарантує: у GCC 13 з libstdc++ на x86-64 це 8 байт, а з function pointer або лямбдою з capture – 16. Про розмір докладніше в `qid:emb-raii-0008`.

```cpp
// Ілюстративний приклад; типи й функції HAL – з драйвера.
bool run_uart_session() {
  if (HAL_UART_Init(&huart1) != HAL_OK) {
    return false;               // init не вдався: teardown не потрібен
  }
  auto del = [](UART_HandleTypeDef* h) { HAL_UART_DeInit(h); };
  std::unique_ptr<UART_HandleTypeDef, decltype(del)> uart(&huart1, del);

  use_uart(uart.get());
  return true;                  // ~unique_ptr викликає HAL_UART_DeInit(&huart1)
}
```

Guard створюють після успішного `HAL_UART_Init`: так teardown виконується лише для handle, який справді ініціалізовано, і на кожному виході з функції.

**Типові помилки:**

- Забути deleter: `std::unique_ptr<UART_HandleTypeDef>(&huart1)` використає `default_delete`, а той викличе `delete`[^cpp-draft-unique-ptr-dltr-dflt] на статичному об’єкті, що не створено через `new`, і це undefined behavior.[^cpp-draft-expr-delete]
- Два власники одного handle (два `unique_ptr` чи `unique_ptr` плюс ручний `HAL_UART_DeInit`): teardown виконається двічі.
- Лямбда з capture або інший deleter зі станом як тип deleter: стан зберігається в `unique_ptr` і зазвичай збільшує його розмір.[^cpp-draft-lambda-capture]

## Sources

<!-- generated from frontmatter -->
