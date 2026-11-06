---
id: emb-elinteg-0014
title: "Why must CAD library symbols and footprints always be verified against the manufacturer datasheet?"
track: electronics
section: digital-integration
sources:
  - source_id: horowitz-hill-art-electronics
    title: "Paul Horowitz, Winfield Hill: The Art of Electronics (3rd Edition), Cambridge University Press"
    url: https://artofelectronics.net/
  - source_id: ipc-7351-generic-requirements
    title: "IPC-7351B: Generic Requirements for Surface Mount Design and Land Pattern Standard"
    url: https://www.ipc.org/
  - source_id: ti-pcb-layout-guidelines
    title: "Texas Instruments: PCB Design Guidelines for Operational Amplifiers and Logic ICs (SLVA959)"
    url: https://www.ti.com/lit/an/slva959a/slva959a.pdf
---

## Short answer

CAD library components are created by humans and frequently contain latent errors in pin numbering or signal assignments. Furthermore, schematic symbols group pins by logical function, whereas physical component footprints follow specific mechanical pin arrangements. An unverified pinout error typically yields a nonfunctional printed circuit board that requires costly redesign.[^horowitz-hill-art-electronics]

## Detailed explanation

TODO
