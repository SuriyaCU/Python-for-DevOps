def fibonacci(n):
    """Calculates the first n Fibonacci numbers.

    Args:
        n (int): The amount of numbers to calculate.

    Returns:
        list(int): The first n Fibonacci numbers.
    """
    seq = [0, 1]

    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])

    return seq[:n]

print(fibonacci(10))
print(fibonacci(1))