import random
count = 0


while True:
    choice = input("Role your Dice? (y/n): ").lower()
    if choice == "y":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"({die1}, {die2})")
        count = count + 1
        print(f"Your role dice count is {count}")
    elif choice == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid Choice")