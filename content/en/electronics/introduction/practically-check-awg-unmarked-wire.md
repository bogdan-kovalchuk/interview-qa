---
id: emb-elintro-0278
title: "How can you practically check the AWG of an unmarked wire?"
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
  - source_id: nist-awg-wire-diameter
    title: "NIST: Evaluation of Wire Detection in X-Ray Images"
    url: https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=919567
---

## Short answer

De-energize the wire, strip the insulation from the end, and measure the diameter of the bare conductor using calipers or a micrometer. Compare the measured value with an AWG table: 24 AWG is about `0.51 mm`, and 30 AWG is about `0.26 mm`.[^nist-awg-wire-diameter]

## Detailed explanation

An unmarked wire can be tentatively classified using the diameter of the bare conductor and an AWG table. Insulation is not part of the nominal conductor size, so measuring the outer diameter of the cable yields an overestimated result. Before preparing the wire, ensure that it is de-energized and that the exposed end does not touch any other conductors.[^nist-awg-wire-diameter]

Carefully strip a small section of insulation without nicking the copper, and measure the bare conductor with calipers or a micrometer. For 24 AWG, a reference is approximately `0.511 mm`, and for 30 AWG, `0.255 mm`. Close values help narrow the search, but the result depends on instrument accuracy, wire deformation, and whether the conductor is solid or stranded.[^nist-awg-wire-diameter]

If the wire is stranded, do not measure the outer contour of the bundle and compare it directly to a solid-conductor table. To determine the cross-section, you can measure individual strands and account for their count, or check the spool marking, manufacturer datasheet, or measured resistance over a known length. The first method requires careful counting; the second requires accurate length measurement and reliable contact.[^nist-awg-wire-diameter]

**Common mistake:** mistaking thick insulation for a thick copper conductor or concluding allowable current based solely on the measured diameter. AWG describes conductor size, not its thermal operating envelope in a specific assembly. After determining the size, separately verify the current and voltage ratings for the material, insulation, and installation conditions. If the size is critical for safety or terminal compatibility, use markings or manufacturer documentation rather than an approximate measurement.[^nist-awg-wire-diameter]
