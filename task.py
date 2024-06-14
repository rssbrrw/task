
"""

CommerceCo wants to determine its most profitable period in the past 12 months.

Given:
    - `months`
        A list of integers of length x representing the monthly profit values for the previous x months
    - `n`
        An integer representing the maximum number of contiguous months that should be used to calculate the answer.

You should complete the `calculate_max_profit` function such that it returns the highest possible
sum of a contiguous sublist of `months` with maximum length n.

If no such sublist has a sum above 0, the function should return 0.


Example 1:

    months = [4, 3, 5, 6, 2], n = 3

    The maximum possible profit from a sublist of up to 3 elements is 14, made from the elements [3, 5, 6].


Example 2:

    months = [4, -1, 5, 6, -3], n = 3

    The maximum possible profit from a sublist of up to 3 elements is 11, made from the elements [5, 6].

    Although n is 3, all sublists of length 3 have totals less than 11.

"""

def calculate_max_profit(months: list[int], n: int) -> int:
    # Complete this function
    ...
