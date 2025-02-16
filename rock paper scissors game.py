# Rock Paper Scissors 
import random
emojis={
    'r':'🪨',
    'p':'📃',
    's':'✂️'
}
choices=('r','p','s')

print("Welcome to the Rock, Paper, Scissors game! Let's play 🎮")

def getchoice():
    while True:
        userchoice=input("Rock,paper, or scissors? (r/p/s):").lower()
        if userchoice in choices:
            return userchoice
        else:
            print("Invalid Choice.")

def display_choices(userchoice,computer_choice):
    print(f'You chose{emojis[userchoice]}')
    print("Computer chose",emojis[computer_choice])

def winner(userchoice,computer_choice):
    if userchoice==computer_choice:
        print("Tie..")
    elif (userchoice=='r' and computer_choice=='s') or (userchoice=='s' and computer_choice=='p') or (userchoice=='p' and computer_choice=='r'):
        print("You Won🥳🎉")
    else:
        print("Computer won. You lost!")

def playgame():            
    while True:  
        userchoice= getchoice() 
        computer_choice=random.choice(choices)
        display_choices(userchoice,computer_choice)
        winner(userchoice,computer_choice)
        should_continue=input("Continue? (y/n):").lower()
        if should_continue=='n':
            print("Thanks for playing.👋")
            break
playgame()
    



