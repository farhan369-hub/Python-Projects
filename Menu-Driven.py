def calculator():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    ch = int(input("Enter choice: "))
    if ch == 1:
        print("Result:", a + b)
    elif ch == 2:
        print("Result:", a - b)
    elif ch == 3:
        print("Result:", a * b)
    elif ch == 4:
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero")
def string_operations():
    s = input("Enter a string: ")
    print("1.Upper")
    print("2.Lower")
    print("3.Length")
    ch = int(input("Enter choice: "))
    if ch == 1:
        print(s.upper())
    elif ch == 2:
        print(s.lower())
    elif ch == 3:
        print(len(s))
def number_utilities():
    n = int(input("Enter a number: "))
    print("1.Even or Odd")
    print("2.Square")
    print("3.Cube")
    ch = int(input("Enter choice: "))
    if ch == 1:
        if n % 2 == 0:
            print("Even")
        else:
            print("Odd")
    elif ch == 2:
        print(n * n)
    elif ch == 3:
        print(n * n * n)
while True:
    print("1.Calculator")
    print("2.String Operations")
    print("3.Number Utilities")
    print("4.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        calculator()
    elif ch == 2:
        string_operations()
    elif ch == 3:
        number_utilities()
    elif ch == 4:
        break
    else:
        print("Invalid choice")