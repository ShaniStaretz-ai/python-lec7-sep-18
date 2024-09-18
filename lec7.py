from random import randint
## simple way:
smallest: int = 101;
biggest: int = 0

for _ in range(10):
    num: int = randint(1, 100);
    print(num)
    if num > biggest:
        biggest = num;
    if num < smallest:
        smallest = num
print("the biggest number is :", biggest)
print("the smallest number is :", smallest)

#with None type

smallest: int = None;
biggest: int = None

for _ in range(10):
    num: int = randint(1, 100);
    print(num)
    if smallest is None or num > biggest:
        biggest = num;
    if smallest is None or num < smallest:
        smallest = num
print("the biggest number is :", biggest)
print("the smallest number is :", smallest)