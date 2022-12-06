# Tuning Trouble
from Day_1 import TextInput
def solution_1(text_string, jumper):
    index = 0
    temp_char = ""
    while index != len(text_string)-1:
        temp_char = text_string[index:index+jumper]
        marker = check_for_marker(temp_char)
        if marker:
            return index+jumper
        temp_char = ""
        index += 1


def check_for_marker(string):
    string_copy = string
    for index, char in enumerate(string):
        if char in string[:index]:
            # duplicate
            return False
    return string_copy

if __name__ == "__main__":
    text = TextInput("./inputs/day_6.txt").values[0]
    print(solution_1(text, 4))
    print(solution_1(text, 14))