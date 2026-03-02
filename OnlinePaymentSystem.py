# Base class
class Payment:
    def pay(self, amount):
        print("Processing payment of ₹", amount)


# Subclass 1
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Payment of ₹{amount} made using Credit Card.")
        print("Verifying card details...")
        print("Transaction Successful!\n")


# Subclass 2
class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Payment of ₹{amount} made using UPI.")
        print("Sending OTP to registered mobile number...")
        print("Transaction Successful!\n")


# Subclass 3
class WalletPayment(Payment):
    def pay(self, amount):
        print(f"Payment of ₹{amount} made using Wallet.")
        print("Checking wallet balance...")
        print("Transaction Successful!\n")


# Processing payments using different objects
payments = [
    CreditCardPayment(),
    UPIPayment(),
    WalletPayment()
]

amount = 1000

for payment in payments:
    payment.pay(amount)