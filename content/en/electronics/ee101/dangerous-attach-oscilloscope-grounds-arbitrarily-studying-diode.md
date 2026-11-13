---
id: emb-elee-0140
title: "Why is it dangerous to attach oscilloscope grounds arbitrarily when studying a diode bridge?"
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
  - source_id: tektronix-abcs-probes
    title: "Tektronix: ABCs of Probes Primer"
    url: https://download.tek.com/document/02_ABCs-of-Probes-Primer.pdf
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification
---

## Short answer

Probes of a standard oscilloscope share earth ground through the line cord safety conductor, so connecting ground clips to two different bridge nodes, such as the negative DC rail and an AC input terminal, shorts out part of the bridge.[^tektronix-abcs-probes] If the bridge is fed directly from the AC mains, the ground lead also creates a dangerous short to earth ground.[^tektronix-abcs-probes] Bridges are safely studied in simulation or from an isolated low-voltage transformer secondary, keeping all ground clips on the negative DC output.

## Detailed explanation

**Why grounds are shared.** An oscilloscope displays a voltage at a point relative to its own reference node. In a standard bench oscilloscope, probes are grounded indirectly through the safety grounding conductor of the power cord, and the ground lead must only be connected to earth ground.[^tektronix-abcs-probes] Therefore, ground leads of both channels connect to a single node inside the instrument and to wall outlet earth ground: wherever you connect them, those circuit nodes become tied together into a single node. Certain oscilloscopes are specifically designed for floating measurements, but they follow dedicated operating procedures, and what is described here applies to conventional bench oscilloscopes.[^tektronix-abcs-probes]

**What happens in a bridge.** In Fiore's schematic, the negative DC output is the shared node for diodes D1 and D3: cathode D1 connects to the top secondary terminal, and cathode D3 connects to the bottom terminal.[^fiore-rectification] Suppose channel 1's ground lead is placed on the negative DC output and channel 2's ground lead is placed on the top AC terminal. Diode D1 is then directly shorted out, and during the half-cycle when the top terminal is positive, current flows through the secondary winding, through these grounding leads, and through forward-biased D3, completely bypassing the load and D2.[^fiore-rectification] The current is limited only by the winding and lead impedances. An illustrative estimate: for 12 V RMS, the peak is `12*sqrt(2) ≈ 17.0 V`, and assuming a total loop resistance of 1 Ω, the surge would be `(17.0 - 0.7)/1 ≈ 16 A`. This destroys D3, damages the transformer, and burns out the thin probe ground leads.

**Mains-fed circuits.** If the bridge is powered directly from the AC line without an isolation transformer, none of its nodes (with the possible exception of neutral) are at earth ground potential, so attaching a ground lead shorts a live node directly to earth ground. Tektronix notes in an example of a motor drive with a rectified mains bus that placing a probe ground lead on any part of such a circuit creates a short circuit to earth ground; a transformerless bridge rectifier poses the identical hazard.[^tektronix-abcs-probes] Attempting to "work around" this by cutting or "cheating" the oscilloscope earth ground is even more dangerous: the instrument chassis can float at mains potential.[^tektronix-abcs-probes]

**How to measure safely.** Use an isolated low-voltage transformer secondary, connect all probe ground leads to a single node (such as the negative DC rail), and measure other nodes using the probe tips referenced to that ground. To measure voltage between two nodes where neither is ground, use a high-voltage differential probe or an isolated measurement system; channel subtraction (A - B) is typically the poorest alternative.[^tektronix-abcs-probes] For educational study, circuit simulation is also well-suited.

**Common mistakes:**

- Connecting the ground clips of two channels to different nodes in the circuit.
- Removing or floating the power cord ground pin to float the oscilloscope at bridge potential.
- Using a standard oscilloscope to measure a bridge connected directly to the AC mains.
