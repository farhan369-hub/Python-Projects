class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        area = self.length * self.breadth
        print(f"Area of Rectangle: {area}")

    def update_dimensions(self, new_length, new_breadth):
        if new_length > 0 and new_breadth > 0:
            self.length = new_length
            self.breadth = new_breadth
            print("Dimensions updated successfully.")
        else:
            print("Invalid dimensions.")

rect1 = Rectangle(10, 5)
rect1.calculate_area()
rect1.update_dimensions(15, 8)
rect1.calculate_area()