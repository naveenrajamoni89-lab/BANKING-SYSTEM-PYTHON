# Simple Python Banking System

A terminal-based banking application built with Python that demonstrates core **Object-Oriented Programming (OOP)** principles. This system allows users to create accounts, manage balances, and track transaction history with data persistence using JSON.

## 🚀 Features

* **Account Management**: Create Standard or Savings accounts.
* **Transactions**: Perform deposits and withdrawals with real-time balance updates.
* **Savings Logic**: Automatic interest calculation for Savings accounts.
* **Transaction History**: Detailed logs for every action, including timestamps and unique transaction IDs.
* **Data Persistence**: All account data is saved to a `bank_data.json` file, allowing you to resume your session later.
* **Duplicate Detection**: Built-in logic to prevent duplicate transaction IDs using Python Sets.

## 🛠️ Concepts Demonstrated

* **Encapsulation**: Using protected members (e.g., `_balance`) to control how data is accessed and modified.
* **Inheritance**: The `SavingsAccount` class inherits from `BankAccount` while adding specific interest-bearing functionality.
* **Method Overriding**: Customizing the `to_dict` method in the subclass to handle specific data fields.
* **Composition**: The `BankSystem` class manages a collection of `BankAccount` objects.
* **File I/O**: Reading from and writing to JSON files for permanent storage.

## 📋 Prerequisites

* Python 3.x installed on your machine.

## 🔧 Installation & Usage

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/BANKING-SYSTEM-PYTHON.git
cd banking-system

```


2. **Run the application**:
```bash
python bank_system.py

```


3. **Navigate the Menu**: Use the numeric inputs (1-7) to interact with the system. Ensure you select **Option 7 (Exit)** to save your data before closing.

## 📂 Project Structure

* `bank_system.py`: The main logic containing `Transaction`, `BankAccount`, `SavingsAccount`, and `BankSystem` classes.
* `bank_data.json`: (Generated automatically) Stores all account and transaction information in a structured format.

## 📝 Example JSON Structure

The system saves data in the following format:

```json
{
    "1234": {
        "name": "John Doe",
        "balance": 1050.0,
        "account_number": 1234,
        "transactions": [
            {
                "id": 543210,
                "type": "Deposit",
                "amount": 1000.0,
                "timestamp": "2024-05-20 10:00:00"
            }
        ],
        "type": "Standard"
    }
}

```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page if you want to contribute.

---

### 💡 Future Improvements

* [ ] Implement password protection/PINs for accounts.
* [ ] Add a GUI (Graphical User Interface) using Tkinter or PyQt.
* [ ] Implement transfer functionality between accounts.
