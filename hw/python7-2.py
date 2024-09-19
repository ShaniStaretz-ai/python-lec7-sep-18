count_GOOD_RECORD = 0
sum_GOOD_RECORD = 0
GOOD_RECORD: float = 5.80;
name: str = None;
world_record: float = 6.23;
best_record: float = 0
for _ in range(4):
    record = float(input("enter high jump record:"));
    if record < GOOD_RECORD:
        continue;
    elif record >= GOOD_RECORD:
        count_GOOD_RECORD += 1;
        sum_GOOD_RECORD += record;
        if best_record < record:
            best_record = record
        if record > world_record:
            world_record = record
            name = input("enter this athlete's name:");

print(f"\033[4;31mStatistical results:\033[0m")
print(
    f"total good records were \033[1;33m{count_GOOD_RECORD}\033[0m with average of \033[1;33m{(sum_GOOD_RECORD / count_GOOD_RECORD):.2f}\033[0m");
print(f"best record in the competition was: \033[1;33m{best_record}\033[0m")
if name is not None:
    print(f"new world record is \033[1;33m{world_record}\033[0m made by the athlete {name}")
else:
    print("None")
