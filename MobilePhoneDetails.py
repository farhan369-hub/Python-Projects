class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def apply_discount(self, discount_amount):
        if discount_amount > 0 and discount_amount <= self.price:
            self.price -= discount_amount
            print(f"Discount of ₹{discount_amount} applied.")
        else:
            print("Invalid discount amount.")

    def display_mobile(self):
        print("\n--- Mobile Details ---")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: ₹{self.price}")

mobile1 = Mobile("Apple", "iPhone 14", 70000)
mobile1.display_mobile()
mobile1.apply_discount(5000)
mobile1.display_mobile()