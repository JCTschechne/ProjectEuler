from shared import get_prime_factors

def nth_triangular(n):
    return int(n * (n+1) / 2)


def get_divisors(num):
    prime_factors = get_prime_factors([num])
    current = 0
    divisors = 1
    while current < len(prime_factors):
        mult = prime_factors.count(prime_factors[current])
        current += mult
        divisors *= (mult + 1)
    return divisors


def highly_divisible_triangular_number(nth_divisors):
    n = 1
    divisors = 1
    while divisors + 2 < nth_divisors:
        n += 1
        divisors = get_divisors(nth_triangular(n))
        print(n, "(", divisors, ") ")
    return divisors
