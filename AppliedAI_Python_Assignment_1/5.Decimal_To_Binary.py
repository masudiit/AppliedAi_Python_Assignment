

# decimal to binary 
def decToBinary(n): 
      
    binaryNum = [];   
    while (n > 0):  
        binaryNum.append (n% 2); 
        n = int(n / 2); 

    result= list(reversed(binaryNum))
    #print(result)
    return result

if __name__ == '__main__':
     #inputValue =int(input())
    #decToBinary(inputValue)
    inputValue =  20
    result= decToBinary(inputValue)
    print('Decimal to Binary> {0} > {1}'.format(str(inputValue),str(result)))