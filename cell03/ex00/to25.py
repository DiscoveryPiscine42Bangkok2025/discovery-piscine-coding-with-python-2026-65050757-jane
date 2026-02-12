inp = int(input("Enter a number less than 25\n"))

if inp < 25:
    while inp < 26:
        print(f"Inside the loop, my variable is {num}")
        inp += 1
else :
    print("Error")