def my_steps(n: int) -> int:
    if not isinstance(n, int):
        raise ValueError("n must be an integer")
    if n < 1 or n > 25:
        raise ValueError("n out of bounds (1 ≤ n ≤ 25)")

    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a

