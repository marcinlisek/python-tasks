def greates_common_divider():
    
    no_of_entries=int(input("Enter the number of calculations to perform "))
    
    for i in range(0,no_of_entries):
        
        num1=int(input("Enter the first number "))
        num2=int(input("Enter the secont number "))
        
        if num1>num2:
            for divider in range(num2,0,-1):
                if num1%divider==0 and num2%divider==0:
                    print(divider)
                    break
        
        elif num2>num1:
            for divider in range(num1,0,-1):
                if num1%divider==0 and num2%divider==0:
                    print(divider)
                    break
                
                
        else:
            print(divider)
            break
