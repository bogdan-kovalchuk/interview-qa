---
id: emb-elintro-0080
title: "What are the nominal voltage and frequency of Ukraine's low-voltage grid?"
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
  - source_id: nerc-voltage-quality
    title: "НКРЕКП: Якість електричної енергії"
    url: https://www.nerc.gov.ua/sferi-diyalnosti/elektroenergiya/yakist-elektropostachannya/yakist-elektrichnoyi-energiyi
  - source_id: aac-ac-magnitude
    title: "All About Circuits: Measurements of AC Magnitude"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-1/measurements-ac-magnitude
---
## Short answer

The nominal parameters of Ukraine's low-voltage grid are 230 V `RMS` and 50 Hz; the actual voltage fluctuates within permissible limits. For a sine wave, the peak would be about `325 V`, but that is a calculated amplitude, not the grid nominal.[^nerc-voltage-quality] [^aac-ac-magnitude]

## Detailed explanation

For Ukraine's low-voltage grid, the nominal voltage is `230 V RMS`, and the nominal frequency is `50 Hz`. A nominal value does not mean that the instantaneous voltage equals 230 V at all times: for a sine wave, it varies throughout each cycle, and the RMS value has a regulatory tolerance.[^nerc-voltage-quality]

NEURC specifies `230 V` between phase and neutral conductors in a three-phase four-wire low-voltage grid and `50 Hz` as the nominal frequency. For systems synchronously connected to the IPS of Ukraine, frequency quality ranges are specified: a deviation of ±1% during 99.5% of a year, as well as wider limits for all time. These are supply quality criteria, not a promise of an absolutely constant frequency at every instant.[^nerc-voltage-quality]

The same source requires that 95% of ten-minute RMS voltage values in a week be within ±10% of 230 V, that is, 207–253 V. This range helps explain why measured voltage may deviate from nominal without automatically constituting a violation of the criterion.[^nerc-voltage-quality]

For an ideal sine wave, `230 V RMS` corresponds to a peak of `230*√2 ≈ 325 V` and a peak-to-peak of about `650 V`. This is the geometry of a pure sine wave; the actual waveform may be distorted, and the measurement result depends on the instrument. A frequency of `50 Hz` means 50 complete cycles per second.[^aac-ac-magnitude] [^nerc-voltage-quality]

**Example:** for a load designed for a standard grid, you rely on the RMS voltage and the device's rated datasheet range. Peak voltage is important for insulation and components, but it should not be substituted for the grid's nominal value.[^nerc-voltage-quality] [^aac-ac-magnitude]

**Common mistake:** presenting 325 V as the "outlet voltage" or generalizing Ukraine's parameters to all of Europe without checking the national standard. Distinguish between the RMS nominal, calculated peak, and permissible tolerances; the statement here applies specifically to Ukraine.[^nerc-voltage-quality] [^aac-ac-magnitude]
