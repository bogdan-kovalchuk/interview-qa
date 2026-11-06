---
id: emb-elpcb-0006
title: "What files do the PCB manufacturer and assembler need?"
track: electronics
section: pcb-design
sources:
  - source_id: ipc-2581
    title: "IPC-2581C: Generic Requirements for Printed Board Assembly Products Manufacturing Description Data and Transfer Methodology"
    url: https://www.ipc.org/
  - source_id: ipc-d-356a
    title: "IPC-D-356A: Bare Substrate Electrical Test Data Format"
    url: https://www.ipc.org/
  - source_id: ipc-7351b
    title: "IPC-7351B: Generic Requirements for Surface Mount Design and Land Pattern Standard"
    url: https://www.ipc.org/
  - source_id: ucamco-gerber-spec
    title: "Ucamco. The Gerber Format Specification: High-level Format Description"
    url: https://www.ucamco.com/en/gerber/specification
---

## Short answer

A bare-board fabricator requires Gerber files (RS-274X or Gerber X2) for each layer (copper, solder mask, silkscreen, board outline), Excellon drill files (PTH and NPTH), and an IPC-D-356 netlist for electrical testing. For automated assembly (PCBA), the assembler additionally requires a bill of materials (BOM), a Pick-and-Place centroid file, and assembly drawings.[^ipc-2581]

## Detailed explanation

TODO
