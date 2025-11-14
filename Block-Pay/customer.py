def register():
    name = input("Full Name: ")
    email = input("Email: ")
    password = input("Password: ")

def login():
    email = input("Email: ")
    password = input("Password: ")

def new_transaction():
    merchant = input("Merchant Name: ")
    amount = float(input("Amount: "))
    description = input("Description: ")

def view_transactions():
    print("List of all your transactions...")

def give_feedback():
    merchant = input("Merchant Name: ")
    feedback = input("Your Feedback: ")

def main():
    print("1. Register\n2. Login")
    choice = input("Choose: ")
    if choice == "1":
        register()
    else:
        login()

    while True:
        print("\n1. New Transaction\n2. View Transactions\n3. Feedback\n4. Exit")
        choice = input("Choose: ")
        if choice == "1":
            new_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            give_feedback()
        elif choice == "4":
            break

if __name__ == "__main__":
    main()
