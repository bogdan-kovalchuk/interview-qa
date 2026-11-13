---
id: emb-elintro-0286
title: "What is a hot air station for?"
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
  - source_id: hakko-fr801-manual
    title: "HAKKO FR-801 SMD Rework Station Instruction Manual"
    url: https://www.hakko.com/english/support/doc/result.php?mode=download&seq=4968
---

## Short answer

A hot air station provides adjustable heated air and airflow for localized heating of solder during SMD component assembly or rework. The component and pads are heated until the solder melts, with airflow and temperature settings chosen based on the nozzle, board, and component package.[^hakko-fr801-manual] The station's displayed temperature does not necessarily match the temperature of the part itself, so verify it separately if needed.[^hakko-fr801-manual]

## Detailed explanation

A hot air station is a tool for localized board heating using a stream of heated air. Unlike a soldering iron that transfers heat through tip contact, a hot air station heats multiple leads or board regions simultaneously. This is convenient for multi-lead SMD packages, such as QFP, as well as for desoldering small chip resistors and capacitors. Once the solder on all target leads reaches its melting point, the component can be lifted without tearing copper pads off the board.[^hakko-fr801-manual]

On the station, temperature and airflow rate are adjusted independently. Nozzle size, standoff distance to the board, dwell time, and thermal mass of the assembly are also critical. The same dial setting does not guarantee the same component temperature across different stations, which is why manufacturer HAKKO describes measuring temperature not only in the air stream near the nozzle, but also directly on the workpiece. Excessive airflow can dislodge adjacent lightweight components, while excessive heating can damage the component body or laminate.[^hakko-fr801-manual]

Example: when desoldering a QFP, a matching nozzle is directed at the lead rows and heats them evenly; the operator waits until the solder fully melts and only then lifts the package using a vacuum pickup or tweezers. After rework, the joints must be inspected, because hot air does not inherently prevent solder bridging, solder balls, or insufficient wetting.[^hakko-fr801-manual]

**Common mistakes:** assuming the set temperature reflects the temperature of the component itself, setting excessive airflow, or pulling on the component body before the solder has completely melted. Process settings should be chosen based on component and solder paste datasheets, results verified under magnification, and adjacent parts shielded from the hot air stream.
