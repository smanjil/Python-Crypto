
def numInput():
    a , b = input("Enter a : ") , input("Enter b : ")
    print euclidGCD(a , b)
    
def euclidGCD(a , b):
    while(b):
        a , b = b , a % b
    return a

numInput()



