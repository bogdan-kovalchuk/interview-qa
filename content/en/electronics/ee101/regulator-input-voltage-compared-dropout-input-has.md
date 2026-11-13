---
id: emb-elee-0156
title: "Which regulator input voltage is compared with the dropout if the input has ripple?"
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
  - source_id: ti-slva079
    title: "Texas Instruments SLVA079: Understanding the Terms and Definitions of LDO Voltage Regulators"
    url: https://www.ti.com/lit/an/slva079/slva079.pdf
  - source_id: ti-tps752q1-datasheet
    title: "Texas Instruments TPS752-Q1 datasheet"
    url: https://www.ti.com/lit/ds/symlink/tps752-q1.pdf
---

## Short answer

The minimum instantaneous input voltage (the ripple trough) is compared against dropout rather than the average voltage: `V_in,min > V_out + V_dropout` is required. Dropout depends on load current and junction temperature, so worst-case maximum current numbers must be taken from the datasheet. If the ripple trough falls below this threshold, regulation ceases during troughs and input ripple passes straight to the output.[^ti-slva079][^ti-tps752q1-datasheet]

## Detailed explanation

Dropout is the input-to-output differential at which the regulator ceases to regulate the output upon any further reduction of input voltage.[^ti-slva079] The condition `V_in - V_out >= V_dropout` must be satisfied at every instant in time, not merely on average: the pass element responds to the instantaneous input voltage; at 100–120 Hz ripple frequencies, the LDO output capacitance cannot bridge the dip, causing regulation to break down during those intervals (though output capacitance may smooth out extremely short transients). Therefore, calculations must use `V_in,min` – the lowest instantaneous value of the input voltage over the ripple cycle. For a rectifier with a filter capacitor, this corresponds to the trough between charging pulses rather than the average DC level.

Dropout voltage itself is not a fixed constant. In a PMOS pass element, it equals `V_dropout = I_o*R_on`, meaning it scales with load current.[^ti-slva079] The TPS752-Q1 datasheet notes that dropout is roughly proportional to output current and illustrates its dependence on junction temperature; minimum input voltage is specified as `V_I(min) = V_O(max) + V_DO(max load)`.[^ti-tps752q1-datasheet] Thus, dropout must be verified at maximum load current and at the datasheet junction temperature where it reaches its peak, rather than using typical values measured under light load. The lowest supply tolerance limit (mains variations, rectifier diode forward drops) must also be incorporated into `V_in,min`.

As long as the input remains above this threshold, the regulator suppresses ripple according to its PSRR, defined as `V_o,ripple/V_i,ripple`.[^ti-slva079] Below this threshold, the regulator falls out of regulation, so datasheet PSRR ratings no longer apply: the output begins tracking the input, and ripple troughs appear directly at the output – for example, at 100 Hz for a full-wave rectifier on 50 Hz mains.

**Example (illustrative numbers):** `V_out = 5 V`, dropout at maximum current `0.5 V`, requiring `V_in,min > 5.5 V`. If the average post-rectifier voltage is `6.5 V` with a ripple amplitude of `2 V` peak-to-peak (spanning `5.5 V` to `7.5 V`), checking against the average indicates a "1 V margin" (`6.5 - 5.5`), but at the ripple trough the margin is zero: `5.5 - 5.5 = 0 V`. The slightest line sag or load current spike drops the regulator out of regulation. The only remedy is to raise the trough itself: by reducing ripple (larger capacitance, lower current) or increasing average voltage, after which `V_in,min` must be re-evaluated.

**Common mistakes:**

- Comparing dropout against average input voltage rather than `V_in,min`.
- Using typical dropout values under light load instead of worst-case values at maximum current and temperature.
- Neglecting mains tolerances, line sags, diode drops, and transient dips when determining `V_in,min`.
