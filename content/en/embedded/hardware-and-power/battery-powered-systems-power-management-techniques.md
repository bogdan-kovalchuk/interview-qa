---
id: emb-power-0001
title: "What are the common power management techniques used in battery-powered embedded systems?"
track: embedded
section: hardware-and-power
sources:
  - source_id: arm-cortex-m-low-power
    title: "ARM: Cortex-M Low Power Design"
    url: https://developer.arm.com/documentation/102499/0100/
---

## Short answer

**Reduce average energy by duty cycling the workload: batch useful work, wake on the required event or timer, and return to a suitable sleep state.** Disable unused peripheral clocks, gate power domains when the hardware permits it, and reduce clock frequency and voltage only within the device's supported operating points.[^arm-cortex-m-low-power] Radio and sensor on-time, regulator quiescent current, and leakage can matter more than CPU time. The deepest sleep state is not automatically best: include wake energy and latency, state retention, clock restart time, and real-time deadlines in the choice.

## Detailed explanation

TODO
