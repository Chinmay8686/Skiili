def primesInRange(start: int, end: int) -> list[int]:
    if end < 2:
        return []
    
    # Sieve of Eratosthenes up to the upper bound (end)
    is_prime = [True] * (end + 1)
    is_prime[0] = is_prime[1] = False
    
    p = 2
    while p * p <= end:
        if is_prime[p]:
            for i in range(p * p, end + 1, p):
                is_prime[i] = False
        p += 1
        
    # Filter the primes within the inclusive range [start, end]
    actual_start = max(2, start)
    return [i for i in range(actual_start, end + 1) if is_prime[i]]