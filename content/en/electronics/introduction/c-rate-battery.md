---
id: emb-elintro-0064
title: "What is the C-rate of a battery?"
track: electronics
section: introduction
sources:
  - source_id: ti-crate
    title: "Battery Gauging Fundamentals"
    url: https://www.ti.com/lit/pdf/slyp812
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

`C-rate` specifies the charge or discharge current relative to a battery's nominal capacity: for a capacity of `2000 mAh`, a current of `1C` equals `2 A`, and `0.5C` is `1 A`.[^ti-crate] This is a normalized metric, not an inherent guarantee of safe current: allowable limits are determined by the specific battery manufacturer.

## Detailed explanation

`C-rate` is the ratio of charge or discharge current to nominal capacity expressed in ampere-hours. It allows operating regimes of batteries with different capacities to be compared: an identical C-rate represents an identical fraction of nominal capacity per hour, but the absolute currents will differ.[^ti-crate]

**Worked example:**

For a battery rated at `2000 mAh = 2 Ah`:

```text
1C = 1 * 2 Ah = 2 A
0.5C = 0.5 * 2 Ah = 1 A
2C = 2 * 2 Ah = 4 A
```

This is an arithmetic unit conversion and definition of C-rate, not a prediction of exact runtime. For an ideal battery, discharging at `1C` would correspond to roughly one hour, but actual available capacity depends on chemistry, temperature, aging, cutoff voltage, and current magnitude; TI explicitly notes that in practice, a battery discharged at `1C` often depletes in less than an hour.[^ti-crate]

Separate limits must apply to charging and discharging. For instance, a `2C` rating for discharge does not automatically mean the battery can be charged at that same current. Consult the battery datasheet, including temperature ratings, continuous versus pulsed current modes, and charge termination conditions.

**Common mistakes:**

- Confusing C-rate with the capacity unit Ah. The `C` in `1C` is a ratio, whereas Ah describes charge under specified conditions.
- Treating `1C` as a universal recommended current or a guarantee of one hour of runtime. It is only a scaling of the rating; available capacity depends on test and application conditions.[^ti-crate]

If a datasheet specifies current in C-rate, multiply it by the capacity in Ah to obtain amperes, then verify that value against the separate limits for charge and discharge. For example, for `2 Ah` and an allowable `0.5C`, the current is `1 A`; it may be used only under the other conditions specified by the manufacturer.
