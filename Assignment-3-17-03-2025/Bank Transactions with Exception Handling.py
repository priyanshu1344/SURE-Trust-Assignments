class BankAccount:
    def __init__(self):
        self.balance = 0 

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}. Balance: ₹{self.balance}")
        else:
            print("Deposit must be positive!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. Balance: ₹{self.balance}")

account = BankAccount()

while True:
    choice = input("\n1. Deposit\n2. Withdraw\n3. Exit\nChoose (1/2/3): ")

    if choice == "1":
        account.deposit(float(input("Enter amount: ₹")))
    elif choice == "2":
        account.withdraw(float(input("Enter amount: ₹")))
    elif choice == "3":
        print("Goodbye")
        break
    else:
        print("Invalid choice!")
