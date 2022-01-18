single_digit = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}

digit_ending = {
    2: "ty",
    3: "hundred",
    4: "thousand"
}

special = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty"
}


def get_digits(n):
    digits = 0
    while(n != 0):
        n = n // 10
        digits += 1
    return digits


def number_to_word(n):
    if n == 0:
        return "zero"
    digits = get_digits(n)
    has_and = digits > 2
    result = ""

    while(digits > 0):
        if n in special:
            # a special value will always finish the number
            result += special.get(n)
            return result
        else:
            digit = n // (10**(digits-1))
            print(digit, n)
            result += single_digit.get(digit)
            n %= 10**(digits-1)
            if digits in digit_ending and digit != 0:
                result += digit_ending.get(digits)
                if n != 0:
                    result += " and " if has_and else " "
                    has_and = False

        digits -= 1
    return result


