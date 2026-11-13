---
id: emb-elee-0137
title: "Why does a very small signal pass poorly through a diode bridge?"
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
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification
  - source_id: libretexts-fiore-diode-models
    title: "Fiore: Semiconductor Devices, 2.4 Diode Circuit Models (Engineering LibreTexts)"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/02:_PN_Junctions_and_Diodes/2.4:_Diode_Circuit_Models
---

## Short answer

In each half-cycle, load current flows through two bridge diodes in series, requiring an input voltage of approximately `2*V_F`, or about 1.4 V for silicon.[^fiore-rectification] Any signal with peak amplitude below this threshold cannot initiate conduction, while a signal only slightly above it produces only short, clipped peaks attenuated by `2*V_F`.[^fiore-rectification]

## Detailed explanation

In each half-cycle, the bridge passes current through two diodes, and the load sees the input voltage minus two forward drops.[^fiore-rectification] In a simple model with a knee voltage, a silicon diode begins conducting noticeably at approximately 0.6–0.7 V.[^fiore-rectification] The textbook cautions that these are behavioral models, not literal 0.7 V sources inside the diode.[^libretexts-fiore-diode-models] For two diodes in series, the threshold doubles: `2*V_F ≈ 1.4 V`. Therefore, for a bridge, a "small" signal is one whose amplitude is comparable to 1.4 V, rather than to zero.

The actual diode characteristic is smooth, so below the threshold current is not strictly zero, but merely very small. The textbook estimates the dynamic junction resistance as `26 mV/I`.[^libretexts-fiore-diode-models] Under this approximation, at 10 µA it equals about `0.026/10^-5 = 2.6 kΩ`, while at 1 mA it is about `0.026/10^-3 = 26 Ω`. Consequently, a weak signal creates little current, the diodes present a high impedance, and if that impedance exceeds the load resistance, most of the voltage drops across the diodes rather than across the load.

**Example (model with `V_F = 0.7 V`, sine wave with amplitude `A`).** Output peak is `A - 1.4 V`, and diodes conduct only when `|v_in| > 1.4 V`, corresponding to a fraction of the half-cycle `(180° - 2*asin(1.4/A))/180°`:

- `A = 1 V`: output is zero, diodes do not turn on;
- `A = 1.41 V` (this is a 1 V RMS signal): peak output is `0.01 V`, practically zero;
- `A = 2 V`: peak `0.6 V` (30% of input), conduction over about 91° of 180°, or ≈ 51%;
- `A = 5 V`: peak `3.6 V` (72%), conduction ≈ 82%;
- `A = 20 V`: peak `18.6 V` (93%), and the threshold is barely noticeable.

This demonstrates that the significance of diode drops depends on the ratio of signal amplitude to `2*V_F`: at high voltages it is a minor correction, while at low voltages it is the dominant effect. The same calculation highlights waveform distortion: when the amplitude is only slightly above threshold, the output consists of narrow pulses near the peaks rather than a replica of the input.

Therefore, a diode bridge is unsuitable for rectifying signals whose amplitude is comparable to 1.4 V, such as weak measurement or radio signals. Those require alternative approaches that compensate for diode drops or utilize diodes with lower `V_F`; those topologies are outside the scope here.

**Common mistakes:**

- Assuming a diode passes any positive voltage and ignoring the threshold of about 0.7 V per diode.
- Subtracting only a single drop instead of two for a bridge.
- Comparing the threshold against the RMS value rather than peak amplitude: a 1 V RMS signal has a 1.41 V peak.
