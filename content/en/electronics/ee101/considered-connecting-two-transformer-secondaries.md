---
id: emb-elee-0176
title: "What must be considered when connecting two transformer secondaries?"
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
  - source_id: kuphaldt-phasing
    title: "Workforce LibreTexts: Lessons in Electric Circuits, Vol. II (Kuphaldt), 10.4 Phasing"
    url: https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_II_-_Alternating_Current_(Kuphaldt)/10:_Transformers/10.04:_Phasing
  - source_id: esp-transformers-part2
    title: "Elliott Sound Products: Beginners’ Guide to Transformers, Part 2 (section 8, Windings in Series and Parallel)"
    url: https://sound-au.com/xfmr2.htm
  - source_id: hammond-266m20
    title: "Hammond Manufacturing: 266M20 power transformer, dual primary and secondary (datasheet)"
    url: https://www.hammfg.com/files/parts/pdf/266M20.pdf
---

## Short answer

First determine the phasing from terminal dot conventions and verify the rated voltages of the windings.[^kuphaldt-phasing] An in-phase series connection adds the voltages, and the current is limited by the lower-rated winding; an out-of-phase series connection subtracts the voltages.[^esp-transformers-part2] Windings should be connected in parallel only if they have identical voltages, are in phase, and the manufacturer permits it: out-of-phase parallel connection creates a near dead short.[^esp-transformers-part2]

## Detailed explanation

**Phasing.** Each winding has a start and an end, and dot convention designates terminals that share the same instantaneous polarity.[^kuphaldt-phasing] Two windings connected in series aiding (in phase) add their voltages, whereas series bucking (out of phase) subtracts them.[^esp-transformers-part2] Example: a transformer with two 25 V / 5 A (250 VA) windings connected in series provides 50 V at 5 A, and in parallel provides 25 V at 10 A; total apparent power in VA remains identical.[^esp-transformers-part2] Manufacturers list such complementary configurations in datasheets: for the Hammond 266M20 (60 VA), the ratings are 20 V / 3 A in series and 10 V / 6 A in parallel, where `20*3 = 10*6 = 60 VA`.[^hammond-266m20]

**Series connection.** Windings may be connected in series regardless of whether their rated voltages match, and the maximum allowable current is limited to the rating of the lower-rated winding.[^esp-transformers-part2] A phasing error in a series connection is not destructive: for two identical windings connected out of phase, the combined output voltage is zero, causing no damage to the transformer.[^esp-transformers-part2] Consequently, such an error is immediately apparent from a zero voltage reading.

**Parallel connection.** Paralleling is permissible only for windings having identical voltages connected strictly in phase: even a 1 V difference drives a circulating current limited only by winding resistance.[^esp-transformers-part2] For two windings with 0.25 Ω resistance each, a 1 V difference produces `1/0.5 = 2 A` of circulating current, causing wasted power and excess heating. For two 25 V windings connected out of phase in parallel, the net loop voltage is 50 V, driving a circulating current on the order of `50/0.5 = 100 A` until a fuse blows or the winding burns out.[^esp-transformers-part2] The 0.25 Ω figure is an example for a 5 A winding from that same article, and the actual current will also be limited by leakage inductance.

**Recommended procedure.** A parallel configuration should be used only when explicitly permitted by the manufacturer: for the 266M20, Hammond explicitly states that the secondary windings can be used with a center tap, in parallel, or independently.[^hammond-266m20] If manufacturer guidance is unavailable, winding voltages must be measured accurately and never paralleled if they differ by more than a few hundred millivolts; any newly configured connection must be verified with an inline fuse.[^esp-transformers-part2]

**Common mistakes:**

- Paralleling windings that have unequal voltages or unknown phasing.
- Assuming that parallel connection increases voltage and series increases current (in reality, the reverse is true).
- Drawing a current greater than the rating of the lowest-rated winding in a series configuration.
- Powering up a new winding interconnection without fuse protection.
