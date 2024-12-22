size = int(input("Enter the size of the pattern: "))
pattern = size 
while pattern > 0 and pattern != 0:
    for num in range(size):
        print("*", end="")
    print("")
    pattern -= 1