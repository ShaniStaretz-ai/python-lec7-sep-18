max_num: int = int(input("enter odd number:"))
while not max_num % 2 == 1:
    max_num: int = int(input("enter odd number:"))
for row in range(1, max_num + 2, 2):
    for _ in range(0, ((max_num - row) // 2)):
        print(" ", end="")
    for i in range(1, row + 1):
        print(i, end="")
    print()
for row in range(max_num - 1, 0, -2):
    max_spaces = (max_num - row) // 2
    for _ in range(0, max_spaces + 1):
        print(" ", end="")
    for i in range(1, row):
        print(i, end="")
    print()
