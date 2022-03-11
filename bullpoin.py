#! /usr/bin/python 
'''
Adding Bullets To Lists
'''
import sys, pyperclip

text = '''Harry Potter Sorcerers Stone
Harry Potter Chambers Of Secrets
Harry Potter Prisoner Of Azkaban
Harry Potter Goblet Of Fire'''
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '*' + ' ' + lines[i]

text = '\n'.join(lines)
pyperclip.copy(text)
print(text)






