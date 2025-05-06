
print("====User Registration====")
def get_customer_info():
    
        name = input("Enter your name: ")
        address = input("Enter your address: ")       
        username = input("Enter username: ")
        password = input("Enter password: ")
        print("Registeration successfully")
        
        return [name, address, username, password]
       
def create_customer():
    customer = get_customer_info()
    if customer:  # Only write to file if customer data is valid
        with open("customer.txt", "a") as file:
            file.write(f"{customer[0]},{customer[1]}\n")
        print("Customer data saved.")

def create_user():
    customer = get_customer_info()
    if customer:  # Only write to file if customer data is valid
        with open("user.txt", "a") as file:
            file.write(f"{customer[2]},{customer[3]}\n")
        print("User data saved.")

def create_customer_next_id():
    
    #Generate the next customer ID based on the entries in 'customer.txt'.
    #If the file does not exist or is empty, start with 'C1'.
    
    try:
        with open("customer.txt", "r") as customer_file:
            lines = customer_file.readlines()
            if not lines:  # If the file is empty
                next_id = "C1"
            else:
                # Extract the last customer ID, e.g., 'C1', from the last line
                last_id_str = lines[-1].strip().split(",")[0]  # Assuming ID is in the first column
                last_id_num = int(last_id_str[1:])  # Extract the numeric part
                next_id = f"C{last_id_num + 1}"  # Increment to get the next ID
            print(f"Next customer ID: {next_id}")
            return next_id
    except FileNotFoundError:
        # If the file does not exist, start with ID 'C1'
        print("Customer file not found. Starting with ID C1.")
        return "C1"

create_user() 
create_customer_next_id()    

def create_account():
    print("Create Bank Account")
    name = input("Enter your username: ")
    password = input("Enter your password: ")
    acc_number = input("Enter your account number: ")
    try:
        balance = float(input("Enter the initial balance: "))
    except ValueError:
        print("Invalid input. Enter the number.")
        return
    account_data = f"{name},{password},{acc_number},{balance}\n"
    try:
        with open("accounts.txt", "a") as file:
            file.write(account_data)
        print("Account created successfully and saved to file.")
    except IOError:
        print("An error occurred while writing to the file.")

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
                    line = f"{name},{password},{acc_number},{new_balance}\n"
                    record_transaction(account_number, "Deposit", amount, new_balance)
                accounts.append(line)

        if not account_found:
            print("Account not found.")
            return

        with open("accounts.txt", "w") as file:
            file.writelines(accounts)

    except FileNotFoundError:
        print("Accounts file not found.")
    except ValueError:
        print("Error processing account data.")
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

        if not account_found:
            print("Account not found.")
            return

        # Write updated accounts back to the file
        with open("accounts.txt", "w") as file:
            file.writelines(accounts)

    except FileNotFoundError:
        print("Accounts file not found.")
    except ValueError:
        print("Error processing account data.")
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

def menu():
    while True:
            print("---Mini Banking System---")
            print("1.Customer Create")
            print("2.Deposit Money")
            print("3.Withdrawal Money")
            print("4.Cheak balance")
            print("5.Transaction History")
            print("6.Exit")

            choice = input("Enter a choice 1-6: ")
            #Customer Create
            if choice == "1":
                create_account()

            elif choice == '2':
                account_number = input("Enter your account number: ")
                try:
                    amount = float(input("Enter the amount to deposit: "))
                    deposit(account_number, amount)
                except ValueError:
                    print("Invalid amount. Please enter a number.")
        
            elif choice == '3':
                account_number = input("Enter your account number: ")
                try:
                    amount = float(input("Enter the amount to withdraw: "))
                    withdraw(account_number, amount)
                except ValueError:
                    print("Invalid amount. Please enter a number.")
        
            elif choice == '4':
                check_balance()
            
            elif choice == "5":
                account_number = input("Enter the account number: ")
                display_transaction_history(account_number)

            elif choice == "6":
                print("Thank you for using Mini Banking System. Have a nice day.")

                break # Exit the loop to stop the program
            else:
                print("Invalid input. please enter the number 1-6")

create_customer()             
menu()

        






