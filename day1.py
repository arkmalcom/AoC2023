from common.utils import get_input


def find_first_and_last_digits(string) -> int:
    digits = [digit for digit in string if digit.isdigit()]
    return int(digits[0] + digits[-1])


def find_sum_of_digits() -> int:
    lines = get_input("day1.txt")
    return sum([find_first_and_last_digits(line) for line in lines])


print(find_sum_of_digits())
