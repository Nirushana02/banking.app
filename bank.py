import os
def get_customer_info():
        print("----Enter Customer Details----")
        name = input("Enter your name: ")
        address = input("Enter your address: ")       
        username = input("Enter username: ")
        password = input("Enter password: ")
            
        return [name, address, username, password]
       
def save_customer(customer):
    with open("customer.txt", "a") as file:
        file.write(f"{create_customer_next_id()},{customer[0]},{customer[1]}\n")
    print("Customer data saved.")

def save_user(customer):
    with open("user.txt", "a") as file:
        file.write(f"{customer[2]},{customer[3]}\n")
    print("User credentials saved.")

    #Generate the next customer ID based on the entries in 'customer.txt'.
    #If the file does not exist or is empty, start with 'C1'.
def create_customer_next_id():    
    try:
        with open("customer.txt", "r") as customer_file:
            lines = customer_file.readlines()
            if not lines:  # If the file is empty
                return "C1"
            last_id_str = lines[-1].split(",")[0]  # Assuming ID is in the first column
            last_id_num = int(last_id_str[1:])  # Extract the numeric part
            return  f"C{last_id_num + 1}"  # Increment to get the next ID
    except FileNotFoundError:
        return "C1"

#User login check
def user_login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    try:
        with open("user.txt", "r") as file:
            for line in file:
                user, pwd = line.strip().split(",")
                if user == username and pwd == password:
                    print("Login successful.")
                    return True
    except FileNotFoundError:
        pass
    print("Invalid username or password.")
    return False

#Create a bank account
def create_account():
    print("Create Bank Account")
    name = input("Enter your username: ")
    while True:
        password = input("Enter your password: ")
        if len(password) >= 6:
            print("Password is ok.")
        else:
            print("Password must be at least 6 characters.")
        return
    acc_number = input("Enter your account number: ")
    try:
        balance = float(input("Enter the initial balance: "))
    except ValueError:
        print("Invalid input. Enter the number.")
        return
    with open("accounts.txt", "a") as file:
        file.write(f"{name},{password},{acc_number},{balance}\n")
        print("Account created successfully and saved to file.")
   
#Deposit
def deposit(account_number, amount):
    if amount <= 0:
        print("Invalid deposit amount. Amount must be greater than 0.")
        return
    try:
        accounts = []
        account_found = False

        with open("accounts.txt", "r") as file:
            for line in file:
                name, password, acc_number, balance = line.strip().split(",")
                if acc_number == account_number:
                    account_found = True
                    new_balance = float(balance) + amount
                    print(f"Successfully deposited {amount}. New balance: {new_balance}")

                    #Create updated line for the account
                    line = f"{name},{password},{acc_number},{new_balance}\n"
                    accounts.append(line) 
                    #Record the transaction
                    record_transaction(account_number, "Deposit", amount, new_balance)
                else: 
                    accounts.append(line)  #keep the other accounts unchanged   

        if not account_found:
            print("Account not found.")

        with open("accounts.txt", "w") as file:
            file.writelines(accounts)
    except IOError:
        print("An error occurred while reading or writing to the file.")

#Withdraw
def withdraw(account_number, amount):
    if amount <= 0:
        print("Invalid withdrawal amount. Must be greater than 0.")
        return
    try:
        accounts = []
        account_found = False

        # Read accounts from the file
        with open("accounts.txt", "r") as file:
            for line in file:
                name, password, acc_number, balance = line.strip().split(",")
                if acc_number == account_number:
                    account_found = True
                    balance = float(balance)
                    if amount > balance:
                        print("Insufficient funds.")
                        return
                    else:
                        balance -= amount
                        print(f"Successfully withdrawn {amount}. New balance: {balance}")
                        line = f"{name},{password},{acc_number},{balance}\n"
                        record_transaction(account_number, "Withdraw", amount, balance)
                        accounts.append(line)
                else:
                    accounts.append(line)
    except FileNotFoundError:
        print("Accounts file not found.")
        return
    if not account_found:
        print("Account not found.")
        return

    # Write updated accounts back to the file
    try:
        with open("accounts.txt", "w") as file:
            file.writelines(accounts)
    except IOError:
        print("An error occurred while reading or writing to the file.")

def check_balance():
    customer_acc_number = input("Enter the account number: ")
    try:
        with open("accounts.txt", "r") as file:
            for line in file:
                name, password, acc_number, balance = line.strip().split(",")
                if acc_number == customer_acc_number:
                    print(f"Account Holder: {name}")
                    print(f"Account Number: {acc_number}")
                    print(f"Current Balance: {balance}")
                    return
        print("Account not found.")
    except FileNotFoundError:
        print("Accounts file not found.")
    except IOError:
        print("An error occurred while reading the file.")


#Transaction Histroy
def record_transaction(account_number, transaction_type, amount, new_balance):
    
    #Records a transaction into the 'transactions.txt' file.
    
    try:
        with open("transactions.txt", "a") as file:
            file.write(f"{account_number},{transaction_type},{amount},{new_balance}\n")
    except IOError:
        print("Error occurred while writing the transaction history.")

