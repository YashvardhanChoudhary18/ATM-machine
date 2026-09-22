class ATM:
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        print("Your balance is:", self.balance)

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.balance += amount
        print("Deposited! New balance:", self.balance)

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("Withdrawn! New balance:", self.balance)

    def menu(self):
        while True:
            print("\n1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = int(input("Enter choice: "))

            if choice == 1:
                self.check_balance()
            elif choice == 2:
                self.deposit()
            elif choice == 3:
                self.withdraw()
            elif choice == 4:
                print("Thank you!")
                break
            else:
                print("Invalid choice")


# ---------- Program Start ----------
my_atm = ATM(pin=1234, balance=5000)

entered_pin = int(input("Enter your PIN: "))

if entered_pin == my_atm.pin:
    print("PIN Correct!")
    my_atm.menu()
else:
    print("Wrong PIN!")