def register_user():
    name = input("Enter your name: ")
    username = input("Create a new username: ")
    password = input("Create a new password: ")
    print("Registration Successfull")
    return

def login_user():
    username = input("Enter username: ")
    password = input("Enter userpassword: ")
    print("Login Successfull")

def create_account():
    print("Create Bank Account")
    name = input("Enter your username: ")
    password = input("Enter your password: ")
    try:
        balance = float(input("Enter the initial balance: "))
    except ValueError:
        print("Invalid input. Enter the number.")
        return
    print("Account created successfully.")


def deposit(inital_balance,amount):
    if amount <= 0:
        print("Invalid deposit amount. Amount must be greater than 0")
        return inital_balance
    inital_balance = inital_balance + amount
    print(f"Successfully deposited {amount}.New balance {balance}")
    return balance

def withdraw(inital_balance, amount):
    if amount <= 0:
        print("Invalid withdrawal amount. Must be greater than 0.")
    elif amount > balance:
        print("Insufficient funds.")
    else:
        balance -= amount
        print(f"Successfully withdrawn {amount}. New balance: {balance}")
    return balance

def cheak_balance():
    print("Current")


def menu():
    while True:
            print("---Mini Banking System---")
            print("1.Customer Create")
            print("3.Deposit Money")
            print("4.Withdrawal Money")
            print("5.Cheak balance")
            print("6.Transaction History")
            print("7.Exit")

    while True:
        choice = input("Enter a choice 1-7")
        #Customer Create
        if choice == "1":
            create_account()

        elif choice == "2":
            try:
                customer_acc_number = int(input("Enter the account number:"))
                amount = float(input("Enter the deposit amount:"))
                inital_balance += amount
                print("Initial balance is {inital_balance}")
            except ValueError:
                print("Enter a valid amount.")

        elif choice == "3":
            try:
                customer_acc_number = int(input("Enter the account number:"))
                withdraw_amount = float(input("Enter the withdrawel amount:"))
                inital_balance -= withdraw_amount
                print("Initial balance is {inital_balance}")
            except ValueError:
                print("Enter a valid number.")
        #Cheak balance
        elif choice == "4":
            customer_acc_number = int(input("Enter the account number:"))
            print("Current Balance is {inital_balance}.")
        #Transaction History
        elif choice == "5":
            customer_acc_number = int(input("Enter the account number:"))
            transaction = []
def add_transaction(description,amount):
    new = datetime.new
    transaction.append({
        "datetime" : new,
        "description" : description,
        "amount" : amount
    })

        





#Exit
elif choice == "6":
    print("Thank you for using Mini Banking Sysytem.")
else:
    print("Choose the valid number 1-7")

menu():




