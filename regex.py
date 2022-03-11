#This is some functions to cover regex in python

#REGEX COMPILE AND SEARCH
#Will create a pattern and then return the matches if found from text provided
import re

def regexobj():
    #will match the pattern of a phone number
    #the phone number is 0700-000-000
    phonepattern = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d')
    result = phonepattern.search('This is my phone number: 0707-285-682')
    print('Phone number found from the text passed : {}'.format(result.group(0)))

#regexobj()

#REGEX GROUPS
def regexgroup():
    #will match the pattern of an area code and print  the country
    #the area code is +000
    countrycodes={
            '+254':'Kenya',
            '+255':'Tanzania'
            }
    phonepattern = re.compile(r'(\+\d\d\d)-(\d\d\d\d\d\d\d\d\d)')
    result = phonepattern.search('This is my phone number: +254-707285682')
    print('Phone number found from the text passed : {}'.format(result.group(0)))
    for i in countrycodes.keys():
        if i == result.group(1):
            country = countrycodes[i]
            print('The country code is {}, from {}'.format(result.group(1), country))
    code, phonenumber = result.groups()
    phonenumber = '0'+phonenumber
    print('The phone number is :{}'.format(phonenumber))
regexgroup()


