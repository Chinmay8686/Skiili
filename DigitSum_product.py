def subtractProductAndSum(n: int) -> int:
    product_val = 1
    sum_val = 0
    
    for digit in str(n):
        d = int(digit)
        product_val *= d
        sum_val += d
        
    return product_val - sum_val