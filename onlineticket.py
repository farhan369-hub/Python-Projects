def book_tickets():
    seats = 50

    print("🎬 Welcome to Ticket Booking System")
    print(f"🪑 Total Seats Available: {seats}\n")

    while seats > 0:
        try:
            user_input = input("Enter number of tickets to book: ")

            # Handle text input
            if not user_input.isdigit():
                raise Exception("❌ Please enter a valid number.")

            tickets = int(user_input)

            # Handle zero or negative
            if tickets <= 0:
                raise Exception("❌ Number of tickets must be greater than 0.")

            # Handle overbooking
            if tickets > seats:
                raise Exception(f"❌ Only {seats} seats available.")

            # Booking success
            seats -= tickets
            print(f"✅ Booking successful! {tickets} tickets booked.")
            print(f"🪑 Seats remaining: {seats}\n")

        except Exception as e:
            print(e)
            print()

    print("🚫 All seats are booked. House Full!")


# 🔹 Run program
book_tickets()