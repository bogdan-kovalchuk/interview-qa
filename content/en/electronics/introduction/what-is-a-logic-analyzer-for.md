---
id: emb-elintro-0271
title: "What is a logic analyzer for?"
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
  - source_id: tek-oscilloscope-types
    title: "Tektronix: Oscilloscope Types"
    url: https://www.tek.com/en/documents/primer/oscilloscope-types
---

## Short answer

A logic analyzer records multiple digital channels simultaneously and decodes bus protocols such as `I²C`, `SPI`, and `UART`. This is useful when verifying timing sequences and protocol state machines across many lines rather than analyzing analog signal fidelity.[^tek-oscilloscope-types]

## Detailed explanation

A logic analyzer captures multiple digital input channels simultaneously and displays their logic states and transitions over time. It compares each sample against a configured threshold voltage, classifying it strictly as high or low; consequently, the display reflects discrete logic states and transitions rather than analog amplitude or edge shape. The logic threshold must be set to match the operating levels of the logic family under test, as an incorrect threshold can cause false bit detection.[^tek-oscilloscope-types]

Capturing multiple lines synchronously reveals the timing relationship between events. For instance, you can verify whether a chip-select signal asserts before SPI clock pulses begin, confirm whether an acknowledge (ACK) bit follows an I²C byte, or measure microcontroller pulse durations. If the instrument supports protocol decoding, it groups raw bits into packets and displays their interpreted values. Decoding reliability depends on the sampling rate, memory depth, configured threshold, and probe signal integrity.[^tek-oscilloscope-types]

Analyzing the analog behavior of a digital trace – such as ringing, overshoot, slow edge rates, or supply bounce – requires an oscilloscope channel. A logic analyzer may register an erroneous logic transition, but it cannot display the analog voltage anomaly that triggered it. If a protocol decoder flags an invalid UART byte, verify the baud rate, polarity, and threshold settings, and then inspect the physical line with an oscilloscope to examine the analog waveform.

**Common mistakes:**

- Assuming a logic analyzer measures precise analog voltage levels or edge quality.
- Relying blindly on protocol decoder output without verifying capture and threshold parameters.
- Overlooking maximum input voltage ratings or proper ground clip connections.
