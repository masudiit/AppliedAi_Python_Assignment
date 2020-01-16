"""
9. Write a function sumPdivisors() that finds the sum of proper divisors of a number. Proper
divisors of a number are those numbers by which the number is divisible, except the
number itself. For example proper divisors of 36 are 1, 2, 3, 4, 6, 9, 18
Ref: https://www.geeksforgeeks.org/sum-of-all-proper-divisors-of-a-natural-number/
"""

import math 

def sumPdivisors(num):
    result=0
    #for i in range(1, int(math.sqrt(num))):
    for i in range(1, num):
       if num % i == 0:
          print(i)
          result += i 
    print(' Summation:' + str(result))


if __name__ == '__main__':
    inputValue = 36
    sumPdivisors(inputValue)


