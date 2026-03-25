# The EED Conjecture
### *Entropy — Energy — Depth*

[![status](https://img.shields.io/badge/status-active--research-blue)](.)
[![stage](https://img.shields.io/badge/stage-early--experimental-orange)](.)
[![license](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![type](https://img.shields.io/badge/type-open--conjecture-purple)](.)
[![response](https://img.shields.io/badge/Aaronson-replied-gold)](.)
[![measurements](https://img.shields.io/badge/measurements-1150%2B-darkblue)](.)
[![counterexamples](https://img.shields.io/badge/counterexamples%20(n%3E6)-0-brightgreen)](.)

> **"Identical outputs do not imply identical physical processes."**

---

## What This Is

Classical computer science evaluates algorithms on time and space complexity — both of which treat computation as occurring in a physics-free environment.

This project proposes that computation has a **three-dimensional physical cost** that classical analysis discards:

```
C(n) = αΔS + βE + γD
```

Where:

| Symbol | Name | Definition |
|--------|------|-----------|
| **ΔS** | Entropy Cost | Count of irreversible state transitions in the computation DAG. Grounded in Landauer's Principle: each such operation costs at least kT ln2 joules. |
| **E** | Energy Cost | Physical energy expended. Bounded below by the Landauer limit. Measured via runtime as proxy. |
| **D** | Causal Structure | Vector: `(depth, avg_branching_factor)` — longest path in the computation DAG plus mean out-degree of non-leaf nodes. Hardware-independent structural property. |

The coefficients α, β, γ ∈ ℝ⁺ are context-dependent weights set by the physical system.

---

## The Conjecture

**EED Conjecture of Computational Distinguishability:**

> For any two structurally distinct algorithms computing the same function on inputs of size **n > n\***, no identical (ΔS, E, D) triplet has been observed under tested conditions.

**n\* = 6** — empirically located. Below n\*, degenerate cases emerge where algorithmic structures have not yet differentiated. Above n\*, no triplet match has been found.

This is a **conjecture, not a theorem**. A formal proof remains open.

---

## Why This Matters

The Von Neumann computational model recovers from C(n) by setting α=0 and γ=0 — collapsing to scalar E alone. This means:

**The Von Neumann model is a constrained special case of the EED framework.**

Two cost dimensions are discarded by the standard model. EED restores them.

---

## Evidence

| Experiment | Pairs Tested | Counterexamples (n > n*) |
|-----------|-------------|--------------------------|
| 7 sorting algorithms × 3 scales × 50 runs | 1,050 measurements | 0 |
| Cross-domain: graph, DP, recursion, parallel, search | 54 pairs | 0 |
| Targeted attack: same-logic impls, non-comparison sorts, same O(n log n) class | 45 pairs | 0 |
| Phase transition test: n=5 to n=200, 15 seeds | 15 scales | Degenerate only at n ≤ 6 |
| **Total** | **1,150+ measurements** | **0 for n > n\*** |

---

## Sharpest Single Finding

**Sequential vs Tree-Parallel Prefix Sum:**

Both algorithms achieve identical ΔS at every tested scale. But D splits by factor 2:
- Sequential: `D = (n-1, 1.0)`
- Tree-parallel: `D = (n-1, 2.0)`

Two algorithms identical by every classical metric — physically distinguished by causal structure alone. D captures parallelism potential that neither entropy analysis nor classical complexity theory expresses.

---

## Key Results

**1. Dimension Coupling**
Constraining any two dimensions produces amplified divergence in the third under tested conditions — consistent with compensatory behavior.

**2. Scale Amplification**
At n=1,000, Bubble Sort and Insertion Sort share identical ΔS=238,363 — but E splits 39,293μs vs 18,101μs and D splits 499,500 vs 239,362.

**3. Model Refinement Under Attack**
Scalar D produced false matches between 2-way and 4-way parallel tree reduction. D was enriched to a vector `(depth, branching)`, resolving all false matches. Every attack sharpened the model.

**4. EED Captures Execution, Not Labels**
BinaryInsertionSort shares an EED signature with BubbleSort — not MergeSort — because its execution is sequential despite its conceptual lineage. EED measures physical structure, not human categories.

---

## Prior Art

| Reference | Relevance |
|-----------|-----------|
| Landauer (1961) | Foundation for ΔS: every irreversible bit costs kT ln2 joules |
| Bennett (1982) | Maxwell's Demon resolution: erasure = irreversible step |
| Bennett Logical Depth (1988) | Closest prior concept to D |
| Lloyd Thermodynamic Depth (1988) | Closest ancestor of full C(n) |

---

## External Response

> *"Sorry, I don't understand the notation you're using, I don't understand what 'structurally distinct' means, etc, so I can't comment."*
> — **Scott Aaronson**, UT Austin, replied March 21 2026

Clarification sent. Conversation ongoing.

---

## Limitations

- **E is a proxy.** Runtime ≠ physical energy. Future work: hardware-level measurement via RAPL.
- **ΔS is approximate.** Operation count does not distinguish between operation types by irreversibility.
- **Python overhead.** Needs validation in C or Rust.
- **No formal proof.** The claim: no counterexample observed in 1,150+ measurements for n > n\*. Not that no counterexample can exist.
- **The EED model is empirical and subject to refinement as measurement precision improves.**

---

## Repo Structure

```
eed-computation-model/
├── experiments/
│   ├── kill_test_v1.py
│   ├── kill_test_v2.py
│   ├── kill_test_v3.py
│   ├── phase_transition.py
│   ├── brutal_kill_test.py
│   ├── enriched_d.py
│   ├── equivalence_test.py
│   └── class_theory.py
├── theory/
│   └── EED_Conjecture_Paper.pdf
├── data/
│   └── results/
└── README.md
```

---

## Open Problems

1. **Formal proof** — Does the EED Conjecture hold universally for n > n\*?
2. **Physical validation** — Replace proxies with direct hardware measurement.
3. **Untested domains** — Cryptographic operations, matrix algorithms, ML inference.
4. **Equivalence classes** — Are there algorithm families that genuinely share EED signatures?
5. **The coefficients** — What determines α, β, γ in different physical substrates?

---

## Citation

```
EED Conjecture of Computational Distinguishability
D.S. Ofuowoicho — BlackArchive Initiative
March 2026 — Draft 0.2
https://github.com/er4700345-coder/eed-computation-model
```

---

## Status

Early-stage independent research. Actively tested. No counterexample found for n > n\* across 1,150+ measurements.

**The conjecture is open. Try to break it.**

---

*Built at 2:11 AM. March 21, 2026.*
```
