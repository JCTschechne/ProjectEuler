problem = """
Starting with the number $1$ and moving to the right in a clockwise direction a $5$ by $5$ spiral is formed as follows:
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 1217 16 15 14 13
It can be verified that the sum of the numbers on the diagonals is $101$.
What is the sum of the numbers on the diagonals in a $1001$ by $1001$ spiral formed in the same way?
"""

def solve():
    sol = 1
    num = 1
    for step in range(1, 501):
        for i in range(4):
            num += (step*2)
            sol += num
    return sol

if __name__ == "__main__":
    print(problem)
    print("Solution: ", solve())