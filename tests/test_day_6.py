from Day_6 import solution_1

def test_day_6_sol_1():
    assert solution_1("bvwbjplbgvbhsrlpgdmjqwftvncz", 4) == 5
    assert solution_1("nppdvjthqldpwncqszvftbrmjlhg", 4) == 6
    assert solution_1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4) == 10
    assert solution_1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4) == 11

def test_day_6_sol_2():
    assert solution_1("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14) == 19
    assert solution_1("bvwbjplbgvbhsrlpgdmjqwftvncz", 14) == 23
    assert solution_1("nppdvjthqldpwncqszvftbrmjlhg", 14) == 23
    assert solution_1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14) == 29
    assert solution_1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14) == 26
