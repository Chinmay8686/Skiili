def numberTrianglePattern(n: int) -> list[str]:
    # Generate each row i (from 1 to n) containing numbers from 1 to i separated by a single space
    return [" ".join(str(j) for j in range(1, i + 1)) for i in range(1, n + 1)]