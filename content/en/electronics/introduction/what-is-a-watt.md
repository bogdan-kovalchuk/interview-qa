---
id: emb-elintro-0024
title: "What is a watt?"
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
  - source_id: bipm-si-brochure
    title: "BIPM: The International System of Units, 9th edition"
    url: https://www.bipm.org/en/si-brochure-9
---

## Short answer

The watt (W) is the unit of power; `1 W = 1 J/s`. Power describes the rate of energy transfer or conversion.[^bipm-si-brochure]

## Detailed explanation

Power indicates how much energy is transferred or converted per unit time. One watt equals one joule per second, so `P = E/t` for constant power.[^bipm-si-brochure]

In an electrical circuit, the power delivered to a load can be converted into heat, light, sound, or mechanical work. The specific outcome depends on the device, but the unit characterizes the rate of energy conversion rather than the total amount of energy.[^aac-direct-current]

For a resistive element under appropriate operating conditions, power can also be calculated as `P = V*I`. If current or voltage varies with time, instantaneous power also varies, and finding the energy over an interval requires accounting for that time dependence.[^aac-direct-current]

Equal power does not mean an equal amount of transferred energy: operating duration is also essential. For example, a load with a power of `5 W` that operates for `10 s` receives `50 J`, assuming power is constant. For a real source and load, actual values depend on the operating point and losses, so a component's rated power should not automatically be assumed to be the power it continuously consumes.[^aac-direct-current]

**Example:** a device that over `10 s` transfers `50 J` of energy has an average power of `P = E/t = 50 J/10 s = 5 W`.
