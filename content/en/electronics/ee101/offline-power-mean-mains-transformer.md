---
id: emb-elee-0172
title: "What does offline power mean, and what does a mains transformer do?"
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
  - source_id: ti-an556
    title: "Texas Instruments AN-556 (SNVA006B): Introduction to Power Supplies"
    url: https://www.ti.com/lit/an/snva006b/snva006b.pdf
  - source_id: kuphaldt-transformer-operation
    title: "Tony R. Kuphaldt: Lessons In Electric Circuits, Vol. II (AC), 10.1 Mutual Inductance and Basic Operation (LibreTexts)"
    url: https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_II_-_Alternating_Current_(Kuphaldt)/10:_Transformers/10.01:_Mutual_Inductance_and_Basic_Operation
  - source_id: kuphaldt-transformer-isolation
    title: "Tony R. Kuphaldt: Lessons In Electric Circuits, Vol. II (AC), 10.3 Electrical Isolation (LibreTexts)"
    url: https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_II_-_Alternating_Current_(Kuphaldt)/10:_Transformers/10.03:_Electrical_Isolation
  - source_id: kuphaldt-transformer-practical
    title: "Tony R. Kuphaldt: Lessons In Electric Circuits, Vol. II (AC), 10.8 Practical Considerations – Transformers (LibreTexts)"
    url: https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_II_-_Alternating_Current_(Kuphaldt)/10:_Transformers/10.08:_Practical_Considerations_-_Transformers
---

## Short answer

Offline power draws energy directly from the AC mains. A mains transformer (50/60 Hz) converts AC voltage via magnetic coupling and provides galvanic isolation when the windings are separate, but it neither rectifies nor regulates: the secondary output remains AC.[^ti-an556][^kuphaldt-transformer-isolation] In offline switching supplies, the mains voltage is rectified before the transformer, and high-frequency transformer operation provides isolation.[^ti-an556]

## Detailed explanation

The word "offline" here describes the energy source rather than an absence of connection: an offline power supply takes energy directly from the AC utility mains rather than from a battery or pre-regulated low-voltage supply. In TI application note AN-556, an offline switching power supply is named as such because DC voltage for the power switch is generated directly from the mains line.[^ti-an556] The objectives of such a supply are the same as any other: rectify the incoming AC, convert the voltage to the required level, filter out ripple, regulate the output, and isolate the secondary from the mains; in a linear supply, these functions are performed by separate circuit stages.[^ti-an556]

A conventional linear supply with a mains transformer is constructed sequentially: a transformer with a secondary winding (center-tapped or driving a bridge), rectifier diodes, a bulk filter capacitor, and a linear regulator.[^ti-an556] The transformer in this chain solely scales the AC voltage level and isolates the circuits: alternating current in the primary winding generates an alternating magnetic flux in the common core, which induces a voltage in the secondary.[^kuphaldt-transformer-operation] If a steady DC voltage were applied across the primary, the magnetic flux in steady state would not change, producing zero secondary voltage. For example, for 12 V RMS on the secondary, the peak amplitude is `12*sqrt(2) ≈ 17.0 V`, but the voltage alternates in polarity and cannot power DC circuits until rectified.

Galvanic isolation occurs because energy is transferred via the magnetic field without a conductive electrical connection between the circuits, preventing common-mode voltages on the secondary side from reaching the primary.[^kuphaldt-transformer-isolation] This is a property of transformers with physically separate windings, and depends on construction quality: the windings must be adequately insulated from each other.[^kuphaldt-transformer-practical] A mains transformer operates at 50 or 60 Hz; core size is inversely proportional to operating frequency (within practical limits), making 50/60 Hz mains transformers physically bulky and heavy.[^ti-an556]

This is precisely why modern offline switching supplies rectify the AC mains first and perform conversion using a high-frequency switch afterwards. AN-556 explains that for supplies running off 110/220 V lines, electrical isolation is mandatory, and in a flyback topology this isolation is provided by the coupled inductor/transformer; at high switching frequencies, this transformer is vastly smaller than a 50/60 Hz mains transformer, while the feedback loop must also be isolated using an optocoupler or small pulse transformer.[^ti-an556] Thus, offline does not mean "using a 50/60 Hz mains transformer", nor does a mains transformer provide voltage regulation.

**Common mistakes:**

- Assuming a transformer provides DC voltage or regulates voltage: rectification, filtering, and regulation are handled by the diodes, capacitor, and regulator stage.[^ti-an556]
- Equating offline power supplies with supplies using 50/60 Hz transformers: in offline switching supplies, the mains line is rectified before reaching the transformer.[^ti-an556]
- Assuming galvanic isolation is inherent: it depends on winding construction and the insulation barrier between primary and secondary.[^kuphaldt-transformer-practical]
