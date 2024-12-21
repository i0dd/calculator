# Calculator
print("options \n 1 - add \n 2 - subtract \n 3 - multiply \n 4 - divide \n 5 - exit")


while True:
    option = int(input("please enter the number of the option you want to do: "))
    firstnum = float(input("enter your first number: "))
    secondnum = float(input("enter your second number: "))

    if option == 1:
        result = firstnum + secondnum
        print(f"the ans is: {result}")
    elif option == 2:
        result = firstnum - secondnum
        print(f"the ans is: {result}")
    elif option == 3:
        result = firstnum * secondnum
        print(f"the ans is: {result}")
    elif option == 4:
        if secondnum != 0:
            result = firstnum / secondnum
            print(f"the ans is: {result}")
        else:
            print("division by zero is not allowed.")
    elif option == 5:
        print("thank you for using this calculator")
        break
    else:
        print("Invalid please try again")
