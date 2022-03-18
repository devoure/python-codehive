'''
This script will copy the file and make multiple copies of it
'''
#! /usr/bin/python

import os, shutil

moptions = ['03', '05', '06', '09', '11', '12']
doptions = ['22', '11', '09', '30', '31', '29']
yoptions = ['2003', '2005', '2006', '2009', '2011', '2012']

path = os.getcwd()
print(path)
for (a, b ,c) in zip(moptions, doptions, yoptions):
    filepath = path + '/11-10-1998.txt'
    shutil.copy(filepath, '{}-{}-{}.txt'.format(a,b,c))
