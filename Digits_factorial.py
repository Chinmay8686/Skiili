import math

def digitsInFactorial(n: int) -> int:
    if n <= 1:
        return 1
    
    # Sum the logarithms of all numbers from 1 to n
    total_digits = 0
    for i in range(1, n + 1):
        total_digits += math.log10(i)
        
    return math.floor(total_digits) + 1