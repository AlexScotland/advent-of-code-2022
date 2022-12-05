# Rucksack
from Day_1 import TextInput
# from intertools impor 
UPPER_ORD_MINUS = 38
LOWER_ORD_MINUS = 96

def solution_1():
    file = TextInput("./inputs/day_3.txt")
    all_similarities = []
    for rucksack_content in file.values:
        rucksack_content = rucksack_content.strip()
        ruck = Rucksack(rucksack_content)
        all_similarities.append(ruck.similarities)
    return add_all_priorities(all_similarities)

def solution_2():
    file = TextInput("./inputs/day_3.txt")
    all_groups = []
    breaker = False
    index = 0
    while index <= len(file.values) -1:
        ruck1 = file.values[index].strip()
        ruck2 = file.values[index + 1].strip()
        ruck3 = file.values[index + 2].strip()
        all_groups.append(Group(ruck1, ruck2, ruck3))
        index += 3
    all_sims = 0
    for group in all_groups:
        for key in group.similarities:
            all_sims += group.similarities[key]
    return all_sims
        
class Group():
    
    def __init__(self, ruck1, ruck2, ruck3):
        self.ruck1 = ruck1
        self.ruck2 = ruck2
        self.ruck3 = ruck3
        self.similarities = self.find_sim_between_all_rucks()
    
    def find_sim_between_all_rucks(self):
        sim = {}
        for character in self.ruck1:
            if character in self.ruck2 and character in self.ruck3:
                if character.isupper():
                    sim[character] = ord(character) - UPPER_ORD_MINUS
                else:
                    sim[character] = ord(character) - LOWER_ORD_MINUS
        return sim

class Rucksack():

    def __init__(self, content):
        len_of_content = len(content)
        mid = int(len_of_content/2)
        self.contents = (content[0:mid], content[mid:len_of_content])
        self.similarities = self.__find_similar_contents()
    
    def __find_similar_contents(self):
        similarity_counter = {}
        for content in self.contents[0]:
            if content in self.contents[1]:
                if content.isupper():
                    similarity_counter[content] = ord(content) - UPPER_ORD_MINUS
                else:
                    similarity_counter[content] = ord(content) - LOWER_ORD_MINUS
        return similarity_counter

def add_all_priorities(priority_list):
    counter = 0
    for sims in priority_list:
        for key in sims.keys():
            counter += sims[key]
    return counter
if __name__ == "__main__":
    # print(solution_1())
    print(solution_2())