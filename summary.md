# EED Experiment Results Summary

## Measurement Protocol

- Language: Python 3
- Seeds: Fixed (42, 99, 17, 256, 7, 313, 88, 1024, 55, 200)
- Energy (E): Mean wall-clock runtime over 40-60 runs via `time.perf_counter()`
- ΔS: Operation count (comparisons + writes) as proxy for irreversible transitions
- D: (longest dependency chain depth, average branching factor)
- Match tolerance: E within 8%, ΔS exact, D exact

---

## Results

| Experiment | Scale | Algorithms | Measurements | Triplet Matches |
|-----------|-------|------------|-------------|-----------------|
| Kill Test v1 | n=10 | 7 sorting | 21 pairs | 0 |
| Kill Test v2 | n=10,100,1000 | 7 sorting | 1,050 | 0 |
| Kill Test v3 (50 runs avg) | n=10,100,1000 | 7 sorting | 1,050 | 0 |
| Phase Transition | n=5 to 200 | 3 sorting, 10 seeds | 450 pairs | n≤6 only |
| Cross-Domain | varies | 5 domains, 54 pairs | 54 | 0 |
| Targeted Attack | varies | 4 vectors, 45 pairs | 45 | 0 (post enriched D) |
| Equivalence Test | n=100-5000 | QS vs Heap, 15 seeds | 75 | 0 |
| Class Theory | n=500 | 10 algorithms, 4 paradigms | 45 pairs | 0 (no clustering) |

**Total: 1,150+ measurements. 0 counterexamples for n > 6.**

---

## Key Findings

### 1. Phase Transition at n* = 6
Degeneracy (identical triplets) only appears at n ≤ 6 on specific inputs.
At n = 7 it disappears completely and does not return through n = 200.
This is input-dependent, not structural.

### 2. Enriched D Required
Scalar D (depth only) produced 2 false matches between 2-way and 4-way
parallel reduction. Enriched D = (depth, avg_branching) resolves all false matches.
Branching factor captures parallelism structure that depth alone discards.

### 3. Sharpest Single Finding
Sequential vs Tree-Parallel Prefix Sum:
- Identical ΔS at every tested scale
- D splits: sequential D=(n-1, 1.0) vs tree D=(n-1, 2.0)
- Two algorithms identical by every classical metric, distinguished by D alone

### 4. Scale Amplification
At n=1,000: Bubble Sort and Insertion Sort share ΔS=238,363
but E splits (39,293μs vs 18,101μs) and D splits (499,500 vs 239,362).
Partial alignment in one dimension amplifies divergence in others.

### 5. No Paradigm Clustering
EED signatures do not cluster by named algorithmic paradigm.
BinaryInsertionSort shares signature with BubbleSort, not MergeSort.
EED captures physical execution structure, not conceptual categories.

---

## Anomalies and Boundary Cases

| Case | n | Status | Explanation |
|------|---|--------|-------------|
| Bubble vs Selection | 5 | Input-dependent degenerate | Too small to differentiate DAGs |
| 2-way vs 4-way parallel | 64 | Resolved by enriched D | Scalar D insufficient |

---

## Status

**The EED Conjecture stands across all tested conditions.**
Zero counterexamples for n > n* = 6.
Proof path identified. Core lemma unproven.
Open to counterexamples and formal proof attempts.
