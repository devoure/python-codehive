#! /usr/bin/python 
'''
This is a python script to copy and paste a password saved in the file
'''
PASSWORDS = {
        'gmail':'thisismygmailpassword',
        'blog':'thisismyblogpassword',
        'student-portal':'thisisyourstudentportal'
        }

import sys, pyperclip

if len(sys.argv) < 2:
    print('Password Manager Script'.center(20) + '{}'.format(sys.argv[0]))
    print('USAGE'.center(20, '*'))
    print('Step 1'.rjust(5, '*') + 'Enter the account you want to get password')
    print('Step 2'.rjust(5, '*') + 'The scripts copies the password if found')
    print('START'.center(20))
    sys.exit()

account = sys.argv[1]
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('SUCCESS'.center(20, '*'))
    print('The password for {} was  copied to clipboard!'.format(account))
else:
    print('FAIL'.center(20, '*'))
    print('No password for account {} found'.format(account))

print('THANK YOU'.center(20, '*'))








