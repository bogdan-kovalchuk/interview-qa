---
id: emb-elintro-0281
title: "Why are square pins used for wire wrapping?"
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
  - source_id: cooper-wire-wrap
    title: "CooperTools: Wire-Wrap Connections"
    url: https://static6.arrow.com/aropdfconversion/fc981550a66dae636e73dfb0581f75e8ea6a96eb/wirewrap.pdf
  - source_id: qatech-wire-wrap
    title: "QA Technology: Socket and Termination Selections"
    url: https://www.qatech.com/en/resources-general/socket-termination-selection.html
---

## Short answer

During wire wrapping, tensioned wire is pulled against the sharp corners of a square pin, creating multiple high-pressure contact points and a gas-tight connection. This is a property of a properly matched wire, pin, and tool, rather than a universal guarantee against any round post.[^cooper-wire-wrap]

## Detailed explanation

Wire wrapping is a mechanical method of creating a solderless electrical connection. A tool wraps stripped wire around a metal pin under controlled tension. On a square pin, the sharp corner edges bite into the wire surface, and the wire wraps around the corners at multiple points. This high localized pressure ensures intimate metal-to-metal contact; a properly executed joint is termed gas-tight because the contact areas are sealed against air ingress and corrosion.[^cooper-wire-wrap]

The square shape also provides predictable geometry for the tool's specialized wrapping bit. However, the pin shape alone is insufficient: a compatible wire diameter, terminal size, turn count, and matching wrap tool are all essential. An incorrect bit or insufficient tension can result in a loose or open wrap lacking mechanical stability. Contact resistance and reliability depend on materials, plating, and workmanship, so the term "gas-tight" does not mean that any hand-made wrap is automatically durable.[^cooper-wire-wrap]

Unlike soldering, the joint here is formed by pressure and deformation of the mating surfaces rather than by melting solder. This method is convenient for backplanes and prototypes where numerous points must be connected quickly and rewired if necessary. It requires compatible dedicated pins and tooling and is not a universal replacement for soldering or connectors.[^qatech-wire-wrap]

Example: if the terminal documentation specifies a 0.025 in square pin and 30 AWG wire, the corresponding tool bit and sleeve must be used, rather than simply wrapping arbitrary wire around any square post.[^cooper-wire-wrap]

**Common mistakes:**
- Assuming that the square shape alone guarantees reliability without the correct tool and wire parameters.
- Explaining the operating principle solely by "sharp corners" without mentioning wire tension, contact pressure, and multiple contact points.
- Claiming that a round post always slips or rotates: the outcome depends on the design of the specific termination.
