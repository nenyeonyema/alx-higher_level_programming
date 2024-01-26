#!/usr/bin/python3
"""
This module contains a function to find a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.
    A peak is defined as an element that is greater than or equal to its neighbors.
    Returns the peak element if found, otherwise returns None.
    """
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return list_of_integers[low]


if __name__ == "__main__":
    # Test cases
    print(find_peak([1, 2, 4, 6, 3]))   # Output: 6
    print(find_peak([4, 2, 1, 2, 3, 1])) # Output: 4 or 3
    print(find_peak([2, 2, 2]))           # Output: 2
    print(find_peak([]))                  # Output: None
    print(find_peak([-2, -4, 2, 1]))      # Output: 2
    print(find_peak([4, 2, 1, 2, 2, 2, 3, 1])) # Output: 4
