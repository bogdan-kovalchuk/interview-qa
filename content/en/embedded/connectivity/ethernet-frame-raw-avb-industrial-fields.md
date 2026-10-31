---
id: emb-conn-0010
title: "What is an Ethernet frame and which fields matter when working with raw Ethernet, AVB, or industrial Ethernet?"
track: embedded
section: connectivity
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: linux-if-ether-h
    title: "Linux kernel source: include/uapi/linux/if_ether.h"
    url: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/include/uapi/linux/if_ether.h
  - source_id: rfc-894-ip-over-ethernet
    title: "RFC 894: A Standard for the Transmission of IP Datagrams over Ethernet Networks"
    url: https://www.rfc-editor.org/rfc/rfc894.html
  - source_id: rfc-9542-ieee802-params
    title: "RFC 9542: IANA Considerations and IETF Protocol and Documentation Usage for IEEE 802 Parameters"
    url: https://www.rfc-editor.org/rfc/rfc9542.html
  - source_id: linux-if-vlan-h
    title: "Linux kernel source: include/linux/if_vlan.h"
    url: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/include/linux/if_vlan.h
  - source_id: linux-man-packet
    title: "packet(7) – Linux manual page"
    url: https://man7.org/linux/man-pages/man7/packet.7.html
  - source_id: lwip-opts-arp
    title: "lwIP 2.1.0: ARP options (lwipopts.h)"
    url: https://www.nongnu.org/lwip/2_1_x/group__lwip__opts__arp.html
  - source_id: linux-man-tc-cbs
    title: "tc-cbs(8) – Linux manual page"
    url: https://man7.org/linux/man-pages/man8/tc-cbs.8.html
  - source_id: linux-man-tc-taprio
    title: "tc-taprio(8) – Linux manual page"
    url: https://man7.org/linux/man-pages/man8/tc-taprio.8.html
  - source_id: linux-timestamping
    title: "Linux kernel documentation: Timestamping"
    url: https://docs.kernel.org/networking/timestamping.html
---

## Short answer

An **Ethernet frame** contains destination/source MAC, EtherType or length, payload and FCS; a VLAN tag can add priority/VID. For raw Ethernet, MAC filtering, MTU, padding and EtherType matter. For AVB/industrial Ethernet, timestamping, priority/QoS, deterministic latency and MAC/PHY/driver interaction are critical.[^dou-embedded-interview]

## Detailed explanation

TODO
