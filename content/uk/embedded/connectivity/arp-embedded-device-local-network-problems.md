---
id: emb-conn-0008
title: "Що таке ARP і коли embedded-пристрій реально стикається з ARP-проблемами у локальній мережі?"
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

**ARP** зіставляє IPv4 address з MAC address у локальному Ethernet/Wi-Fi сегменті. Embedded device стикається з ARP при першому connect до gateway/peer, IP conflict, stale ARP cache, link flap або sleep/wake сценаріях. Симптоми: ping не проходить у LAN, перший packet губиться, після зміни IP/MAC потрібен gratuitous ARP.[^dou-embedded-interview]

## Detailed explanation

TODO
