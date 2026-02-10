inp = int(input("Enter a number less than 25\n"))

if inp < 25:
    for num in range(inp, 26):
        print(f"Inside the loop, my variable is {num}")
else :
    print("Error")