#!/usr/bin/env python3

first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")
result = int(first_number) * int(second_number)
print(f"{first_number} X {second_number} = {result}")

if result < 0:
    print("The result is negative.")
elif result > 0:
    print("The result is positive.")
else:
    print("The result is positive and negative.")