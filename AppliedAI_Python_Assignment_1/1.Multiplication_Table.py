"""
1.Write a function that inputs a number and prints the multiplication table of that number
"""

def multiplicationTable(num):
    for i in range(1,11):
        print(num, 'x', i, '=', num*i)

if __name__ == '__main__':
    #inputValue =int(input())
    #multiplicationTable(inputValue)
    inputValue =10
    multiplicationTable(inputValue)
	


