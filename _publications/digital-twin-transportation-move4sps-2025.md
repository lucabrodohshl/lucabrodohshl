---
title: "Towards a Digital Twin Framework for Secure and Efficient Cyber-Physical Transportation Systems"
authors:
  - Luca Brodo
  - Giuseppe Scalora
  - Stefan Henkler
date: 2025-05-06
venue: "Proceedings of the 1st Workshop on Modeling and Verification for Secure and Performant Cyber-Physical Systems (MoVe4SPS ’25)"
venue_detail: "pp. 1–6"
venue_short: "MoVe4SPS 2025 Workshop"
venue_type: conference
citation_venue: "Proceedings of the 1st Workshop on Modeling and Verification for Secure and Performant Cyber-Physical Systems"
publisher: ACM
firstpage: "1"
lastpage: "6"
status: Published
status_note: "Version of record available from ACM via the DOI. No local PDF is provided on this site yet."
doi: "10.1145/3735948.3736156"
featured: false
research_area: autonomous-systems   # id from _data/research.yml (Research page grouping)
topics: [Digital twins, Cyber-physical systems]
keywords:
  - digital twins
  - cyber-physical systems
  - autonomous vehicles
  - model predictive control
  - intrusion detection
  - transportation systems
description: "MoVe4SPS 2025 paper proposing a digital twin framework that combines model predictive control and behavioural profiling for secure, efficient autonomous transport."
summary_short: "A digital twin framework for a centralised network of autonomous vehicles carrying people and goods, combining model predictive control for efficiency with behavioural profiling for intrusion detection."
related:
  - digital-twin-evolution-asyde-2026
  - runtime-self-optimization-seams-2026
abstract: |
  Cyber-Physical Systems (CPS) integrating autonomous vehicles (AVs) for mixed transport of people and goods necessitate robust methodologies to ensure secure, high-performance operations. This paper proposes a Digital Twin (DT) framework for a centralized transportation network, designed to optimize performance and enhance security using feedback-driven mechanisms. Real-time data from AVs is fed into the DT to enable Model Predictive Control (MPC), optimizing efficiency while ensuring compliance with system constraints. Behavioral profiling and pattern recognition are employed to detect misuse and anomalous vehicle behavior, bolstering system security through intrusion detection. The feedback loops compare DT predictions against real-world data to preemptively mitigate threats and operational inefficiencies, offering a flexible approach to securing and improving CPS performance.
bibtex: |
  @inproceedings{brodo2025dttransport,
    author    = {Brodo, Luca and Scalora, Giuseppe and Henkler, Stefan},
    title     = {Towards a Digital Twin Framework for Secure and Efficient Cyber-Physical Transportation Systems},
    booktitle = {Proceedings of the 1st Workshop on Modeling and Verification for Secure and Performant Cyber-Physical Systems},
    series    = {MoVe4SPS '25},
    pages     = {1--6},
    year      = {2025},
    publisher = {Association for Computing Machinery},
    doi       = {10.1145/3735948.3736156},
    url       = {https://doi.org/10.1145/3735948.3736156}
  }
---

*This overview is based on the published abstract; the full text is available from ACM via the DOI.*

### Research question

Transport networks in which autonomous vehicles (AVs) move both people and goods are cyber-physical systems with two demanding goals at once: they must operate efficiently, and they must be protected against misuse. The paper asks how a digital twin (DT) of a centrally coordinated transportation network can support both goals.

### Approach and contribution

The paper proposes a DT framework built around feedback loops. Real-time data from the vehicles feeds the digital twin, which runs **model predictive control (MPC)** to optimise efficiency while respecting the system's constraints. In parallel, behavioural profiling and pattern recognition detect misuse and anomalous vehicle behaviour, acting as an **intrusion detection** layer. By continuously comparing DT predictions with real-world observations, the framework aims to mitigate threats and operational inefficiencies before they escalate.

### Why it matters

The paper outlines how a single digital twin can serve both performance optimisation and security monitoring in cyber-physical transportation systems. Later papers by the same authors study digital twins and runtime optimisation with formal guarantees, listed under related papers below.
