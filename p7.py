from shared import gen_primes


def get_nth_prime(n):
    gen = gen_primes()
    for n in range(n-1):
        next(gen)
    return next(gen)