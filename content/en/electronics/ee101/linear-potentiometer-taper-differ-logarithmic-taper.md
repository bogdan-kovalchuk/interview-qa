---
id: emb-elee-0013
title: "How does a linear potentiometer differ from a logarithmic one?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: analog-devices-taper
    title: "Analog Devices: Taper"
    url: https://www.analog.com/en/resources/glossary/logarithmic_linear_taper.html
---

## Short answer

In a linear potentiometer, resistance from wiper to terminal varies roughly proportionally to mechanical displacement; in a logarithmic potentiometer, this relationship is non-linear. The precise curve, direction, and A/B marking depend on the manufacturer and regional conventions, so they must be verified in the specific model datasheet.[^analog-devices-taper]

## Detailed explanation

Taper describes the relationship between the resistance from the wiper to an end terminal and the physical position of the wiper contact. In a linear potentiometer, resistance changes roughly proportionally to mechanical displacement: at the midpoint of mechanical travel, the resistance is approximately half of the total resistance. This is convenient when knob position should directly map to a fraction of a control signal, such as in a simple voltage divider.[^analog-devices-taper]

In a logarithmic potentiometer, resistance varies along a non-linear curve. For an audio taper, resistance changes more slowly at the beginning of travel and more rapidly near the end, providing a subjectively smoother volume adjustment. The actual curve is often an approximation rather than a mathematically exact logarithm; identical resistance markings across different manufacturers do not guarantee identical taper profiles.[^analog-devices-taper]

For example, in an unloaded 10 kΩ linear potentiometer, approximately 50% travel yields about 5 kΩ from the wiper to one end terminal. For an audio taper, this does not hold: the mechanical midpoint does not necessarily correspond to half the resistance or half the voltage. External loading also alters the output characteristic for both types.[^analog-devices-taper]

Markings are not universal across all markets and product series: the letter A or B can have different meanings depending on the manufacturer. Before replacing a component, check the taper description in the datasheet rather than relying solely on the letter code or vendor catalog description.[^analog-devices-taper]

**Common mistake:** applying the rule "B is linear, A is log" universally to every component and assuming that a log taper always follows an exact curve. First determine the actual characteristic from the datasheet and confirm whether it matches the circuit function.
