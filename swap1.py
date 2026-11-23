arr = [10, 20, 30, 40, 50, 60]
r = 2

tempArr = []

# Store the first r elements
for i in range(r):
    tempArr.append(arr[i])

# Shift remaining elements to the left
for i in range(0, len(arr)-r, 1):
    arr[i] = arr[i+r]

# Fill the remaining positions with 0
for i in range(len(arr)-r, len(arr), 1):
    arr[i] = 0

print(arr)

#if r is greater than or equal to arr then r = 8 