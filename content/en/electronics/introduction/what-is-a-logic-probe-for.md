---
id: emb-elintro-0267
title: "What is a logic probe for?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: tek-logic-probe
    title: "Tektronix: Logic Probe"
    url: https://www.tek.com/en/products/oscilloscopes/oscilloscope-probes/logic-probe
---

## Short answer

A logic probe quickly verifies whether a digital line is recognized as `HIGH` or `LOW`, and some models can also detect activity pulses.[^tek-logic-probe] Detection thresholds and pulse-stretching features depend on the probe model and logic family; inspecting the actual analog waveform requires an oscilloscope.[^tek-logic-probe]

## Detailed explanation

A logic probe is a test instrument designed to quickly determine the digital state of a signal line, typically indicating whether it is `HIGH` or `LOW`. It is used during the verification and troubleshooting of digital circuits, including TTL and CMOS logic, to check whether a specific node is toggling or stuck in a single logic state.[^tek-logic-probe]

The probe connects to a common reference/ground and power supply rail according to its model-specific instructions, while its probe tip touches the test point. Internal input comparators evaluate the signal voltage against logic thresholds, lighting an LED, activating an audible tone, or driving an indicator to show the detected state. In the undefined region between valid `LOW` and `HIGH` limits, the indication may be floating or erratic; threshold levels are not universal across TTL and CMOS families.[^tek-logic-probe]

Example: if a logic gate output is expected to stay `HIGH` but the probe registers `LOW`, this prompts inspection of the gate's supply voltage, input logic levels, trace connections, and potential output shorts. Some logic probes include pulse detection or stretching features to signal transient activity, though extremely narrow glitches may be missed depending on bandwidth and pulse-capture limits. Basic logic state indication does not reveal exact signal amplitude, edge transition time, or analog waveform fidelity.[^tek-logic-probe]

**Common mistakes:**

- Assuming that `HIGH` always corresponds to a fixed voltage such as 5 V: detection thresholds are defined by the probe's selected logic family compatibility.
- Using a logic probe as an oscilloscope replacement when analog amplitude, noise margins, rise/fall times, or pulse widths matter.
- Forgetting to connect the common ground clip or exceeding the allowable input voltage rating specified in the instrument manual.
