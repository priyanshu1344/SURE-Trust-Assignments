class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ₹{amount}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough balance.")
        else:
            self.balance -= amount
            print(f"Withdrawn: ₹{amount}")
    
if __name__ == "__main__":
    account = BankAccount(float(input("Enter starting balance: ")))
    
    while True:
        action = input("Deposit, Withdraw, or Exit? ").lower()
        if action == "exit":
            break
        elif action in ("deposit", "withdraw"):
            amount = float(input("Enter amount: "))
            if action == "deposit":
                account.deposit(amount)
            else:
                account.withdraw(amount)
            print(f"Balance: ₹{account.balance}")
        else:
            print("Invalid choice.")
