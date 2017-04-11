"""
Create on 04/06/2017
@author: Simon
"""

import random
def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100 
    '''
    return random.randrange(0, 100, 2)

def testGenEven(n=100):
    result = ''
    for i in range(n):
        result += str(genEven()) + '-'
    return result

if __name__ == '__main__':
    print testGenEven()