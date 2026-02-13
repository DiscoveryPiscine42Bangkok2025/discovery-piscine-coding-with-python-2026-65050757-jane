#!/usr/bin/env python3
year = [10,20,30]

inp = int(input("Please tell me your age: "))
print(f"You are currently {inp} years old")

for i in range(len(year)):
    print(f"In {year[i]} years, you'll be {inp+year[i]} years old")