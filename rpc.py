import random
def get_user_choice():
    return input("Choose rock, paper, or scissors: ").lower()

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!!!"
    elif ((user_choice == "rock" and computer_choice == "scissors") or 
         (user_choice == "scissors" and computer_choice == "paper") or 
         (user_choice == "paper" and computer_choice == "rock")):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_score, computer_score = 0, 0

    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(["rock", "paper", "scissors"])
        
        result = determine_winner(user_choice, computer_choice)
        print(f"You chose {user_choice}. The computer chose {computer_choice}. {result}")

        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1

        print(f"Score: You {user_score} - {computer_score} Computer")

        if input("Do you want to play again? (yes/no): ").lower() != "yes":
            break

if __name__ == "__main__":
    print("Welcome to Rock-Paper-Scissors Game!")
    play_game()
