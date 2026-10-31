---
id: emb-conn-0004
title: "How does TCP differ from UDP for telemetry, control commands, and firmware updates?"
track: embedded
section: connectivity
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: rfc-768-udp
    title: "RFC 768: User Datagram Protocol"
    url: https://www.rfc-editor.org/rfc/rfc768.html
  - source_id: rfc-8085-udp-guidelines
    title: "RFC 8085: UDP Usage Guidelines"
    url: https://www.rfc-editor.org/rfc/rfc8085.html
  - source_id: rfc-9293-tcp
    title: "RFC 9293: Transmission Control Protocol (TCP)"
    url: https://www.rfc-editor.org/rfc/rfc9293.html
  - source_id: rfc-6298-tcp-rto
    title: "RFC 6298: Computing TCP's Retransmission Timer"
    url: https://www.rfc-editor.org/rfc/rfc6298.html
  - source_id: rfc-7252-coap
    title: "RFC 7252: The Constrained Application Protocol (CoAP)"
    url: https://www.rfc-editor.org/rfc/rfc7252.html
  - source_id: rfc-7959-coap-block
    title: "RFC 7959: Block-Wise Transfers in the Constrained Application Protocol (CoAP)"
    url: https://www.rfc-editor.org/rfc/rfc7959.html
---

## Short answer

TCP provides an ordered reliable byte stream with retransmission and flow control, making it suitable for firmware updates or commands where integrity matters. UDP provides datagrams with no delivery or ordering guarantee, but lower overhead and latency, useful for frequent telemetry samples or real-time data. If UDP is used for a critical command or update, reliability, ordering and authentication must be built on top.[^dou-embedded-interview]

## Detailed explanation

TODO
