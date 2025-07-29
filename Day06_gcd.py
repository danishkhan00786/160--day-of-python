number1 , number2 = map(int,input("enter numbers").split())
def gcd(number1, number2 ):
    if number2==0:
        return number1
    else :
        return gcd(number2,number1%number2)
print(f"gcd of yours {number1},{number2} is ", gcd(number1,number2) )  
