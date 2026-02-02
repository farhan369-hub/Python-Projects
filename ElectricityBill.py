def input_units():
    name = input("Enter customer name: ")
    units = int(input("Enter units consumed: "))
    return name, units
def calculate_bill(units):
    bill = 0
    if units <= 100:
        bill = units * 3
    elif units <= 200:
        bill = 100 * 3 + (units - 100) * 5
    else:
        bill = 100 * 3 + 100 * 5 + (units - 200) * 7
    return bill
def generate_summary(name, units, bill):
    print("Name:", name)
    print("Units:", units)
    print("Bill Amount:", bill)

name, units = input_units()
bill = calculate_bill(units)
generate_summary(name, units, bill)