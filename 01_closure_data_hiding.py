"""
Use Case: ✅ Data Hiding using Closures
---------------------------------------
Closures allow functions to store state in a private scope.
This is useful when you want to retain information across function calls
without using global variables or object-oriented programming.

🔒 Real-life Analogy:
A vending machine remembers how much money you've inserted, 
but this state isn't visible or modifiable from outside.

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
