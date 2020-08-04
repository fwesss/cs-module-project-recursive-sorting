def binary_search(arr, target, start, end):
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
def agnostic_binary_search(arr, target):
    # Your code here
    pass
