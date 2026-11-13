---
id: emb-elintro-0284
title: "What is flux for in soldering?"
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
  - source_id: koki-flux-wetting
    title: "KOKI: Powerful Wetting Wave Soldering Flux for General Applications"
    url: https://koki-global.com/product/js-e-15x/
  - source_id: kester-cored-solder-wire
    title: "Kester: 275 Flux-Cored Wire"
    url: https://www.kester.com/products/product/275-flux-cored-wire
  - source_id: hse-solder-fume-indg248
    title: "Health and Safety Executive: Solder fume and you (INDG248)"
    url: https://www.hse.gov.uk/pubns/indg248.pdf
---

## Short answer

Flux helps remove or prevent oxide formation on heated metal surfaces and facilitates wetting by molten solder. It is not a heat transfer medium; some solder wires for hand soldering contain a flux core to deliver flux directly to the joint area.[^koki-flux-wetting] [^kester-cored-solder-wire]

## Detailed explanation

Flux is a chemical agent that facilitates the wetting of metal surfaces by solder during heating. Metal surfaces rapidly form oxides, and this thin layer prevents molten solder from coming into direct contact with the base metal. Active flux removes existing oxides or inhibits their formation during heating, allowing the solder to flow across the joint rather than beading up into a ball.[^koki-flux-wetting]

Flux is no substitute for proper heating of the joint components. Heat is transferred from the iron tip to the contacts via direct physical contact; flux simply maintains a chemically receptive surface for wetting. The required flux type is governed by the materials and soldering process. For instance, electronics flux must be compatible with circuit board substrates and cleaning procedures; plumbing acid flux must never be used on printed circuit boards. Residues of certain formulations can be corrosive, so always verify manufacturer markings and datasheets.[^koki-flux-wetting]

Solder wire for hand soldering is manufactured with a flux core; for example, the Kester 275 product line specifies various core sizes and flux percentages. When heated, this flux is delivered directly to the point where the solder melts. This is convenient, but it does not mean external flux is never necessary: on heavily oxidized surfaces or under challenging thermal conditions, supplemental flux is applied in accordance with the assembly process and material specifications.[^kester-cored-solder-wire]

Example: if solder forms a bead on an oxidized copper pad, applying a suitable electronics flux can help clean the surface and achieve wetting. If the joint itself remains cold, however, flux cannot compensate for a lack of thermal transfer from the tip or poor mechanical contact.[^koki-flux-wetting]

**Common mistakes:**
- Attributing mechanical cleaning or heat transfer to flux instead of recognizing its chemical role in oxide removal and wetting.
- Assuming any flux is suitable for electronics and leaving unidentified active residues on the board.
- Inhaling solder fumes: rosin flux fumes pose health hazards, so use proper fume extraction and keep your face out of the plume.[^hse-solder-fume-indg248]
