from Day_8 import Forest, solution_1, solution_2
from Day_1 import TextInput

def test_day_6_sol_1():
    forest = Forest()
    assert solution_1(TextInput("tests/fixtures/test_day_8.txt"), forest).visible_trees() == 21

def test_day_6_sol_2():
    forest = Forest()
    forest = solution_1(TextInput("tests/fixtures/test_day_8.txt"), forest)
    assert solution_2(forest) == 8
