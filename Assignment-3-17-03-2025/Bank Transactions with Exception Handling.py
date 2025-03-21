
class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the account balance"""
    pass

class BankAccount:
    def __init__(self):
        self.balance = 0 

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("You must deposit a positive amount.")
        self.balance += amount
        print(f"You've deposited ₹{amount}. Your new balance is ₹{self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Not enough funds! Please check your balance.")
        self.balance -= amount
        print(f" Withdrawal of ₹{amount} successful! Remaining balance: ₹{self.balance}.")

account = BankAccount()

while True:
    print("\n Welcome to Your Bank Account")
    print("1️ Deposit Money")
    print("2️ Withdraw Money")
    print("3️ Exit")
    
    choice = input("Choose an option (1/2/3): ")
    
    if choice == "1":
        try:
            amount = float(input("Enter amount to deposit: ₹"))
            account.deposit(amount)
        except ValueError as ve:
            print(f" Error: {ve}")

    elif choice == "2":
        try:
            amount = float(input("Enter amount to withdraw: ₹"))
            account.withdraw(amount)
        except ValueError as ve:
            print(f" Error: {ve}")
        except InsufficientFundsError as ife:
            print(f" Error: {ife}")

    elif choice == "3":
        print("Thank you for banking with us")
        break

    else:
        print(" Invalid choice! Please enter 1, 2, or 3.")
