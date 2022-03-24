#! /usr/bin/python

'''
This is a python script to:
    get a street address from the command line arguements or clipboard
    open the web browser to the google maps page for the address
'''

import webbrowser , sys, pyperclip

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/'+address)



