# Rock Paper Scissors
from Day_1 import TextInput
WIN_PTS = 6
DRAW_PTS = 3

def determine_choice_for_win(option, npc = None):
    choice_map = {
        "A": Rock(),
        "X": Rock(),
        "B": Paper(),
        "Y": Paper(),
        "C": Scissors(),
        "Z": Scissors()
        }
    return choice_map.get(option)

def find_winning_move(losing_choice):
    for choice in [Rock(), Paper(), Scissors()]:
        if isinstance(losing_choice, choice.beats):
            return choice

def determine_choice_for_win_reversed(option, npc):
    choice_map = {
        "A": Rock(),
        "X": npc.choice.beats(),
        "B": Paper(),
        "Y": npc.choice,
        "C": Scissors(),
        "Z": find_winning_move(npc.choice)
        }
    return choice_map[option]


def get_all_scores_for_player(games):
    total_score = 0
    for game in games:
        total_score += game.player.points
    return total_score

class Player():
    def __init__(self):
        self.points = 0
        self.choice = None

class Rock():
    def __init__(self):
        self.score = 1
        self.beats = Scissors

class Paper():
    def __init__(self):
        self.score = 2
        self.beats = Rock

class Scissors():
    def __init__(self):
        self.score = 3
        self.beats = Paper

class Game():
    def __init__(self, choice_list):
        self.player = Player()
        self.npc = Player()
        self.game_choice = choice_list
        self.result = self.__calculate_game_for_player_and_npc()
    
    def __calculate_game_for_player_and_npc(self):
        results = self.game_choice.split()
        self.npc.choice = determine_choice_for_win(results[0])
        self.player.choice = determine_choice_for_win(results[1])
        self.npc.points += self.npc.choice.score
        self.player.points += self.player.choice.score
        self.__determine_winner(self.npc, self.player)


    def __determine_winner(self, npc, player):
        if isinstance(player.choice, npc.choice.beats):
            npc.points += WIN_PTS
        elif isinstance(npc.choice, player.choice.beats):
            player.points += WIN_PTS
        else:
            player.points += DRAW_PTS
            npc.points += DRAW_PTS

class ReversedGame(Game):
    
    def __init__(self, choice_list):
        self.player = Player()
        self.npc = Player()
        self.game_choice = choice_list
        self.result = self.__calculate_game_for_player_and_npc()
    
    def __calculate_game_for_player_and_npc(self):
        results = self.game_choice.split()
        self.npc.choice = determine_choice_for_win(results[0])
        self.player.choice = determine_choice_for_win_reversed(results[1], self.npc)
        self.npc.points += self.npc.choice.score
        self.player.points += self.player.choice.score
        self.__determine_winner(self.npc, self.player)
    
    def __determine_winner(self, npc, player):
        if isinstance(player.choice, npc.choice.beats):
            npc.points += WIN_PTS
        elif isinstance(npc.choice, player.choice.beats):
            player.points += WIN_PTS
        else:
            player.points += DRAW_PTS
            npc.points += DRAW_PTS


class GameChoiceFactory():
    def __init__(self, game_type):
        self.all_games = self.__create_games_from_sheet(TextInput("./inputs/day_2.txt"), game_type)
    
    def __create_games_from_sheet(self, game_sheet, game_type):
        list_of_all_games = []
        for game in game_sheet.values:
            list_of_all_games.append(game_type(game))
        return list_of_all_games


if __name__ == "__main__":
    all_games = GameChoiceFactory(Game)
    print("Solution 1")
    print(get_all_scores_for_player(all_games.all_games))
    print("Solution 2")
    all_games = GameChoiceFactory(ReversedGame)
    print(get_all_scores_for_player(all_games.all_games))
