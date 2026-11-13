---
id: emb-elee-0263
title: "What does a TVS diode protect against, and what does a PTC fuse protect against at a regulator input?"
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
  - source_id: littelfuse-tvs-diodes
    title: "Littelfuse Application Note: TVS Diode Application and Theory"
    url: https://www.littelfuse.com/~/media/electronics/application_notes/littelfuse_tvs_diode_application_note.pdf.pdf
  - source_id: bourns-multifuse-ptc
    title: "Bourns Multifuse Polymer PTC Resettable Fuses Application Guide"
    url: https://www.bourns.com/docs/technical-documents/technical-library/circuit-protection/publications/bourns_multifuse_app_guide.pdf
  - source_id: art-of-electronics
    title: "Horowitz P., Hill W. The Art of Electronics. 3rd ed. Cambridge University Press, 2015"
    url: https://artofelectronics.net/
---

## Short answer

A TVS diode clamps brief high-voltage transients within nanoseconds, protecting against surges like lightning, but it does not protect against sustained overcurrent. A resettable PTC fuse limits sustained overcurrent: as it heats up, its resistance rises sharply to choke current, and it resets automatically once cooled down.[^udemy-electronics-course]

## Detailed explanation

Protecting a voltage regulator input requires mitigating two fundamentally different threats: ultra-high voltage but short-duration transient spikes, and sustained overcurrent or overload conditions. To address these challenges, two complementary components are used: a TVS diode and a PTC fuse[^udemy-electronics-course][^art-of-electronics].

### TVS diode: transient overvoltage clamping

A TVS diode (Transient Voltage Suppressor) is a semiconductor device optimized for absorbing ultra-high-power transients[^littelfuse-tvs-diodes]:
- **Connection method:** Connected in **parallel** with the input power line (between the positive rail and ground).
- **Operating principle:** Based on controlled reverse avalanche breakdown of a semiconductor p-n junction (similar to a Zener diode, but with a much larger silicon die area). In the normal state at operating voltage `V_RWM` (Reverse Working Maximum), the diode is off and draws only microamperes of leakage current. When the input voltage exceeds breakdown voltage `V_BR`, diode impedance drops to fractions of an ohm, shunting excess current to ground and clamping voltage across the protected node at clamping voltage `V_clamp`[^littelfuse-tvs-diodes].
- **Response speed:** Extremely fast – response time is under 1 picosecond for silicon dies (in practice limited by package lead inductance to less than 1 ns)[^littelfuse-tvs-diodes].
- **Power handling capability:** Capable of dissipating peak pulse power of hundreds to thousands of watts (typically 400–1500 W for standard 10/1000 µs or 8/20 µs waveforms)[^littelfuse-tvs-diodes].
- **Limitations:** Does not protect against sustained overvoltage. If high voltage persists for longer than a few milliseconds, the die overheats and suffers thermal destruction, almost always failing as a short circuit (short-circuit failure mode)[^littelfuse-tvs-diodes][^art-of-electronics].

### PTC fuse: sustained overcurrent protection

A PTC fuse (Polymer Positive Temperature Coefficient, or PolySwitch) is a thermistor with a sharp positive temperature coefficient of resistance[^bourns-multifuse-ptc]:
- **Connection method:** Connected in **series** within the input supply line.
- **Operating principle:** Fabricated from a non-conductive crystalline polymer filled with finely dispersed carbon black particles that form conductive chains. At normal current, element resistance is very low (`R_initial ≈ 0.05–0.5 Ω`). When current exceeds the trip threshold (`I_trip ≈ 2 * I_hold`), Joule heating (`P = I^2 * R`) heats the polymer above its phase transition temperature (around 120–130 °C). The polymer becomes amorphous and expands, breaking the carbon conductive chains. Fuse resistance jumps by 4–6 orders of magnitude (up to tens or hundreds of kilohms), throttling fault current to a safe residual milliampere level[^bourns-multifuse-ptc].
- **Response speed:** Slow – the device relies on thermal inertia; trip time varies from hundreds of milliseconds to several seconds depending on overcurrent severity[^bourns-multifuse-ptc].
- **Self-resetting:** Once the overload is removed or power is disconnected, the polymer cools, the structure resets, and resistance returns to its initial low value[^bourns-multifuse-ptc].

### Coordination in a unified protection system

Combining a PTC fuse and a TVS diode provides coordinated multi-level protection[^bourns-multifuse-ptc][^art-of-electronics]:
1. A PTC fuse is placed in series with the input line, followed by a TVS diode connected in parallel across the rail.
2. When a microsecond high-voltage transient occurs (ESD or inductive kickback), the TVS diode clamps the voltage instantaneously, protecting the regulator input. Due to its slow thermal response, the PTC fuse ignores this brief transient.
3. If sustained overvoltage is applied to the input or a short circuit occurs in the load, the TVS diode turns on and conducts heavy current. This current rapidly heats the series-connected PTC fuse, tripping it into a high-resistance state. The PTC opens the fault path, protecting the TVS diode from burning out and saving the regulator from destruction[^bourns-multifuse-ptc][^art-of-electronics].
