---
id: emb-elee-0174
title: "A transformer has a \"9 V AC\" output. What voltage will a charged capacitor show after the bridge?"
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
  - source_id: kuphaldt-transformer-regulation
    title: "Tony R. Kuphaldt: Lessons In Electric Circuits, Vol. II (AC), 10.6 Voltage Regulation (LibreTexts)"
    url: https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_II_-_Alternating_Current_(Kuphaldt)/10:_Transformers/10.06:_Voltage_Regulation
  - source_id: vishay-1n400x
    title: "Vishay: 1N4001–1N4007 datasheet"
    url: https://www.vishay.com/docs/88503/1n4001.pdf
---

## Short answer

Without a load, it will show approximately 11.3 V rather than 9 V: 9 V is the RMS value, giving a peak of `9*sqrt(2) ≈ 12.73 V`, minus two diode drops in the bridge, `2*0.7 V = 1.4 V`.[^fiore-rectification] Under load, the voltage will have ripple and sag, and the transformer's secondary voltage itself also varies with load.[^fiore-rectification][^kuphaldt-transformer-regulation]

## Detailed explanation

The designation "9 V AC" represents an RMS (root-mean-square) value, whereas a filter capacitor following a rectifier charges to the waveform peak rather than the RMS level. For a sinusoidal waveform, the peak is `sqrt(2)` times higher than the RMS value: `9*1.414 ≈ 12.73 V`. In a full-wave bridge rectifier, two diodes conduct at any given instant, meaning the load sees the secondary voltage minus two forward diode drops; approximating `0.7 V` per diode yields `12.73 - 1.4 ≈ 11.33 V`.[^fiore-rectification] This is the voltage a DC voltmeter should measure across the capacitor under no-load conditions: with negligible load, the output floats up to the peak of the secondary winding.[^fiore-rectification]

A forward drop of `0.7 V` is only an approximation. In the Vishay 1N4001–1N4007 datasheet, the maximum instantaneous forward drop at 1 A is 1.1 V.[^vishay-1n400x] Assuming this upper-bound figure on each of the two conducting diodes, `12.73 - 2*1.1 ≈ 10.5 V`, which serves as a lower bound for a bridge composed of such diodes carrying 1 A; at lighter currents the forward drop is smaller, placing the actual no-load level between `10.5 V` and `11.3 V`.

Under load, the voltage across the capacitor is no longer constant. Between AC peaks the diodes stop conducting, and the capacitor discharges into the load, creating ripple; the ripple amplitude increases with load current while the average output voltage sags.[^fiore-rectification] A rough estimate from the definition of capacitance: with a load current of `0.1 A`, `C = 1000 µF`, and a worst-case non-conduction interval of approximately `10 ms` (one half-cycle of a 50 Hz line), the voltage drop is `0.1*0.01/0.001 ≈ 1 V`, meaning the voltage fluctuates approximately between `11.3 V` and `10.3 V` assuming a constant secondary AC voltage.

Furthermore, the secondary AC voltage itself does not remain fixed. In a real transformer, secondary voltage decreases as load current increases: in the SPICE example cited from Kuphaldt, the secondary produces 9.990 V unloaded and 9.348 V at full rated load, which means the open-circuit voltage is approximately `(9.990 - 9.348)/9.348 ≈ 6.9%` higher.[^kuphaldt-transformer-regulation] If we assume a similar regulation figure for this transformer and consider "9 V" to specify full-load operation, then without load the secondary delivers `9*1.069 ≈ 9.6 V RMS`, giving a peak of `≈ 13.6 V` and a capacitor voltage of approximately `13.6 - 1.4 ≈ 12.2 V`. This calculation is purely illustrative: actual voltage regulation depends on transformer design, and a quality power transformer operating into a resistive load typically exhibits regulation under 3%.[^kuphaldt-transformer-regulation] Variations in mains line voltage likewise affect the resulting DC level.

**Common mistakes:**

- Treating "9 V AC" as DC voltage or confusing peak voltage with RMS: the capacitor charges to the peak of `RMS*sqrt(2)`.[^fiore-rectification]
- Forgetting the two diode drops in a bridge rectifier: a bridge drops two diode voltages, not one.[^fiore-rectification]
- Selecting a capacitor voltage rating close to the RMS voltage: the capacitor must be rated comfortably above the peak voltage, since under light loads the output reaches the peak.[^fiore-rectification]
- Relying on a nominal 9 V rating without considering transformer load regulation.[^kuphaldt-transformer-regulation]
