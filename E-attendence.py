names = []
attendance = []
def mark_attendance():
    name = input("Enter employee name: ")
    days = int(input("Enter days present: "))
    names.append(name)
    attendance.append(days)
    print("Attendance marked")
def calculate_working_days():
    name = input("Enter employee name: ")
    if name in names:
        i = names.index(name)
        print("Working Days:", attendance[i])
    else:
        print("Employee not found")
def generate_report():
    i = 0
    while i < len(names):
        print(names[i], "-", attendance[i])
        i = i + 1
while True:
    print("1.Mark Attendance")
    print("2.Calculate Working Days")
    print("3.Generate Report")
    print("4.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        mark_attendance()
    elif ch == 2:
        calculate_working_days()
    elif ch == 3:
        generate_report()
    elif ch == 4:
        break
    else:
        print("Invalid choice")