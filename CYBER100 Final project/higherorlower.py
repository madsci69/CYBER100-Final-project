import random

# Creates lists of suits and values associated with the card.
suits = ['clubs', 'spades', 'hearts', 'diamonds']
values = [("Ace", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5), ("6", 6), ("7", 7), ("8", 8), ("9", 9), ("10", 10), ("J", 11), ("Q", 12), ("K", 13) ]
continueInput = False

# Loop to continue based on prompt at the end
while not continueInput:
    validInput = False # Initalize variable to check for valid input
    # Creates random card and prints it
    starting_card = random.choice(values)
    starting_card_value = starting_card[1]
    starting_card_value_string = str(starting_card[0])
    starting_card_suit = random.choice(suits)
    print("Your starting card is: " + starting_card_value_string + " of " + starting_card_suit)
    # Prompt user to choose higher or lower while checking valid input.
    while not validInput:
        bet = input("Do you bet higher or lower?")
        betcheck = bet.casefold() #makes input case-insensitive
        if betcheck == "higher" or betcheck == "lower":
            validInput = True
        else:
            print("Please enter 'higher' or 'lower'")
    print("You have selected " + bet)
    
    # Draws the next card and prints it
    next_card = random.choice(values)
    next_card_value = next_card[1]
    next_card_value_string = str(next_card[0])
    next_card_suit = random.choice(suits)
    print("The card drawn is: " + next_card_value_string + " of " + next_card_suit)
    # Loop to check the if the player won based on bet
    if betcheck == "higher":
        if starting_card_value > next_card_value:
            print("You have lost!")
        elif starting_card_value < next_card_value:
            print("You have won!")
        else:
            print("You have tied!")
    else:
        if starting_card_value > next_card_value:
            print("You have won!")
        elif starting_card_value < next_card_value:
            print("You have lost!")
        else:
            print("You have tied!")
    # Prompt to ask if the player wants to play again
    while not continueInput:
        continue_Playing = input("Did you want to keep playing? Y/N")
        continuecheck = continue_Playing.casefold() #makes input case-insensitive
        if continuecheck == 'y' or continuecheck == 'n':
            break
        else:
            print("Please type 'Y' or 'N'")
    if continuecheck == 'y':
        continueInput = False
    else:
        print("Ending game.")
        continueInput = True
        break