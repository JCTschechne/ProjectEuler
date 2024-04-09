import math
from shared import number_to_digits

problem = """
n! means n x (n-1) x ... x 3 x 2 x 1.
For example, 10! = 10 x 9 x 8 x ... x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0  = 27.
Find the sum of the digits in the number 100!.
"""

if __name__ == "__main__":
    print(problem)
    print("Solution: ", sum(number_to_digits(math.factorial(100))))