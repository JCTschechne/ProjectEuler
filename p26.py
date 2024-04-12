problem = """
A unit fraction contains   1   in the numerator. The decimal 
representation of the unit fractions with denominators   2   
to   10   are given:

1/2   = 0.5    
1/3   =0.(3)    
1/4   =0.25    
1/5   = 0.2    
1/6   = 0.1(6)    
1/7   = 0.(142857)    
1/8   = 0.125    
1/9   = 0.(1)    
1/10   = 0.1

Where   0.1(6)   means   0.166666...  , and has a   1-digit 
recurring cycle. It can be seen that   1/7   has a   6-digit 
recurring cycle.

Find the value of   d < 1000   for which   1/d   contains the 
longest recurring cycle in its decimal fraction part.
"""


def one_fraction_of(d):
    decimal = []
    rests = []
    rest = 1
    while len(decimal) < 30 and rest != 0:
        if rest < d:
            rest *= 10
        else:
            decimal.append(rest // d)
            rest %= d
            rests.append(rest)
    return decimal, rests


def cycle_length_in_fraction(d):
    rests = []
    rest = 1
    while rest != 0:
        if rest < d:
            rest *= 10
        else:
            rest %= d
            if rest in rests:
                return len(rests) - rests.index(rest)
            rests.append(rest)
    # no cycle in fraction
    return 0


def solve():
    index = 0
    cycle_len_max = 0
    for n in range(1, 1000):
        cycle_len = cycle_length_in_fraction(n)
        if cycle_len > cycle_len_max:
            index = n
            cycle_len_max = cycle_len
    return index


if __name__ == "__main__":
    print(problem)
    print("Solution: ", solve())
