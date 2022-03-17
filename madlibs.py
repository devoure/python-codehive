#! /usr/bin/python
'''
Find occurrences and prompt the user to replace them
'''
import os, re

adj = input('Enter an adjective:\n')
noun = input('Enter a noun:\n')
verb = input('Enter a verb\n')
noun2 = input('Enter another noun\n')

currentpath = os.getcwd()
filepath = os.path.join(currentpath, 'madlibs.txt')
txtfile = open(filepath, 'r+')
content = str(txtfile.read())
print('The content: ', content)

adjregex = re.compile(r'ADJECTIVE')
nounregex = re.compile(r'NOUN')
verbregex = re.compile(r'VERB')
noun2regex = re.compile(r'NOUN2')

content = adjregex.sub(adj, content)
content = nounregex.sub(noun, content)
content = verbregex.sub(verb, content)
content = noun2regex.sub(noun2, content)
print(content)
txtfile.write(content)
txtfile.close()








