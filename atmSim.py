import random, os, sys
customers_info = []

def clear(): os.system('cls' if os.name == 'nt' else 'clear')

def open_account(customers_info):
    name = input("Your Name? ")
    while True:
        if len(pin := input("A Four-Digit Pincode: ")) == 4 and pin.isdigit(): pin = int(pin); break
        else: print("Only Four Digits Allowed!")
    while True:
        identity = random.randint(1000, 9999)
        if all((identity := random.randint(1000,9999)) != customer["id"] for customer in customers_info): break
    customers_info.append({"name": name, "id": identity, "pin": pin, "amount": 0}); print(f"Account created successfully! ID: {identity}")

def close_account(customers_info):
    if (customer := check_id(int(input("ID: ")))):
        if input("Are you sure you want to delete it? (Y/n) ").lower() == "y": customers_info.remove(customer); print("Account Deleted.")
    else: print("Account not found or incorrect PIN.")

def check_id(identity):
    for customer in customers_info:
        if identity == customer['id']: 
            if (pin := int(input(f"Enter your pincode for '{customer['name']}': "))) == customer["pin"]: return customer
            else: print("Incorrect PIN."); continue
    print("ID Not Found."); return

def exchange(customer, amount, deposit):
    if amount <= 0: print("Amount must be positive."); return
    if not deposit and amount > customer["amount"]: print("Insufficient balance."); return
    action = 'deposit' if deposit else 'withdraw'
    if input(f"Confirm to {action} ₹{amount}? (Y/n): ").lower() == "y": customer["amount"] += amount if deposit else -amount; print(f"Transaction successful! New Balance: ₹{customer['amount']}")
    else: print("Transaction canceled.")

def reveal(customer): print(f"\nName: {customer['name']}\nID: {customer['id']}\nBalance: ₹{customer['amount']}\n") 

while True:
    if not (cmd := input("~$ ").split()): continue  
    if (action := cmd[0].lower()) in ["atm"]:
        if len(cmd) < 2: print("Please provide an ID."); continue
        if (customer := check_id(int(cmd[1]))):
            while True:
                if not (sub_cmd := input("> ").split()): continue
                if (sub_action := sub_cmd[0].lower()) == "exit": break
                elif sub_action in ["withdraw", "wtdw"] and len(sub_cmd) > 1: exchange(customer, int(sub_cmd[1]), False)
                elif sub_action in ["deposit", "dpst"] and len(sub_cmd) > 1: exchange(customer, int(sub_cmd[1]), True)
                elif sub_action in ["reveal", "rvel", "show"]: reveal(customer)
                elif sub_action in ["cls", "clear", "clean"]: clear()
                else: print(f"'{sub_action}' is not a recognized command.")
                    
    elif action in ["new", "create", "open"]: open_account(customers_info)
    elif action in ["close", "del", "rem"]: close_account(customers_info)
    elif action in ["cls", "clear", "clean"]: clear()
    elif action in ["exit"]:
        if random.choice([True, False]): print("breaks applied"); break
        else:print("walked out the exit door!"); sys.exit()
    else: print("Error! Command not recognized.")
