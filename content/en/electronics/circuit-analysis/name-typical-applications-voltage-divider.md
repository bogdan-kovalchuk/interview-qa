---
id: emb-elcirc-0036
title: "Name typical applications of a voltage divider."
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: adi-voltage-divider
    title: "Analog Devices: Voltage Divider"
    url: https://www.analog.com/en/resources/glossary/voltage-divider.html
  - source_id: ti-voltage-divider-adc
    title: "Texas Instruments: Interfacing 5V Sensors and Signals to 3.3V Input SAR ADCs"
    url: https://www.ti.com/lit/an/sprad89/sprad89.pdf
---

## Short answer

A voltage divider scales down a signal level for an ADC input and enables measuring battery voltage if its output matches the allowed input range. A potentiometer is used as an adjustable divider to set a signal level; a passive divider itself is not a stable power source.[^adi-voltage-divider] For an ADC, one must consider its input loading, source resistance, and settling time rather than only the ideal resistor ratio.[^ti-voltage-divider-adc]

## Detailed explanation

A voltage divider uses series resistors to obtain a fraction of the input voltage at its midpoint; a typical application is scaling a signal down to match the range of a meter or an ADC input.[^adi-voltage-divider]

For two resistors `R1` and `R2`, where the output is taken across `R2`, the ideal voltage is `Vout = Vin*R2/(R1 + R2)`. This follows from the fact that the same current flows through the series resistors, and the voltage share across each equals its fraction of the total resistance. For example, with `Vin = 5 V`, `R1 = 10 kΩ`, and `R2 = 20 kΩ`, the midpoint sits at `3.33 V` without an attached load.[^adi-voltage-divider]

In practice, the midpoint exhibits non-zero output resistance. An attached load appears in parallel with `R2`, reducing the equivalent lower resistance and typically lowering the output voltage. Because of this, a divider is convenient for measurement or generating a low-current signal, but on its own it is not suitable for powering a load that draws appreciable current.[^adi-voltage-divider]

For a battery or a sensor, a divider can scale the voltage to fit ADC limits, but the ratio must be chosen so that the maximum input level does not exceed the allowed range when accounting for tolerances and transients. A SAR ADC input includes a sampling capacitor and requires time to charge; excessive source resistance can lead to settling errors. Recommendations depend on the specific ADC, sampling rate, and driving circuit, so one should check the datasheet and, if necessary, add a capacitor or buffer amplifier.[^ti-voltage-divider-adc]

**Common mistake:** Assuming the voltage calculated without a load remains guaranteed once an ADC or other circuit is connected. First account for loading in parallel with the lower resistor, and then verify the settling time and safe input limits.[^adi-voltage-divider] [^ti-voltage-divider-adc]
