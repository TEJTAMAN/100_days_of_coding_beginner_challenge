#Implement sorting algorithms (e.g., bubble sort, merge sort).


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:  # Swap if the element is greater
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example usage
arr = [64, 25, 12, 22, 11]
print("Bubble Sort:", bubble_sort(arr))
