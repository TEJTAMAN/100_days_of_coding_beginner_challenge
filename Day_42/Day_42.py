#Create a class for a bank account with methods for deposit and withdrawal.


class BankAccount:
    """A simple bank account class."""

    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} deposited. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds. Current balance: ${self.balance:.2f}.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"${amount:.2f} withdrawn. New balance: ${self.balance:.2f}")

    def __str__(self):
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance:.2f}"


# Main program
def main():
    name = input("Enter the account holder's name: ").strip()
    initial_balance = float(input("Enter the initial balance: ").strip())

    account = BankAccount(name, initial_balance)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. View Account Details")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            amount = float(input("Enter deposit amount: ").strip())
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: ").strip())
            account.withdraw(amount)
        elif choice == "3":
            print(account)
        elif choice == "4":
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
