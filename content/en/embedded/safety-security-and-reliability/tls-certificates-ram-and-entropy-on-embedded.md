---
id: emb-safety-0002
title: "What is TLS for an embedded device, and what problems do certificates, RAM, and the entropy source create?"
track: embedded
section: safety-security-and-reliability
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iec-61508-1-2010
    title: "IEC 61508-1:2010 ? Functional safety: General requirements"
    url: https://webstore.iec.ch/en/publication/5515
---

## Short answer

**TLS** encrypts transport, authenticates server and client, and protects telemetry or firmware update from MITM. Embedded problems: certificate chain takes flash and RAM, handshake needs buffers and crypto time, and keys require a quality entropy source or TRNG. <span class="warn">Without proper time and certificate validation, TLS may appear enabled but not provide real authentication</span>.[^dou-embedded-interview]

## Detailed explanation

TODO
