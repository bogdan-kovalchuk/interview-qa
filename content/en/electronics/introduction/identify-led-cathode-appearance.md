---
id: emb-elintro-0116
title: "How do you identify an `LED`'s cathode by its appearance?"
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
  - source_id: aac-led-cathode
    title: "All About Circuits: Special-purpose Diodes"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-3/special-purpose-diodes/
---

## Short answer

On a standard through-hole `LED`, the shorter lead and the flat side of the package indicate the cathode; the longer lead is the anode.[^aac-led-cathode] The larger internal electrode is often also connected to the cathode, but this is not a universal rule for every package. If the leads are trimmed or the package lacks a flat side, check the markings and datasheet of the specific part.

## Detailed explanation

The cathode of an `LED` is the electrode connected to the lower potential during forward bias; in a typical through-hole package, it can be identified by the shorter lead and the flat edge of the body.[^aac-led-cathode]

An `LED` is a diode, so direction matters. In the forward direction, current flows from anode to cathode, and light emission occurs in the semiconductor junction. External markings help determine this direction prior to assembly, when electrical verification has not yet been performed.[^aac-led-cathode]

For a common round through-hole package, compare the leads: the longer one is typically the anode, the shorter one is the cathode. The package often has a notch or flat area near the cathode. Inside, the larger metal anvil is often connected to the cathode, and the thin wire to the anode; however, the internal shape should not be considered a guaranteed standard for all products.[^aac-led-cathode]

**Verification example:** if a new round `LED` has one shorter lead and one longer lead, identify the shorter one as the cathode and the longer one as the anode. If the leads are already trimmed, look for the flat side; when markings are unreadable or the package is unusual, you need to check the part number against the datasheet or test it using a multimeter's diode-test mode.

**Common mistakes:**

- Assuming that any larger internal element unmistakably indicates the cathode. Geometry depends on construction, so it is more reliable to cross-check several indicators or documentation.
- Confusing the cathode with the positive lead because the lead seems bulkier. In normal forward bias, the anode is at a higher potential than the cathode.
- Drawing a conclusion solely from the color of the plastic: it determines the package appearance, not the polarity.

After leads are trimmed, the geometric indication of length is lost, and surface-mount components have no long leads. In such cases, orientation is taken from the footprint diagram and datasheet, rather than transferring a rule for a through-hole package to another component type.[^aac-led-cathode]
