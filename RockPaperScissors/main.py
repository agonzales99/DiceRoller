import random

def playerChoice():
    userInput = input("Please select rock, paper, or scissors")

    return userInput.capitalize()

def rockPaperScissors(selection, aiSelection, game):

    lose = "You lose"
    win = "You win"
    tie = "You tied with the computer"

    if(selection == game[0]):
        if(aiSelection == game[1]):
            print(lose)
        elif(aiSelection == game[2]):
            print(win)
        else:
            print(tie)
    elif(selection == game[1]):
        if(aiSelection == game[0]):
            print(win)
        elif(aiSelection == game[2]):
            print(lose)
        else:
            print(tie)
    elif(selection == game[2]):
        if(aiSelection == game[0]):
            print(lose)
        elif(aiSelection == game[1]):
            print(win)
        else:
            print(tie)
    else:
        print("Invalid")

selection = playerChoice()

game = ["Rock", "Paper", "Scissors"]

print("You selected " + selection)

aiSelection = random.choice(game)

print("The computer selected " + aiSelection)

rockPaperScissors(selection, aiSelection, game)
