---
title: "Bridging Social and Technical Compliance in Autonomous Systems through a Standardized Pattern Catalog"
authors:
  - Luca Brodo
  - Giuseppe Scalora
  - Lukas Walter
  - Stefan Henkler
date: 2026-10-04
venue: "ACM/IEEE 29th International Conference on Model Driven Engineering Languages and Systems: Companion Proceedings (MODELS Companion ’26)"
venue_detail: "Málaga, Spain, pp. 386–395"
venue_short: "MODELS 2026 Companion"
venue_type: conference
citation_venue: "Proceedings of the ACM/IEEE 29th International Conference on Model Driven Engineering Languages and Systems: Companion Proceedings (MODELS Companion ’26)"
publisher: ACM
firstpage: "386"
lastpage: "395"
status: Published
status_note: "Version of record available from ACM via the DOI."
doi: "10.1145/3837062.3838903"
pdf: /publications/social-norm-pattern-catalog-models-2026/brodo-2026-social-norm-pattern-catalog-models.pdf  # served next to the paper page (Google Scholar guideline); original kept in assets/paper/norms.pdf
pdf_note: "Authors' version (CC BY 4.0)"
license: https://creativecommons.org/licenses/by/4.0/
license_label: "CC BY 4.0"
featured: false
research_area: autonomous-systems   # id from _data/research.yml (Research page grouping)
topics: [Social norms, Formal verification]
keywords:
  - social norms
  - social compliance
  - formal verification
  - specification patterns
  - TCTL
  - observer automata
  - UPPAAL
  - autonomous systems
description: "MODELS 2026 Companion paper: a catalog of observer patterns that lets engineers verify social norms in TCTL/CTL alongside safety and liveness in UPPAAL."
summary_short: "A catalog of reusable observer patterns for regulative and constitutive social norms, each with a natural-language template, a (T)CTL formalization and an observer automaton for model checking."
related:
  - property-refinement-ltl-fse-2026
  - minimal-sufficient-temporal-properties-icse-2026
abstract: |
  As autonomous systems move into human-centered environments, their correctness can no longer be defined in purely technical terms. Beyond safety and liveness, these systems must comply with social norms: the implicit, context-dependent rules that govern acceptable conduct, such as yielding to pedestrians or avoiding noise near residential areas. Temporal logics such as TCTL and CTL are well established for technical properties, but engineers have no systematic way to verify social norms alongside them: encoding such norms in (T)CTL by hand is error-prone, hard to trace back to requirements, and not reusable. We address this gap with a standardized catalog of reusable observer patterns spanning both families of social norm: regulative norms, which constrain behavior (permission, prohibition, obligation, exceptions, role-based authority, and graded compliance), and constitutive norms, which create institutional facts. Each pattern couples a natural-language template, a (T)CTL formalization, and an observer automaton for integration into existing workflows. We evaluate the catalog on smart-farming and autonomous-transport scenarios, showing how engineers formalize social requirements, resolve norm conflicts, and quantify compliance–performance trade-offs.
bibtex: |
  @inproceedings{brodo2026socialnorms,
    author    = {Brodo, Luca and Scalora, Giuseppe and Walter, Lukas and Henkler, Stefan},
    title     = {Bridging Social and Technical Compliance in Autonomous Systems through a Standardized Pattern Catalog},
    booktitle = {Proceedings of the ACM/IEEE 29th International Conference on Model Driven Engineering Languages and Systems: Companion Proceedings},
    series    = {MODELS Companion '26},
    pages     = {386--395},
    year      = {2026},
    address   = {M\'{a}laga, Spain},
    publisher = {Association for Computing Machinery},
    doi       = {10.1145/3837062.3838903},
    url       = {https://doi.org/10.1145/3837062.3838903}
  }
---

### Research question

Autonomous systems are moving into places shared with people — roads, fields, residential areas. For them to be accepted, being safe and completing tasks on time is no longer enough: they also have to respect *social norms*, the implicit and context-dependent rules of acceptable conduct, such as yielding to a pedestrian or keeping quiet near homes in the evening. Timed and untimed Computation Tree Logic (TCTL and CTL), checked with tools such as UPPAAL on timed-automata models, are the standard way to verify technical properties. The paper asks how engineers can verify social norms in the same workflow, without hand-crafting error-prone temporal formulas that are hard to trace back to the original requirement.

### Approach

The paper contributes a standardized **catalog of reusable observer patterns** covering both families of social norm distinguished in the literature:

- **regulative norms**, which constrain behaviour — permission, prohibition, obligation, exceptions (defeasible norms), role-based authority and graded compliance;
- **constitutive norms**, which create institutional facts, statuses and powers, following the "X counts as Y in context C" form.

Each pattern has a three-part interface: a natural-language template for requirements elicitation, a precise (T)CTL formalization, and an observer automaton that can be composed with an existing model. Each norm is monitored by a dedicated observer that does not change the system's behaviour, so social properties can be co-verified alongside safety and liveness properties. The authors state that, to their knowledge, it is the first catalog to cover both norm families.

The running example is a fleet of autonomous tractors sharing peri-urban roads with workers, residents and traffic, with requirements such as not entering a residential zone after 5 pm unless carrying time-critical harvest, pulling over when vehicles queue behind, and entering a processing hub only with the clearance of an empowered human coordinator.

### Results

The catalog is evaluated on seven UPPAAL models from smart-farming and autonomous-transport scenarios, addressing the reusability of the patterns, verification performance and scalability, the resolution of conflicts between norms, and the quantitative impact of social norms on behaviour, i.e. the trade-off between social compliance and performance.

### Why it matters

The paper gives requirements and verification engineers a practical route from a stakeholder's social expectation to a verified temporal property, and gives researchers in normative systems a bridge to established model-checking toolchains. It applies the specification-pattern idea, well known for technical timing and behavioural properties, to social and institutional requirements of autonomous systems.
