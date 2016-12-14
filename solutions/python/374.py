def sum_two_smallest_numbers(numbers: list) -> int:
    """
    This could be done in O(n) as opposed to O(n log n)
    by simply traversing the array and finding the two
    smallest numbers in a sequence, but I couldn't resist
    a one-liner.
    """
    return sum(sorted(numbers)[:2])