def roundToNearest(s: str) -> int:
    num = int(s)
    remainder = num % 10
    
    if remainder <= 5:
        return num - remainder
    else:
        return num + (10 - remainder)