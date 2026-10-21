import math

def digitsInFactorial(n: int) -> int:
    if isinstance(n, dict):
        n = n.get('n', 0)
    elif isinstance(n, str):
        n = int(n)
        
    if n <= 1:
        return 1
    
    total_digits = 0
    for i in range(1, n + 1):
        total_digits += math.log10(i)
        
    # This return statement must be outside (unindented from) the for loop
    return math.floor(total_digits) + 116oct