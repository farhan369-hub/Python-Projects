def input_details():
    name = input("Enter employee name : ")
    basic = float(input("Enter basic salary : "))
    allowance = float(input("Enter allowance : "))
    return name, basic, allowance

def calculate_gross(basic, allowance):
    gross = basic + allowance
    return gross

def calculate_deductions(gross):
    tax = gross * 0.1
    pf = gross * 0.05
    total_deduction = tax + pf
    return total_deduction

def display_final(name, gross, deduction):
    final_salary = gross - deduction
    print("Employee Name:", name)
    print("Gross Salary:", gross)
    print("Deductions:", deduction)
    print("Final Salary:", final_salary)

name, basic, allowance = input_details()
gross = calculate_gross(basic, allowance)
deduction = calculate_deductions(gross)
display_final(name, gross, deduction)