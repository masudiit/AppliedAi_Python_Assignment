"""
2. Write a program to print twin primes less than 1000. If two consecutive odd numbers are
both prime then they are known as twin primes
"""
   

def isPrime(num):
    if (num==1):
        return False
    elif (num==2):
        return True
    else:
        for x in range(2,num):
            if(num % x==0):
                return False
        return True


def twinPrime(n):
    
    prime = [False for i in range(n + 2)] 
    
    for i in range(2,n):
        if isPrime(i) :
           prime[i] =True 
           #print(str(i) + '> T '  )
        #else:
           #print(str(i) + '> F '  )
           
    #print(prime)
    
    for p in range(2,n):
         if prime[p] and prime[p + 2]: 
            print("(",p,",", (p + 2), ")" ,end='') 


if __name__ == '__main__':
    #inputValue =int(input())
    #twinPrime(inputValue)
    inputValue =  100
    twinPrime(inputValue)