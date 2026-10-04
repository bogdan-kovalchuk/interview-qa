---
id: emb-patterns-0028
title: "Що таке init-once (idempotent) патерн?"
description: "Прапорець гарантує, що ініціалізація виконається лише раз, навіть якщо init викликати кілька разів."
track: embedded
section: common-code-patterns
level: junior
type: mechanism
tags: []
status: published
updated: 2026-10-04
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
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; це джерело не є доказом тверджень."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
---

## Question code

```c
static bool initialized = false;
err_t subsystem_init(void) {
  if (initialized) return ERR_OK; // idempotent
  // one-time HW setup
  initialized = true;
  return ERR_OK;
}
```

## Short answer

**Прапорець гарантує, що ініціалізація виконається лише раз**, навіть якщо `init` викликати кілька разів.

Спрощує startup-послідовність, коли кілька модулів залежать від однієї підсистеми.

Прапорець ставлять лише після успішного завершення налаштування; звичайний `bool` не захищає від одночасних викликів із різних потоків або ISR, тож потрібна визначена серіалізація.[^iso-c-n1570]

## Detailed explanation

Init-once – це патерн, у якому повторний виклик функції ініціалізації не повторює вже виконане налаштування. У прикладі прапорець `initialized` зберігає факт успішного завершення: наступний виклик повертає `ERR_OK`, не налаштовуючи периферію вдруге. Така властивість корисна, коли кілька модулів можуть ініціювати startup тієї самої підсистеми.[^iso-c-n1570]

Порядок операцій має значення: прапорець ставлять після успішного налаштування. Якщо поставити його раніше, помилка посеред ініціалізації змусить наступний виклик помилково вважати підсистему готовою. Реальна функція часто має повертати статус, щоб невдалу спробу можна було повторити або безпечно відкотити.

Простий глобальний `bool` не робить функцію thread-safe. Два потоки можуть одночасно побачити `false` і виконати налаштування двічі; ISR також не повинна переривати частково завершену ініціалізацію. Залежно від системи потрібні критична секція, mutex, атомарний стан або вимога викликати init лише до запуску scheduler. `volatile` не усуває race condition.

Приклад відображає лише однопотоковий випадок:

```c
if (initialized) return ERR_OK;
if (configure_hardware() != OK) return ERR_INIT;
initialized = true;
return ERR_OK;
```

**Типові помилки:**

- Називати прапорець гарантією потокобезпечності.
- Встановлювати його до перевірки результату налаштування.
- Не визначити, що робити після частково виконаної невдалої ініціалізації.

## Sources

<!-- generated from frontmatter -->
