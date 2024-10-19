#python bank management

def show_balance(balance):
    print("         *******************************************************       ")
    print(f"your balance is ${balance :.2f}")
    print("         *******************************************************       ")

def deposit():

    amount = float(input("please enter the amount you want to deposit "))

    if amount <0:
        print("         *******************************************************       ")
        print("enter a valid amount")
        print("         *******************************************************       ")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("enter amount you want to withdraw"))

    if amount > balance:
        print("         *******************************************************       ")
        print("you have insufficient fund")
        print("         *******************************************************       ")
        return 0
    elif amount < 0:
        print("         *******************************************************       ")
        print("please enter a valid amount to proceed  ")
        print("         *******************************************************       ")


        return 0
    else:
        return amount

def main():

    balance = 0
    is_running = True

    while is_running:
        print("**********************************************************************************************************")
        print("                                     WORLD CHANGER BANKING MANAGEMENT                      ")
        print("**********************************************************************************************************")
        print("1. show balance")
        print("2. deposit")
        print("3. withdraw")
        print("4.Exit")
        print(
            "**********************************************************************************************************")


        choice =input("select a number to proceed ")
        if choice == '1':
            show_balance(balance)

        elif choice == '2':
            balance =+ deposit()

        elif choice == '3':
           balance -= withdraw(balance)

        elif choice == '4':
            is_running = False

        else:
            print(
                "**********************************************************************************************************")
            print(" invalid choice")
            print(
                "**********************************************************************************************************")




    print("**********************************************************************************************************")
    print("It was great working with you. Welcome back again")
    print("**********************************************************************************************************")
if __name__ == '__main__':
    main()
