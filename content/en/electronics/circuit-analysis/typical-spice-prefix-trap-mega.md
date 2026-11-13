---
id: emb-elcirc-0039
title: "What is the typical mega-prefix trap in ngspice?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: ngspice-number-suffixes
    title: "ngspice User's Manual: Some naming conventions"
    url: https://nmg.gitlab.io/ngspice-manual/circuitdescription/generalstructureandconventions/somenamingconventions.html
---

## Short answer

In ngspice, the suffix `m` denotes milli (10^-3) and `Meg` denotes mega (10^6), regardless of letter case.[^ngspice-number-suffixes] Therefore, `1M` represents 1 mΩ as a numeric suffix, whereas 1 MΩ must be written as `1Meg`.[^ngspice-number-suffixes] Rules can depend on the specific SPICE-compatible simulator, so they should be checked in its manual.[^ngspice-number-suffixes]

## Detailed explanation

In ngspice, the letter `m` in a numeric suffix denotes milli, or a multiplier of 10^-3; for mega, `Meg` is used to represent 10^6.[^ngspice-number-suffixes]

This differs from standard SI notation, where an uppercase M denotes mega. ngspice parses suffixes case-insensitively, so `M` and `m` cannot represent two distinct units: both mean milli. Consequently, in a resistor line such as `R1 in out 1M`, the resistance evaluates to one milliohm rather than one megohm. For a 1 MΩ resistor, one must write `R1 in out 1Meg`.[^ngspice-number-suffixes]

This mix-up changes the value by a factor of one billion: `10^6 / 10^-3 = 10^9`. In a simple divider, this can turn an intended high resistance into a near-short-circuit, altering both branch currents and output voltages. Other suffixes are also worth remembering: `k` represents 10^3, `u` represents 10^-6, and `n` represents 10^-9; appending text unit letters after the scale suffix does not necessarily alter the numeric multiplier.[^ngspice-number-suffixes]

This rule should not be automatically assumed across all simulators. LTspice, ngspice, and other tools may accept similar but not identical syntax or additional scale suffixes. For reproducible netlists, specify which simulator is used and verify notation against its documentation; for portable examples, powers of ten can be written in exponential scientific format if parser support is confirmed.[^ngspice-number-suffixes]

**Common mistake:** Interpreting `1M` as standard SI mega without verifying parser conventions. In ngspice, use `Meg` for mega, and then check simulated or calculated quantities for the expected order of magnitude.[^ngspice-number-suffixes]
