# EED Computation Model

An empirical framework for analyzing computational cost beyond classical time complexity.

## Overview

Classical computer science evaluates algorithms primarily by time and space complexity.  
This model proposes that computation can be described using three interacting dimensions:

- **ΔS (Entropy)** — number of state changes / operations
- **E (Energy)** — measured runtime (proxy)
- **D (Causal Depth)** — dependency chain length

We define the computational cost model as:

C = αΔS + βE + γD

Where α, β, γ are scaling constants.

---

## Core Claim

Across multiple algorithms and test conditions:

> No two implementations of the same computation were observed to share identical (ΔS, E, D) triplets.

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

## Interpretation

This suggests that entropy, energy, and causal depth are not independent variables, but are structurally coupled in computation.

---

## Disclaimer

- Energy is approximated using runtime and is not a direct physical measurement  
- Results are empirical and subject to refinement  
- The model is a working hypothesis, not a proven law  

---

## Status

Early-stage research.  
Actively being tested against additional algorithms and edge cases.
