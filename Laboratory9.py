rowInput = int(input("Enter the number of rows: "))
number1 = 1
for i in range(1, rowInput + 1):
    for j in range(i):
        print(number1, end=" ")
        number1 += 1
    print()
