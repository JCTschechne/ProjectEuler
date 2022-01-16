from shared import gen_primes

def sum_of_primes_below(n):
    gen = gen_primes()
    p = next(gen)
    som = 0
    while p < n:
        som += p
        p = next(gen)
    return som

