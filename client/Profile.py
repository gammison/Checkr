import os
import re

class Profile():

    def __init__(self, path):
        self.path = open(path, 'r')
        self.profile_name = ""
        self.file_path = []
        self.x_vector = []
        self.y_vector = []

    # Setting files
    def set_profile_name(self):
        self.profile_name = self.path.readline()

    def set_file_paths(self):
        line_path = self.path.readline()
        for line in line_path.split(" "):
            self.file_path.append(line)
        return self.file_path

    def set_x_vector(self):
        x_vector = self.path.readline()
        for array in x_vector.split(" "):
            temp_array = []
            array = re.sub("[\[]", '', array)
            array = array.replace(']', '')
            for single in array.split(','):
                if single.strip().isnumeric():
                    temp_array.append(int(single))
            self.x_vector.append(temp_array)

    def set_y_vector(self):
        y_vector = self.path.readline()
        print(y_vector)
        for array in y_vector.split(" "):
            print(array)
            self.y_vector.append(array)

    # Accessing files
    def get_profile_name(self):
        return self.profile_name

    def get_file_paths(self):
        return self.file_path

    def get_x_vector(self):
        return self.x_vector

    def get_y_vector(self):
        return self.y_vector

path = os.path.realpath('profiles/test.txt')
test = Profile(path)
test.set_profile_name()
test.set_file_paths()
test.set_y_vector()
test.set_x_vector()
print(test.get_profile_name())
print(test.get_file_paths())
# print(test.get_x_vector())
print(test.get_y_vector())
