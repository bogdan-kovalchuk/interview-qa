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
    title: "IEC 61508-1:2010 – Functional safety: General requirements"
    url: https://webstore.iec.ch/en/publication/5515
  - source_id: rfc-8446-tls13
    title: "RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3"
    url: https://www.rfc-editor.org/rfc/rfc8446
  - source_id: rfc-5280-x509
    title: "RFC 5280: Internet X.509 Public Key Infrastructure Certificate and CRL Profile"
    url: https://www.rfc-editor.org/rfc/rfc5280
  - source_id: rfc-9525-service-identity
    title: "RFC 9525: Service Identity in TLS"
    url: https://www.rfc-editor.org/rfc/rfc9525
  - source_id: rfc-8449-record-size-limit
    title: "RFC 8449: Record Size Limit Extension for TLS"
    url: https://www.rfc-editor.org/rfc/rfc8449
  - source_id: rfc-6066-tls-extensions
    title: "RFC 6066: Transport Layer Security (TLS) Extensions: Extension Definitions"
    url: https://www.rfc-editor.org/rfc/rfc6066
  - source_id: esp-idf-mbedtls
    title: "ESP-IDF Programming Guide (ESP32): Mbed TLS"
    url: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/protocols/mbedtls.html
  - source_id: rfc-4086-randomness
    title: "RFC 4086: Randomness Requirements for Security"
    url: https://www.rfc-editor.org/rfc/rfc4086
  - source_id: esp-idf-random
    title: "ESP-IDF Programming Guide (ESP32): Random Number Generation"
    url: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/system/random.html
---

## Short answer

**TLS** encrypts transport, authenticates server and client, and protects telemetry or firmware update from MITM. Embedded problems: certificate chain takes flash and RAM, handshake needs buffers and crypto time, and keys require a quality entropy source or TRNG. <span class="warn">Without proper time and certificate validation, TLS may appear enabled but not provide real authentication</span>.[^dou-embedded-interview]

## Detailed explanation

TODO
