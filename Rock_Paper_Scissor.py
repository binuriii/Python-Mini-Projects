import random

choices = ("r", "p", "s")

def get_user_choice():
    while True:
        user_choice = input("Rock, Paper or scissors? (r/p/s): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice! ")

def display_choices(user_choice, computer_choice):
    print(f"You choose {user_choice}")
    print(f"Computer choose {computer_choice}")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Tie! ")
        return "tie"
    elif (
        (user_choice == "r" and computer_choice == "s") or 
        (user_choice == "s" and computer_choice == "p") or
        (user_choice == "p" and computer_choice == "r")):
        print("You Win!")
        return "user"
    else:
        print("You Lose")
        return "computer"

def play_game():
    total_wins = 0
    total_losses = 0
    total_ties = 0

    while True:
        user_score = 0
        computer_score = 0
        
        while user_score < 2 and computer_score < 2:
            user_choice = get_user_choice()
            computer_choice = random.choice(choices)
            display_choices(user_choice, computer_choice)
            winner = determine_winner(user_choice, computer_choice)
            
            if winner == "user":
                user_score += 1
                total_wins += 1
            elif winner == "computer":
                computer_score += 1
                total_losses += 1
            else:
                total_ties += 1
    
            print(f"Score: You {user_score} - Computer {computer_score}\n")
    
        if user_score == 2:
            print("You won the match!")
        else:
            print("Computer won the match!")
            
        should_continue = input("Continue (y/n): ").lower()
        if should_continue == "n":
            print("\nGame Over!")
            print(f"Total Wins: {total_wins}")
            print(f"Total Losses: {total_losses}")
            print(f"Total Ties: {total_ties}")
            break

play_game()