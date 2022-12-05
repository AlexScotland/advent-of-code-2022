from Day_2 import *

def test_day_2_sol_1():
    all_games = GameChoiceFactory(Game)
    assert get_all_scores_for_player(all_games.all_games) == 13526

def test_day_2_sol_2():
    all_games = GameChoiceFactory(ReversedGame)
    assert get_all_scores_for_player(all_games.all_games) == 14204
