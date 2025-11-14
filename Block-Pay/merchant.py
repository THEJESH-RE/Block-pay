def login():
    username = input("Merchant Username: ")
    password = input("Password: ")

def view_profile():
    print("Merchant Profile Details...")

def change_password():
    print("Change Password Process...")

def view_transactions():
    print("Transactions List...")

def service_transaction():
    print("Process Service Payment...")

def renew_agreement():
    print("Renew Agreement Approval...")

def main():
    login()
    while True:
        print("\n1. Profile\n2. Change Password\n3. View Transactions\n4. Service Payment\n5. Renew Agreement\n6. Exit")
        choice = input("Choose: ")
        if choice == "1":
            view_profile()
        elif choice == "2":
            change_password()
        elif choice == "3":
            view_transactions()
        elif choice == "4":
            service_transaction()
        elif choice == "5":
            renew_agreement()
        elif choice == "6":
            break

if __name__ == "__main__":
    main()
