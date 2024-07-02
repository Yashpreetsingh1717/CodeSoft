while True:
    
    print("-----Calculator-----")
    print('''
          1. Addition
          2. Substraction
          3. Multiplication
          4. Division
          5. Exit
          ''')
    userchoice = int(input("Enter the operator: "))
    
    if userchoice == 1:
        num = int(input("\nValue 1: "))
        num2 = int(input("Value 2: "))
        result = num+num2
        print("=",result)              
        
    elif userchoice == 2:
        num = int(input("\nValue 1: "))
        num2 = int(input("Value 2: "))
        result = num-num2
        print("=",result)
    
    elif userchoice == 3:
        num = int(input("\nValue 1: "))
        num2 = int(input("Value 2: "))
        result = num*num2
        print("=",result)
    
    elif userchoice == 4:
        num = int(input("\nValue 1: "))
        num2 = int(input("Value 2: "))
        result = num/num2
        print("=",result)
    
    elif userchoice == 5:
        break
    
    else:
        print("\n!!!!! Invalid Input !!!!!")                