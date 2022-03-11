def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,4):
        if not text[i].isdecimal():
            return False
    if text[4] != '-':
        return False
    for i in range(5,8):
        if not text[i].isdecimal():
            return False
    if text[8] != '-':
        return False
    for i in range(9,12):
        if not text[i].isdecimal():
            return False
    return True

message = 'Call me tomorrow, Thank you!'
counter = 0
for i in range(len(message)):
    chunk = message[i:i+12]
    result = isPhoneNumber(chunk)
    if result == True:
        print('Phone number found from the text , {}'.format(chunk))
        counter += 1

if counter == 0:
    print('Phone number not found from the text')
print('Done')
