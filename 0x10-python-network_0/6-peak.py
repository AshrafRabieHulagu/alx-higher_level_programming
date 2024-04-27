def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): List of unsorted integers.

    Returns:
        int or None: A peak element from the list or None if the list is empty.
    """
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1
    while left <= right:
        mid = (left + right) // 2
        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]
        elif mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            right = mid - 1
        else:
            left = mid + 1

# Test cases
print(find_peak([1, 2, 4, 6, 3]))    # Output: 6
print(find_peak([4, 2, 1, 2, 3, 1])) # Output: 3
print(find_peak([2, 2, 2]))          # Output: 2
print(find_peak([]))                 # Output: None
print(find_peak([-2, -4, 2, 1]))     # Output: 2
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1])) # Output: 4
