from shared import get_prime_factors
from functools import reduce

def smallest_multiple(n):
    all_factors = []
    for i in range(2, n):
        facts = get_prime_factors([i])
        factors_copy = all_factors.copy()
        for fac in facts:
            try:
                factors_copy.remove(fac)
            except ValueError:
                all_factors.append(fac)
    return reduce(lambda x, y: x*y, all_factors)


