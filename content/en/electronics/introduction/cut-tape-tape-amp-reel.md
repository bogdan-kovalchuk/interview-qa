---
id: emb-elintro-0180
title: "What are cut tape and tape &amp; reel?"
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
  - source_id: digikey-cut-tape
    title: "DigiKey: A Closer Look at Taped Packaging including Cut Tape and Tape and Reels"
    url: https://forum.digikey.com/t/a-closer-look-at-taped-packaging-including-cut-tape-and-tape-and-reels/17211
---

## Short answer

Cut tape is a cut strip of tape with the ordered quantity of components, convenient for small batches and prototypes. Factory tape and reel is supplied on a reel and designed for feeding components into pick-and-place equipment; the quantity on a reel depends on the specific part. The minimum order quantity for cut tape also depends on the distributor and the line item.[^digikey-cut-tape]

## Detailed explanation

In tape packaging, components sit in pockets of a carrier tape sealed with a cover tape; the tape geometry maintains them in a specified orientation. The equipment feeder advances the tape at the pitch of the pockets, and the pick-and-place machine picks up the components and places them onto the board. This packaging format helps automate assembly and protects parts during storage and transit.[^digikey-cut-tape]

Factory tape and reel is a production tape wound onto a reel according to the format of the specific component. The quantity on a reel is not fixed: it is specified by the manufacturer for a given part, and can be in the hundreds or thousands. Cut tape is a shorter section of that same tape cut by the distributor from a production reel in the ordered quantity. It is convenient for manual assembly, lab work, and prototypes, but a short section cannot always be fed directly into an automated feeder.[^digikey-cut-tape]

Some distributors offer rewinding of a short order onto a small reel with extra empty leader and trailer sections. At DigiKey, such a service is called Digi-Reel; this is a distributor-specific commercial offering, not a synonym for a full factory reel. Terms, minimum order quantity, and fees depend on the vendor, specific component, and chosen packaging.[^digikey-cut-tape]

**Example:** for a prototype of several boards, an engineer can order the required quantity of components on cut tape instead of a full factory reel. For production assembly, the tape is verified for feeder compatibility, component orientation, and leader tape requirements; the label "cut tape" alone is not enough to guarantee machine feeding.[^digikey-cut-tape]

**Common mistakes:**
- assuming that every factory reel contains the same number of parts;
- assuming that any piece of cut tape is ready for an automated line;
- treating minimum order quantity as a property of the packaging rather than a seller's condition.[^digikey-cut-tape]
