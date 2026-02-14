def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")
    if amount > balance:
        raise ValueError("Insufficient balance.")
    
    return balance - amount


def atm():
    balance = 10000
    print("💳 Welcome to ATM")
    print(f"Your balance: ₹{balance}")

    while True:
        try:
            user_input = input("\nEnter amount to withdraw (or type 'exit'): ")

            if user_input.lower() == 'exit':
                print("👋 Thank you for using ATM")
                break

            amount = float(user_input)

            # ✅ IMPORTANT LINE (this was your bug)
            balance = withdraw(balance, amount)

            print("✅ Withdrawal successful!")
            print(f"💰 Remaining balance: ₹{balance}")

        except ValueError as e:
            print(f"❌ Error: {e}")

        except:
            print("❌ Invalid input! Please enter a number.")


atm()