base = [0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0]
plus = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(11):
    if i == 0:
        print(f"Table de {i}: ", *base)
        continue
    for j in range(len(base) - 1):
        base[j + 1] = base[j + 1] + plus[j + 1]
    print(f"Table de {i}: ", *base)

        