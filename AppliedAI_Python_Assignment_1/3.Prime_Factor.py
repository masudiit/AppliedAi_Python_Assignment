"""
3. Write a program to find out the prime factors of a number. Example: prime factors of 56 - 2, 2, 2, 7
Ref; https://www.youtube.com/watch?v=6PDtgHhpCHo
"""

import math 
        

def isPrimeFactor(n):
     for i in range(2, int(math.sqrt(n)) + 1 ):
         if n%i == 0 :
             while n%i == 0:
                n = n/i 
                print(str(i) )
            
            
if __name__ == '__main__':
    inputValue =  100
    isPrimeFactor(inputValue)