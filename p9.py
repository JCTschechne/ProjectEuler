from shared import gen_pythagorean_triplet

def triplet_sum(n):
    gen = gen_pythagorean_triplet()
    a, b, c = next(gen)
    while a+b+c != n:
        a, b, c = next(gen)
    return a, b, c