#Implement searching algorithms (e.g., binary search).


def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Element not found

# Example usage
arr = [10, 20, 30, 40, 50]
target = 30
print("Binary Search:", binary_search(arr, target))  # Output: 2
