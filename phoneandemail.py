#!  /usr/bin/python
'''
Find phone numbers and emails from a string and save it to clipboard
'''
import pyperclip, re

phoneregex = re.compile(r'''
        ((\d{3}|\(\d{3}\))?  #area code, could be optional
        (\s|-|\.)?  #separator
        (\d{3})     #first 3 digits
        (\s|-|\.)   #separator
        (\d{4})     #last 4 digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))?)
        ''', re.VERBOSE)

emailregex = re.compile(r'''
        ([a-zA-Z0-9._%+-]+  #username
        @  #@ symbol
        [a-zA-Z0-9.-]+  #domain name
        (\.[a-zA-Z]{2,4})
        )''', re.VERBOSE)

text = '''
This are my two numbers: 800-420-7240, 415-863-9900
This is my email address: buy@gmail.com
'''
matches = []
for groups in phoneregex.findall(text):
    phonenum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phonenum += ' x' + groups[8]
    matches.append(phonenum)

for groups in emailregex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print('No emails or phone numbers found!')
