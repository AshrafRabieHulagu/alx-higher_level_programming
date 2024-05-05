Python
def find_peak(list_of_integers):
  """
  Finds a peak element in an unsorted list of integers.

  Args:
      list_of_integers: A list of integers.

  Returns:
      The index of a peak element in the list, or None if the list is empty.
  """

  # Handle empty list case
  if not list_of_integers:
    return None

  # Implement Binary Search with peak detection logic
  left, right = 0, len(list_of_integers) - 1

  while left <= right:
    mid = (left + right) // 2

    # Check if mid is a peak element
    if (mid == 0 or list_of_integers[mid] > list_of_integers[mid - 1]) and \
       (mid == len(list_of_integers) - 1 or list_of_integers[mid] > list_of_integers[mid + 1]):
      return mid

    # Move to the side with the potentially higher peak
    elif mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
      right = mid - 1
    else:
      left = mid + 1

  # No peak found (shouldn't happen with proper input)
  return None
