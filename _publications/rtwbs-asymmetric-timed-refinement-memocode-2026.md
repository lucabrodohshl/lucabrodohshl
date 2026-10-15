---
title: "Asymmetric Timed Refinement for Correct Post-Deployment Updates in Real-Time Systems"
authors:
  - Luca Brodo
  - Giuseppe Scalora
  - Stefan Henkler
date: 2026-10-08
date_note: "MEMOCODE 2026 conference date"
venue: "ACM/IEEE International Symposium on Formal Methods and Models for System Design (MEMOCODE 2026)"
venue_detail: "Barcelona, Spain"
venue_short: "MEMOCODE 2026"
venue_type: conference
citation_venue: "ACM/IEEE International Symposium on Formal Methods and Models for System Design (MEMOCODE 2026)"
award: "Best Paper Award"
status: Accepted
status_note: "Presented at MEMOCODE 2026. A proceedings DOI is not yet listed here; the paper is openly available on Zenodo."
zenodo: https://zenodo.org/records/22746507
zenodo_doi: "10.5281/zenodo.22746507"
pdf: /publications/rtwbs-asymmetric-timed-refinement-memocode-2026/brodo-2026-asymmetric-timed-refinement-rtwbs-memocode.pdf  # served next to the paper page (Google Scholar guideline); original kept in assets/paper/RTWBS.pdf
pdf_note: "Authors' version (CC BY 4.0)"
license: https://creativecommons.org/licenses/by/4.0/
license_label: "CC BY 4.0"
featured: true   # shown under "Selected publications"
featured_order: 1  # position in the selected list
research_area: timed-refinement   # id from _data/research.yml (Research page grouping)
topics: [Real-time systems, Timed refinement]
keywords:
  - Relaxed Weak Timed Bisimulation (RWTBS)
  - timed refinement
  - real-time systems
  - post-deployment updates
  - model-based design
  - timed automata
  - compositional verification
  - cyber-physical systems
description: "Best Paper at MEMOCODE 2026: Relaxed Weak Timed Bisimulation (RWTBS), a timed refinement that keeps output deadlines while relaxing input timing for safe updates."
summary_short: "Introduces Relaxed Weak Timed Bisimulation (RWTBS), a refinement relation for real-time systems that strictly preserves output timing while allowing controlled relaxation of input reception timing, so buffered or asynchronous updates can be validated compositionally."
related:
  - digital-twin-evolution-asyde-2026
  - runtime-self-optimization-seams-2026
abstract: |
  Model-based systems engineering is a well-established framework for developing post-deployment updates in cyber-physical systems. In real-time and safety-critical settings in particular, these updates must be shown to preserve previously verified properties. Refinement relations over timed models provide an attractive alternative to full model checking, as they establish correctness by behavioral inclusion and can be checked efficiently and compositionally. However, traditional relations enforce symmetric timing preservation for all observable events, rejecting adaptations such as buffering or asynchronous communication, which preserve all safety-critical output deadlines but would require relaxed reception timing. We address this limitation by introducing Relaxed Weak Timed Bisimulation (RWTBS), a novel refinement relation that strictly preserves output timing while permitting controlled relaxation of input reception timing. We prove key property preservation and present a symbolic algorithm to decide RWTBS. Our evaluation demonstrates that RWTBS accepts updates rejected by classical refinement, can be used to correctly identify the operating boundary beyond which updates become unsafe, and achieves speedups of up to five orders of magnitude over model-checking with memory savings of three orders of magnitude.
cite_note: "Citation for the openly available version on Zenodo. Replace it with the proceedings entry once the MEMOCODE 2026 DOI is available."
bibtex: |
  @misc{brodo2026rwtbs,
    author       = {Brodo, Luca and Scalora, Giuseppe and Henkler, Stefan},
    title        = {Asymmetric Timed Refinement for Correct Post-Deployment Updates in Real-Time Systems},
    year         = {2026},
    howpublished = {ACM/IEEE International Symposium on Formal Methods and Models for System Design (MEMOCODE 2026)},
    note         = {Best Paper Award. Authors' version available on Zenodo},
    publisher    = {Zenodo},
    doi          = {10.5281/zenodo.22746507},
    url          = {https://doi.org/10.5281/zenodo.22746507}
  }
---

### Research question

Cyber-physical systems are increasingly updated after deployment, and in real-time and safety-critical settings every update has to preserve the guarantees that were verified before. Refinement relations over timed models are an attractive way to show this, because they establish correctness by behavioural inclusion and can be checked component by component instead of model-checking the whole system again. The problem is that classical timed refinement relations, such as timed bisimulation and its variants, demand the same timing for *every* observable event. They therefore reject perfectly reasonable updates — buffering an input, or communicating asynchronously — that keep every output deadline but receive inputs slightly later. The paper asks how to formalise this natural asymmetry between what a component must deliver on time and what it may consume with some flexibility.

### Approach

The paper introduces **Relaxed Weak Timed Bisimulation (RWTBS)**. Emitted events are treated as real-time obligations whose timing must be preserved exactly, while the reception of input events may be relaxed in a controlled way. The model grounds this in explicitly buffered input ports, separating the arrival of an event from its processing; an alternating send/receive constraint bounds buffer occupancy so that the admissible reception delay stays finite.

RWTBS is placed inside a multi-view evolution framework that relates the deployed system, a candidate update derived from a virtual or simulation-based model, and the system specification. The authors prove that RWTBS preserves key properties across updates — including output deadlines and compositional contract preservation — and give a zone-based symbolic algorithm to decide the relation, implemented in C++ with an OpenMP-parallel variant.

A motivating example is a field-survey drone whose GPS-driven position controller gains a GPS–IMU sensor-fusion filter after deployment: the 100 ms waypoint deadline is unchanged, but a GPS fix may now be consumed up to 50 ms after it arrives. Classical timed refinement rejects this update; RWTBS accepts it.

### Results

The evaluation compares compositional RWTBS checking against full model checking with UPPAAL on 20 generated timed-automata configurations representative of smart-farming models. RWTBS accepts updates that classical refinement rejects and identifies the operating boundary beyond which an update becomes unsafe. From around three components onwards, compositional checking avoids building the global product automaton: for five- and seven-component systems, RWTBS completes in well under a second where UPPAAL exceeded the ten-hour limit, a speedup of up to five orders of magnitude, with memory use about three orders of magnitude lower.

### Why it matters

RWTBS gives engineers working on real-time and cyber-physical systems a formally grounded way to validate post-deployment updates that relax input timing without touching output timing, and to do so compositionally. The relation also underpins the correct-by-construction digital-twin evolution work presented at ASYDE 2026. The paper received the **Best Paper Award** at MEMOCODE 2026.
