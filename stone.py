import random

def stone_paper_scissor():
    user_choice = input("Enter your choice (stone, paper, scissor): ").lower()
    computer_choice = random.choice(['stone', 'paper', 'scissor'])

    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'stone' and computer_choice == 'scissor') or \
         (user_choice == 'paper' and computer_choice == 'stone') or \
         (user_choice == 'scissor' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("You lose!")

stone_paper_scissor()
