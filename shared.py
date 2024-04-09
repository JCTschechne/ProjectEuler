from math import sqrt

def number_to_digits(number):
    return [int(x) for x in str(number)]

def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))


def is_palindrome(candidate):
    return True if (len(candidate) < 2) else candidate[0] == candidate[-1] and is_palindrome(candidate[1:-1])


def get_prime_factors(numbers):
    factors = []
    for num in numbers:
        if is_prime(num):
            factors.append(num)
        else:
            factors.extend(get_prime_factors(split(num)))
    return factors


def split(num):
    if num == 1:
        return [1]
    a = 2
    while num % a != 0 and a < num:
        a += 1
    b = num / a
    return [a, b]


def gen_pythagorean_triplet():
    a = 1
    b = 1
    c = 1
    while True:
        if (a**2 + b**2) == c**2:
            yield a, b, c
            c += 1
        else:
            if b**2 > c**2:
                c += 1
                a = 1
                b = 1
            elif a == b:
                a = 1
                b += 1
            else:
                a += 1


# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/

def gen_primes():
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

