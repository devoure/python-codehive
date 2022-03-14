#!  /usr/bin/python
'''
A strip regex function that functions like the strip function
'''

import re, sys

if len(sys.argv) ==  1:
    startspace = re.compile(r'^\s')
    endspace = re.compile(r'\s$')
    result = startspace.sub("", ' This ')
    result = endspace.sub("", ' This ')
    print(result)
elif len(sys.argv) == 2:
    userinput = str(sys.argv[1])
    inputregex = re.compile(userinput)
    result = inputregex.sub("", 'This')
    print(result)
