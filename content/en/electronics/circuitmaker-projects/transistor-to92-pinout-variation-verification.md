---
id: emb-elcmproj-0043
title: "Why must the pinout of a TO-92 transistor be verified against the manufacturer drawing?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: onsemi-2n3904
    title: "onsemi: 2N3904 / MMBT3904 General Purpose Transistors Datasheet"
    url: https://www.onsemi.com/pdf/datasheet/2n3904-d.pdf
  - source_id: nexperia-bc547
    title: "Nexperia: BC547 / BC548 NPN general-purpose transistors Datasheet"
    url: https://www.nexperia.com/products/bipolar-transistors/general-purpose-bipolar-transistors/BC547.html
  - source_id: toshiba-2sc1815
    title: "Toshiba: 2SC1815 Bipolar Transistor Silicon NPN Epitaxial Type Datasheet"
    url: https://toshiba.semicon-storage.com/info/2SC1815_datasheet_en_20140703.pdf
  - source_id: horowitz-art-of-electronics
    title: "Paul Horowitz, Winfield Hill: The Art of Electronics (3rd Edition), Cambridge University Press"
    url: https://artofelectronics.net/
---

## Short answer

The standard three-lead TO-92 package lacks a universal pinout convention. Depending on the naming standard (JEDEC, Pro Electron, or JIS), pin arrangements vary: 2N3904 uses an E-B-C pinout, BC547 uses C-B-E, and 2SC1815 uses E-C-B. Incorrect schematic symbol to footprint mapping can swap the base or invert the transistor, dropping gain to near zero or causing junction breakdown.[^onsemi-2n3904]

## Detailed explanation

TODO
