i: int = 0;
count_negative: int = 0;
count_positive: int = 0;
count_zero: int = 0;
count_div9: int = 0;
last_positive_num: int = None;
last_negative_num: int = None;
while i <= 10:
    num = int(input("enter number:"));
    if num == -9999:
        break;
    if num > 1000 or num < -1000:
        continue;
    if num < 0:
        count_negative += 1;
        last_negative_num = num;
    elif num > 0:
        count_positive += 1;
        last_positive_num = num;
    else:
        count_zero += 1;
    if num % 7 == 0:
        count_div9 += 1;
    i += 1;
else:
    print(f"\033[4;31mStatistical results:\033[0m")
    print(f"count negative numbers: {count_negative}");
    print(f"count positive numbers:  {count_positive}");
    print(f"count zeroes: {count_negative}");
    print(f"count numbers dived by 7:{count_negative}");
    print(f"last negative number was:{last_negative_num}");
    print(f"last positive number was:{last_positive_num}");
