def reverseInteger(x: int) -> int:
    sign = -1 if x < 0 else 1
    x = abs(x)
    rev = 0
    
    while x != 0:
        pop = x % 10
        x //= 10
        rev = rev * 10 + pop
        
    rev *= sign
    
    # 32-bit integer overflow check
    if rev < -2**31 or rev > 2**31 - 1:
        return 0
        
    return rev