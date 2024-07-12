import random

def rps(choice):
    options = ["Rock", "Paper", "Scissors"]
    
    user_choice = choice
    computer_choice = random.choice(options)
    
    print("You chose: ", user_choice)
    print("Computer chose: ", computer_choice)
    
    if user_choice == computer_choice:
        result_from_rps = "It's a tie!"
    elif user_choice == "Rock" and computer_choice == "Scissors":
        result_from_rps = "You win!"
    elif user_choice == "Paper" and computer_choice == "Rock":
        result_from_rps = "You win!"
    elif user_choice == "Scissors" and computer_choice == "Paper":
        result_from_rps = "You win!"
    else:
        result_from_rps = "Computer wins!"


    print(f'You chose: {user_choice} BrainzBot chose: {computer_choice}. The result was: {result_from_rps}')    
    return f'You chose: {user_choice} BrainzBot chose: {computer_choice}. The result was: {result_from_rps}'