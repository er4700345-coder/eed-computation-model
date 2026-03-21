# Experimental Methodology

This document outlines how EED measurements are obtained.

## Metrics

- ΔS (Entropy):
  Count of irreversible operations:
  - comparisons
  - swaps / writes

- E (Energy):
  Measured as execution runtime (wall-clock time)

- D (Causal Depth):
  Estimated as the number of dependent execution steps
  (loop iterations or recursive depth)

---

## Procedure

1. Select algorithms solving the same problem (e.g., sorting)
2. Generate identical random input arrays
3. Run each algorithm on the same input
4. Record:
   - total operations (ΔS)
   - runtime (E)
   - execution depth (D)

5. Repeat multiple times and average results

---

## Test Design

- Algorithms tested:
  Bubble, Insertion, Selection, Merge, Quick, Heap, Shell

- Input sizes:
  n = 10, 100, 1000

- Runs per configuration:
  50

---

## Goal

Attempt to construct two algorithms that produce identical:

(ΔS, E, D)

---

## Result

No non-trivial identical triplet observed at scale.

When one or two dimensions align, the remaining dimension diverges.

---

## Note

All measurements are approximations and subject to refinement with improved instrumentation.
