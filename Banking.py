balance = 0
def deposit():
    global balance
    amt = float(input("Enter amount to deposit: "))
    balance = balance + amt
    print("Deposited:", amt)
def withdraw():
    global balance
    amt = float(input("Enter amount to withdraw: "))
    if amt <= balance:
        balance = balance - amt
        print("Withdrawn:", amt)
    else:
        print("Insufficient balance")
def check_balance():
    print("Current Balance:", balance)
while True:
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Check Balance")
    print("4.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        deposit()
    elif choice == 2:
        withdraw()
    elif choice == 3:
        check_balance()
    elif choice == 4:
        break
    else:
        print("Invalid choice")