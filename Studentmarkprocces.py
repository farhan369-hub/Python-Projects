def process_marks(filename):
    total = 0
    count = 0
    invalid_count = 0

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

            # Check empty file
            if not lines:
                print("⚠ File is empty.")
                return

            print("\n📊 Student Marks:\n")

            for line in lines:
                try:
                    # Remove spaces and newline
                    line = line.strip()

                    # Validate format
                    if ',' not in line:
                        raise ValueError("Incorrect format")

                    name, marks = line.split(',')

                    # Convert marks to integer
                    marks = int(marks)

                    print(f"{name} → {marks}")

                    total += marks
                    count += 1

                except ValueError:
                    print(f"❌ Invalid record skipped: {line}")
                    invalid_count += 1

            # Calculate average
            if count > 0:
                average = total / count
                print("\n📈 Average Marks:", round(average, 2))
            else:
                print("\n⚠ No valid records to calculate average.")

            print(f"\n✅ Valid Records: {count}")
            print(f"❌ Invalid Records: {invalid_count}")

    except FileNotFoundError:
        print("❌ Error: File not found.")


# 🔹 Run the program
filename = input("Enter file name: ")
process_marks(filename)