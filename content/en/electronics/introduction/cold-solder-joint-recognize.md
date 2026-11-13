---
id: emb-elintro-0305
title: "What is a cold solder joint and how do you recognize it?"
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
  - source_id: ipc-cold-solder-definition
    title: "IPC: Acceptance Testing Of Low-Ag Reflow Solder Alloys"
    url: https://www.ipc.org/system/files/technical_resource/E38%26S14-01%20-%20KrisTroxel.pdf
  - source_id: fluke-continuity-test
    title: "Fluke: A Guide to Continuity Testing with a Multimeter"
    url: https://www.fluke.com/en-us/learn/blog/digital-multimeters/how-to-test-for-continuity
---

## Short answer

A cold solder joint exhibits poor wetting and typically has a dull, grayish, or porous appearance, often caused by insufficient heat or surface contamination. Visual inspection provides a clue rather than a definitive test, so suspicious joints should be verified with unpowered electrical measurements and reflowed or resoldered if necessary.[^ipc-cold-solder-definition]

## Detailed explanation

A cold solder joint is a soldered connection where the solder failed to properly wet the mating metal surfaces, resulting in an unreliable bond. IPC describes it as a joint exhibiting poor wetting and a dull, grayish, or porous appearance; common causes include insufficient heat, surface contamination, and impurities in the solder alloy.[^ipc-cold-solder-definition]

During visual inspection, look for a dull, grainy surface, porosity, an irregular shape, or a distinct boundary where solder balls up on the lead rather than smoothly feathering out across both lead and pad. However, surface luster alone is not a definitive criterion: different alloys and fluxes produce different finishes, and some defects remain hidden beneath component bodies. Visual cues must be evaluated in conjunction with fillet wetting angles and mechanical integrity.[^ipc-cold-solder-definition]

Electrically, the defect can manifest as an open circuit or an intermittent connection: the board works only when touched or flexed slightly, an LED flickers, or multimeter readings drift erratically. To verify the joint, disconnect power and measure continuity or resistance; interpret a zero or fluctuating reading carefully by accounting for other parallel circuit paths on the board. Never measure resistance on an energized circuit.[^fluke-continuity-test]

To prevent cold joints, ensure clean surfaces, use appropriate flux, and sufficiently heat both the lead and the pad simultaneously rather than simply melting solder against the iron tip. Do not disturb or move the component while the joint is solidifying. A suspicious joint should be cleaned if necessary and reflowed with proper thermal contact; adding more solder over a poorly wetted surface does not cure the root cause. For production assemblies, specific acceptance criteria are defined by the applicable IPC standard class and revision.[^ipc-cold-solder-definition]
