---
id: emb-raii-0024
title: "Як виглядає `unique_ptr` з HAL-deinit як function pointer?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-unique-ptr-single
    title: "C++ working draft: unique_ptr for single objects ([unique.ptr.single])"
    url: https://eel.is/c++draft/unique.ptr.single
  - source_id: cpp-draft-intro-object
    title: "C++ working draft: Object model ([intro.object])"
    url: https://eel.is/c++draft/intro.object
---

## Question code

```cpp
std::unique_ptr<HAL_Type, decltype(&HAL_DeInit)>
  res(&hal_obj, &HAL_DeInit);
// очищення гарантоване при виході зі scope
```

## Short answer

**Тип deleter'а – `decltype(&HAL_DeInit)`, передаємо саму функцію.**

При знищенні `res`, якщо вказівник не `nullptr`, викличеться `HAL_DeInit(&hal_obj)`. Function pointer deleter читабельний, але `unique_ptr` зберігає і вказівник на об’єкт, і вказівник на функцію, тож займає щонайменше два вказівники.[^cpp-draft-unique-ptr-single]

Правило: function pointer deleter простий; stateless lambda або empty functor можуть не додавати байтів, тож їх варто брати, якщо критичний `sizeof(unique_ptr)`.[^cpp-draft-intro-object]

## Detailed explanation

`decltype(&HAL_DeInit)` дає тип вказівника на функцію з тією самою сигнатурою, що й `HAL_DeInit`. Тут deleter – звичайний вказівник на функцію, а не клас. Конструктор `res(&hal_obj, &HAL_DeInit)` зберігає і вказівник на `hal_obj`, і вказівник на функцію.[^cpp-draft-unique-ptr-single] Деструктор робить еквівалент `if (get()) get_deleter()(get())`, тож при виході зі scope `HAL_DeInit(&hal_obj)` викликається один раз, якщо вказівник не `nullptr`.

```cpp
// Illustrative: HAL_Type and HAL_DeInit come from the vendor HAL.
void use_once(HAL_Type& hal_obj) {
    std::unique_ptr<HAL_Type, decltype(&HAL_DeInit)> res(&hal_obj, &HAL_DeInit);
    // ... use res.get() ...
}   // HAL_DeInit(&hal_obj) runs here; its return value is discarded
```

Значення, яке повертає `HAL_DeInit`, деструктор нікуди не записує, тож статус завершення губиться. Якщо статус потрібен, деініціалізацію треба викликати явно з перевіркою результату, а вказівник відпустити через `release()`, щоб деструктор не викликав deleter удруге.[^cpp-draft-unique-ptr-single]

Через це `unique_ptr` з function pointer deleter більший за сирий вказівник. Порівняйте з обгорткою-лямбдою без захоплення: `auto deinit = [](HAL_Type* h) { HAL_DeInit(h); };`. На практиці (GCC, Clang) closure-тип такої лямбди порожній і standard-layout, хоча стандарт дозволяє реалізації змінити його розмір і standard-layout-ність, тож перевіряй `sizeof`. Якщо так, її можна зберігати як порожню базу, і `unique_ptr<HAL_Type, decltype(deinit)>` може не займати зайвих байтів.[^cpp-draft-intro-object] Точний розмір залежить від реалізації, тому його варто перевірити через `sizeof` на цільовому тулчейні.

Function pointer deleter підходить, коли функція деініціалізації фіксована і не потребує контексту. Якщо потрібні додаткові аргументи, наприклад інший дескриптор, їх доведеться захопити лямбдою, і обгортка стане stateful з більшим розміром; тоді вибір між читабельністю і `sizeof` вирішується вже в дизайні.

**Типові помилки:**

- Очікувати, що `unique_ptr` з function pointer має розмір сирого вказівника.
- Очікувати, що статус від `HAL_DeInit` дійде до коду: деструктор його відкидає.
- Вважати, що `res` з `nullptr` викличе `HAL_DeInit`: при нульовому вказівнику deleter не викликається.[^cpp-draft-unique-ptr-single]
