import random

salary = int(input("Enter your salary: "))
bonus = random.choice([True, False])

if bonus:
    random_bonus = random.randint(0, 10000)
    total = salary + random_bonus
    print(f"{salary}, {bonus} - '${salary + random_bonus}'")
else:
    print(f"{salary}, {bonus} - '${salary}'")
