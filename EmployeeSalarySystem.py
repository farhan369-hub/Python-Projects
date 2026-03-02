# Base class
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary


# Subclass 1: Manager
class Manager(Employee):
    def calculate_salary(self):
        bonus = 0.20 * self.base_salary
        return self.base_salary + bonus


# Subclass 2: Developer
class Developer(Employee):
    def calculate_salary(self):
        bonus = 0.10 * self.base_salary
        return self.base_salary + bonus


# Subclass 3: Intern
class Intern(Employee):
    def calculate_salary(self):
        stipend = 0.05 * self.base_salary
        return self.base_salary + stipend


# Creating objects
employees = [
    Manager("Rahul", 50000),
    Developer("Aman", 40000),
    Intern("Riya", 20000)
]

# Display salary details
for emp in employees:
    print("Name:", emp.name)
    print("Total Salary:", emp.calculate_salary())
    print()