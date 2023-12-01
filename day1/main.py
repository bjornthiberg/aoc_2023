import re
import unittest


def get_lines(file) -> list:
    with open(file) as f:
        lines = f.readlines()
    return lines


def word_to_digit(strNum) -> str:
    """Takes a digit as a string, returns the string integer.
    Example: "two" -> "2", "3"->"3"
    """
    if strNum.isdigit():
        return strNum
    numStrings = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    return str(1 + numStrings.index(strNum))


def str_to_sum_first_last(line) -> int:
    """Find all numbers in the line string and returns
    the value of the combination of the first and last number.
    Example: "three23twoone5 -> 35, "237" -> 27, "twoone" -> 21
    """
    regExp = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
    nums = re.findall(regExp, line)
    nums = list(map(word_to_digit, nums))

    return int(nums[0] + nums[-1])


def main(file):
    digit_sum = 0

    for line in get_lines(file):
        digit_sum += str_to_sum_first_last(line)
    return digit_sum


class TestDay1(unittest.TestCase):
    def test_numbers(self):
        self.assertEqual(str_to_sum_first_last("11"), 11)
        self.assertEqual(str_to_sum_first_last("123"), 13)
        self.assertEqual(str_to_sum_first_last("5"), 55)

    def test_longer(self):
        self.assertEqual(str_to_sum_first_last("two"), 22)
        self.assertEqual(str_to_sum_first_last("twone"), 21)

    def test_both(self):
        self.assertEqual(str_to_sum_first_last("twooneleven1"), 21)
        self.assertEqual(str_to_sum_first_last("threefive"), 35)


if __name__ == "__main__":
    # unittest.main() # uncomment for unit tests
    result = main("input1.txt")
    print(f"Result: {result}")
