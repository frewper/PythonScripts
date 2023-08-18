


def optionExecutor(userInput):

    if isnumeric(userInput):
        
   
    if(userInput==1):
        print("Enter the numbers to add")
    elif (userInput==2):
        print("Enter the numbers to subtract")
    elif userInput == 6 :
        print("Exiting")
        exit()

while True:
    print("Please Select one of the follwing options")
    print("1. Add numbers")
    print("2. Subtract numbers")
    print("3. Multiply numbers")
    print("4. Divide numbers")
    print("5. Modulo numbers")
    print("6. Modulo numbers")

    userInput = input()

    print(userInput)

    optionExecutor(userInput)

    


 