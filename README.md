![status](https://img.shields.io/badge/status-active--research-blue)
![stage](https://img.shields.io/badge/stage-early--experimental-orange)
![license](https://img.shields.io/badge/license-MIT-green)

# EED Computation Model

An empirical framework for analyzing computational cost beyond classical time complexity.

---

## Overview

Classical computer science evaluates algorithms primarily by time and space complexity.  
This model proposes that computation can be described using three interacting dimensions:

- **ΔS (Entropy)** — number of state changes / operations  
- **E (Energy)** — measured runtime (proxy)  
- **D (Causal Depth)** — dependency chain length  

We define the computational cost model as:

**C = αΔS + βE + γD**

Where α, β, γ are scaling constants.

---

## Core Claim

Across multiple algorithms and test conditions:

> No two implementations of the same computation were observed to share identical (ΔS, E, D) triplets under tested conditions.

When one dimension is constrained, the others shift.

---

## Experimental Summary

- 7 sorting algorithms tested  
- 3 input scales (n = 10, 100, 1000)  
- 50 averaged runs per configuration  
- Total measurements: **1,050**

**Result:**
- Zero non-trivial identical triplets observed  
- Near-matches diverge in at least one dimension  
- Divergence increases with scale  

---

## Methodology

See `experiments/methodology.md` for measurement definitions and testing procedure.

---

## Reproducibility

The experiment design, measurement assumptions, and testing structure are documented to allow independent replication and validation.

---

## Interpretation

This suggests that entropy (ΔS), energy (E), and causal depth (D) are not independent variables, but structurally coupled in computation.

---

## Disclaimer

- Energy is approximated using runtime and is not a direct physical measurement  
- Results are empirical and subject to refinement  
- The model is a working hypothesis, not a proven law  

---

## Status

Early-stage research.  
Actively being tested against additional algorithms and edge cases.

---

## Future Work

- Refine entropy (ΔS) measurement beyond operation counts  
- Replace runtime proxy with hardware-level energy measurement  
- Formalize causal depth (D) using DAG-based computation graphs  
- Explore equivalence classes of algorithms under EED  

---

## Note

This is an experimental model.  
The goal is to break it, refine it, or replace it.

---
