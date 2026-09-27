# Section 7 Completion and Verification Report

**Section:** 7 – Printed Circuit Board Design and Technology with CircuitMaker  
**Lectures:** 107–109 (3 lectures)  
**IQA Section:** `embedded/electronics-course-pcb-design`  
**ID Prefix:** `emb-elpcb`  
**Date:** 2026-09-27  

---

## 1. Overview and Scope

This work order completed all flashcard deliverables for Section 7 of the Udemy course "Crash Course Electronics and PCB Design" (Andre LaMothe) according to the specifications in `imports/electronics-course/pending/agy-cards-brief.md` and `meta/questions.md`.

All three lecture transcripts under `COURSE/subtitles/Section 7 - Printed Circuit Board Design and Technology with CircuitMaker` were analyzed end to end:
1. Lecture 107: *PCB Basics and Installing CircuitMaker* (37,942 bytes transcript)
2. Lecture 108: *PCB Design End to End for Beginners* (77,492 bytes transcript)
3. Lecture 109: *Hands on PCB Teardowns* (86,113 bytes transcript)

Prior to this work order, Section 7 had 11 existing flashcards authored from lecture notes (`emb-elpcb-0001` through `emb-elpcb-0011`), whose registration was pending in `imports/electronics-course/pending/section-7-registry.csv`.

During this work order:
- All 11 pre-existing questions were audited against the transcripts and verified accurate (0 factual errors).
- 14 new single-concept questions (28 Markdown files across Ukrainian and English) were authored to cover all remaining primary concepts, design rules, and hardware engineering pitfalls.
- All 25 questions (`emb-elpcb-0001` through `emb-elpcb-0025`) were registered in `meta/id-registry.csv`.
- The pending file `imports/electronics-course/pending/section-7-registry.csv` was processed and removed.
- `tests/corpus.py` was updated to reflect the new corpus size.
- The entire library passed `iqa validate` (0 blocking failures, 0 warnings) and all 111 pytest test cases passed.

The complete Section 7 card set comprises 25 questions:
- 23 `type: concept` cards covering schematic vs layout domain separation, multi-constraint placement optimization, SMT size codes, via architectures (through, blind, buried), 4-layer power/ground plane benefits, manufacturing outputs (Gerber RS-274X, NC Drill, Centroid/Pick-and-Place, BOM), 1 oz copper weight, through-hole connectors on SMT boards, ENIG vs HASL surface finishes, mixed-assembly sequences, BOM specifications, 3D visualization and STEP export for enclosure collision checking, single-layer routing display, FR-4 composite structure (core and prepreg), symmetrical stackup warpage prevention, DRC manufacturing constraints, polygon ground copper pour, ratsnest guidance, IC socket trade-offs, soldermask function and color contrast, orthogonal routing on 2-layer boards, panelization (V-scoring and mouse bites), and design-for-debugging (test points and zero-ohm jumpers).
- 2 `type: pitfall` cards covering critical hardware engineering pitfalls:
  1. `emb-elpcb-0018`: *Verifying Gerbers with independent viewer* – Preventing fatal fabrication defects caused by relying exclusively on CAD built-in viewers that mask export errors from internal project databases.
  2. `emb-elpcb-0025`: *Checking component stock and lifecycle before layout* – Avoiding costly PCB respins and layout redesigns caused by placing obsolete (EOL/NRND) or unstocked parts.

---

## 2. Per-Lecture Audit and Deliverables

