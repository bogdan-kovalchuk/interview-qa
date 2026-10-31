---
id: emb-conn-0009
title: "How does TCP work in the context of a constrained embedded device: handshake, retransmission, buffers, and keepalive?"
track: embedded
section: connectivity
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: rfc-9293-tcp
    title: "RFC 9293: Transmission Control Protocol (TCP)"
    url: https://www.rfc-editor.org/rfc/rfc9293.html
  - source_id: lwip-opts-tcp
    title: "lwIP 2.1.0: TCP options (lwipopts.h)"
    url: https://www.nongnu.org/lwip/2_1_x/group__lwip__opts__tcp.html
  - source_id: rfc-6298-tcp-rto
    title: "RFC 6298: Computing TCP's Retransmission Timer"
    url: https://www.rfc-editor.org/rfc/rfc6298.html
  - source_id: linux-man-tcp
    title: "tcp(7) – Linux manual page"
    url: https://man7.org/linux/man-pages/man7/tcp.7.html
  - source_id: posix-send
    title: "POSIX.1-2024: send()"
    url: https://pubs.opengroup.org/onlinepubs/9799919799/functions/send.html
  - source_id: lwip-tcp-raw-api
    title: "lwIP 2.1.0: TCP raw API"
    url: https://www.nongnu.org/lwip/2_1_x/group__tcp__raw.html
---

## Short answer

TCP starts with a **three-way handshake**, then guarantees an ordered byte stream via ACK, retransmission, windowing and congestion control. On embedded, RAM buffers, timeout/reconnect logic, partial writes/reads and backpressure from the network stack matter. <span class="warn">Keepalive does not replace an application-level heartbeat if you need to detect a hung peer quickly.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
