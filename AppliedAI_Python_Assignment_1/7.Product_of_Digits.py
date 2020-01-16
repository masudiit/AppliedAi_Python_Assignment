"""
7. Write a function prodDigits() that inputs a number and returns the product of digits of that
number.
"""

from functools import reduce

def  prodDigits(num):
     digit_lst =list(map(int,str(num)))
     products = reduce(lambda x,y: x*y, digit_lst)
     print('Product of digits: {0}'.format(str(products)))


if __name__ == '__main__':
    inputValue = 4513
    prodDigits(inputValue)


