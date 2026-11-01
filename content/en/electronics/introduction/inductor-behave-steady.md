---
id: emb-elintro-0142
title: "How does an inductor behave with steady `DC`?"
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
---

## Short answer

Under steady `DC`, an ideal inductance has zero voltage because `di/dt = 0`. A real coil also has a winding resistance `R_wire`, across which a drop `V = I*R_wire` appears.[^aac-direct-current]

## Detailed explanation

Under steady direct current, the inductor's magnetic field no longer changes, so the ideal inductive component produces no voltage across its terminals. This follows from `v = L*(di/dt)`: if current is constant, its time derivative is zero. That is why an ideal inductor in steady-state `DC` is equivalent to a short circuit, not an open circuit.[^aac-direct-current]

A real coil is made of wire that has resistance, and may have additional core losses. Therefore, after the transient process ends, it can be approximated as an ideal inductance in series with winding resistance. By Ohm's law, a voltage `V = I*R_wire` remains across this resistance; it does not vanish simply because the current has become constant. For a coil with a winding resistance of `10 Ω` carrying `0.2 A`, the drop is `2 V`, provided that resistance does not change due to heating.[^aac-direct-current]

Immediately after applying a source, the behavior is different: inductance opposes a rapid change in current, so current rises gradually. In a simple series `RL` circuit, the time constant equals `τ = L/R`; after several time constants, the transient process is practically complete, although mathematically the current approaches its steady-state value asymptotically.[^aac-direct-current]

**Common mistake:** Saying that any inductor has zero resistance after settling. Zero voltage applies to the ideal inductive component; an ohmmeter on a real coil primarily measures its wire resistance, and in-circuit measurement can include parallel paths.[^aac-direct-current]
