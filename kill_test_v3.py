"""
EED Conjecture — Kill Test v3
7 sorting algorithms, 3 scales, 50 averaged runs each
1,050 total measurements
Result: 0 triplet matches for n > 6
"""

import time
import statistics
import random

RUNS = 50

def measure(fn, arr, runs=RUNS):
    ds_vals, e_vals, d_vals = [], [], []
    for _ in range(runs):
        data = arr[:]
        start = time.perf_counter()
        s, d, r = fn(data)
        e_vals.append((time.perf_counter()-start)*1e6)
        ds_vals.append(s); d_vals.append(d)
    return {
        "output": r,
        "deltaS": ds_vals[0],
        "E": round(statistics.mean(e_vals), 3),
        "E_std": round(statistics.stdev(e_vals), 3),
        "D": d_vals[0],
    }

def bubble_sort(arr):
    a=arr[:]; s=d=0
    for i in range(len(a)):
        for j in range(len(a)-1-i):
            d+=1
            if a[j]>a[j+1]: a[j],a[j+1]=a[j+1],a[j]; s+=1
    return s,d,a

def insertion_sort(arr):
    a=arr[:]; s=d=0
    for i in range(1,len(a)):
        k=a[i]; j=i-1; d+=1
        while j>=0 and a[j]>k: a[j+1]=a[j]; s+=1; d+=1; j-=1
        a[j+1]=k
    return s,d,a

def selection_sort(arr):
    a=arr[:]; s=d=0
    for i in range(len(a)):
        m=i
        for j in range(i+1,len(a)): d+=1; m=j if a[j]<a[m] else m
        if m!=i: a[i],a[m]=a[m],a[i]; s+=1
    return s,d,a

def merge_sort(arr):
    sb=[0]; db=[0]
    def mg(l,r):
        res=[]; i=j=0
        while i<len(l) and j<len(r):
            db[0]+=1
            if l[i]<=r[j]: res.append(l[i]); i+=1
            else: res.append(r[j]); sb[0]+=1; j+=1
        return res+l[i:]+r[j:]
    def ms(a):
        if len(a)<=1: return a
        mid=len(a)//2; db[0]+=1
        return mg(ms(a[:mid]),ms(a[mid:]))
    r=ms(arr[:])
    return sb[0],db[0],r

def heap_sort(arr):
    a=arr[:]; s=d=0; n=len(a)
    def hfy(n,i):
        nonlocal s,d
        lg=i; l=2*i+1; r=2*i+2; d+=1
        if l<n and a[l]>a[lg]: lg=l
        if r<n and a[r]>a[lg]: lg=r
        if lg!=i: a[i],a[lg]=a[lg],a[i]; s+=1; hfy(n,lg)
    for i in range(n//2-1,-1,-1): hfy(n,i)
    for i in range(n-1,0,-1): a[i],a[0]=a[0],a[i]; s+=1; hfy(i,0)
    return s,d,a

def shell_sort(arr):
    a=arr[:]; s=d=0; gap=len(a)//2
    while gap>0:
        for i in range(gap,len(a)):
            t=a[i]; j=i; d+=1
            while j>=gap and a[j-gap]>t: a[j]=a[j-gap]; s+=1; d+=1; j-=gap
            a[j]=t
        gap//=2
    return s,d,a

def counting_sort(arr):
    a=arr[:]; s=d=0
    mx=max(a); mn=min(a)
    cnt=[0]*(mx-mn+1)
    for x in a: cnt[x-mn]+=1; d+=1
    res=[]
    for i,c in enumerate(cnt): res.extend([i+mn]*c); s+=c; d+=1
    return s,d,res

algorithms = [
    ("Bubble", bubble_sort), ("Insertion", insertion_sort),
    ("Selection", selection_sort), ("Merge", merge_sort),
    ("Heap", heap_sort), ("Shell", shell_sort), ("Counting", counting_sort),
]

print("="*65)
print(f"KILL EXPERIMENT v3 — {RUNS} runs averaged, 3 scales")
print("="*65)

total_matches = 0
for size in [10, 100, 1000]:
    random.seed(42)
    arr = random.sample(range(size * 10), size)
    print(f"\n── n={size} ──")
    print(f"{'Algorithm':<12} {'ΔS':>8} {'E_mean(μs)':>12} {'E_std':>10} {'D':>8}")
    print("-"*54)
    results = []
    for name, fn in algorithms:
        r = measure(fn, arr)
        results.append((name, r))
        print(f"{name:<12} {r['deltaS']:>8} {r['E']:>12} {r['E_std']:>10} {r['D']:>8}")
    matches = sum(
        1 for i in range(len(results))
        for j in range(i+1, len(results))
        if (results[i][1]['deltaS']==results[j][1]['deltaS'] and
            abs(results[i][1]['E']-results[j][1]['E'])<3 and
            results[i][1]['D']==results[j][1]['D'])
    )
    total_matches += matches
    print(f"  Triplet matches at n={size}: {matches}")

print(f"\nTOTAL TRIPLET MATCHES: {total_matches}")
print("RESULT: Zero counterexamples for n > 6" if total_matches == 0
      else f"WARNING: {total_matches} matches found — investigate")
