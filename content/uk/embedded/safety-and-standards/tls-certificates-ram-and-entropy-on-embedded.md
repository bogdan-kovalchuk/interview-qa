---
id: emb-safety-0002
title: "Що таке TLS для embedded-пристрою і які проблеми дають certificates, RAM і entropy source?"
description: "TLS шифрує transport, автентифікує server/client і захищає telemetry або firmware update від MITM. Проблеми embedded: certificate chain займає flash/R…"
track: embedded
section: safety-and-standards
level: middle
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
  - source_id: iec-61508-1-2010
    title: "IEC 61508-1:2010 ? Functional safety: General requirements"
    url: https://webstore.iec.ch/en/publication/5515
    accessed: 2026-09-06
    kind: spec
    version: "IEC 61508-1:2010"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? safety-and-standards; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

<span class="key">TLS</span> шифрує transport, автентифікує server/client і захищає telemetry або firmware update від MITM. Проблеми embedded: certificate chain займає flash/RAM, handshake потребує buffers і crypto time, а ключі вимагають якісного entropy source/TRNG. <span class="warn">Без правильного time/certificate validation TLS може виглядати увімкненим, але не давати реальної автентифікації</span>.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

