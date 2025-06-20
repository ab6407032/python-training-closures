"""
Use Case: ✅ Data Hiding using Closures
---------------------------------------
Closures allow functions to store state in a private scope.
This is useful when you want to retain information across function calls
without using global variables or object-oriented programming.

Problem Statement:
You are tasked with designing a simple bank account system that can:

Accept deposits
Process withdrawals
Return the current balance

However, you must ensure the account balance remains private and cannot be accessed or modified directly from outside the function.

Requirements:
Use closures to encapsulate and protect the account balance.
Allow only specific actions (deposit, withdraw, balance) to interact with the account.
Use the nonlocal keyword to modify the balance within the inner function.
Prevent direct access to the balance variable from outside.
"""

def create_account(initial_balance):
    balance = initial_balance

    def account(action, amount=0):
        nonlocal balance
        if action == "deposit":
            balance += amount
        elif action == "withdraw":
            if amount <= balance:
                balance -= amount
            else:
                return "Insufficient funds"
        elif action == "balance":
            return balance
        return "Transaction complete"

    return account

# Example usage
my_account = create_account(1000)
print(my_account("balance"))     # ➜ 1000
print(my_account("deposit", 500))# ➜ Transaction complete
print(my_account("balance"))     # ➜ 1500
print(my_account("withdraw", 2000)) # ➜ Insufficient funds
