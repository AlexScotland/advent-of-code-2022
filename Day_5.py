# Stack Game

from Day_1 import TextInput

class Instruction():

    def __init__(self, num_to_move, from_val, to):
        self.num_to_move = int(num_to_move)
        self.from_val = int(from_val)
        self.to = int(to)

def extract_game_from_text(text, strip = True):
    game_text = []
    for line in text.values:
        if line =="\n":
            return game_text
        if strip:
            game_text.append(line.strip())
        else:
            game_text.append(line)

def generate_all_instructions(text):
    all_instructions = []
    for instruction in text.values:
        instruction = instruction.strip().split()
        if len(instruction) > 0:
            all_instructions.append(Instruction(instruction[1],instruction[3],instruction[5]))
    return all_instructions
        

def solution_1():
    text = TextInput("./inputs/day_5.txt")
    stack = StackSystemBuilder.create_stack_game(text)
    extracted_text = extract_game_from_text(text, False)
    for i in extracted_text:
        text.values.remove(i)
    stack.add_row(50)
    for instruction in generate_all_instructions(text):
        source_column = stack.get_all_in_column(instruction.from_val -1)
        destination_column = stack.get_all_in_column(instruction.to - 1)
        for number in range(0, instruction.num_to_move):
            stack.move_to_new_column(source_column, instruction.from_val -1, destination_column, instruction.to -1)
    return stack

def solution_2():
    text = TextInput("./inputs/day_5.txt")
    stack = StackSystemBuilder.create_stack_game(text)
    extracted_text = extract_game_from_text(text, False)
    for i in extracted_text:
        text.values.remove(i)
    stack.add_row(50)
    for instruction in generate_all_instructions(text):
        source_column = stack.get_all_in_column(instruction.from_val -1)
        destination_column = stack.get_all_in_column(instruction.to - 1)
        stack.move_all_to_new_column(source_column, instruction.from_val -1, destination_column, instruction.to -1, instruction.num_to_move)
    return stack
        
class Block():
    
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f"[{self.value}]"

    def __str__(self):
        return f"[{self.value}]"

def add_to_end_of_column(value, column):
    last_col_index = None
    reverse_index = len(column) - 1
    while reverse_index >= 0:
        if column[reverse_index].value == " ":
            last_col_index = reverse_index
        else:
            break
        reverse_index -= 1
    column[last_col_index] = value
        

def find_largest_digit(string):
    largest_digit = 0
    for char in string:
        if char.isdigit():
            if int(char) > largest_digit:
                largest_digit = int(char)
    return largest_digit

class StackSystem():

    def __init__(self, cols):
        self.cols = cols
        self.row = {}
    
    def add_row(self, rows):
        for num in range(1, rows):
            row = [Block(' '), Block(' '), Block(' '), Block(' '), Block(' '), Block(' '),Block(' '), Block(' '), Block(' ')]
            new_row = max(self.row.keys()) + num
            self.row[new_row] = row
    
    def get_all_in_column(self, column):
        col = []
        for row in self.row.keys():
            col.append(self.row[row][column])
        return col
    
    def replace_column(self, column, src_idx):
        counter = 0
        for row in self.row.keys():
            self.row[row][src_idx] = column[counter]
            counter+=1
    
    def move_to_new_column(self, source_column, src_idx, destination_column, dest_idx):
        src_itm_idx = self.__get_last_block_in_col(source_column)
        last_value_in_col = source_column[src_itm_idx]
        source_column[src_itm_idx] = Block(" ")
        self.replace_column(source_column, src_idx)
        add_to_end_of_column(last_value_in_col, destination_column)
        self.replace_column(destination_column, dest_idx)
    
    def move_all_to_new_column(self, source_column, src_idx, destination_column, dest_idx, amount_to_grab):
        src_itm_idx = self.__get_last_block_in_col(source_column) +1
        counter = amount_to_grab
        while counter != -1:
            # print(src_itm_idx)
            add_to_end_of_column(source_column[src_itm_idx - counter], destination_column)
            source_column[src_itm_idx - counter] = Block(" ")
            counter -= 1
        # add_to_end_of_column(last_value_in_col, destination_column)
        self.replace_column(source_column, src_idx)
        self.replace_column(destination_column, dest_idx)

    def __get_last_block_in_col(self, column):
        last_one = len(column) - 1
        for index, item in enumerate(column):
            if item.value != " ":
                last_one = index
        return last_one
    
    def __str__(self):
        full_str = ""
        for ridx, row in enumerate(reversed(self.row.keys())):
            row_str = ""
            for item in self.row[row]:
                row_str += f" {str(item)} "
            full_str += row_str + "\n"
        for num in range(0,self.cols):
            full_str += f"  {num+1}  "
        return full_str

class StackSystemBuilder():

    @staticmethod
    def create_stack_game(text):
        game_board = extract_game_from_text(text, False)
        largest_digit = find_largest_digit(game_board[-1].strip())
        gamer = StackSystem(largest_digit)
        all_board = []
        for board_piece in game_board[0:-1]:
            all_board.append(board_piece)
        all_board.reverse()
        for row_index, row in enumerate(all_board):
            row_counter = 0
            length_of_row = len(row)
            while row_counter < length_of_row:
                cur_obj = f"{str(row[row_counter])}{row[row_counter+1]}{row[row_counter+2]}"
                if not gamer.row.get(row_index + 1):
                    gamer.row[row_index + 1] = []
                gamer.row[row_index + 1].append(Block(cur_obj[1]))
                row_counter += 4
        return gamer

if __name__ == "__main__":
    print(solution_1())
    # print(solution_2())
