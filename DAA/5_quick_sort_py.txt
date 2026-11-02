
# Quick Sort using Deterministic and Randomized Pivot

import random
import time

# Partition Function
def partition(arr, low, high):

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):

        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


# Deterministic Quick Sort
def deterministic_quick_sort(arr, low, high):

    if low < high:
        p = partition(arr, low, high)

        deterministic_quick_sort(arr, low, p - 1)
        deterministic_quick_sort(arr, p + 1, high)


# Randomized Quick Sort
def randomized_quick_sort(arr, low, high):

    if low < high:

        # Select a random pivot
        random_index = random.randint(low, high)

        arr[random_index], arr[high] = arr[high], arr[random_index]

        p = partition(arr, low, high)

        randomized_quick_sort(arr, low, p - 1)
        randomized_quick_sort(arr, p + 1, high)


# Main Program
arr = list(map(int, input("Enter array elements separated by space: ").split()))

if len(arr) == 0:
    print("Array is empty")

else:
    arr1 = arr.copy()
    arr2 = arr.copy()

    # Deterministic Quick Sort
    start = time.perf_counter()
    deterministic_quick_sort(arr1, 0, len(arr1) - 1)
    end = time.perf_counter()

    deterministic_time = end - start

    # Randomized Quick Sort
    start = time.perf_counter()
    randomized_quick_sort(arr2, 0, len(arr2) - 1)
    end = time.perf_counter()

    randomized_time = end - start

    print("\nDeterministic Quick Sort:")
    print("Sorted Array:", arr1)
    print("Execution Time:", deterministic_time)

    print("\nRandomized Quick Sort:")
    print("Sorted Array:", arr2)
    print("Execution Time:", randomized_time)