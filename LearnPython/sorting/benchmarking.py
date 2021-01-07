from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from quick_sort import quick_sort
from merge_sort import merge_sort
from random import randint
from time import time


def create_array(size = 10, max_val = 100):
    return [ randint(0, max_val) for _ in range(size)]

## benchmarking
stats={'bubble-sort':[],
       'selection-sort':[],
       'insertion-sort':[],
       'merge-sort':[],
       'quick-sort':[],
       'built-in':[]}

batch = [10,100,1000,10000]

for b in batch:
    a = create_array(b,b)

    t0 = time()
    a = bubble_sort(a)
    t1 = time()
    stats['bubble-sort'].append(t1-t0)

    t0 = time()
    a = selection_sort(a)
    t1 = time()
    stats['selection-sort'].append(t1-t0)

    t0 = time()
    a = insertion_sort(a)
    t1 = time()
    stats['insertion-sort'].append(t1-t0)

    t0 = time()
    a = merge_sort(a)
    t1 = time()
    stats['merge-sort'].append(t1-t0)

    t0 = time()
    a = quick_sort(a)
    t1 = time()
    stats['quick-sort'].append(t1-t0)

    t0 = time()
    a = sorted(a)
    t1 = time()
    stats['built-in'].append(t1-t0)

print("\nn\tBubble-sort\tSelection-sort\tInsertion-sort\tMerge-sort\tQuick-sort\tBuilt-in")
print("_"*60)

for i, b in enumerate(batch):
    print("%d \t%0.5f \t%0.5f \t%0.5f \t%0.5f \t%0.5f \t%0.5f" %
          (b,
           stats['bubble-sort'][i],
           stats['selection-sort'][i],
           stats['insertion-sort'][i],
           stats['merge-sort'][i],
           stats['quick-sort'][i],
           stats['built-in'][i]
           ))

print("\n")

