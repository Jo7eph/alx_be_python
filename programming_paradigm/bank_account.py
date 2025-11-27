class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional initial balance (default 0)."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Deduct the amount from the account balance if sufficient funds exist.
        Returns True if successful, False otherwise.
        """
        if amount > self.account_balance:
            return False
        elif amount < 0:
            print("Withdrawal amount must be positive.")
            return False
        else:
            self.account_balance -= amount
            return True

    def display_balance(self):
        """Print the current account balance with 2 decimal places."""
        print(f"Current Balance: ${self.account_balance:.2f}")
