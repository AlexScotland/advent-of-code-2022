# Tuning Trouble
import pandas as pd
import numpy as np

from Day_1 import TextInput

def is_tree_visible_from_sides(tree_index, row):
    current_tree = row[tree_index]
    # Right
    right_visibility = True
    right_side = row[tree_index:]
    right_side = np.delete(right_side, 0)
    for tree in right_side:
        if tree.height >= current_tree.height:
            right_visibility = False
        else:
            current_tree
    # Left
    left_visibility = True

    for tree in row[0:tree_index]:
        if tree.height >= current_tree.height:
            left_visibility = False

    if left_visibility or right_visibility:
        return True
    return False

class Forest:
    def __init__(self):
        self.trees = []
        self.highest_tree_score = 0
    
    def __str__(self):
        ret_str = "\n"
        for row in self.trees:
            for tree in row:
                if tree.visible:
                    ret_str+="Y"
                else:
                    ret_str+="N"
            ret_str+="\n"
        return ret_str

    def add_trees_to_forest(self, tree_list):
        self.trees.append(tree_list)
    
    def __assign_side_visibility(self):
        for row_index, row in enumerate(self.trees[1:len(self.trees)-1]):
            for tree_index, tree in enumerate(row):
                if tree.visible:
                    continue
                tree.visible = is_tree_visible_from_sides(tree_index, row)
        
    def __assign_vertical_visibility(self):
        for col in self.trees.T:
            for index, tree in enumerate(col):
                if tree.visible:
                    continue
                tree.visible = is_tree_visible_from_sides(index, col)

    def __set_perimeter(self, value):
        # First Row
        for tree in self.trees[0]:
            tree.visible = value
        # Last Row
        for tree in self.trees[-1,:]:
            tree.visible = value
        # First Column
        for tree in self.trees[:, 0]:
            tree.visible = value
        # Last Column
        for tree in self.trees[:, -1]:
            tree.visible = value

    def __find_visibility_for_all_trees_in_forest(self):
        self.__assign_side_visibility()
        self.__assign_vertical_visibility()
    
    def set_tree_visibility_for_forest(self):
        self.trees = self.trees.to_numpy()
        self.__set_perimeter(True)
        self.__find_visibility_for_all_trees_in_forest()
        
    def calculate_all_scores(self):
        for index_row, tree_row in enumerate(self.trees):
            for col_index, tree in enumerate(tree_row):
                score = tree.score
                if score > self.highest_tree_score:
                    self.highest_tree_score = score
                    print(f"Highest score is {self.highest_tree_score} set by {tree.height} at row {index_row} col{col_index}")
        return self.highest_tree_score

    def visible_trees(self):
        counter = 0
        for tree_row in self.trees:
            for tree in tree_row:
                if tree.visible:
                    counter += 1
        return counter


class Tree:
    def __init__(self, height):
        self.height = height
        self.visible = None
        self.scores = []
        self.score = 1
    
    def set_visibility(self, visiblity):
        self.visible = visiblity
    
    def calculate_score(self):
        self.score = np.prod(self.scores)
        return self.score

def calculate_horizontal_score(list_of_trees, col_index):
    cur_tree = list_of_trees[col_index]
    left_list = np.flip(list_of_trees[:col_index])
    right_list = list_of_trees[col_index:]
    right_list = np.delete(right_list, 0)
    left_score = 0
    right_score = 0
    for tree in left_list:
        left_score += 1
        if tree.height >= cur_tree.height:
            break
    
    for tree in right_list:
        right_score += 1
        if tree.height >= cur_tree.height:
            break
    return left_score, right_score


def calculate_scores(list_of_trees, row_index, col_index):
    current_tree = list_of_trees[row_index][col_index]
    row = list_of_trees[row_index]
    col = list_of_trees.T[col_index]
    up, left, right, down = 0, 0, 0, 0
    left, right = calculate_horizontal_score(row, col_index)
    up, down = calculate_horizontal_score(col, row_index)

    return up, left, right, down

    
def solution_1(text_string, forest_obj):
    forest = forest_obj
    for row in text_string.values:
        row = row.strip()
        tree_row = []
        for character in row:
            tree_row.append(Tree(int(character)))
        forest.add_trees_to_forest(tree_row)
    # Calculate visibility:
    forest.trees = pd.DataFrame(forest.trees)
    forest.set_tree_visibility_for_forest()
    return forest

def solution_2(forest_obj):
    for row_index, tree_row in enumerate(forest_obj.trees):
        for col_index, tree in enumerate(tree_row):
            up, left, right, down = calculate_scores(forest_obj.trees, row_index, col_index)
            tree.score = up * left * right * down
    
    forest_obj.calculate_all_scores()
    return forest_obj.highest_tree_score

if __name__ == "__main__":
    text = TextInput("./inputs/day_8.txt")
    forest = solution_1(text, Forest())
    # print(forest.visible_trees()) # Sol 1
    print(solution_2(forest))
    # TEST:  259308


