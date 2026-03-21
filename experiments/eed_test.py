import time
import random

# --------- METRICS ---------

class Metrics:
    def __init__(self):
        self.swaps = 0
        self.comparisons = 0
        self.depth = 0

    def total_entropy(self):
        return self.swaps + self.comparisons


# --------- BUBBLE SORT ---------

def bubble_sort(arr):
    m = Metrics()
    n = len(arr)
    depth = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            m.comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                m.swaps += 1
            depth += 1

    m.depth = depth
    return arr, m


# --------- INSERTION SORT ---------

def insertion_sort(arr):
    m = Metrics()
    depth = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0:
            m.comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                m.swaps += 1
                j -= 1
            else:
                break
            depth += 1

        arr[j + 1] = key

    m.depth = depth
    return arr, m


# --------- RUN TEST ---------

def run_test(n=100):
    data = [random.randint(0, 1000) for _ in range(n)]

    for algo in [bubble_sort, insertion_sort]:
        arr = data.copy()

        start = time.time()
        _, m = algo(arr)
        end = time.time()

        E = end - start
        ΔS = m.total_entropy()
        D = m.depth

        print(f"{algo.__name__}: ΔS={ΔS}, E={E:.6f}, D={D}")


if __name__ == "__main__":
    run_test(100)
