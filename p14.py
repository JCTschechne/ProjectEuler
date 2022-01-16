def collatz_to_one(n):
    terms = 1
    while n != 1:
        terms += 1
        if n%2 == 0:
            n = n/2
        else:
            n = 3*n+1
    return terms

def collatz_length(n):
    return collatz_to_one(n)

def solve():
    print(max([(collatz_length(x), x) for x in range(100, 1000000)]))
