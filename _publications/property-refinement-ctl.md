---
title: "Property Refinement in Computation Tree Logic"
authors:
  - Luca Brodo
  - Giuseppe Scalora
  - Stefan Henkler
date: 2026-09-13
date_note: "Zenodo publication date"
venue: "Preprint, deposited on Zenodo"
venue_short: "Preprint · Zenodo 2026"
venue_type: preprint
status: Preprint
status_note: "Openly available on Zenodo; no peer-reviewed venue is listed for it yet."
zenodo: https://zenodo.org/records/22734610
zenodo_doi: "10.5281/zenodo.22734610"
pdf: /publications/property-refinement-ctl/brodo-2026-property-refinement-ctl-preprint.pdf  # served next to the paper page (Google Scholar guideline); original kept in assets/paper/CTlRef.pdf
pdf_note: "Preprint (CC BY 4.0)"
license: https://creativecommons.org/licenses/by/4.0/
license_label: "CC BY 4.0"
featured: false
topics: [Property refinement, CTL]
keywords:
  - property refinement
  - Computation Tree Logic (CTL)
  - specification debt
  - CTL satisfiability
  - tableau
  - minimal sufficient set
  - formal verification
description: "Preprint by Brodo, Scalora and Henkler: a complete, decidable theory of property refinement for CTL and an exact algorithm for the minimal sufficient property set."
summary_short: "Closes the gap left by simulation-based CTL refinement: a complete, decidable refinement theory and an exact algorithm, evaluated on more than 3,000 suites with over 52,000 properties."
related:
  - minimal-sufficient-temporal-properties-icse-2026
  - property-refinement-ltl-fse-2026
abstract: |
  Safety-critical systems rely on formal methods to verify behavioral properties, often expressed in Computation Tree Logic (CTL). As these systems evolve, their specifications accumulate redundant or subsumed properties, a phenomenon known as specification debt, inflating verification effort without improving assurance. Property refinement, which captures when one property is stronger than another, offers a principled way to eliminate such redundancy. A prior extension to CTL relied on a simulation preorder over tree automata, yielding a sound but incomplete check that only over-approximates the minimal sufficient set of properties. We close this gap with a complete theory of property refinement for CTL. We show that refinement is decidable, forms a preorder, whose characteristics we leverage to propose a complete algorithm for computing the minimal sufficient set. Evaluated on more than 3,000 suites comprising over 52,000 properties, our approach proves both effective (up to 27% average reduction) and efficient (consistently lower 70 ms per refinement check), reducing the number of expensive satisfiability checks by up to a factor of six compared to prior work.
cite_note: "Citation for the Zenodo preprint. Please update it if a peer-reviewed version becomes available."
bibtex: |
  @misc{brodo2026ctlrefinement,
    author       = {Brodo, Luca and Scalora, Giuseppe and Henkler, Stefan},
    title        = {Property Refinement in Computation Tree Logic},
    year         = {2026},
    month        = sep,
    howpublished = {Preprint, Zenodo},
    publisher    = {Zenodo},
    doi          = {10.5281/zenodo.22734610},
    url          = {https://doi.org/10.5281/zenodo.22734610}
  }
---

### Research question

Property refinement — the relation stating that verifying one temporal property already guarantees another — was introduced for Linear Temporal Logic (LTL) and later carried over to Computation Tree Logic (CTL) using a simulation preorder on tree automata. Simulation implies language inclusion but not the other way round, so that check is *sound but incomplete*: it never reports a false refinement, yet it misses genuine ones and therefore keeps redundant properties in the computed minimal sufficient set. This paper asks whether refinement for CTL can be decided exactly, and at what cost.

### Approach

The authors develop a complete theory of property refinement for CTL. They show that refinement is decidable, that it is a preorder, and that it forms a lattice modulo logical equivalence. Building on these properties, they give a complete algorithm for computing the minimal sufficient set of a specification suite, deciding refinement with tableau-based CTL satisfiability checking. Because satisfiability checks are the expensive step, the algorithm reuses stored models and transitivity to rule out or confirm refinements before falling back to a full check. The analysis is model-independent: it works on the properties alone, before any system model exists.

The paper motivates the problem with an agricultural drone-monitoring example in which coverage, battery-safety and return-to-base requirements are introduced by different teams, and the combined requirement silently refines the earlier ones.

### Results

On more than 3,000 specification suites with over 52,000 properties, the approach achieves up to 27% average reduction while keeping each refinement check consistently under 70 ms, and it needs up to six times fewer expensive satisfiability checks than prior work. An ablation study quantifies the contribution of the individual optimisations.

### Why it matters

For researchers interested in specification quality, vacuity and redundancy, or CTL satisfiability, this work turns CTL property refinement from a heuristic over-approximation into an exact, decidable analysis, completing the line of work that began with refinement for LTL (FSE 2026) and the simulation-based CTL check (ICSE 2026 Companion).
