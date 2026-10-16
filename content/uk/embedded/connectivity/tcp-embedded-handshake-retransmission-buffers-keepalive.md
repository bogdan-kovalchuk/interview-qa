---
id: emb-conn-0009
title: "Як працює TCP у контексті обмеженого embedded-пристрою: handshake, retransmission, buffers і keepalive?"
track: embedded
section: connectivity
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
---

## Short answer

TCP починається з **three-way handshake**, потім гарантує ordered byte stream через ACK, retransmission, windowing і congestion control. На embedded важливі RAM buffers, timeout/reconnect logic, partial writes/reads і backpressure від network stack. <span class="warn">Keepalive не замінює application-level heartbeat, якщо треба швидко виявляти завислий peer.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
