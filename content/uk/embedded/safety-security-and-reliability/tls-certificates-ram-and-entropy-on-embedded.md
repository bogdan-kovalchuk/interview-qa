---
id: emb-safety-0002
title: "Що таке TLS для embedded-пристрою і які проблеми дають certificates, RAM і entropy source?"
track: embedded
section: safety-security-and-reliability
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iec-61508-1-2010
    title: "IEC 61508-1:2010 ? Functional safety: General requirements"
    url: https://webstore.iec.ch/en/publication/5515
---

## Short answer

**TLS** шифрує transport, автентифікує server/client і захищає telemetry або firmware update від MITM. Проблеми embedded: certificate chain займає flash/RAM, handshake потребує buffers і crypto time, а ключі вимагають якісного entropy source/TRNG. <span class="warn">Без правильного time/certificate validation TLS може виглядати увімкненим, але не давати реальної автентифікації</span>.[^dou-embedded-interview]

## Detailed explanation

TODO