### Lecture 107: PCB Basics and Installing CircuitMaker
- **Transcripts analyzed:** CircuitMaker cloud architecture and Altium lineage; cloud component libraries and community-driven design sharing; schematic editor (.SchDoc) describing logical electrical connectivity vs PCB layout (.PcbDoc) describing physical copper, footprints, and layer stackups; multi-constraint component placement optimization (mechanical enclosure boundaries, ergonomics, thermal dissipation, signal flow, and why automated placers fail); 2D vs 3D visualization modes (keys 2 and 3); rotating and inspecting boards in 3D (Shift + Right Mouse button); STEP 3D model export to MCAD packages (SolidWorks, Inventor) to verify mechanical clearances and prevent enclosure collisions; single-layer display mode (soloing active copper layers to eliminate visual clutter); imperial SMT package size codes (0805, 0603, 0402) and why 0805 is the recommended starting size for hand soldering.
- **Existing cards checked (3):**
  - `emb-elpcb-0001`: `difference-between-schematic-and-pcb-layout` (concept) – Verified accurate.
  - `emb-elpcb-0002`: `why-component-placement-not-left-automation` (concept) – Verified accurate.
  - `emb-elpcb-0003`: `smt-size-code-0805-meaning` (concept) – Verified accurate.
- **Cards fixed:** None.
- **Cards added (2):**
  - `emb-elpcb-0012`: `step-export-and-3d-pcb-clearance-verification` (concept) – 3D CAD visualization, STEP model export, and mechanical collision detection with enclosures.
  - `emb-elpcb-0013`: `single-layer-mode-pcb-routing-visibility` (concept) – Isolating active routing layers in Single Layer Mode to reduce visual clutter and inspect routing channels.

### Lecture 108: PCB Design End to End for Beginners
- **Transcripts analyzed:** Physical PCB construction and substrate materials; FR-4 (woven fiberglass impregnated with flame-retardant epoxy resin) vs FR-2 (phenolic paper); core (cured laminate with copper foil) vs prepreg (uncured resin sheets that bond cores in a lamination press); standard finished PCB thickness of 0.062 inches (1.6 mm / 62 mils); necessity of symmetrical layer stackups with even layer counts (2, 4, 6, 8) to balance thermal expansion stresses and prevent warpage (bow and twist); 4-layer stackup topology (signals outer, ground and power inner) providing short return paths, distributed interplane capacitance, and EMI suppression; via architectures (through-hole, blind, buried) and testing/cost trade-offs; Design Rule Checking (DRC) validating layout geometry against fabrication shop capabilities (minimum trace width, clearances, drill hole diameter, annular ring); ground copper pour (polygon pour) benefits (low ground return impedance, heatsinking, and balancing copper density for etching); ratsnest airwires connecting unrouted pins according to netlist; manufacturing fabrication files (Gerber RS-274X, Excellon NC Drill, Centroid / Pick-and-Place); necessity of verifying raw Gerbers with an independent third-party viewer (e.g. ViewMate by PentaLogix) to avoid built-in CAD viewer rendering bugs; copper thickness measurement in ounces per square foot ($1\text{ oz/ft}^2 \approx 35\ \mu\text{m} \approx 1{,}4\text{ mil}$).
- **Existing cards checked (4):**
  - `emb-elpcb-0004`: `through-blind-buried-vias-differ` (concept) – Verified accurate.
  - `emb-elpcb-0005`: `four-layer-pcb-inner-ground-power-planes` (concept) – Verified accurate.
  - `emb-elpcb-0006`: `files-pcb-manufacturer-assembler-need` (concept) – Verified accurate.
  - `emb-elpcb-0007`: `pcb-copper-weight-one-ounce-meaning` (concept) – Verified accurate.
- **Cards fixed:** None.
- **Cards added (6):**
  - `emb-elpcb-0014`: `pcb-substrate-fr4-core-and-prepreg` (concept) – FR-4 composite structure, cured copper-clad core, and prepreg lamination under heat and pressure.
  - `emb-elpcb-0015`: `symmetrical-pcb-layer-stackup-prevents-warping` (concept) – Symmetrical even-layer stackup balancing thermal expansion and preventing board warpage during soldering.
  - `emb-elpcb-0016`: `pcb-design-rule-check-manufacturing-constraints` (concept) – Automated DRC validation against fabricator process limits (width, clearance, drill size, annular ring).
  - `emb-elpcb-0017`: `polygon-ground-copper-pour-benefits` (concept) – Ground pour lowering return loop impedance, heatsinking power components, and balancing etching chemicals.
  - `emb-elpcb-0018`: `verifying-gerbers-with-independent-viewer` (pitfall) – Avoiding CAD built-in viewer export-masking bugs by inspecting raw manufacturing vectors in an independent viewer.
  - `emb-elpcb-0019`: `ratsnest-role-in-component-placement` (concept) – Unrouted netlist airwires guiding component placement to minimize crossings and routing congestion.

