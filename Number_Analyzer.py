import math

def analyzeNumber(n: int) -> dict:
    # 1. Check if even
    is_even = (n % 2 == 0)
    
    # 2. Check if positive
    is_positive = (n > 0)
    
    # 3. Check if prime (must be greater than 1 with no divisors other than 1 and itself)
    if n <= 1:
        is_prime = False
    else:
        is_prime = True
        for i in range(2, int(math.isqrt(n)) + 1):
            if n % i == 0:
                is_prime = False
                break
                
    # 4. Check if perfect square
    if n >= 0:
        root = int(math.isqrt(n))
        is_perfect_square = (root * root == n)
    else:
        is_perfect_square = False
        
    # 5. Count digits of the absolute value of n
    digit_count = len(str(abs(n)))
    
    return {
        "is_even": is_even,
        "is_positive": is_positive,
        "is_prime": is_prime,
        "is_perfect_square": is_perfect_square,
        "digit_count": digit_count
    }