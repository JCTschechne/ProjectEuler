from shared import is_palindrome

res = [(x, y) for x in range(100, 1000) for y in range(100, 1000) if is_palindrome(str(x*y))]

print(res)
