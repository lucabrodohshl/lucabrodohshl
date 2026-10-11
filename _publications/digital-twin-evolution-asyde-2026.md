---
title: "Correct-by-Construction Evolution of Digital Twins for Real-Time Autonomous Systems"
authors:
  - Luca Brodo
  - Giuseppe Scalora
  - Stefan Henkler
date: 2026-10-08
venue: "Proceedings of the 8th International Workshop on Automated and verifiable Software sYstem DEvelopment (ASYDE ’26)"
venue_detail: "pp. 17–24"
venue_short: "ASYDE 2026 Workshop"
venue_type: conference
citation_venue: "Proceedings of the 8th International Workshop on Automated and verifiable Software sYstem DEvelopment"
publisher: ACM
firstpage: "17"
lastpage: "24"
status: Published
status_note: "Version of record available from ACM via the DOI. No local PDF is provided on this site yet."
doi: "10.1145/3843777.3844533"
license: https://creativecommons.org/licenses/by/4.0/
license_label: "CC BY 4.0"
featured: false
topics: [Digital twins, Real-time systems]
keywords:
  - digital twins
  - model-based systems engineering
  - refinement
  - Relaxed Weak Timed Bisimulation (RWTBS)
  - timed automata
  - code generation
  - FreeRTOS
  - ROS 2
description: "ASYDE 2026 paper: a refinement-based paradigm for digital-twin systems engineering that uses RWTBS for safe updates and compiles timed automata to FreeRTOS and ROS 2."
summary_short: "Uses refinement twice in digital-twin–based engineering: to guarantee that updates proposed by a digital twin preserve certified behaviour (via RWTBS), and to generate FreeRTOS and ROS 2 code from timed automata that is correct by construction."
related:
  - rtwbs-asymmetric-timed-refinement-memocode-2026
  - digital-twin-transportation-move4sps-2025
abstract: |
  Safety-critical cyber-physical systems must evolve---through adaptation and post-deployment updates---without forfeiting the guarantees on which their certification rests. Yet digital-twin (DT)--based model-based systems engineering (MBSE) lacks a formal mechanism for preserving correctness as the physical twin (PT) and its DT co-evolve. We argue that refinement can play this role twice: as a correctness guarantee and as a constructive device that automates deployment. We present a refinement-based paradigm for DT-based MBSE that organizes correctness into a small set of locally verifiable obligations over a multi-view decomposition and two flows for design and evolution. The central evolution obligation is instantiated by Relaxed Weak Timed Bisimulation (RWTBS), which allows a DT to propose updates to its PT that preserve output-timing while tolerating bounded input-timing flexibility. The same discipline then compiles timed automata into FreeRTOS and ROS~2 code that refines its model up to a single bounded relaxation---correct by construction.
bibtex: |
  @inproceedings{brodo2026dtevolution,
    author    = {Brodo, Luca and Scalora, Giuseppe and Henkler, Stefan},
    title     = {Correct-by-Construction Evolution of Digital Twins for Real-Time Autonomous Systems},
    booktitle = {Proceedings of the 8th International Workshop on Automated and verifiable Software sYstem DEvelopment},
    series    = {ASYDE '26},
    pages     = {17--24},
    year      = {2026},
    publisher = {Association for Computing Machinery},
    doi       = {10.1145/3843777.3844533},
    url       = {https://doi.org/10.1145/3843777.3844533}
  }
---

*This overview is based on the published abstract; the full text is available from ACM via the DOI.*

### Research question

When a safety-critical cyber-physical system is paired with a digital twin (DT), the physical twin (PT) and its DT change over time: the system adapts, receives post-deployment updates, and the models are revised. Digital-twin–based model-based systems engineering (MBSE) has, according to the paper, no formal mechanism for keeping the two correctly related as they co-evolve, even though certification depends on exactly that.

### Approach and contribution

The paper argues that **refinement** can serve two roles at once: as the correctness guarantee between versions, and as a constructive device that automates deployment. It proposes a refinement-based paradigm for DT-based MBSE that breaks correctness down into a small set of locally verifiable obligations, organised over a multi-view decomposition and two flows, one for design and one for evolution.

The central evolution obligation is discharged with **Relaxed Weak Timed Bisimulation (RWTBS)**, so a DT can propose updates to its PT that keep output timing intact while tolerating bounded flexibility in input timing. The same discipline is then used to compile timed automata into FreeRTOS and ROS 2 code that refines its model up to a single bounded relaxation, giving implementations that are correct by construction.

### Why it matters

The work connects formal timed refinement with day-to-day engineering of autonomous and real-time systems: verification obligations stay local, and code generation for common embedded and robotics platforms inherits the guarantees of the verified models. It builds directly on the RWTBS relation presented at MEMOCODE 2026.
