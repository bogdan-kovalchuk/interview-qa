---
id: emb-macros-0045
title: "Чому повідомлення компілятора про помилку в макросі важко читати?"
description: "Помилка вказує на розгорнутий код, а не на рядок #define."
track: embedded
section: inline-and-macros
level: junior
type: concept
tags: []
status: published
updated: 2026-09-06
content_revision: 1
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
    applicability: "Походження питання і відповіді; відповідь незалежно не перевірена."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
---

## Short answer

**Помилка вказує на розгорнутий код, а не на рядок `#define`.**

Компілятор бачить уже підставлений текст у місці виклику, тому діагностика посилається туди; вкладені макроси ще й перемножують ефект. Це класична причина, чому складну логіку не варто ховати в макрос.

Захист: дивись `gcc -E`, щоб побачити фактичне розгортання; для логіки, яку доведеться діагностувати, обирай `static inline`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
