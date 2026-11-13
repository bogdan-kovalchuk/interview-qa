---
id: emb-elintro-0280
title: "What is wire wrapping and why is it useful?"
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
  - source_id: te-wire-wrap-terminal
    title: "TE Connectivity: AMP Type III+ Wire-Wrap Contact 66460-1"
    url: https://www.te.com/en/product-66460-1.html
---

## Short answer

Wire wrapping is a method of connecting a stripped wire by wrapping it with a tool around a dedicated square post designed for such termination. It eliminates soldering at the wire joint itself, but requires compatible posts, wire, and wrapping tools.[^te-wire-wrap-terminal]

## Detailed explanation

Wire wrapping is a method of making an electrical connection by tightly wrapping a stripped wire around a square post contact designated by the manufacturer for such termination. For example, the TE Connectivity 66460-1 contact features a square post and is specified as Wire Wrap; the manufacturer designates a compatible wire size of 32 AWG. This is a specialized wire-and-contact pair, not a universal method for wrapping any wire around any pin.[^te-wire-wrap-terminal]

During properly executed assembly, the tool forms tight turns that hold the wire on the contact post and create an electrical contact without solder in the joint. In classic assembly, a dedicated wire-wrap tool, compatible wire, and matching post are used; the dimensions, material, and plating of the contact must meet the manufacturer specifications. Requirements from one contact should not be transferred to others: even outwardly similar square pins may lack the geometry or plating required for wire wrapping.[^te-wire-wrap-terminal]

This method proved useful in backplanes with numerous connection points, prototypes, and systems where many individual wires needed to be routed neatly. It can be reworked with an unwrapping tool, but reusing wire or contact posts depends on their physical condition and the manufacturer requirements. For a practical build, strain relief, insulation, and mechanical operating conditions are also critical; the term "wire wrap" by itself does not imply that any assembly will withstand vibration or carry any current.[^te-wire-wrap-terminal]

**Common mistake:** assuming that simply twisting copper wire around an arbitrary pin by hand produces a reliable connection. First verify that the post is rated for wire-wrap and that the wire gauge and procedure match its documentation; use a dedicated tool and avoid loose wraps or nicking the conductor. If such compatibility is lacking, choose a manufacturer-specified connection method, such as soldering or an appropriate crimp.[^te-wire-wrap-terminal]
