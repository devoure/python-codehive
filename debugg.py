'''
This contains a summary on debugging tools for python
'''
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info('RAISING EXCEPTIONS PART')
#RAISING EXCEPTIONS

def boxdrawer(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbom must be a single character string')
    if width <= 2:
        raise Exception('width must be greater than 2')
    if height <= 2:
        raise Exception('Height must be greater than 2')
    print(symbol * width)
    for i in range(height -2):
        print(symbol +  (' '*(width - 2)) + symbol)
    print(symbol * width)

#for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('*',1, 3), ('ZZ', 3, 3)):
    #try:
        #boxdrawer(sym, w, h)
    #except Exception as err:
        #print('An exception happened: '+str(err))

logging.info('TRACEBACK PART')

#TRACEBACK
import traceback

def boxdrawer(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbom must be a single character string')
    if width <= 2:
        raise Exception('width must be greater than 2')
    if height <= 2:
        raise Exception('Height must be greater than 2')
    print(symbol * width)
    for i in range(height -2):
        print(symbol +  (' '*(width - 2)) + symbol)
    print(symbol * width)

#for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('*',1, 3), ('ZZ', 3, 3)):
#    try:
#        boxdrawer(sym, w, h)
#    except:
#        print(traceback.format_exc())

logging.info('ASSERTION PART')

#ASSERTIONS

var_a = 2
var_b = 3
assert var_a == var_b, 'The two variables dont match'

#LOGGING
