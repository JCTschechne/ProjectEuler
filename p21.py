problem = """
Let d(n) be defined as the sum of proper divisors of n (numbers less than 
n which divide evenly into n). If  d(a) = b  and  d(b) = a , where  a
e b , then  a  and  b  are an amicable pair and each of  a  and  b  are 
called amicable numbers.

For example, the proper divisors of  220  are  1, 2, 4, 5, 10, 11, 20, 22, 
44, 55  and  110 ; therefore  d(220) = 284 . The proper divisors of  284  are  
1, 2, 4, 71  and  142 ; so  d(284) = 220 .

Evaluate the sum of all the amicable numbers under  10000 .
"""

def get_divisors(num):
    return [x for x in range(1, (num//2) + 1) if num % x == 0]

def is_amicable(num):
    partner = sum(get_divisors(num))
    return sum(get_divisors(partner)) == num and partner != num

def solve():
    amicable_sum = 0
    for i in range(10000):
        if is_amicable(i):
            amicable_sum += i
    return amicable_sum

if __name__ == "__main__":
    print(problem)
    print("Solution: ", solve())
