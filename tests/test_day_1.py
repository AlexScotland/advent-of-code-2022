from Day_1 import *

def test_day_1_sol_1():
    all_elves = ElfFactory()
    assert all_elves.elves[0].calories == 67622

def test_day_1_sol_2():
    all_elves = ElfFactory()
    assert sum(all_elves.get_top_elves(3)) == 201491
