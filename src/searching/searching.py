from typing import List


def binary_search(arr: List[int], target: int, start: int, end: int) -> int:
    if len(arr) > 0:
        if arr[start] == target:
            return start

        if arr[end] == target:
            return end

        middle = (end - start) // 2
        if arr[middle] == target:
            return middle

        if target < arr[middle]:
            return binary_search(arr, target, start, middle)

        if target > arr[middle]:
            return binary_search(arr, target, middle, end)

    return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr: List[int], target: int) -> int:
    start = 0
    end = len(arr) - 1

    while start <= end:
        if start is target:
            return start

        if end is target:
            return end

        middle = start + (end - start) // 2
        if arr[middle] is target:
            return middle

        if arr[start] < arr[end]:
            if arr[middle] > target:
                end = middle - 1
            else:
                start = middle + 1
        else:
            if arr[middle] < target:
                end = middle - 1
            else:
                start = middle + 1

    return -1
