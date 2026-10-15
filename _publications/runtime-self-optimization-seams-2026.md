---
title: "Runtime Self-Optimization Through Knowledge-Driven Design Space Reduction"
authors:
  - Luca Brodo
  - Giuseppe Scalora
  - Stefan Henkler
date: 2026-04-13
venue: "21st International Conference on Software Engineering for Adaptive and Self-Managing Systems (SEAMS ’26)"
venue_detail: "Rio de Janeiro, Brazil, pp. 1–12"
venue_short: "SEAMS 2026"
venue_type: conference
citation_venue: "Proceedings of the 21st International Conference on Software Engineering for Adaptive and Self-Managing Systems (SEAMS ’26)"
publisher: ACM
firstpage: "1"
lastpage: "12"
status: Published
status_note: "Version of record available from ACM via the DOI."
doi: "10.1145/3788550.3794861"
pdf: /publications/runtime-self-optimization-seams-2026/brodo-2026-runtime-self-optimization-seams.pdf  # served next to the paper page (Google Scholar guideline); original kept in assets/paper/RTOPT.pdf
pdf_note: "Authors' version (CC BY 4.0)"
license: https://creativecommons.org/licenses/by/4.0/
license_label: "CC BY 4.0"
featured: true   # shown under "Selected publications"
featured_order: 3  # position in the selected list
research_area: autonomous-systems   # id from _data/research.yml (Research page grouping)
topics: [Self-adaptive systems, Optimization]
keywords:
  - runtime self-optimization
  - self-adaptive systems
  - cyber-physical systems
  - design space reduction
  - zonotopes
  - MAPE-K
  - digital twins
  - operational design domain
description: "SEAMS 2026: runtime self-optimization for cyber-physical systems that reuses proven-optimal configurations stored as zonotopes, exact yet fast."
summary_short: "Lets cyber-physical systems re-optimize their configuration at runtime by caching proven-optimal solutions as zonotope regions and pruning the design space, keeping exact optimality with heuristic-level speed."
related:
  - digital-twin-transportation-move4sps-2025
  - rtwbs-asymmetric-timed-refinement-memocode-2026
abstract: |
  Modern Cyber-Physical Systems must operate in volatile environments, with conditions that are often unpredictable at design time, requiring engineering solutions that are able to learn and optimize their configuration at runtime. However, the dimensions of modern systems, which are often complex and highly interconnected, make self-optimization at runtime a challenging task. In this paper, we propose a novel approach to runtime self-optimization that leverages knowledge-driven design space reduction to enable efficient and formally correct optimization of complex systems. Contrary to naïve re-optimization strategies, which are often prohibitive, or heuristic search methods, which sacrifice optimality, our approach guarantees optimal solutions with heuristics-level runtime performance. Specifically, by storing and reusing proven-optimal configurations and intelligently pruning the design space based on learned knowledge, we are able to significantly reduce the search space, hereby enabling fast re-optimization. Upon changes in the operational domain, the knowledge base is efficiently queried and updated, with regions expansion and merging to maintain compactness. The key idea behind the approach is to use Zonotopes as the underlying representation, which offer a compact and efficient way to represent and manipulate high-dimensional design spaces. We evaluate the approach on a smart-farming drone scenario, comparing against common optimization methods demonstrating that our approach not only preserves optimality, but also improves performance up to ∼56x compared to baseline methods with negligible memory and computation overhead.
bibtex: |
  @inproceedings{brodo2026selfoptimization,
    author    = {Brodo, Luca and Scalora, Giuseppe and Henkler, Stefan},
    title     = {Runtime Self-Optimization Through Knowledge-Driven Design Space Reduction},
    booktitle = {Proceedings of the 21st International Conference on Software Engineering for Adaptive and Self-Managing Systems},
    series    = {SEAMS '26},
    pages     = {1--12},
    year      = {2026},
    address   = {Rio de Janeiro, Brazil},
    publisher = {Association for Computing Machinery},
    doi       = {10.1145/3788550.3794861},
    url       = {https://doi.org/10.1145/3788550.3794861}
  }
---

### Research question

Cyber-physical systems such as autonomous vehicles and agricultural drones are configured at design time for a specific operational design domain (ODD). Once deployed, weather, new regulations or ageing components shift the operating conditions, and a configuration that was optimal at deployment can become suboptimal. Self-optimizing systems — a class of self-adaptive systems — should then find a new optimal configuration at runtime. Existing options force a trade-off: re-solving the full optimization problem is too slow for large, interconnected design spaces, while heuristic or search-based methods are fast but give up optimality guarantees. The paper asks whether runtime re-optimization can be both exact and fast.

### Approach

The paper proposes **knowledge-driven design space reduction**, embedded in a digital-twin architecture with a MAPE-K feedback loop. Whenever an optimal configuration is computed for some operating conditions, it is stored in a knowledge base together with the region of conditions for which it is proven optimal. When conditions change, the knowledge base is queried first: a cached configuration is reused directly if it still applies, and otherwise the optimizer searches only the regions of the design space that have not been explored before. Regions are expanded and merged as knowledge accumulates, keeping the knowledge base compact.

The key representation choice is the **zonotope**, a compact geometric description of high-dimensional sets that supports efficient retrieval, expansion and merging. The motivating scenario comes from a multi-year national project on sustainable autonomous farming, where drones adjust parameters such as altitude, speed, spray rate or sensor resolution to changing conditions, and one drone can reuse configurations already found by another.

### Results

On a smart-farming drone scenario, the approach is compared with common optimization methods. The authors report that it preserves optimality while improving performance by up to about 56× over the baselines, with negligible memory and computational overhead for managing the knowledge base.

### Why it matters

For researchers in self-adaptive systems and search-based software engineering, the paper shows a way to combine the guarantees of exact optimization with runtime performance comparable to heuristics, by treating previously solved problems as reusable, formally scoped knowledge rather than discarding them.
