def input_marks():
    name = input("Enter student name: ")
    n = int(input("Enter number of subjects: "))
    total = 0
    for i in range(n):
        m = float(input("Enter mark: "))
        total = total + m
    return name, total, n
def calculate_average(total, n):
    if n == 0:
        return 0
    avg = total / n
    return avg

def assign_grade(avg):
    if avg >= 90:
        return "S"
    elif avg >= 85:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 75:
        return "B+"
    elif avg >= 70:
        return "B"
    elif avg >= 65:
        return "C+"
    elif avg >= 60:
        return "C"
    elif avg >= 55:
        return "D"
    elif avg >= 50:
        return "P"
    else:
        return "F"
def display_result(name, total, avg, grade):
    print("Name:", name)
    print("Total:", total)
    print("Average:", avg)
    print("Grade:", grade)
name, total, n = input_marks()
avg = calculate_average(total, n)
grade = assign_grade(avg)
display_result(name, total, avg, grade)