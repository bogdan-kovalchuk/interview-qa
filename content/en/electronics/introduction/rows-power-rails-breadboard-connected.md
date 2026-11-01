---
id: emb-elintro-0105
title: "How are the rows and power rails of a breadboard connected?"
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
  - source_id: adafruit-breadboards
    title: "Adafruit Learning System: Breadboards for Beginners"
    url: https://learn.adafruit.com/breadboards-for-beginners?view=all
---

## Short answer

In a typical breadboard, five holes of each transverse row in the central field are connected together, while the central trench separates the left and right groups. Side power rails are designed for power distribution, but they can be interrupted in the middle or not connected to each other; check the specific board.[^adafruit-breadboards]

## Detailed explanation

In a typical solderless breadboard, metal spring contacts beneath the holes form electrical nodes. In the central field, usually five holes of a single transverse row on one side of the trench are connected together; the five holes opposite constitute a separate group. These contact groups allow component pins to be connected with short jumpers, but the layout of the holes itself does not determine the electrical connection – it is defined by internal metal contacts.[^adafruit-breadboards]

Long side power rails provide convenient points for bringing power and ground to different sections of the circuit. The "+" and "-" markings merely suggest a typical intended use: a rail has no predefined polarity until you connect a source to it. In many boards, each rail is continuous lengthwise, but rails on opposite sides are usually separate, and a long rail sometimes has a gap in the middle.[^adafruit-breadboards]

**Common mistakes:**
- Do not assume that the plus and minus rails or the left and right rails are connected to each other. Connect them with jumpers if needed.
- Check whether the rail is divided into sections. If a continuous node is required, join the sections with a jumper.
- Before applying power, check questionable points with continuity testing, especially on a different or miniature board model.[^adafruit-breadboards]
