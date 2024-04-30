import math

from shared import is_prime

problem = """
Euler discovered the remarkable quadratic formula:
  n^2 + n + 41  

It turns out that the formula will produce   40   primes for the consecutive 
integer values   0 <=n <= 39  . However, when   n = 40, 40^2 + 40 + 41 = 
40(40 + 1) + 41   is divisible by   41  , and certainly when   n = 41, 41^2 + 41 
+ 41   is clearly divisible by   41  .

The incredible formula   n^2 - 79n + 1601   was discovered, which produces   80   
primes for the consecutive values   0 <= n <= 79  . The product of the 
coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

n^2 + an + b  , where   |a| < 1000   and   |b| <= 1000  where   |n|   is the 
modulus/absolute value of  n  e.g. |11| = 11  and |-4| = 4  

Find the product of the coefficients, a and b, for the quadratic expression 
that produces the maximum number of primes for consecutive values of n, 
starting with n = 0.
"""


def calc_max_primes(a, b):
    for n in range(1000):
        if not is_prime(math.pow(n, 2) + a*n + b):
            return n


def solve():
    max_pair = (0,0)
    max_primes = 0
    # even numbers for a or b or both are not yielding primes
    for a in range(-999, 1000, 2):
        for b in range(-999, 1000, 2):
            primes  = calc_max_primes(a, b)
            if primes > max_primes:
                max_primes = primes
                max_pair = a, b
    print(max_pair, max_primes)
    a, b = max_pair
    return a * b

if __name__ == "__main__":
    print(problem)
    print("Solution: ", solve())