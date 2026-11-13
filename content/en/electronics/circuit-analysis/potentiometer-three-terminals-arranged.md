---
id: emb-elcirc-0004
title: "What is a potentiometer and how are its three terminals arranged?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-potentiometer-divider
    title: "All About Circuits: DC Lab - Potentiometer Voltage Divider"
    url: https://www.allaboutcircuits.com/textbook/experiments/chpt-3/potentiometer-voltage-divider/
---

## Short answer

The two outer terminals of a potentiometer connect to the opposite ends of a resistive element, while the wiper terminal makes movable contact along its track; its physical pinout depends on the package.[^aac-potentiometer-divider] The resistance between the wiper and either end terminal varies as the wiper travels, while the total resistance between the two outer terminals remains essentially constant.[^aac-potentiometer-divider]

## Detailed explanation

A potentiometer comprises a resistive element and a movable contact called a wiper. The two end terminals connect to the opposite ends of this resistive element, so the resistance measured between them represents the total track resistance. The third terminal connects to the wiper, which contacts the resistive track at varying positions as the shaft is rotated or the slider is moved.[^aac-potentiometer-divider]

The phrase "center pin" often describes its functional representation on a schematic, but it does not guarantee that the wiper is the physically central pin on every package. Manufacturers use varied pinouts, and some packages include switch terminals or redundant lugs. To determine terminal assignments on a specific component, consult its datasheet or measure resistance: the resistance between the two end terminals remains virtually constant during adjustment, whereas the resistance between the wiper and each end terminal varies in opposite directions.[^aac-potentiometer-divider]

As a voltage divider, the potentiometer's end terminals are connected across two reference potentials, and the output is tapped from the wiper. Moving the contact adjusts the fraction of the input voltage present at the wiper. When configured as a rheostat, it is connected between the wiper and one end terminal as a two-terminal variable resistor. In this mode, the third terminal is typically unused; in some circuits, the wiper is connected to the unused end terminal to reduce the risk of an open circuit if contact is lost.[^aac-potentiometer-divider]

The direction in which output voltage or resistance increases depends on which end terminal is connected to the lower potential and where the wiper is positioned along the track. Therefore, do not deduce pin functions solely from physical pin order or wire colors. Identify the terminals using a multimeter or the manufacturer pinout diagram before wiring the control into the desired circuit configuration.

**Common mistakes:**

- Referring to the wiper as the "middle pin" as an absolute rule across all physical packages.
- Expecting the resistance between the two end terminals to change during rotation.
- Assuming the output of a potentiometer is always linear with respect to shaft rotation angle: various taper curves exist.