def display_transaction_history(account_number):
    
    #Displays the transaction history for a specific account.

    try:
        with open("transactions.txt", "r") as file:
            print("\n--- Transaction History ---")
            print("{:<12} {:<10} {:<12}".format("Type", "Amount", "Balance"))
            print("-" * 30)
            found = False
            for line in file:
                data = line.strip().split(",")
                if data[0] == account_number:
                    print("{:<12} {:<10} {:<12}".format(data[1], data[2], data[3]))
                    found = True
            if not found:
                print("No transactions found for this account.")
    except FileNotFoundError:
        print("Transaction file not found.")
    except IOError:
        print("Error occurred while reading the transaction history.")

#Transaction Between 2 accounts
def transfer(sender_acc, receiver_acc, amount):
    if amount <= 0:
        print("Transfer amount must be greater than 0.")
        return

    try:
        accounts = []
        sender_found = False
        receiver_found = False
        sender_balance = 0.0
        receiver_balance = 0.0

        # Load and process all accounts
        with open("accounts.txt", "r") as file:
            for line in file:
                name, password, acc_number, balance = line.strip().split(",")
                balance = float(balance)

                if acc_number == sender_acc:
                    sender_found = True
                    if balance < amount:
                        print("Insufficient funds in sender's account.")
                        return
                    sender_balance = balance - amount
                    updated_line = f"{name},{password},{acc_number},{sender_balance}\n"
                    accounts.append(updated_line)
                elif acc_number == receiver_acc:
                    receiver_found = True
                    receiver_balance = balance + amount
                    updated_line = f"{name},{password},{acc_number},{receiver_balance}\n"
                    accounts.append(updated_line)
                else:
                    accounts.append(line)

        if not sender_found:
            print("Sender account not found.")
            return
        if not receiver_found:
            print("Receiver account not found.")
            return

        # Write updated accounts back to file
        with open("accounts.txt", "w") as file:
            file.writelines(accounts)

        # Record both transactions
        record_transaction(sender_acc, "Transfer Out", amount, sender_balance)
        record_transaction(receiver_acc, "Transfer In", amount, receiver_balance)

        print(f"Successfully transferred {amount} from {sender_acc} to {receiver_acc}.")

    except FileNotFoundError:
        print("Accounts file not found.")
    except IOError:
        print("Error occurred while accessing the file.")

def change_password():
    try:
        updated_user = []
        with open ("user.txt", "r") as file:
            for line in file:
                username,password = line.strip().split(",")
                if username == username:
                    current_password = input("Enter your current password: ")
                    if current_password != password:
                        print("Password not match.")
                        return
                    else:
                        new_password = input("Enter your new_password (must be 6 characters): ")
                        confirm_password = input("Enter your confirm_password: ")
                        if new_password == confirm_password:
                            print("Password changed successfully.")
                            updated_user = f"{username},{new_password}\n"
                            user.append(updated_user)
        with open ("user.txt", "w") as file:
            file.readlines(user)        
    except IOError:                
        print("User not found.") 

def display_customer_list():
    try:
        with open ("customer.txt", "r") as file:
            customers = file.readlines()
            for line in customers:
                cus_id,name = line.strip().split(",")
                print("----Disply Customer List----")
                customer_data = customer.line.strip().split(",")
                if customer_data == (f"customer_data[0],customer_data[1]"):
                    print("{customer_data[0]}:{customer_data[1]}")
    except FileNotFoundError:
        print("File not found.")
            
# Main user menu
def user_registration():
    while True:
        print("\n---- Welcome to Mini Banking System ----")
        print("1. Register User")
        print("2. Login")
        print("3. Display Customer List")
        print("4. Change password")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            customer = get_customer_info()
            if customer:
                save_customer(customer)
                save_user(customer)

        elif choice == "2":
            if user_login():
                while True:
                    print("\n--- Main Menu ---")
                    print("1. Create Bank Account")
                    print("2. Deposit Money")
                    print("3. Withdraw Money")
                    print("4. Check Balance")
                    print("5. Transaction History")
                    print("6. Transaction between two accounts")
                    print("7. Logout")
                    menu_choice = input("Enter your choice (1-7): ")

                    if menu_choice == "1":
                        create_account()
                    elif menu_choice == "2":
                        acc = input("Enter account number: ")
                        try:
                            amt = float(input("Enter deposit amount: "))
                            deposit(acc, amt)
                        except ValueError:
                            print("Invalid amount.")
                    elif menu_choice == "3":
                        acc = input("Enter account number: ")
                        try:
                            amt = float(input("Enter withdrawal amount: "))
                            withdraw(acc, amt)
                        except ValueError:
                            print("Invalid amount.")
                    elif menu_choice == "4":
                        check_balance()
                    elif menu_choice == "5":
                        acc = input("Enter account number: ")
                        display_transaction_history(acc)
                    elif menu_choice == "6":
                        sender_acc = input("Enter the account number of sender: ")
                        receiver_acc = input("Enter the account number of receiver: ")
                        try:
                            amount = float(input("Enter the transfer amount: "))
                            transfer(sender_acc, receiver_acc, amount)
                        except ValueError:
                            print("Invalid amount.")
                    elif menu_choice == "7":
                        print("Logged out.")
                        break
                    else:
                        print("Invalid option.")

        elif choice == "3":
            display_customer_list()

        elif choice == "4":
            change_password()
        
        elif choice == "5":
            print("Thank you for using Mini Banking System. Have a Nice Day.")
            break
        else:
            print("Invalid choice. Try again.")

# Start the application
user_registration()