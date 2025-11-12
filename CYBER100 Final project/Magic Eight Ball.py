# Magic Eight Ball

import random
import sys
import time

def shakeTheBall():
    num = random.randint(1, 10)
    return num
def fantasticResponse(num, name):
    if num == 1:
        print("You're going to have a great day, {}. Don't worry about silly questions. ".format)
    elif num == 2:
        print("This is unlikely, {}. I suggest you reconsider your life choices. ".format(name))
    elif num == 3:
        print("What a great question! You're so smart, {}. ".format(name))
    elif num == 4:
        print("¯\_(ツ)_/¯")
    elif num == 5:
        print("I suggest you direct this query to your favorite AI future overlord. ")
    elif num == 6:
        print("Well, {}, I would give that a 50/50 chance. ".format(name))
    elif num == 7:
        print("I'm sure that will work out fine!")
    elif num == 8:
        print("*crickets chirping...*")
    elif num == 9:
        print("That's a pretty silly question, {}. ".format(name))
    else:
        print("Maybe you should shake the ball again. ")


if __name__ == '__main__':

    T = True
    while T == True:
        print("Do you want to shake the magic 8 ball? Press Y to play, and N to quit: ")
        response = input()

        if response.lower().strip() == "y":
            name = input("Okay! Before we start what is your name? ")
            print("Okay {}, ask your question, and prepare to shake the Magic 8 ball. No need to type in your question, we will detect it. ".format(name))
            time.sleep(6)
            shakey_shake = shakeTheBall()
            print(shakey_shake)
            fantasticResponse(shakey_shake, name)

        elif response.lower().strip() == 'n':
            sys.exit()
        
        else:
            print("That is not a valid response. ")


    