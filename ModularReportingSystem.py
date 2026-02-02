def sales_report():
    total = 0
    n = int(input("Enter number of sales: "))
    for i in range(n):
        s = float(input("Enter sale amount: "))
        total = total + s
    print("Total Sales:", total)
def employee_report():
    n = int(input("Enter number of employees: "))
    print("Total Employees:", n)
def finance_report():
    income = float(input("Enter income: "))
    expense = float(input("Enter expense: "))
    profit = income - expense
    print("Profit:", profit)
def central_report(choice):
    if choice == 1:
        sales_report()
    elif choice == 2:
        employee_report()
    elif choice == 3:
        finance_report()
    else:
        print("Invalid choice")
while True:
    print("1.Sales Report")
    print("2.Employee Report")
    print("3.Finance Report")
    print("4.Exit")
    ch = int(input("Enter choice: "))

    if ch == 4:
        break
    central_report(ch)