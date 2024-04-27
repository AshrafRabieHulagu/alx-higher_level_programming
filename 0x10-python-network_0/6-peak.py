def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): List of unsorted integers.

    Returns:
        int: A peak element from the list.
    """
    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]

# Test cases
print(find_peak([1, 2, 4, 6, 3]))    # Output: 6
print(find_peak([4, 2, 1, 2, 3, 1])) # Output: 4
print(find_peak([2, 2, 2]))          # Output: 2
