import json

def login():
    username = input("Admin Username: ")
    password = input("Password: ")
    # Validate from database (db/db_setup.py)

def list_merchants():
    # Fetch from database
    print("All merchants and service periods...")

def notify_merchant():
    merchant = input("Merchant Name: ")
    message = input("Notification Message: ")
    # Send message to merchant (could save in DB + send socket)

def renew_agreement():
    merchant = input("Merchant Name: ")
    new_period = input("New Service Period: ")
    # Update in DB

def fee_transactions():
    # Fetch and display transaction fee records
    pass

def main():
    login()
    while True:
        print("\n1. List Merchants\n2. Notify Merchant\n3. Renew Agreement\n4. Fee Transactions\n5. Exit")
        choice = input("Choose: ")
        if choice == "1":
            list_merchants()
        elif choice == "2":
            notify_merchant()
        elif choice == "3":
            renew_agreement()
        elif choice == "4":
            fee_transactions()
        elif choice == "5":
            break

if __name__ == "__main__":
    main()
