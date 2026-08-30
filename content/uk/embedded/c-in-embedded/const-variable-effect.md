---
id: emb-cemb-0022
title: "Як `const` впливає на змінну?"
description: "`const` задає read-only семантику для доступу через const-qualified ім'я, але не гарантує фізичне розміщення у Flash або ROM."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження цього питання й відповіді; текст відповіді не перевірений незалежно від оригінальної Anki-колоди спільноти."
---

## Short answer

<code>const</code> задає read-only семантику для компілятора: об'єкт не можна змінювати через const-qualified ім'я після ініціалізації: <code>const int x = 5;</code>.[^dou-embedded-interview] Це не є гарантією, що дані фізично будуть саме у Flash або ROM; розміщення залежить від toolchain, linker script і платформи.

З вказівниками важливо читати справа наліво: <code>const int *p</code> – вказівник на незмінні дані; <code>int * const p</code> – незмінний сам вказівник; <code>const int * const p</code> – незмінні і дані, і адреса. <code>const</code> не означає compile-time constant у всіх випадках і може бути знятий cast-ом, але запис у реально const-об'єкт дає undefined behavior.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
