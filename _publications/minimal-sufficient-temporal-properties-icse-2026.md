---
title: "What Do We Really Need? Identifying Minimal Sufficient Temporal Properties via Refinement"
authors:
  - Luca Brodo
  - Giuseppe Scalora
  - Stefan Henkler
date: 2026-04-12
venue: "2026 IEEE/ACM 48th International Conference on Software Engineering: Companion Proceedings (ICSE-Companion ’26)"
venue_detail: "Rio de Janeiro, Brazil, pp. 421–422"
venue_short: "ICSE 2026 Companion"
venue_type: conference
citation_venue: "Proceedings of the 2026 IEEE/ACM 48th International Conference on Software Engineering: Companion Proceedings (ICSE-Companion ’26)"
publisher: ACM
firstpage: "421"
lastpage: "422"
status: Published
status_note: "Two-page companion paper; version of record available from ACM via the DOI."
doi: "10.1145/3774748.3795661"
pdf: /publications/minimal-sufficient-temporal-properties-icse-2026/brodo-2026-minimal-sufficient-temporal-properties-icse.pdf  # served next to the paper page (Google Scholar guideline); original kept in assets/paper/PropRef.pdf
pdf_note: "Authors' version (CC BY 4.0)"
license: https://creativecommons.org/licenses/by/4.0/
license_label: "CC BY 4.0"
featured: false
topics: [Property refinement, CTL]
keywords:
  - property refinement
  - Computation Tree Logic (CTL)
  - model checking
  - formal verification
  - specification debt
  - redundant properties
  - minimal sufficient subset
description: "ICSE 2026 companion paper: a model-agnostic refinement relation for CTL properties that finds redundant specifications, with reductions of up to 70%."
summary_short: "A refinement relation for CTL properties, based on trace inclusion with a non-emptiness guard, that identifies which properties of a specification suite are already guaranteed by others."
related:
  - property-refinement-ltl-fse-2026
  - property-refinement-ctl
abstract: |
  Formal verification relies on specifications formalized in CTL to express desired system behaviors. In practice, specification suites grow and evolve during iterative design cycles, accumulating overlapping and semantically dependent properties that increase engineering and verification cost. We propose to address this specification debt via property refinement, which captures semantic relationships between properties, identifying when one property is already guaranteed by another. This provides engineering insights into these semantic relationships, easing requirements management and the identification of redundant properties. Our evaluation shows reductions of up to 70% and speedups of up to 30 times, showcasing the practical potential in optimising verification workflows and guiding engineers towards identifying what is really needed.
bibtex: |
  @inproceedings{brodo2026whatdoweneed,
    author    = {Brodo, Luca and Scalora, Giuseppe and Henkler, Stefan},
    title     = {What Do We Really Need? Identifying Minimal Sufficient Temporal Properties via Refinement},
    booktitle = {Proceedings of the 2026 IEEE/ACM 48th International Conference on Software Engineering: Companion Proceedings},
    series    = {ICSE-Companion '26},
    pages     = {421--422},
    year      = {2026},
    address   = {Rio de Janeiro, Brazil},
    publisher = {Association for Computing Machinery},
    doi       = {10.1145/3774748.3795661},
    url       = {https://doi.org/10.1145/3774748.3795661}
  }
---

### Research question

Specification suites written in Computation Tree Logic (CTL) tend to grow with every design iteration, and many of their properties end up overlapping or depending on one another. This short paper asks how to tell, without a system model, which CTL properties are already guaranteed by others, so that engineers can see what is really needed and avoid verifying redundant properties.

### Approach

The paper defines **property refinement** for CTL: a property refines another when its set of satisfying execution traces is included in the other's *and* is non-empty. The non-emptiness guard is what separates refinement from plain logical implication or subsumption: an unsatisfiable property implies everything but guarantees nothing, so it must not be allowed to replace weaker properties. Refinement forms a partial order up to logical equivalence, which lets mutually refining properties be collapsed into one representative and lets transitivity prune checks.

To extract a minimal sufficient subset (MSS), properties are first grouped by shared atomic propositions. Within each group, candidate pairs are compared by building alternating tree automata; because exact language inclusion is EXPTIME-complete, the paper uses a simulation relation between automata as a sound, polynomial-time approximation. The MSS consists of the properties that are not refined by any other.

### Results

On 69 benchmark suites drawn from the Model Checking Contest (MCC) and the RERS 2019 challenge, the analysis removes on average 36.6% of the properties, with reductions of up to 70%. In end-to-end experiments on synthetic models, refinement analysis followed by model checking of the MSS outperforms checking every property once models and properties become non-trivial, with speedups of up to 30×; for very small models the analysis overhead is not yet recovered.

### Why it matters

The paper shows that redundancy is common even in curated CTL suites, and that refinement gives engineers traceable insight into where dependencies between requirements come from. It complements the LTL theory published at FSE 2026; its outlook — exact refinement checking via satisfiability instead of simulation — is taken up in the later work on complete property refinement for CTL.
