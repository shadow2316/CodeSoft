import random

def main():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")
    print("Instructions: Type 'rock', 'paper', or 'scissors' to make a choice. Type 'exit' to end the game.")

    while True:
        # User Input
        user_choice = input("\nChoose rock, paper, or scissors: ").lower()

        # Check if the user wants to exit
        if user_choice == "exit":
            print("Thanks for playing!")
            break

        # Validate user input
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue

        # Computer Selection
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        print("Computer chose:", computer_choice)

        # Game Logic
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        # Display current scores
        print("Current Score - You:", user_score, "| Computer:", computer_score)

        # Play Again
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("Final Score - You:", user_score, "| Computer:", computer_score)
            print("Goodbye! Thanks for playing!")
            break

if __name__ == "__main__":
    main()

