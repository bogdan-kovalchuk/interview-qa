---
id: emb-elee-0177
title: "Which AC source is safe to use for self-study power supply exercises?"
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
  - source_id: hammond-catalog
    title: "Hammond Manufacturing: Transformers & Inductors catalog (Line Transformer Selection Guide; Class 2 Energy Limiting, BP series)"
    url: https://www.hammfg.com/files/literature/5c.pdf
  - source_id: busboard-bb170
    title: "BusBoard Prototype Systems: BB170 plug-in solderless breadboard (datasheet)"
    url: https://www.busboard.com/documents/datasheets/BPS-DAT-(BB170)-Datasheet.pdf
---

## Short answer

The best choice is a commercial, enclosed AC wall adapter with an isolated low-voltage AC output, manufactured and certified for this purpose.[^hammond-catalog] The exposed mains (primary) section must never be assembled on a solderless breadboard: such breadboards are rated only for tens of volts, such as 36 V and 2 A for the BusBoard BB170.[^busboard-bb170] An autotransformer is not a substitute for an isolation transformer because its output is not galvanically isolated from the mains.[^hammond-catalog]

## Detailed explanation

**Safety requirements.** Laboratory exercises with rectifiers and linear regulators require alternating voltage, so the source must be an enclosed unit where mains voltage remains fully sealed inside the housing and only isolated low voltage reaches the workbench circuit. A typical example of this type is the Hammond BP series of plug-in Class 2 energy-limiting transformers: enclosed plastic housing, 12–24 V AC output, 20 or 40 VA rating, UL and CSA certifications, with 20 VA models being "inherently limited" and requiring no internal fuse.[^hammond-catalog] A 12 V / 1.67 A model corresponds to `12*1.67 ≈ 20 VA`. This catalog covers 120 V / 60 Hz mains, so for 230 V / 50 Hz one looks for an equivalent certified wall adapter. A true AC output is required (marked AC or `~`): a DC adapter already contains a rectifier and filter, making the bridge rectifier exercise pointless.

**Isolation transformers versus autotransformers.** An isolation (double-wound) transformer features electrically separate primary and secondary windings, providing galvanic isolation from the mains line, whereas an autotransformer provides no such isolation.[^hammond-catalog] An autotransformer stepping 230 V down to 24 V reduces the voltage amplitude, but the circuit remains conductively bonded to the electrical grid. Depending on which mains conductor is connected to the common terminal and which way the plug is inserted into the wall outlet, that circuit node may carry full mains potential relative to earth ground, and an earth-grounded oscilloscope probe clip will create a direct short circuit to ground. For this reason, an autotransformer is not a safe AC source for bench learning exercises.

**Breadboard limitations.** An open primary circuit exposes uninsulated conductors carrying lethal mains voltage, whereas standard solderless breadboards are rated for much lower potentials: the BusBoard BB170 is rated for 36 V and 2 A.[^busboard-bb170] A 230 V RMS mains voltage exceeds this rating by a factor of `230/36 ≈ 6.4`, and its peak amplitude `230*sqrt(2) ≈ 325 V` is even higher. Therefore, the mains plug, fuse, and switch must remain sealed within a commercially manufactured adapter, bringing only low-voltage secondary leads onto the breadboard.

**Low-voltage hazard limits.** Low voltage does not imply zero risk: 20 VA at 12 V delivers approximately 1.7 A, which during a short circuit can quickly overheat thin jumper wires. Current should therefore be limited using an inline fuse or series circuit resistance, and the source power capability sized appropriately for the exercise.

**Common mistakes:**

- Using an autotransformer (variac) for bench exercises without a dedicated isolation transformer.
- Using a DC power adapter when the exercise begins with building a rectifier, or an AC adapter where a pre-regulated DC supply is required.
- Wiring exposed primary-side mains circuitry (mains plug, fuse, power switch) on a solderless breadboard.
- Assuming that any low-voltage source is inherently harmless regardless of available short-circuit current.
