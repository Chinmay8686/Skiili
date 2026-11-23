#23 november 2026
arr = [1, 0, 2, 3, 0, 4, 5, 0]

for i in range(len(arr)):

    if arr[i] == 0:

        # Shift elements to the right
        for j in range(len(arr)-1, i, -1):
            arr[j] = arr[j-1]

        # Insert duplicate zero
        if i + 1 < len(arr):
            arr[i+1] = 0
 
        # Skip the duplicated zero
        i += 1

print(arr)