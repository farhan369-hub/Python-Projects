class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def increase_salary(self, amount):
        if amount > 0:
            self.salary += amount
            print(f"Salary increased by ₹{amount}.")
        else:
            print("Invalid amount.")

    def display_details(self):
        print("\n--- Employee Details ---")
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: ₹{self.salary}")

emp1 = Employee("Farhan", "EMP101", 25000)
emp1.display_details()
emp1.increase_salary(5000)
emp1.display_details()