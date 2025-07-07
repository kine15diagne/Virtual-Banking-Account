from bank_account import BankAccount


print("""
------------------------------------------------------------------------------------------------------------------------
                             Welcome to your Virtual Banking App
------------------------------------------------------------------------------------------------------------------------
    """)

CORRECT_PIN = 123
attempts = 3

while attempts > 0:
    try:
        pin = int(input("Enter your PIN: "))
        if pin == CORRECT_PIN:
            print("PIN accepted. Accessing your account...")
            break
        else:
            attempts -= 1
            print(f"Incorrect PIN. Attempts remaining: {attempts}")
    except ValueError:
        print("Please enter numbers only.")

if attempts == 0:
    print("Too many failed attempts. Access denied.")
else:
    account = BankAccount("Maria", 100)

    continue_session = True
    while continue_session:
        print("\nAvailable operations:")
        print("1. Deposit money")
        print("2. Withdraw money")
        print("3. Check balance")
        print("4. View transaction history")
        print("5. Exit")

        option = input("Select an option (1-5): ")

        if option == "1":
            try:
                amount = float(input("How much would you like to deposit?: "))
                account.deposit(amount)
            except ValueError:
                print("Please enter a valid amount.")
        elif option == "2":
            try:
                amount = float(input("How much would you like to withdraw?: "))
                account.withdraw(amount)
            except ValueError:
                print("Please enter a valid amount.")
        elif option == "3":
            account.check_balance()
        elif option == "4":
            account.view_transaction_history()
        elif option == "5":
            print("Thank you for using Virtual Python Bank. Goodbye!")

            continue_session = False
        else:
            print("Invalid option. Please choose between 1 and 5.")


