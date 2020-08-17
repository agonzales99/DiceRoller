import random

def numberInput():
    diceNumber = input("Please select the number of dice you would like to use ")
    return int(diceNumber)

numberOfDice = numberInput()

def diceRoller(numberOfDice):
    for dice in range(numberOfDice):
        number = random.randint(1, 6)
        print(str(number) + " ")

diceRoller(numberOfDice)