from bubblesort import bubbleSort
from heapsort import heapSort
from mergesort import mergeSort
from quicksort import quickSort

import time
import random

def assertion(array1, table_type):
    array2 = array1
    array3 = array1
    array4 = array1
    print(f"Rodzaj tabeli: {table_type}")

    start1 = time.perf_counter()
    heapSort(array1)
    print(f"heapSort: {time.perf_counter() - start1} sekund")

    start2 = time.perf_counter()
    mergeSort(array2)
    print(f"mergeSort: {time.perf_counter() - start2} sekund")

    start3 = time.perf_counter()
    bubbleSort(array3)
    print(f"bubblesort: {time.perf_counter() - start3} sekund")

    start4 = time.perf_counter()
    try:
        quickSort(array4, 0, len(array4) - 1)
        print(f"quickSort: {time.perf_counter() - start4} sekund")
    except:
        print(f"quickSort sie wywalil")

nums = 300000

sorted = list(range(0, nums))
assertion([random.randint(0, 10000) for _ in range(nums)], "randomowa nieposortowana")
assertion(sorted[::-1], "odwrotnie posortowana")
assertion(sorted, "posortowana")
