---
id: emb-elintro-0082
title: "Why does a cheap 9 V wall adapter output ~14 V with no load?"
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
  - source_id: aac-transformer-regulation
    title: "All About Circuits: Voltage Regulation"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-9/voltage-regulation/
  - source_id: aac-power-supply-circuits
    title: "All About Circuits: Power Supply Circuits"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-9/power-supply-circuits/
---
## Short answer

In a simple unregulated adapter under no load, the transformer's secondary voltage may exceed nominal due to poor voltage regulation, though the exact value depends on the specific model. After the rectifier and filter capacitor, the voltage approaches the peak of the secondary sine wave minus the diode drops; the rated 9 V typically denotes the voltage under a specified load.[^aac-transformer-regulation] [^aac-power-supply-circuits]

## Detailed explanation

A cheap unregulated wall adapter often consists of a transformer, rectifier, and capacitor, without an active regulator to maintain a steady output voltage. The "9 V" rating typically refers to the output under a specific load, rather than a promise of exactly 9 V at any current. The secondary winding has resistance, and the transformer has finite internal impedance, so as load current increases, the output voltage drops; the magnitude of the change depends on the design and load.[^aac-transformer-regulation]

If the output includes a diode rectifier and a capacitor, the diodes charge the capacitor near the peaks of the input sine wave. Under light load, the capacitor loses little charge between peaks, so its voltage approaches the peak voltage of the secondary winding minus the drop across the conducting diodes. When a load is connected, the capacitor discharges between charging pulses, and the internal resistance of the transformer and diodes causes additional voltage sag.[^aac-power-supply-circuits]

An illustrative example: if the secondary winding indeed provides a `9 V RMS` sine wave under no load, its peak is approximately `9*sqrt(2) = 12.7 V`; after a bridge, it will be slightly less due to the drop across two diodes. This is only an illustration, not a measurement of the adapter from the flashcard: the 9 V printed on the case may refer to the loaded condition, and the actual secondary voltage may differ. Common mistake – assuming that approximately 14 V measured with a multimeter is necessarily 14 V DC at the output: first determine where and in which mode the measurement was made, and whether you are measuring the AC of the secondary winding or the rectified voltage.[^aac-transformer-regulation] [^aac-power-supply-circuits]
