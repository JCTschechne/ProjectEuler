"""
By starting at the top of the triangle below and moving to adjacent numbers
on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only
routes, it is possible to solve this problem by trying every route. However, Problem 67,
is the same challenge with a triangle containing one-hundred rows; it cannot be solved
by brute force, and requires a clever method! ;o)
"""

triangle_string = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


def convert_multi_line_string(string):
    # Split the multi-line string into an array of lines
    lines = string.split('\n')

    # Initialize an empty list to store the converted integers
    result = []

    # Iterate through each line
    for line in lines:
        # Split the line by whitespace and convert substrings to integers
        integers = [int(x) for x in line.split()]
        # Append the list of integers to the result list
        result.append(integers)

    return result


def solve_naive_rec(triangle, row, col):
    if row + 1 >= len(triangle):
        return triangle[row][col]

    if triangle[row + 1][col] > triangle[row + 1][col + 1]:
        # left element
        return triangle[row][col] + solve_naive_rec(triangle, row + 1, col)
    else:
        # right element
        return triangle[row][col] + solve_naive_rec(triangle, row + 1, col + 1)


def solve_naive(triangle):
    """
    !!! WARNING: Not able to solve the problem !!!
    Just go from the top to the bottom and always choose the largest number. Misses potential larger paths
    """
    return solve_naive_rec(triangle, 0, 0)


def solve_brut_rec(triangle, row, col):
    if row >= len(triangle):
        return 0
    left = solve_brut_rec(triangle, row + 1, col)
    right = solve_brut_rec(triangle, row + 1, col + 1)

    return left + triangle[row][col] if left > right else right + triangle[row][col]


def solve_brut(triangle):
    """
    Test all possible paths.
    """
    return solve_brut_rec(triangle, 0, 0)


def sum_tri(triangle, row, col):
    if row >= len(triangle):
        return 0
    return triangle[row][col] + sum_tri(triangle, row + 1, col) + sum_tri(triangle, row + 1, col + 1)


def solve_largest_tri_rec(triangle, row, col):
    if row >= len(triangle):
        return 0
    left = sum_tri(triangle, row + 1, col)
    right = sum_tri(triangle, row + 1, col + 1)

    return solve_largest_tri_rec(triangle, row + 1, col) + triangle[row][col] \
        if left > right \
        else solve_largest_tri_rec(triangle, row + 1, col + 1) + triangle[row][col]



def solve_largest_tri(triangle):
    """
    !!! WARNING: Not able to solve the problem !!!
    Divide in sub triangles and chose the larger (sum of all numbers in the triangle)
    """
    return solve_largest_tri_rec(triangle, 0, 0)


def solve_bottom_up_rec(triangle, row, col, current):



def solve_bottom_up(triangle):
    bottom = len(triangle) - 1
    solve_bottom_up_rec(triangle, bottom, 0, 0)


if __name__ == "__main__":
    triangle = convert_multi_line_string(triangle_string)
    print(triangle)
    print("Naive: ", solve_naive(triangle))
    print("Brut: ", solve_brut(triangle))
    print("Largest sub triangle: ", solve_largest_tri(triangle))