### Lecture 109: Hands on PCB Teardowns
- **Transcripts analyzed:** Physical teardowns and examination of commercial and educational boards; mechanical components (connectors, switches, potentiometers, large electrolytic capacitors) requiring through-hole mounting for mechanical strength against insertion/cable strain, with through-hole pins doubling as inter-layer routing transitions; IC sockets on prototype boards facilitating chip replacement, firmware reprogramming, and heat protection vs their elimination in production to reduce BOM cost, vertical profile, and vibration contact failure; mixed-technology assembly process order (SMT first: stencil solder paste application, pick-and-place, reflow oven; Through-Hole second: manual insertion, wave soldering or hand soldering); surface finishes on exposed copper pads: HASL (cheap, solderable, but domed/uneven surface unsuitable for fine pitch) vs ENIG (electroless nickel immersion gold providing flat, coplanar pads for fine-pitch QFP, TSSOP, and BGA); soldermask functionality (insulating copper from oxidation and preventing solder bridging during wave/reflow) and cosmetic color (green standard offering optimal optical contrast and resolution); orthogonal routing on 2-layer PCBs (horizontal top / vertical bottom) preventing channel blockage and capacitive crosstalk; board panelization for volume assembly, separating boards via V-scoring (straight score lines) and mouse bites (perforated breakout tabs); design for debugging/testing (DFD) on prototype revisions: dedicated test points on power/ground/signals, zero-ohm jumper resistors, disconnectable solder jumpers, and prototyping pads; comprehensive Bill of Materials (BOM) contents (reference designators, manufacturer part numbers, descriptions, footprints, supplier links, assembly notes with strict tolerances) and complete documentation packages for contract manufacturers; component selection discipline: checking stock levels, distributor availability, unit costs, and lifecycle status (Active vs EOL/NRND) before committing to footprints.
- **Existing cards checked (4):**
  - `emb-elpcb-0008`: `connectors-through-hole-on-smt-board` (concept) – Verified accurate.
  - `emb-elpcb-0009`: `enig-versus-hasl-surface-finish` (concept) – Verified accurate.
  - `emb-elpcb-0010`: `assembly-order-mixed-smt-through-hole-board` (concept) – Verified accurate.
  - `emb-elpcb-0011`: `bill-of-materials-contents` (concept) – Verified accurate.
- **Cards fixed:** None.
- **Cards added (6):**
  - `emb-elpcb-0020`: `ic-sockets-prototypes-versus-production` (concept) – Prototyping flexibility and thermal protection vs production cost, vertical clearance, and vibration unseating.
  - `emb-elpcb-0021`: `soldermask-function-and-color-significance` (concept) – Copper oxidation protection and solder bridge prevention vs cosmetic color choice and optical inspection contrast.
  - `emb-elpcb-0022`: `orthogonal-routing-two-layer-pcb` (concept) – Dedicated orthogonal routing directions (horizontal top / vertical bottom) preventing routing blockage and crosstalk.
  - `emb-elpcb-0023`: `pcb-panelization-v-scoring-and-mouse-bites` (concept) – Panelized batch assembly and depanelization methods using V-scoring and perforated breakout tabs.
  - `emb-elpcb-0024`: `design-for-debugging-test-points-and-jumpers` (concept) – Adding test points, zero-ohm jumpers, and prototyping pads to prototype revisions for non-destructive rework.
  - `emb-elpcb-0025`: `checking-component-stock-and-lifecycle-before-layout` (pitfall) – Verifying distributor stock, pricing, and active lifecycle status (avoiding EOL/NRND) before layout commitment.

---

## 3. Summary of Deliverables

