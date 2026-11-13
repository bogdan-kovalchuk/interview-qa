---
id: emb-elee-0171
title: "Can a 5 V logic signal be applied to the input of a chip powered from 3.3 V?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: ti-hc00
    title: "TI SN74HC00 quadruple NAND gates datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc00.pdf
  - source_id: ti-sn74lvc1g125
    title: "Texas Instruments SN74LVC1G125 datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74lvc1g125.pdf
---

## Short answer

Only if the chip's datasheet confirms that the input is 5 V tolerant when powered from 3.3 V. A standard CMOS input has clamp diodes to `V_CC` and to ground, and the recommended input voltage is limited to `V_CC`, so applying 5 V exceeds recommended conditions and stresses the upper diode.[^ti-hc00] Certain inputs, such as the `SN74LVC1G125`, explicitly tolerate up to 5.5 V with a 3.3 V supply.[^ti-sn74lvc1g125] A shared ground and separate regulated rails do not by themselves ensure signal compatibility.

## Detailed explanation

The issue is not whether a 3.3 V device "recognizes" five volts as a logic high, but whether the maximum input voltage rating relative to its supply rail is violated. A standard CMOS input incorporates internal clamp diodes to VCC and to ground.[^ti-hc00] In the SN74HC00, the recommended input voltage ranges from 0 to VCC, while absolute maximum ratings are specified via clamp current: for `VI > VCC + 0.5 V`, `IIK` is rated at a maximum of ±20 mA, and voltage ratings may only be exceeded if this current limit is observed.[^ti-hc00] For `VCC = 3.3 V`, this sets a conduction threshold of `3.3 + 0.5 = 3.8 V`, so a 5 V signal exceeds it by 1.2 V; the upper clamp diode to VCC typically begins conducting, dumping current into the 3.3 V rail rather than simply clipping the input signal.

Consequently, there is a fundamental distinction between "the circuit continues to function" and "the operating condition is permissible." The datasheet cautions that prolonged operation under absolute maximum ratings can impair device reliability.[^ti-hc00] Therefore, the absence of immediate failure does not prove that the operating condition is acceptable. Limiting clamp current with a series resistor and relying on internal diodes as part of the operational circuit is acceptable only where the datasheet explicitly permits it, and with full awareness that this current flows directly into the chip's power supply.

Certain input stages are purpose-built for this application. The SN74LVC1G125 tolerates inputs up to 5.5 V while operating from a supply between 1.65 and 5.5 V; with `VCC` between 3 and 3.6 V, the minimum high-level input voltage is `VIH = 2 V`, readily recognizing a 5 V logic output.[^ti-sn74lvc1g125] Such 5 V tolerance is a characteristic of specific ICs (and in microcontrollers, often of specific pins in designated modes) and cannot be generalized across all "3.3 V logic": on microcontrollers, it must be verified in the pin characteristics table of the datasheet. An additional case to verify is when an active signal is present while the 3.3 V rail is powered down; for this, the SN74LVC1G125 provides an `Ioff` specification.[^ti-sn74lvc1g125]

The reverse direction presents its own pitfall. When driving a 5 V CMOS input from a 3.3 V output, for instance on an SN74LVC1G125 powered from 5 V, `VIH(min) = 0.7*VCC`, which equals 3.5 V at `VCC = 5 V`, so a 3.3 V output does not guarantee a valid high.[^ti-sn74lvc1g125] A shared ground provides only a common reference point, and separate regulated rails do not by themselves ensure level compatibility: driver `VOH` must exceed receiver `VIH`, driver `VOL` must remain below receiver `VIL`, and input voltage limits must not be exceeded. If these conditions are not satisfied, level translation is required via a dedicated level shifter or compatible buffer IC.

**Common mistakes:**

- Assuming "5 V-tolerant" is a property of an entire logic family or IC without verifying the specific pin and mode in the datasheet.[^ti-sn74lvc1g125]
- Concluding that "it works, so it is fine": specifications are guaranteed only under recommended operating conditions, and extended operation near absolute maximum ratings impairs reliability.[^ti-hc00]
- Overlooking the reverse direction: a 3.3 V signal driving a 5 V CMOS input may fail to meet `VIH`.[^ti-sn74lvc1g125]
- Expecting that a shared ground and separate regulated rails automatically resolve signal level compatibility.
