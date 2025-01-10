zara=False
while not zara:
    try:
        num=int(input("enter a number: "))
        while num%2==0:
            print("bye")
        zara=True   
    except:
        print("invalid")
    finally:
        print("u the best")    
        

    

