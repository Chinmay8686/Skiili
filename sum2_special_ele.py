def sumOfSquares(nums: list[int]) -> int:
    n = len(nums)
    total_sum = 0
    
    # Iterate through 1-indexed positions
    for i in range(1, n + 1):
        if n % i == 0:
            # nums is 0-indexed in Python, so position i corresponds to index i - 1
            total_sum += nums[i - 1] ** 2
            
    return total_sum