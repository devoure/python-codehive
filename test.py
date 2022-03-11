import re
apattern = re.compile(r'(\+\d{3})-(\d{3}-\d{3})')
result = apattern.search('My number is +254-707-285-682')
print('The resulting object: {}'.format(result))
print('The regex object for matching: {}'.format(apattern))
print('The matched text is : {}'.format(result.group()))
print('The country code is :{}'.format(result.group(1)))
code, number = result.groups()
number = '0' + number
print('The phone number is :{}'.format(number))
