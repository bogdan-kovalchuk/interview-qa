---
id: emb-elee-0006
title: "How does a momentary button differ from a latching switch, and what do NO and NC mean?"
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
  - source_id: aratas-switch-basics
    title: "ARATAS (formerly Omron): What is an Electrical Switch?"
    url: https://www.aratas.com/sg-en/products/basic-knowledge/switches/basics
---

## Short answer

A momentary switch maintains its active state only while actuated and returns when released; a latching switch maintains its state until actuated again. NO designates normally open contacts in the unactuated state, while NC designates normally closed contacts; actuation reverses the respective connection state.[^aratas-switch-basics]

## Detailed explanation

Momentary and latching describe the mechanical behavior of the actuator after actuation, whereas NO and NC describe the initial electrical state of the contacts. These are two independent characteristics: a pushbutton can be momentary with NO, momentary with NC, or provide both contacts, and a mechanical switch can latch into position. One should not infer the contact type from the button shape or assume all pushbuttons are momentary.[^aratas-switch-basics]

In a momentary model, a spring returns the actuator when the user stops pressing, and the contact returns to its initial state. In a latching model, the mechanism maintains the selected position after release; the next actuation changes it. Manufacturers may refer to this action as alternate or self-holding, and the specific positions and contact configuration are specified in the part datasheet.[^aratas-switch-basics]

NO stands for normally open: in the normal state, there is no conductive path between the corresponding contacts, and actuation switches it to a closed state. NC, normally closed, designates a conductive path in the normal state that is interrupted during actuation. "Normal" here refers to the unactuated state defined by the design – such as a released button – rather than the state most commonly observed in a specific system.[^aratas-switch-basics]

Example: with an NO momentary button, a microcontroller detects closure only while the button is pressed; with an NO latching switch, the contact can remain closed after release and open only upon the next actuation. The actual logic voltage depends on the connection, pull-up/pull-down resistors, and input circuitry, so NO does not automatically mean a logic high.

**Common mistake:** treating NO as synonymous with "ON". NO describes an open contact in the normal mechanical state; the external circuit determines the logic signal polarity.[^aratas-switch-basics]
