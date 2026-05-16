import json
import os
import datetime
import random

DATA_FILE = "bank_data.json"

class Transaction:
    def __init__(self, t_type, amount):
        self.id = random.randint(100000, 999999)
        self.type = t_type
        self.amount = amount
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "amount": self.amount,
            "timestamp": self.timestamp
        }

class BankAccount:
    def __init__(self, name, balance=0.0, account_number=None, transactions=None):
        self.name = name
        # Encapsulation: _balance is protected
        self._balance = float(balance)
        self.account_number = account_number if account_number else random.randint(1000, 9999)
        # Lists for history
        self.transaction_history = []
        # Sets to detect duplicate transactions (simulated logic)
        self.transaction_ids = set()
        
        if transactions:
            for t_data in transactions:
                self.transaction_history.append(t_data)
                self.transaction_ids.add(t_data['id'])

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount.")
            return False
        
        t = Transaction("Deposit", amount)
        if t.id in self.transaction_ids:
            print("Duplicate transaction detected! Cancelling.")
            return False
            
        self._balance += amount
        self._add_transaction(t)
        print(f"Deposited ${amount}. New Balance: ${self._balance}")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
            return False
        if amount > self._balance:
            print("Insufficient funds!")
            return False
            
        t = Transaction("Withdrawal", amount)
        self._balance -= amount
        self._add_transaction(t)
        print(f"Withdrew ${amount}. New Balance: ${self._balance}")
        return True

    def _add_transaction(self, transaction):
        self.transaction_ids.add(transaction.id)
        self.transaction_history.append(transaction.to_dict())

    def get_balance(self):
        return self._balance

    def show_history(self):
        print(f"\nTransaction History for {self.name} ({self.account_number}):")
        for t in self.transaction_history:
            print(f"[{t['timestamp']}] {t['type']}: ${t['amount']} (ID: {t['id']})")

    def to_dict(self):
        return {
            "name": self.name,
            "balance": self._balance,
            "account_number": self.account_number,
            "transactions": self.transaction_history,
            "type": "Standard"
        }

class SavingsAccount(BankAccount):
    def __init__(self, name, balance=0.0, account_number=None, transactions=None, interest_rate=0.02):
        super().__init__(name, balance, account_number, transactions)
        self.interest_rate = interest_rate
        # Apply starting interest for newly created savings accounts only.
        if transactions is None:
            self.apply_interest()

    def apply_interest(self):
        interest = self._balance * self.interest_rate
        if interest <= 0:
            return False
        self.deposit(interest)
        print(f"Interest of ${interest} applied.")
        return True

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Savings"
        data["interest_rate"] = self.interest_rate
        return data

class BankSystem:
    def __init__(self):
        self.accounts = {}
        self.load_data()

    def create_account(self):
        name = input("Enter customer name: ")
        acc_type = input("Account type (standard/savings): ").lower()
        
        if acc_type == "savings":
            acc = SavingsAccount(name)
        else:
            acc = BankAccount(name)
            
        self.accounts[acc.account_number] = acc
        print(f"Account created successfully! Account Number: {acc.account_number}")

    def find_account(self):
        try:
            acc_num = int(input("Enter account number: "))
            if acc_num in self.accounts:
                return self.accounts[acc_num]
            else:
                print("Account not found.")
                return None
        except ValueError:
            print("Invalid number format.")
            return None

    def save_data(self):
        data = {acc_id: acc.to_dict() for acc_id, acc in self.accounts.items()}
        try:
            with open(DATA_FILE, "w") as f:
                json.dump(data, f, indent=4)
            print("Data saved successfully.")
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_data(self):
        if not os.path.exists(DATA_FILE):
            return
        
        try:
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                
            for acc_id, acc_data in data.items():
                if acc_data.get("type") == "Savings":
                    acc = SavingsAccount(
                        acc_data["name"], 
                        acc_data["balance"], 
                        acc_data["account_number"], 
                        acc_data["transactions"]
                    )
                else:
                    acc = BankAccount(
                        acc_data["name"], 
                        acc_data["balance"], 
                        acc_data["account_number"], 
                        acc_data["transactions"]
                    )
                self.accounts[int(acc_id)] = acc
        except Exception as e:
            print(f"Error loading data: {e}")

def main():
    bank = BankSystem()
    
    while True:
        print("\n--- Banking System ---")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Show All Accounts (Debug)")
        print("7. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            bank.create_account()
        elif choice == '2':
            acc = bank.find_account()
            if acc:
                amount = float(input("Enter amount to deposit: "))
                acc.deposit(amount)
        elif choice == '3':
            acc = bank.find_account()
            if acc:
                amount = float(input("Enter amount to withdraw: "))
                acc.withdraw(amount)
        elif choice == '4':
            acc = bank.find_account()
            if acc:
                print(f"Current Balance: ${acc.get_balance()}")
        elif choice == '5':
            acc = bank.find_account()
            if acc:
                acc.show_history()
        elif choice == '6':
            for acc in bank.accounts.values():
                print(f"{acc.account_number}: {acc.name} - ${acc.get_balance()}")
        elif choice == '7':
            bank.save_data()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
