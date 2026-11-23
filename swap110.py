#swap the value given arr=[10, 20, 30, 40, 50, 60] r=2 after swapping [20, 30, 40 ,50 , 60, 0] or the arr = given input  
arr = list(map(int, input("Enter array elements: ").split())) # Take array elements from the user
r = int(input("Enter rotation value: ")) # Take the number of positions to shift

n = len(arr) # Find the length of the array

arr = arr[r:] + [0] * r # Shift array elements to the left by r positions
# Fill the remaining empty positions with 0

print("After swapping:", arr) #display