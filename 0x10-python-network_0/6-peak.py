#!/usr/bin/python3

def find_peak(list_of_integers):
    """Finds peaks in a list of unsorted integers."""
    li = list_of_integers
    l = len(li)
    if l == 0:
        return []

    peaks = []

    def _find_peak_assistant(start, end):
        if start > end:
            return

        mid = (start + end) // 2
        if (mid == l - 1 or li[mid] >= li[mid + 1]) and (mid == 0 or li[mid] >= li[mid - 1]):
            peaks.append(li[mid])

        _find_peak_assistant(start, mid - 1)
        _find_peak_assistant(mid + 1, end)

    _find_peak_assistant(0, l - 1)
    return peaks

