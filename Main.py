
import os
import uuid
from datetime import datetime


class BankAccount:
    def __init__(self, name, accountType, balance=0):
        self.name = name
        self.accountType = accountType
        self.balance = balance
        self.accountID = str(uuid.uuid4())[:8]

        # Create a unique statement file for this account
        safe_name = name.replace(" ", "_")
        self.statement_file = (
            f"{safe_name}_{accountType}_{self.accountID}.txt"
        )

        # Create the transaction history file
        with open(self.statement_file, "w") as file:
            file.write("Bank Account Transaction History\n")
            file.write(f"Account Holder: {self.name}\n")
            file.write(f"Account Type: {self.accountType}\n")
            file.write(f"Account ID: {self.accountID}\n")
            file.write(f"Opening Balance: ${self.balance:.2f}\n")
            file.write("-" * 35 + "\n")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return False

        self.balance += amount
        self._record_transaction("Deposit", amount)
        print(f"Successfully deposited ${amount:.2f}.")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return False

        if amount > self.balance:
            print("Insufficient funds. Withdrawal declined.")
            return False

        self.balance -= amount
        self._record_transaction("Withdrawal", amount)
        print(f"Successfully withdrew ${amount:.2f}.")
        return True

    def get_balance(self):
        return self.balance

    def get_account_id(self):
        return self.accountID

    def get_username(self):
        return self.name

    def get_account_type(self):
        return self.accountType

    def _record_transaction(self, transaction_type, amount):
        with open(self.statement_file, "a") as file:
            date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(
                f"{date_time} | {transaction_type}: "
                f"${amount:.2f} | Balance: ${self.balance:.2f}\n"
            )

    def get_transaction_history(self):
        try:
            with open(self.statement_file, "r") as file:
                return file.read()
        except FileNotFoundError:
            return "Transaction history file not found."


def main():
    # Create multiple bank accounts
    account1 = BankAccount("John Smith", "chequing", 500)
    account2 = BankAccount("Mary Jones", "savings", 1000)

    # Perform transactions on the first account
    print("--- John Smith's Account ---")
    account1.deposit(200)
    account1.withdraw(100)
    account1.withdraw(1000)

    print("Account ID:", account1.get_account_id())
    print("Account Holder:", account1.get_username())
    print("Account Type:", account1.get_account_type())
    print("Current Balance: $", format(account1.get_balance(), ".2f"))

    print("\n--- Transaction History ---")
    print(account1.get_transaction_history())

    # Perform transactions on the second account
    print("--- Mary Jones's Account ---")
    account2.deposit(300)
    account2.withdraw(150)

    print("Account ID:", account2.get_account_id())
    print("Current Balance: $", format(account2.get_balance(), ".2f"))

    print("\n--- Transaction History ---")
    print(account2.get_transaction_history())

    return


if __name__ == "__main__":
    main()
