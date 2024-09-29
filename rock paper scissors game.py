import random

def get_computer_choice():
    """Randomly select the computer's choice."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    """Determine the winner of the game based on player and computer choices."""
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'rock') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    """Main function to play the Rock, Paper, Scissors game."""
    print("Welcome to Rock, Paper, Scissors!")
    
    choices = ['rock', 'paper', 'scissors']
    
    while True:
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        
        if player_choice not in choices:
            print("Invalid choice. Please select rock, paper, or scissors.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice)
        print(result)
        
        play_again = input("Do you want to play again? (retry/exit): ").lower()
        if play_again != 'retry':
            print("Thanks for playing! Have a nice day.")
            break

if __name__ == "__main__":
    main()
