# Day 1

class Elf():
    def __init__(self, calorie):
        self.calories = calorie

class TextInput():
    def __init__(self, file):
        self.values = self.__read_file(file)
    
    def __read_file(self, file_name):
        return open(file_name,"r").readlines()

class ElfFactory():
    def __init__(self):
        self.elves = self.build_all_elves(TextInput("./inputs/day_1.txt"))

    def __build_elf(self, cals):
        return Elf(cals)

    def build_all_elves(self, text):
        text = text.values
        list_of_all_elves = []
        cal_count = 0
        for line in text:
            if line != "\n":
                cal_count+= int(line)
            else:
                list_of_all_elves.append(self.__build_elf(cal_count))
                cal_count = 0
        list_of_all_elves.sort(key=lambda elf: elf.calories, reverse=True)
        return list_of_all_elves

    def get_top_elves(self, number):
        top_elves = []
        for num in range(0, number):
            top_elves.append(self.elves[num].calories)
        return top_elves


if __name__ == "__main__":
    all_elves = ElfFactory()
    print(all_elves.elves[0].calories)
    print(sum(all_elves.get_top_elves(3)))