# Fully containing sequences
from Day_1 import TextInput

class Sequence_Range():

    def __init__(self, range_1, range_2):
        self.range_1 = range_1
        self.range_2 = range_2
        self.overlap_range = self.__range_full_over_lap()
    
    def __range_full_over_lap(self):
        return all(item in self.range_1.range for item in self.range_2.range) or all(item in self.range_2.range for item in self.range_1.range)

class Range():

    def __init__(self, sequence_start, sequence_end):
        self.start = int(sequence_start)
        self.end = int(sequence_end) + 1
        self.range = range(self.start, self.end)

class Sequence_Range_All(Sequence_Range):
    def __init__(self, range_1, range_2):
        self.range_1 = range_1
        self.range_2 = range_2
        self.overlap_range = self.__range_full_over_lap()
        
    def __range_full_over_lap(self):
        return any(item in self.range_1.range for item in self.range_2.range) or any(item in self.range_2.range for item in self.range_1.range)


def solution1():
    text = TextInput("./inputs/day_4.txt")
    counter = 0
    for ranges in text.values:
        ranges = ranges.strip()
        nums = ranges.split(",")
        num_1 = nums[0].split("-")
        num_2 = nums[1].split("-")
        range_1 = Range(num_1[0], num_1[1])
        range_2 = Range(num_2[0], num_2[1])
        seq = Sequence_Range(range_1, range_2)
        if seq.overlap_range:
            counter += 1
    return counter

def solution2():
    text = TextInput("./inputs/day_4.txt")
    counter = 0
    for ranges in text.values:
        ranges = ranges.strip()
        nums = ranges.split(",")
        num_1 = nums[0].split("-")
        num_2 = nums[1].split("-")
        range_1 = Range(num_1[0], num_1[1])
        range_2 = Range(num_2[0], num_2[1])
        seq = Sequence_Range_All(range_1, range_2)
        if seq.overlap_range:
            counter += 1
    return counter


if __name__ == "__main__":
    print(solution1())
    print(solution2())