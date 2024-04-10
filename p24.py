problem = """
A permutation is an ordered arrangement of objects. For 
example, 3124 is one possible permutation of the digits 
1, 2, 3 and 4. If all of the permutations are listed 
numerically or alphabetically, we call it lexicographic 
order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the 
digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""


def is_permutation_of_0_to_9(num):
    digits = str(num)
    if len(digits) > 10 or len(digits) < 9:
        return False
    if len(digits) == 9:
        digits = "0" + digits
    return "0" in digits and "1" in digits and "2" in digits and "3" in digits and \
        "4" in digits and "5" in digits and "6" in digits and "7" in digits and \
        "8" in digits and "9" in digits


def solve():
    start = 123456789
    counter = 0

    while counter < 1000000:
        if is_permutation_of_0_to_9(start):
            counter += 1
            print(counter, ": ", start)
        start += 1
    return start - 1


if __name__ == "__main__":
    print(problem)
    print("Solution: ", solve())
