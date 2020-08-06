from typing import List


# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arr_a: List[int], arr_b: List[int]) -> List[int]:
    merged_arr = []

    while len(arr_a) > 0 and len(arr_b) > 0:
        if arr_a[0] < arr_b[0]:
            merged_arr.append(arr_a[0])
            arr_a.pop(0)
        else:
            merged_arr.append(arr_b[0])
            arr_b.pop(0)

    for number in arr_a:
        merged_arr.append(number)
    for number in arr_b:
        merged_arr.append(number)

    return merged_arr


def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) > 1:
        middle = len(arr) // 2
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])

        return merge(left, right)

    return arr


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr: List[int], start: int, middle: int, end: int) -> None:
    new_start = middle + 1

    if arr[middle] <= arr[new_start]:
        return

    while start <= middle and new_start <= end:
        if arr[start] <= arr[new_start]:
            start += 1
        else:
            value = arr[new_start]
            index = new_start

            while index != start:
                arr[index] = arr[index - 1]
                index -= 1

            arr[start] = value

            start += 1
            middle += 1
            new_start += 1


def merge_sort_in_place(arr: List[int], left: int, right: int) -> None:
    if left < right:
        middle = left + (right - left) // 2
        merge_sort_in_place(arr, left, middle)
        merge_sort_in_place(arr, middle + 1, right)

        merge_in_place(arr, left, middle, right)
