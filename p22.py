problem = """
Using names.txt (right click and 'Save Link/Target As...'), a 46K 
text file containing over five-thousand first names, begin by sorting 
it into alphabetical order. Then working out the alphabetical value 
for each name, multiply this value by its alphabetical position in 
the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN,
 which is worth 3 + 15 + 12 + 9 + 14 = 53, is the $938$th name in the 
 list. So, COLIN would obtain a score of 938 times 53 = 49714.

What is the total of all the name scores in the file?
"""


def evaluate(c):
    return ord(c.upper()) - 64


def solve():
    file = open("Res/0022_names.txt")
    names = file.readline().replace('"', '').split(",")
    names.sort()
    score = 0

    for i in range(len(names)):
        score += (sum([evaluate(c) for c in names[i]]) * (i + 1))
    return score


if __name__ == "__main__":
    print(problem)
    print("Solution: ", solve())
