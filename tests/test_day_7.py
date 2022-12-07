from Day_7 import solution_1, solution_2
from Day_1 import TextInput

def test_day_6_sol_1():
    text = TextInput("tests/fixtures/test_day_7.txt").values
    assert solution_1(text, 100000) == 95437
    text = TextInput("./inputs/day_7.txt").values
    assert solution_1(text, 100000) == 1297683

def test_day_6_sol_2():
    text = TextInput("./inputs/day_7.txt").values
    assert solution_2(text, 30000000) == 5756764

