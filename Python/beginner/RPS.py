import random

options=["rock","paper", "scissors"]

def choices():
    player_choice=input("enter Your choice (rock,paper,scissors) : ")
    player_choice=player_choice.replace(" ","").lower()
    computer_choice=random.choice(options) ## random.choice picks random element from given list and returns
    choices={"player_choice":player_choice,"computer_choice":computer_choice}
    return choices

def check_win(player_choice,computer_choice):

    print(f" you chose: {player_choice}\n computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("tie")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("You Win")
    elif player_choice =="rock" and computer_choice == "paper":
        print("You Win")
    elif player_choice =="scissors" and computer_choice =="paper":
        print("You Win")
    else:
        print("You Lost, Try Again")

choices=choices()
result=check_win(choices["player_choice"],choices["computer_choice"])
