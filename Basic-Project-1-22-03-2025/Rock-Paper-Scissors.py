import random

def get_computer_choice(player_history):
    if len(player_history) > 1:
        most_recent = player_history[-1]
        if most_recent == "rock":
            return "paper"  
        elif most_recent == "paper":
            return "scissors"  
        else:
            return "rock"  
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player, computer):
    if player == computer:
        return "draw"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "player"
    else:
        return "computer"

def main():
    player_history = []
    player_score = 0
    computer_score = 0
    match_count = 0
    
    while True:
        print("\nRock, Paper, Scissors - Make your move!")
        player_choice = input("Enter rock, paper, or scissors: ").lower()
        
        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Try again.")
            continue
        
        computer_choice = get_computer_choice(player_history)
        print(f"Computer chose: {computer_choice}")
        
        player_history.append(player_choice)
        
        winner = determine_winner(player_choice, computer_choice)
        if winner == "player":
            print("You win this round!")
            player_score += 1
        elif winner == "computer":
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("It's a draw!")
        
        match_count += 1
        
        if match_count % 3 == 0:
            print(f"\nScore after {match_count} matches - You: {player_score} | Computer: {computer_score}")
            continue_game = input("Do you want to continue? (yes/no): ").lower()
            if continue_game != "yes":
                print("Thanks for playing Final Score - You: {} | Computer: {}".format(player_score, computer_score))
                break

if __name__ == "__main__":
    main()