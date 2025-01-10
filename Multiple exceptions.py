try:
    num1,num2=eval(input("enter two numbers saprated by coma: "))
    division=num1/num2

except SyntaxError:
    print("saprate the numbers with coma like this: 10,12")

except ValueError:
    print("invalid number")    

except:
    print("nothing")    
finally:
    print("yay")    


