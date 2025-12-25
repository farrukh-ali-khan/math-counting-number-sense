# Get two numbers from user
num1 = int(input("Enter first number (1-1000): "))
num2 = int(input("Enter second number (1-1000): "))

# Compare and print result
if num1 > num2:
    print(f"{num1} is larger than {num2}")
elif num2 > num1:
    print(f"{num2} is larger than {num1}")
else:
    print("Both numbers are equal")