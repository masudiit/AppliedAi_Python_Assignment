"""
The number of permutations of n objects taken r at a time is determined by the following formula:

P(n,r)=n!(n−r)!
n! is read n factorial and means all numbers from 1 to n multiplied e.g.

5!=5⋅4⋅3⋅2⋅1
This is read five factorial. 0! Is defined as 1.

0!=1

Example

A code have 4 digits in a specific order, the digits are between 0-9.
How many different permutations are there if one digit may only be used once?

A four digit code could be anything between 0000 to 9999, hence there are 10,000 combinations
if every digit could be used more than one time but since we are told in the question that one digit 
only may be used once it limits our number of combinations. In order to determine the correct number
of permutations we simply plug in our values into our formula:

P(n,r)=10!(10−4)!=10⋅9⋅8⋅7⋅6⋅5⋅4⋅3⋅2⋅16⋅5⋅4⋅3⋅2⋅1=5040


In our example the order of the digits were important, if the order didn't matter
we would have what is the definition of a combination. The number of combinations
of n objects taken r at a time is determined by the following formula:

C(n,r)=n!(n−r)!r!
"""





def factorial(n):    
    fact = 1;  
  
    for i in range(2,n+1):  
        fact = fact * i;  
  
    return fact;  
   
  
# def to calculate permutation  
def nPr(n, r):  
   
    pnr = factorial(n) / factorial(n - r);  
  
    return pnr;  


# def to calculate combination  
def nCr(n, r): 
    cnr = (factorial(n) / (factorial(r)   * factorial(n - r))) 
    return cnr


if __name__ == '__main__':
      n = 10
      r = 4
      print('Permutation> ' + str(int(nPr(n, r))))
      print('Combination> ' + str(int(nCr(n, r))))
