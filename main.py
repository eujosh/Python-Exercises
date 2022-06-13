import random

print('Welcome to [Rock-Paper-Scissors] Game Where: \n "R" stands for "Rock" \n "P" stands for "Paper"\n "S" stands for "Scissor" \n')

list_of_possible_options = ["Rock", "Paper", "Scissors"]

Player = input("Pick an option between : 'Rock', 'Paper' or 'Scissors'\n ").capitalize()
CPU = random.choice(list_of_possible_options)
print(f"Player ({Player}) : CPU ({CPU})")

while Player not in list_of_possible_options:
    print('Error! Try again')
    Player = input("Pick an option between : 'Rock', 'Paper' or 'Scissors'\n ").capitalize()
    
#set player to True
if Player == CPU:
    print("Tie!")    
elif Player == "Rock":
    if CPU == "Paper":
        print("You lose!", CPU, "covers", Player)
    else:
        print("You win!", Player, "smashes", CPU)
elif Player == "Paper":
    if CPU == "Scissors":
        print("You lose!", CPU, "cut", Player)
    else:
        print("You win!", Player, "covers", CPU)
elif Player == "Scissors":
    if CPU == "Rock":
        print("You lose...", CPU, "smashes", Player)
    else:
        print("You win!", Player, "cut", CPU)
else:
    print("Error!. Check your spelling!")

