def add_employee():
    name = input("Enter employee name: ")
    basic = float(input("Enter basic salary: "))
    return name, basic
def handle_bonus_deduction(basic):
    bonus = float(input("Enter bonus: "))
    deduction = float(input("Enter deduction: "))
    salary = basic + bonus - deduction
    return salary
def generate_report(name, salary):
    print("Employee Name:", name)
    print("Final Salary:", salary)

name = ""
basic = 0
salary = 0
while True:
    print("1.Add Employee")
    print("2.Calculate Salary")
    print("3.Generate Report")
    print("4.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        name, basic = add_employee()
    elif ch == 2:
        salary = handle_bonus_deduction(basic)
    elif ch == 3:
        generate_report(name, salary)
    elif ch == 4:
        break
    else:
        print("Invalid choice")