def count_forwards():
    try:
        start = int(input("Enter a number (1–100): "))

        if start < 1 or start > 100:
            print("❌ Number must be between 1 and 100")
            return

        for i, num in enumerate(range(start, start + 10), start=1):
            print(f"{i}. {num}")

    except ValueError:
        print("❌ Invalid input. Please enter a number.")

count_forwards()
