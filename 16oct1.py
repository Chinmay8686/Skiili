def anagram(n1, n2):
    freq = [0] * 10

    while(n1 != 0):
        last_digit = n1 % 10
        freq[last_digit] += 1
        n1 //= 10 

    while(n2 != 0):
        last_digit = n2% 10 
        freq[last_digit] -=1
        n2 //=10 

    for i in freq:
        if(i != 0):
            return False
    return True
n1= 1221
n2= 1212

res = anagram(n1, n2)

print(f"{n1} and {n2} are anagram: {res}")