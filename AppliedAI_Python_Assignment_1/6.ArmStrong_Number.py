"""
6. Write a function cubesum() that accepts an integer and returns the sum of the cubes of
individual digits of that number. Use this function to make functions PrintArmstrong() and
isArmstrong() to print Armstrong numbers and to find whether is an Armstrong number.
Ref: 
https://www.youtube.com/watch?v=YbAvvfiZGZo
https://www.geeksforgeeks.org/program-for-armstrong-numbers/
"""

def isArmstrong(num,digit_lst): 
    length =len(str(num))
    b =list(map(lambda x: x**length,digit_lst))
    summation =sum(b)
    if summation == num:
        printArmstrong('The number {0} is an armstrong'.format(str(num)))
    else:
        printArmstrong('The number {0} is not an armstrong'.format(str(num)))
     

def printArmstrong(str):
    print(str)

def cubesum(num):  
    a =list(map(int,str(num)))  
    individual_digit_sum = sum(a)   
    print ('Sum of individual digit >' +str(individual_digit_sum))
    isArmstrong(num,a)


if __name__ == '__main__':
     #inputValue =int(input())
    #decToBinary(inputValue)
    inputValue = 153 #120 #407 
    cubesum(inputValue)

