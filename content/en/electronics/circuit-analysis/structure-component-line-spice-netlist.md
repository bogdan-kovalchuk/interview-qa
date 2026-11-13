---
id: emb-elcirc-0040
title: "What is the structure of a component line in a SPICE netlist?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: ngspice-netlist-manual
    title: "ngspice User's Manual"
    url: https://ngspice.sourceforge.io/docs/ngspice-manual.pdf
---

## Short answer

In ngspice, a component line typically specifies its name, the nodes required for that specific element type, and then its value or parameters.[^ngspice-netlist-manual] For example, `R1 1 2 1k` defines a resistor, while `V1 1 0 DC 5` defines a DC source between node 1 and ground node 0; the format of remaining fields depends on the component type.[^ngspice-netlist-manual]

## Detailed explanation

In a SPICE netlist, each component is described by a line, but there is no universal number of fields across all components: their structure depends on the element type.[^ngspice-netlist-manual]

In ngspice, the first letter of an instance name specifies its component class: for example, `R` designates a resistor, `C` designates a capacitor, and `V` designates a voltage source (the full identifier, such as `R1` or `V1`, forms a single component-name token). Next, the nodes to which the component connects and its value or parameters are specified. Repeating the same node identifier across different lines indicates an electrical connection; node `0` serves as the reference ground.[^ngspice-netlist-manual]

For a simple resistor, the entry `R1 1 2 1k` specifies resistor R1 with a resistance of 1 kΩ connected between nodes 1 and 2. For an independent voltage source, `V1 1 0 DC 5` describes a 5 V source between node 1 and node 0. Node order is critical for source polarity, whereas more complex devices have additional terminals and may reference a separate model by name.[^ngspice-netlist-manual]

Lines beginning with a period are typically control directives or model definitions rather than component instances. For readability, netlists support comment lines; in ngspice, a line starting with `*` is ignored as a comment. Long lines can be continued onto the next line by starting it with `+` in accordance with parser rules.[^ngspice-netlist-manual]

**Common mistake:** Treating the pattern `name node node value` as a rigid template for every element. A resistor has two nodes and a value, whereas a transistor or subcircuit has more nodes and a model name; verify field order according to the syntax for the specific component type.[^ngspice-netlist-manual]
