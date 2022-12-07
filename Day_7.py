# Tuning Trouble
from Day_1 import TextInput

class Command():
    
    def __init__(self, args):
        self.args = args

class File():
    def __init__(self, name, size):
        self.name = name
        self.size = size

class Directory():
    def __init__(self, name, parent = None):
        self.name = name
        self.contents = []
        self.size = None
        self.parent = parent
    
    def add_file_to_content(self, content):
        self.contents.append(content)
    
    def get_all_child_dirs(self):
        all_children = []
        for child in self.contents:
            if isinstance(child, Directory):
                all_children.append(child)
        return all_children


def parse_string(string, previous_command, directory):
    string_separated = string.split()
    if previous_command.args[0] == "ls":
        if string_separated[0] == "dir":
            new_dir = Directory(string_separated[1], directory)
            directory.contents.append(new_dir)
        else:
            directory.contents.append(File(string_separated[1], string_separated[0]))

def get_directory_from_current(directory_name, current_directory):
    for directory in current_directory.contents:
        if directory.name == directory_name and isinstance(directory, Directory):
            return directory
    return None

def calculate_size_of_directory(directory, size= 0):
    for file in directory:
        if isinstance(file, Directory):
            file.size = calculate_size_of_directory(file.contents)
        size += int(file.size)
    return size

def recur_grab_all_children(directory, max):
    num_summed = 0 
    for file in directory:
        if isinstance(file, Directory):
            num_summed += recur_grab_all_children(file.get_all_child_dirs(), max)
            if file.size <= max:
                num_summed += file.size
    return num_summed

def sum_all_dirs_under_max(root, max):
    return recur_grab_all_children(root.contents, max)
        
def build_structure(text_list):
    current_directory = Directory("/")
    root_directory = current_directory
    previous_command = None
    for line in text_list[1:]:
        if line[0] == "$":
            command_line = line.split()[1:]
            previous_command = Command(command_line)
            if previous_command.args[0] == "cd":
                if previous_command.args[1] == "..":
                    current_directory = current_directory.parent
                    continue
                nested_directory = get_directory_from_current(previous_command.args[1], current_directory)
                if nested_directory:
                    current_directory = nested_directory
                else:
                    current_directory = Directory(previous_command.args[1], current_directory)

        else:
            parse_string(line, previous_command, current_directory)
    return root_directory

# def find_largest_sub_dir_greater_than_max(directory, max, list_of_all_eligible_dirs = []):
#     for file in directory:
#         if isinstance(file, Directory):
#             print(f"we are looking into the children of {file.name} - {file.size}")
#             list_of_all_eligible_dirs.extend(find_largest_sub_dir_greater_than_max(file.get_all_child_dirs(), max, list_of_all_eligible_dirs))
#             if file.size > max:
#                 list_of_all_eligible_dirs.append(file)
#     print(list_of_all_eligible_dirs)
#     return list_of_all_eligible_dirs

def find_lowest_size_from_subdirs(directory, max, lowest = None):
    for file in directory:
        if isinstance(file, Directory):
            print(file.parent.name, file.name, file.size)
            if file.size >= max:
                lowest = find_lowest_size_from_subdirs(file.get_all_child_dirs(), max, lowest)
                if lowest is None:
                    lowest = file.size
                else:
                    if file.size < lowest:
                        lowest = file.size
    return lowest


def sum_all_dirs_under_max(root, max):
    return recur_grab_all_children(root.contents, max)

def solution_1(text_list, max):
    root_directory = build_structure(text_list)
    calculate_size_of_directory(root_directory.contents)
    return sum_all_dirs_under_max(root_directory, max)

def solution_2(text_list, max):
    root_directory = build_structure(text_list)
    calculate_size_of_directory(root_directory.contents)
    summ =0
    for chil in root_directory.get_all_child_dirs():
        summ += chil.size
    unused_space = 70000000 - summ 
    max_we_need = max - unused_space
    largest_sub_dir = find_lowest_size_from_subdirs(root_directory.contents, max_we_need)
    return largest_sub_dir
    


if __name__ == "__main__":
    text = TextInput("./inputs/day_7.txt").values
    print(solution_1(text, 100000))
    print(solution_2(text, 30000000))

    