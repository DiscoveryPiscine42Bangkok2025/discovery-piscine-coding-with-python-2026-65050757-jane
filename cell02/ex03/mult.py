first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")
result = int(first_number) * int(second_number)
if result < 0:
    print("The result is negative.")
elif result > 0:
    print("The result is positive.")
else:
    print("The result is positive and negative.")