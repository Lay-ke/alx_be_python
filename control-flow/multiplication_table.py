number = int(input("Enter a number to see its multiplication table: "))

for multiplier in range(1,11):
    multiply = number * multiplier
    print(f"{number} * {multiplier} = {multiply}")