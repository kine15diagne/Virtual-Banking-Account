from datetime import timedelta, datetime

class BankAccount:
    def __init__(self, holder, initial_balance=0):
        self.holder = holder
        self.balance = initial_balance
        self.history = []

    def deposit(self, amount):
        if amount > 0:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.balance += amount
            self.history.append(f"[{now}] : + {amount}€")
            print(f"Deposit successful. Final balance: {self.balance}€")
        else:
            print("Cannot deposit negative amounts.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.balance -= amount
                self.history.append(f"[{now}] Withdrawal: -{amount}€")
                print(f"Withdrawal successful. Final balance: {self.balance}€")
            else:
                print("Insufficient funds.")
        else:
            print("Negative amounts are not allowed.")

    def check_balance(self):
        print(f"{self.holder}, your current balance is {self.balance}€")

    def view_transaction_history(self):
        print("Transaction History:")
        if not self.history:
            print("No transactions yet.")
        else:
            for transaction in self.history:
                print(f"- {transaction}")



