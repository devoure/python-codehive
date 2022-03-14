#!  /usr/bin/python
'''
Detect the password strength if strong or not
'''

import re, sys

lenregex = re.compile(r'^(.){8,}$')
lenresult = lenregex.findall(str(sys.argv[1]))

upperregex = re.compile(r'[A-Z]')
upperresult=upperregex.findall(str(sys.argv[1]))

lowerregex = re.compile(r'[a-z]')
digitregex = re.compile(r'\d')
lowerresult=digitregex.findall(str(sys.argv[1]))

if len(lenresult) > 0 and len(upperresult) > 0 and len(lowerresult) > 0:
    print("Strong Password")

else:
    print("Weak password")
