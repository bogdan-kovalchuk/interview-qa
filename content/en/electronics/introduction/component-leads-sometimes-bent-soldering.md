---
id: emb-elintro-0300
title: "Why are component leads sometimes bent before soldering?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: kingbright-lead-forming
    title: "Kingbright: Technical Notes"
    url: https://www.kingbrightusa.com/webimages/2015/catalog/Technical%20Notes.pdf
  - source_id: adafruit-perfboard
    title: "Adafruit: Collin's Lab, Breadboards & Perfboards"
    url: https://learn.adafruit.com/collins-lab-breadboards-and-perfboards?view=all
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

Leads are bent to retain through-hole components in the board prior to soldering or to match the required hole pitch. Bending must be done before soldering without applying mechanical stress to the component body, as excessive bending can damage the part or short adjacent pads.[^kingbright-lead-forming]

## Detailed explanation

Through-hole component leads may be bent to temporarily retain the part in the board when flipping it over, or to match the lead pitch to the through-hole spacing. On a perfboard, a lead is also sometimes bent over as a short bridge between pads if this aligns with the schematic. The bend itself does not establish an electrical connection to other pads: contact is made only where the lead is soldered or touches a bare conductor.[^adafruit-perfboard]

To retain a part, slightly clinching the lead tip on the solder side is sufficient; sharply flattening the lead against the board adds no reliability and makes desoldering difficult. Forming leads prior to soldering is critical. For instance, Kingbright LED application guidelines require preventing bending stress from transferring to the package body and epoxy lens, avoiding bending mounted components, and maintaining a clearance gap between the body and the first bend; specific clearance dimensions depend on the component, so consult its datasheet.[^kingbright-lead-forming]

Use needle-nose pliers or a lead-forming tool that clamps the lead close to the bend rather than gripping the component body. Do not repeatedly bend a lead back and forth: metal fatigue will occur, and mechanical stress can fracture the hermetic seal or internal bond wires. After inserting the component, inspect the solder side: trim excess lead length and ensure each lead remains clear of adjacent pads and traces. If a component features a fragile package or strict lead-forming rules, its datasheet supersedes general assembly habits.[^kingbright-lead-forming]
