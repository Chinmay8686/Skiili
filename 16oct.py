# suppose n= 1232144 count how many time digit  or its frequency using an array.
# output:
# 1 -> 2
# 2 -> 2
# 3 -> 1
# 4 -> 2

# n = 1232144 
# s = str(n)
# arr = []
# for d in s:
#     arr.append(int(d))
# print(arr)   
# freq = [0] * 10
# for d in arr:
#     freq[d] += 1   
# for i in range(10):
#     if freq[i] > 0:
#         print(f"{i} -> {freq[i]}")


def countFreq(n):
    freq=[0]*10
    while n!=0:
        last_digit=n%10
        freq[last_digit]+=1
        n//=10
    return freq

n=134654987139
res=countFreq(n)
for i in range(len(res)):
    print(f"{i} -> {res[i]}")