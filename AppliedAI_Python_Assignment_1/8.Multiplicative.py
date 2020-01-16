"""
8. If all digits of a number n are multiplied by each other repeating with the product, the one
digit number obtained at last is called the multiplicative digital root of n. The number of
times digits need to be multiplied to reach one digit is called the multiplicative
persistance of n.
Example: 86 -> 48 -> 32 -> 6 (MDR 6, MPersistence 3)
 341 -> 12->2 (MDR 2, MPersistence 2)
Using the function prodDigits() of previous exercise write functions MDR() and
MPersistence() that input a number and return its multiplicative digital root and
multiplicative persistence respectively
"""

from functools import reduce

def  prodDigits(num):
     digit_lst =list(map(int,str(num)))
     products = reduce(lambda x,y: x*y, digit_lst)
     return products

def MPersistence(count ):
    print('MPersistence : {0}'.format(str(count)))

def MDR(num):
    result =[]
    count=0
    while True:
        product = prodDigits(num)
        #print(product)
        result.append(product)
        num = product
        count =count +1
        if(product == 0 or len(str(product)) == 1):
            break
 
    str1=''
    for item in result:
        str1 += str(item) +'->'

    print(str1)
    print('MDR : {0}'.format(str(result[-1])))
    MPersistence(count)
           

if __name__ == '__main__':
    inputValue = 86 
    MDR(inputValue)
    inputValue = 341 
    MDR(inputValue)


