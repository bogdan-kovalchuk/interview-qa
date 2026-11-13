---
id: emb-elee-0017
title: "What types of potentiometers exist and where are they used?"
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
  - source_id: aac-potentiometer-types
    title: "All About Circuits: Voltage Divider Circuits"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-6/voltage-divider-circuits/
  - source_id: ad-max5481
    title: "Analog Devices: MAX5481 product page"
    url: https://www.analog.com/en/products/max5481.html
  - source_id: microchip-mcp4018
    title: "Microchip: MCP4018 product page"
    url: https://www.microchip.com/en-us/product/mcp4018
---

## Short answer

Mechanical potentiometers include rotary, slide, and trimmer configurations; digital potentiometers adjust resistance electronically. Application and available control interfaces depend on the device construction and model: for instance, specific digital ICs use SPI or I²C.[^aac-potentiometer-types] [^ad-max5481] [^microchip-mcp4018]

## Detailed explanation

A potentiometer contains a resistive track and a movable contact – the wiper – allowing it to operate as an adjustable voltage divider. The terms "rotary" and "slide" describe the mechanical movement: in the former, the wiper moves via shaft rotation, while in the latter, it moves along a linear slide. A rotary control is well suited for volume or tuning knobs; a slide potentiometer provides intuitive linear visual control and is commonly found in audio mixers. These are examples of typical usage rather than strict component limitations.[^aac-potentiometer-types]

A trimmer is a compact potentiometer designed for fine-tuning a circuit parameter during calibration or servicing, often adjusted with a screwdriver. Both single-turn and multi-turn variants exist: multi-turn models provide higher precision over a narrow adjustment window but require more rotations. Do not confuse the mechanical construction with the resistance taper: "linear" can also refer to taper, meaning the resistance profile versus displacement. A linear taper changes roughly proportionally to travel, whereas an audio control may use a logarithmic taper for more natural subjective volume adjustment.[^aac-potentiometer-types]

A digital potentiometer is an integrated circuit that sets an equivalent wiper position in discrete steps under controller command. It is useful for automated or remote tuning, storing reproducible presets, and calibration without manual mechanical access. The digital control interface cannot be generalized: the MAX5481 features SPI-compatible and up/down modes, whereas the MCP4018 uses I²C. Before selection, check the resolution (number of steps), terminal voltage range, current limits, wiper resistance, non-volatility, and interface protocol directly in the model datasheet.[^ad-max5481] [^microchip-mcp4018]

Selection example: for a manual panel signal level, a rotary potentiometer with the required resistance and taper is appropriate; for calibrating amplifier gain during production, a trimmer is preferred; for reproducible software-driven adjustments, a digital model is suitable. In each case, also verify power dissipation, accuracy, rotational life, and signal boundary limits: digital ICs often cannot be used as high-power rheostats and cannot accept voltages beyond their supply rails.[^aac-potentiometer-types] [^ad-max5481]

**Common mistake:** assuming that every mechanical potentiometer rotates through a fixed 270–300° angle or that every digital potentiometer supports both SPI and I²C. The mechanical travel geometry and digital IC features are defined by their specific datasheets; select components based on exact specifications rather than broad category names.[^aac-potentiometer-types] [^ad-max5481] [^microchip-mcp4018]