| Metric | Value |
|---|---|
| Section | 7 – Printed Circuit Board Design and Technology with CircuitMaker |
| Lectures covered | 107–109 (3 lectures) |
| Total existing cards audited | 11 (`emb-elpcb-0001` .. `emb-elpcb-0011`) |
| Cards fixed | 0 (all 11 verified accurate) |
| Cards added | 14 (`emb-elpcb-0012` .. `emb-elpcb-0025`) |
| – Concept cards added | 12 |
| – Pitfall cards added | 2 (`emb-elpcb-0018`, `emb-elpcb-0025`) |
| Total new Markdown files authored | 28 (14 UK + 14 EN) |
| Total IDs registered in `meta/id-registry.csv` | 25 (11 previously pending + 14 new) |
| Final total cards in Section 7 | 25 |

---

## 4. Verification and Quality Gates

### A. Format and Quality Gate Audit
All 25 questions (50 Markdown files across Ukrainian and English) satisfy all project rules:
- **Sentence count:** All Ukrainian short answers strictly contain 2–5 sentences (sentence boundary detection evaluated before uppercase letters, digits, and markdown tokens).
- **Word count:** All Ukrainian short answers are well within the 90-word threshold (between 28 and 64 words).
- **Forbidden characters:** Exactly 0 occurrences of em dash U+2014 or arrows U+2190 / U+2192 across all files.
- **Mathematical formatting:** All mathematical expressions and units are formatted using `<span class="formula">\(...\)</span>`.
- **Citations:** Every Ukrainian answer terminates with `[^udemy-electronics-course]`.
- **Sources in Frontmatter:** Exactly matches across both languages with all seven required keys (`source_id`, `title`, `url`, `accessed`, `kind`, `version`, `applicability`). Sources used:
  1. `udemy-electronics-course`: primary course source referencing specific lecture transcripts.
  2. `circuitmaker-docs`: official section-level authority (*CircuitMaker documentation*).
- **English companion files:** All 25 files exist under `content/en/embedded/electronics-course-pcb-design/` with translated titles, descriptions, and standard `TODO` sections.
- **Section structure:** Concept cards have `## Short answer`, `## Detailed explanation`, and `## Sources`. Pitfall cards include `## Symptom`, `## Why it happens`, and `## How to avoid` before `## Sources`.

### B. Registry and Corpus Size Updates
- `imports/electronics-course/pending/section-7-registry.csv` rows (`emb-elpcb-0001` through `emb-elpcb-0011`) were appended to `meta/id-registry.csv`, followed by the 14 new card rows (`emb-elpcb-0012` through `emb-elpcb-0025`).
- `imports/electronics-course/pending/section-7-registry.csv` was deleted.
- `tests/corpus.py` was updated to reflect the new corpus size:
  - `FILES = 4032` (+28 files from Section 7 over 4004 baseline)
  - `QUESTIONS = 2016` (+14 questions from Section 7 over 2002 baseline)
  - `UK_CARDS = 2003` (+14 cards from Section 7 over 1989 baseline)
  - `EN_CARDS = 1055` (unchanged)

### C. Repository Validation (`python -m iqa validate`)
Validation was executed with `$env:PYTHONPATH='tools'`:
- **Result:** `checked 4032 question files, 2016 questions`.
- **Status:** **0 blocking failures, 0 warnings** across the entire repository.

### D. Packaging Verification (`python -m iqa deck --language uk`)
Export and deck compilation verified:
- `python -m iqa export`: Exported 2016 questions into `dist/export/questions.json`.
- `python -m iqa deck --language uk`: Generated `Interview QA - Full Library.apkg: 2003 notes`.

### E. Pytest Suite Execution (`python -m pytest -q -p no:cacheprovider`)
- **Result:** `111 passed in 104.42s (0:01:44)`.
- 100% passing rate with zero test failures or regressions.

---

## 5. Items Doubted or Out of Scope

None. All Section 7 deliverables are complete, verified against the primary lecture transcripts and notes, registered in `meta/id-registry.csv`, and validated through the test suite.
