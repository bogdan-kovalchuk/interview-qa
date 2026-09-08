---
id: emb-power-0001
title: "What are the common power management techniques used in battery-powered embedded systems?"
description: "Battery-powered systems reduce average energy through duty cycling, suitable sleep states, clock or power gating, and workload-aware frequency or voltage control when the hardware supports it."
track: embedded
section: power-management
level: middle
type: concept
tags: []
status: published
updated: 2026-09-08
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: arm-cortex-m-low-power
    title: "ARM: Cortex-M Low Power Design"
    url: https://developer.arm.com/documentation/102499/0100/
    accessed: 2026-09-08
    kind: official
    version: null
    applicability: "ARM official documentation on low-power design for Cortex-M."
---

## Short answer

**Reduce average energy by duty cycling the workload: batch useful work, wake on the required event or timer, and return to a suitable sleep state.** Disable unused peripheral clocks, gate power domains when the hardware permits it, and reduce clock frequency and voltage only within the device's supported operating points.[^arm-cortex-m-low-power] Radio and sensor on-time, regulator quiescent current, and leakage can matter more than CPU time. The deepest sleep state is not automatically best: include wake energy and latency, state retention, clock restart time, and real-time deadlines in the choice.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
