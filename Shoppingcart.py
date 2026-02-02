cart = []
prices = []
def add_item():
    item = input("Enter item name: ")
    price = float(input("Enter price: "))
    cart.append(item)
    prices.append(price)
    print("Item added")
def remove_item():
    item = input("Enter item name to remove: ")
    if item in cart:
        i = cart.index(item)
        cart.pop(i)
        prices.pop(i)
        print("Item removed")
    else:
        print("Item not found")
def calculate_total():
    total = 0
    for p in prices:
        total = total + p
    return total
def apply_discount(total):
    d = float(input("Enter discount percentage: "))
    final = total - (total * d / 100)
    return final

while True:
    print("1.Add Item")
    print("2.Remove Item")
    print("3.Total Bill")
    print("4.Apply Discount")
    print("5.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        add_item()
    elif ch == 2:
        remove_item()
    elif ch == 3:
        t = calculate_total()
        print("Total:", t)
    elif ch == 4:
        t = calculate_total()
        f = apply_discount(t)
        print("Final Bill:", f)
    elif ch == 5:
        break
    else:
        print("Invalid choice")