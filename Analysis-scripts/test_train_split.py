import os
'''
#folder path
dir_path = r'C:\Users\tghon\Desktop\RCOS\Project_CodeNet\data\p00027\Python'

#list to store files
res = []

#iterate through directory
for path in os.listdir(dir_path):
    #check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)

#print(res)
'''

def get_files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

from random import shuffle
def randomize_files(file_list):
    shuffle(file_list)

from math import floor
def get_training_and_testing_sets(file_list):
    split = 0.7
    split_index = floor(len(file_list) * split)
    training = file_list[:split_index]
    testing = file_list[split_index:]
    return training, testing
