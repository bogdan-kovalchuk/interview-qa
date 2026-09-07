---
id: emb-safety-0002
title: "What is TLS for an embedded device, and what problems do certificates, RAM, and the entropy source create?"
description: "TLS encrypts transport and authenticates endpoints, but certificate storage, handshake buffers, crypto time, and entropy are constrained in embedded."
track: embedded
section: safety-and-standards
level: middle
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of this question and answer; the answer text is not independently verified against the original community Anki deck."
  - source_id: iec-61508-1-2010
    title: "IEC 61508-1:2010 ? Functional safety: General requirements"
    url: https://webstore.iec.ch/en/publication/5515
    accessed: 2026-09-06
    kind: spec
    version: "IEC 61508-1:2010"
    applicability: "Authoritative section-level reference for safety and standards concepts; details of specific devices and toolchains can differ."
---

## Short answer

**TLS** encrypts transport, authenticates server and client, and protects telemetry or firmware update from MITM. Embedded problems: certificate chain takes flash and RAM, handshake needs buffers and crypto time, and keys require a quality entropy source or TRNG. <span class="warn">Without proper time and certificate validation, TLS may appear enabled but not provide real authentication</span>.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

