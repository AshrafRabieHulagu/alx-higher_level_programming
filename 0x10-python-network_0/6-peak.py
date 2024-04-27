def find_peak(arr):
    n = len(arr)
    if n == 0:
        return None

    def binary_search(left, right):
        if left == right:
            return left

        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1]:
            # Peak is on the left side
            return binary_search(left, mid)
        else:
            # Peak is on the right side
            return binary_search(mid + 1, right)

    return binary_search(0, n - 1)

# Example usage
arr1 = [1, 2, 4, 6, 3]
arr2 = [4, 2, 1, 2, 3, 1]
arr3 = [2, 2, 2]

print(find_peak(arr1))  # Output: 6
print(find_peak(arr2))  # Output: 3
print(find_peak(arr3))  # Output: 2
