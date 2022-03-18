'''
This allows you to walk through a directory
'''

import os

path = os.getcwd()

for filename, subfolder, filenames in os.walk(path):
    print('The folder name is :{}'.format(filename))
    for a in subfolder:
        print('The subfolders in {} are :\n{}'.format(filename, a))
    for b in filenames:
        print('The filenames in {} are :\n{}'.format(filename, b))

