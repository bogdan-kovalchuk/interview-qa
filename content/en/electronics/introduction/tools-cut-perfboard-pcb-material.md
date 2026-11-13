---
id: emb-elintro-0306
title: "Which tools can cut perfboard or PCB material?"
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
  - source_id: isola-fr402-sds
    title: "Isola FR402 Prepreg Safety Data Sheet"
    url: https://www.isola-group.com/wp-content/uploads/FR402-Prepreg-SDS-2020.07.19.pdf
---

## Short answer

Tool selection depends on board thickness, reinforcement, and construction: thin perfboard can be carefully cut with sheet-metal shears, whereas rigid fiberglass laminate requires mechanical sawing or routing with dust control. Fiberglass dust is irritating to skin and lungs, so machining requires eye protection, proper ventilation or dust collection, and clean handling procedures.[^isola-fr402-sds]

## Detailed explanation

The method used to cut a board depends on its substrate material, thickness, copper cladding, and the required edge quality. Thin perfboard can sometimes be sheared using hand tools intended for sheet material; thicker FR-4 is more safely cut using a suitable saw or router while securely clamping the workpiece. The final edge quality depends on the cutting tool and workpiece support: excessive mechanical force can flex the board, delaminate the fiberglass, or lift copper pads near the cut line.

FR-4 is a composite of woven fiberglass and epoxy resin. Mechanical machining generates fine dust and glass fibers, so never lean closely over the cutting zone or disperse waste with compressed air. For FR402, the manufacturer recommends dust extraction and local exhaust ventilation during powered machining, safety glasses with side shields, and vacuuming debris using a high-efficiency particulate air filter or wet cleanup methods.[^isola-fr402-sds] These recommendations apply specifically to the cited material; always consult the Safety Data Sheet (SDS) for your specific laminate and adhere to workshop safety rules.

Prior to cutting, scribe the line clearly, support the board firmly on both sides, and test the cutting technique on scrap material first. After cutting, deburr the edges with a fine file without touching sharp edges with bare fingers, and clean up debris and dust. If an edge must be straight and repeatable, use a saw guide or dedicated shear rather than attempting to compensate for an inappropriate tool by applying excessive force.

**Common mistakes:**

- Assuming all board substrates can be cut identically: thin perforated prototyping board and reinforced FR-4 react very differently to bending and shearing forces.
- Machining fiberglass laminate without dust control or clearing debris with compressed air; dust can irritate eyes and the respiratory tract.[^isola-fr402-sds]
- Leaving sharp edges or burrs: they can cause injury during handling and abrade wire insulation.
