import random

best_score = None  # Track fewest attempts across games

while True:  # Loop to allow multiple games
    minimum_value = int(input("Enter the minimum value for difficulty level: "))
    maximum_value = int(input("Enter the maximum value for difficulty level: "))

    number_to_guess = random.randint(minimum_value, maximum_value)

    guess_count = 0
    max_attempts = 5

    while guess_count < max_attempts:
        try:
            guess = int(input(f"Make a guess between {minimum_value}-{maximum_value}: "))
            guess_count += 1

            if guess < number_to_guess:
                print("Too Low!")
            elif guess > number_to_guess:
                print("Too High!")
            else:
                print("Congratulations! You guessed the number.")
                if best_score is None or guess_count < best_score:
                    best_score = guess_count
                    print(f" New best score: {best_score} attempt(s)!")
                else:
                    print(f" Your best score is still {best_score} attempt(s).")
                break
        except ValueError:
            print("Invalid! Try again with a valid number.")
    else:
        print(f" You're out of attempts. The correct number was {number_to_guess}.")
        if best_score is not None:
            print(f" Your best score remains {best_score} attempt(s).")
        else:
            print("No best score set yet.")

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! ")
        break