name=input("Enter your full name: ")
balance=0
print("Welcome Dear",name,"Please choose from the given options")

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        dep_amount = int(input("Enter the amount to be deposited: "))
        balance += dep_amount
        print("Amount",dep_amount,"Deposited Successfully!Dear",name)
    elif choice == 2:
        wd_amount = int(input("Enter the amount to withdraw: "))
        if wd_amount > balance:
            print("Insufficient balance! Withdrawal failed.")
        else:
            balance -= wd_amount
            print("Amount",wd_amount,"Withdrawn Successfully!Dear",name)

    elif choice == 3:
        print("Your current balance is:", balance)

    elif choice == 4:
        break   
    else:
        print("Invalid choice! Check properly.")

print("\nThank you for using the Simple Banking System,", name)
print("Have a nice day!")


