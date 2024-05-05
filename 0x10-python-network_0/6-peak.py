#!/usr/bin/python3
""" CachamaLover 4ever """


def find_peak(list_of_integers):
    """
    This function returns the peak of a list
    """
    if list_of_integers == []:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
