# The EED Conjecture
### *Entropy — Energy — Depth*

[![status](https://img.shields.io/badge/status-active--research-blue)](.)
[![stage](https://img.shields.io/badge/stage-early--experimental-orange)](.)
[![license](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![conjecture](https://img.shields.io/badge/type-open--conjecture-purple)](.)

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
At n=1,000, Bubble Sort and Insertion Sort share identical ΔS=238,363 — but E splits 39,293μs vs 18,101μs and D splits 499,500 vs 239,362. Partial alignment doesn't stabilize the system. It amplifies divergence.

**3. Model Refinement Under Attack**
Scalar D produced false matches between 2-way and 4-way parallel tree reduction. D was enriched to a vector `(depth, branching)`, resolving all false matches. Every attack sharpened the model.

**4. EED Captures Execution, Not Labels**
Class theory testing showed EED signatures do not cluster by named algorithmic paradigm. BinaryInsertionSort shares an EED signature with BubbleSort — not MergeSort — because its execution is sequential despite its conceptual lineage. EED measures physical structure, not human categories.

---

## Limitations

- **E is a proxy.** Runtime ≠ physical energy. Future work: hardware-level measurement via RAPL.
- **ΔS is approximate.** Operation count does not distinguish between operation types by irreversibility. Future work: hardware-level entropy measurement.
- **Python overhead.** GC and interpreter noise affect E. Needs validation in C or Rust.
- **No formal proof.** This is empirical. The claim is precisely: no counterexample observed in 1,150+ measurements for n > n\*. Not that no counterexample can exist.
- **The EED model is empirical and subject to refinement as measurement precision improves.**

---

## Repo Structure

```
eed-computation-model/
├── experiments/
│   ├── kill_test_v1.py          # 7 sorting algorithms, basic
│   ├── kill_test_v2.py          # 7 algorithms × 3 scales × 50 runs
│   ├── kill_test_v3.py          # Averaged measurements
│   ├── phase_transition.py      # Locating n* = 6
│   ├── brutal_kill_test.py      # 5 new domains, 45 targeted pairs
│   ├── enriched_d.py            # D vector refinement
│   ├── equivalence_test.py      # QS vs Heap deep test
│   └── class_theory.py          # Paradigm clustering analysis
├── theory/
│   └── paper.pdf                # Full academic preprint (6 pages)
├── data/
│   └── results/                 # Raw measurement outputs
└── README.md
```

---

## Open Problems

1. **Formal proof** — Does the EED Conjecture hold universally for n > n\*? What is the mathematical structure behind the observed coupling?

2. **Physical validation** — Replace runtime and operation-count proxies with direct hardware measurement. Does the pattern hold at the physical layer?

3. **Untested domains** — Cryptographic operations, matrix algorithms, ML inference, numerical methods. Does the conjecture survive?

4. **Equivalence classes** — Are there algorithm families that genuinely share EED signatures? What is the structure of those classes?

5. **The coefficients** — What determines α, β, γ in different physical substrates? Do they vary predictably across hardware architectures?

---

## Citation

If you use or build on this work:

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
