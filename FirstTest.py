


def optionExecutor(userInput):

    print(type(userInput))
    
    try:
        userInput = (int(userInput))
        if (userInput):
            print("is Numeric")
        else:
            print("In Correct Value")
            return
    except:
        print("Value is not numeric")
   
    if userInput==1:
        print("Enter the numbers to add")
    elif userInput==2:
        print("Enter the numbers to subtract")
    elif userInput == 6 :
        print("Exiting")
        exit()


def clearTerminal():
    print("\n\n\n\n\n\\n\n\n\n*******************************************")

while True:
    print("Please Select one of the follwing options")
    print("1. Add numbers")
    print("2. Subtract numbers")
    print("3. Multiply numbers")
    print("4. Divide numbers")
    print("5. Modulo numbers")
    print("6. Modulo numbers")

    userInput = input();
    optionExecutor(userInput)

    


 