#! /usr/bin/python
'''
A script for renaming Files with american style dates to european style date
'''

import shutil, os, re

datepattern = re.compile(r'''^(.*?) #all text before the date
        ((0|1)?\d)-                 #one or two digits for the month
        ((0|1|2|3)?\d)-             #one or two digits for the day
        ((19|20)\d\d)               #four digits for the year
        (.*?)$
        ''', re.VERBOSE)
for a in os.listdir('.'):
    result = datepattern.search(a)

    if result == None:
        continue
    beforepart = result.group(1)
    monthpart = result.group(2)
    daypart = result.group(4)
    yearpart = result.group(6)
    afterpart = result.group(8)

    eurofilename = beforepart + daypart + '-' + monthpart + '-' + yearpart + afterpart

    absworkingdir = os.path.abspath('.')
    amrfilename = os.path.join(absworkingdir, a)
    eurofilename = os.path.join(absworkingdir, eurofilename)

    print('Renaming {} to {}'.format(amrfilename, eurofilename))
    shutil.move(amrfilename, eurofilename)
