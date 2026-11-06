---
id: emb-elcmproj-0010
title: "How does handling generic versus specific parts differ during schematic capture?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: altium-component-management
    title: "Altium LLC: Component Management and Unified Components in Altium Design Systems"
    url: https://www.altium.com/documentation/altium-designer
  - source_id: ipc-7351b
    title: "IPC: IPC-7351B Generic Requirements for Surface Mount Design and Land Pattern Standard, 2010"
    url: https://www.ipc.org/
  - source_id: mitzner-complete-pcb-design
    title: "Kraig Mitzner: Complete PCB Design Using OrCAD Capture and PCB Editor, 2nd Edition. Newnes, 2019"
    url: https://www.elsevier.com/books/complete-pcb-design-using-orcad-capture-and-pcb-editor/mitzner/978-0-12-817684-9
  - source_id: horowitz-art-of-electronics
    title: "Paul Horowitz, Winfield Hill: The Art of Electronics, 3rd Edition. Cambridge University Press, 2015"
    url: https://artofelectronics.net/
---

## Short answer

Generic passives (resistors, capacitors) are placed on schematics as parametric symbols, assigning standard footprints and manufacturer part numbers during BOM consolidation. Specific components (connectors, switches, microcontrollers) possess unique pinouts and mechanical geometries. Before placement, they must be mapped to exact manufacturer part numbers, verified footprints, and datasheet-matched 3D models.[^altium-component-management]

## Detailed explanation

TODO
