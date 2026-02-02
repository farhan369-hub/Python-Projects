def tax_india(amount):
    return amount * 0.18
def tax_us(amount):
    return amount * 0.10
def tax_uk(amount):
    return amount * 0.15
def billing(amount, tax_func):
    tax = tax_func(amount)
    total = amount + tax
    return total

amt = float(input("Enter bill amount: "))
print("1.India")
print("2.US")
print("3.UK")
ch = int(input("Choose region: "))

if ch == 1:
    final = billing(amt, tax_india)
elif ch == 2:
    final = billing(amt, tax_us)
elif ch == 3:
    final = billing(amt, tax_uk)
else:
    final = amt

print("Final Amount:", final)