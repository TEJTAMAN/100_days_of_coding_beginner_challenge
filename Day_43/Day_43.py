#Implement encapsulation in a class.

"""Encapsulation ensures that sensitive data is hidden from direct access and can only be modified through specific methods."""

class BankAccount:
    """A bank account class demonstrating encapsulation."""

    def __init__(self, account_holder, initial_balance=0):
        """
        Initialize the account with an account holder's name and an initial balance.
        """
        self.__account_holder = account_holder  # Private attribute
        self.__balance = initial_balance  # Private attribute

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.__balance += amount
            print(f"${amount:.2f} deposited. New balance: ${self.__balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > self.__balance:
            print(f"Insufficient funds. Current balance: ${self.__balance:.2f}.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.__balance -= amount
            print(f"${amount:.2f} withdrawn. New balance: ${self.__balance:.2f}")

    def get_balance(self):
        """Return the current balance."""
        return self.__balance

    def get_account_holder(self):
        """Return the account holder's name."""
        return self.__account_holder

    def set_account_holder(self, new_holder):
        """Change the account holder's name."""
        if new_holder.strip():
            self.__account_holder = new_holder.strip()
            print(f"Account holder name updated to {self.__account_holder}.")
        else:
            print("Invalid name. Account holder name not updated.")

    def __str__(self):
        """Return account details."""
        return f"Account Holder: {self.__account_holder}, Balance: ${self.__balance:.2f}"


# Example Usage
if __name__ == "__main__":
    # Create a new bank account
    account = BankAccount("John Doe", 500)

    # Display account details
    print(account)  # Output: Account Holder: John Doe, Balance: $500.00

    # Deposit money
    account.deposit(200)  # Output: $200.00 deposited. New balance: $700.00

    # Withdraw money
    account.withdraw(100)  # Output: $100.00 withdrawn. New balance: $600.00

    # Access and modify private attributes using getters and setters
    print(f"Current balance: ${account.get_balance():.2f}")  # Output: Current balance: $600.00
    account.set_account_holder("Jane Doe")  # Output: Account holder name updated to Jane Doe
    print(account.get_account_holder())  # Output: Jane Doe

    # Attempt to withdraw an invalid amount
    account.withdraw(700)  # Output: Insufficient funds. Current balance: $600.00.
