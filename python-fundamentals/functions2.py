def sum_even(numbers):
    """Calculates the sum of even numbers from a list.

    Args:
        numbers (list(int)): The list of numbers to evaluate.

    Returns:
        int: The sum of the even numbers.
    """
    return sum(x for x in numbers if x % 2 == 0)

print(sum_even([1, 2, 3, 4, 5, 6]))