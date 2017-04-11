"""
Create on 04/06/2017
@author: Simon
"""


import random
def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21.
    :return: an even number
    '''
    return random.randrange(10, 22, 2)

def my_test(n = 100):
    result = ''
    for i in range(n):
        result += str(deterministicNumber()) + '-'
    return result

if __name__ == '__main__':
    print my_test(10)