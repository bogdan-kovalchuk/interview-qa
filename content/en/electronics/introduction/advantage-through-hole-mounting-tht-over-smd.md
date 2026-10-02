---
id: emb-elintro-0013
title: What is the advantage of through-hole mounting (`THT`) over `SMD`?
description: What is the advantage of through-hole mounting (`THT`) over `SMD`?
track: electronics
section: introduction
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 3
anki:
  export: true
sources:
- source_id: udemy-electronics-course
  title: 'Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards'
  url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  accessed: 2026-09-27
  kind: community
  version: null
  applicability: 'Historical question provenance: lecture 3 of the Udemy course. Original flashcards remain in imports.
    Current answers and explanations were independently revised against cited technical sources on 2026-10-04; this
    source is not factual proof of the revised prose.'
- source_id: aac-direct-current
  title: 'All About Circuits textbook, Volume I: DC'
  url: https://www.allaboutcircuits.com/textbook/direct-current/
  accessed: 2026-09-27
  kind: book
  version: null
  applicability: 'Authoritative section-level reference: DC circuits, Ohm''s law, Kirchhoff''s laws, sources and
    measurement; specific component values and circuits of the course can differ.'
- source_id: aac-semiconductors
  title: 'All About Circuits textbook, Volume III: Semiconductors'
  url: https://www.allaboutcircuits.com/textbook/semiconductors/
  accessed: 2026-09-27
  kind: book
  version: null
  applicability: 'Authoritative section-level reference: diodes, Zener diodes, bipolar and field-effect transistors
    and power supplies; specific component values and circuits of the course can differ.'
- source_id: ti-hc00
  title: TI SN74HC00 quadruple NAND gates datasheet
  url: https://www.ti.com/lit/ds/symlink/sn74hc00.pdf
  accessed: 2026-10-04
  kind: official
  version: SCLS181H
  applicability: Section 6.3 input thresholds; switching characteristics and PDIP/SOIC package drawings.
- source_id: vishay-sizes
  title: Vishay D/CRCW e3 standard thick film chip resistors
  url: https://www.vishay.com/docs/20035/dcrcwe3.pdf
  accessed: 2026-10-04
  kind: official
  version: null
  applicability: Imperial/metric package designations and nominal dimensions of 0402/0805.
---

## Short answer

Through-hole mounting uses leads inserted through PCB holes and can be convenient for hand assembly, prototyping and some mechanically loaded connections. These advantages depend on the part and construction; it is not universally stronger than every SMD solution. Larger lead pitch can make manual handling easier. [^ti-hc00]

## Detailed explanation

THT leads pass through holes; surface-mount terminations attach to pads on the board surface. A practical advantage of many through-hole parts is physical access: leads can be handled, bent and soldered individually. Treat that as a construction-dependent reason to choose a part, not proof of universal mechanical superiority.

For a concrete geometry comparison, the TI SN74HC00 datasheet includes a PDIP package with 2.54 mm lead pitch and an SOIC package with 1.27 mm pitch. The wider pitch can make hand wiring easier. Small SMD chip resistors can be much smaller still: Vishay’s imperial 0402 body is nominally 1.0 by 0.5 mm. These are specific examples, not dimensions of all THT or all SMD components. [^ti-hc00] [^vishay-sizes]

For a connector that will be plugged repeatedly, assess the complete load path: body support, mounting hardware, solder joints and PCB construction. A through-hole lead may help retain a particular part, while a well-supported SMD connector can also be robust. SMD remains useful when board area and automated assembly matter; the choice follows the actual design requirements.

## Sources

<!-- generated from frontmatter -->
