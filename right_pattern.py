def rightTrianglePattern(n: int) -> list[str]:
    # Generate each row with 'i' asterisks where i ranges from 1 to n
    return ["*" * i for i in range(1, n + 1)]