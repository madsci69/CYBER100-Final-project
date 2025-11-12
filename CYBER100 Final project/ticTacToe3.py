


#1. Create Board Dictionary (done)
#2. print board function (done)
#3. oneplayer function//computer play function
#4. twoplayer function (NEED CHECK FOR INVALID RESPONSES)(done)
#5. Main function (done)

#Written by Lauren Pajerski for Cyber100 at Penn State University

import time
import sys


tttBoard = {'topL': ' ', 'topM': ' ', 'topR' : ' ', 'midL': ' ', 'midM' : ' ', 'midR': ' ', 'botL' : ' ', 'botM' : ' ', 'botR' : ' '}

def printBoard(board):
    print(board['topL'] + "|" + board['topM'] + "|" + board['topR'])
    print("-+-+-")
    print(board['midL'] + "|" + board['midM'] + "|" + board['midR'])
    print("-+-+-") 
    print(board['botL'] + "|" + board['botM'] + "|" + board['botR'])
    
def playerMove(player, board):
    print("The available moves are: {}. ".format(", ".join(checkAvailableMoves(board))))
        
    movePos = True
    while movePos == True:
        move = input("Player {} will move now. Where do you want to move? ".format(player))
        if checkValidMove(move) == False:
            move = input("That was not a valid reponse. Please enter a valid reponse. If you need a list of valid responses, press 1: ")
            if move == "1":
                print("Moves are topL, topM, topR, midL, midM, midR, botL, botM, botR. ")
                
        elif move not in checkAvailableMoves(board):
            print("That is not an available move. Please choose from the available moves. ")
            print("The available moves are: {}. ".format(", ".join(checkAvailableMoves(board))))

        else:
            board[move] = player
            printBoard(board)
            movePos = False
            
    return board
    
def twoPersonTTT(tttBoard):
    turn = "X"
    for i in range(0,9,1): 
        if turn == "X":
            tttBoard = playerMove(turn, tttBoard)
            if checkWinCon(tttBoard, turn) == True:
                break
                # print("The loop has broken")
            turn = "O"
                        
        elif turn == "O":
            tttBoard = playerMove(turn, tttBoard)
            if checkWinCon(tttBoard, turn) == True:
                break
                # print("The loop has broken")
            turn = "X"
    if checkWinCon(tttBoard, turn) == True:
        print("{} won the game! Congratulations! ".format(turn))
    else:            
        print("Nobody won this time! Better luck next time!")

def isBoardFull(board):
    for key, value in board.items():
        if value == ' ':
            return False
    return True
    # return all([cell != " " for row in board for cell in row]) would be a better way to write this, but what is present is my original solution. 
def minimax(board, depth, is_max):
    #This function checks each move to see what the best move is. 
    #Each iteration will check for a win condition. If the is_max value is true, it is the computer player (Maximizing)
    #After checking plays, the function simulates a play, and calls the minimax function on the newest play, passing it a decreased depth value.
    #Removes the play from the board. There may be a better way, using an additional simulated board, but since tictactoe is simple, this works.
    if checkWinCon(board, "X"):
        return -1
    elif checkWinCon(board, "O"):
        return 1
    elif isBoardFull(board):
        return 0
    if is_max:
        best_score = -float('inf')
        for move in checkAvailableMoves(board):
            board[move] = "O"
            
            score = minimax(board, depth -1, False)
            
            board[move] = " "
            
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for move in checkAvailableMoves(board):
            board[move] = "X"
            
            score = minimax(board, depth-1, True)
            
            board[move] = " "
            
            best_score = min(best_score, score)
        return best_score
def best_move(board):
    best_score = -float('inf')
    best_move = None
    for move in checkAvailableMoves(board):
        
        board[move] = "O"
        
        score = minimax(board, 4, False) #What is going wrong?
        
        board[move] = " "
        
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def checkAvailableMoves(board):
    availableMoves = []
    for key, value in board.items():
        if board[key].strip() == "":
            availableMoves.append(key)
    return availableMoves

def checkWinCon(board, player):
    win_conditions = [['topL', 'topM', 'topR'], ['midL', 'midM', 'midR'], ['botL', 'botM', 'botR'],
                      ['topL', 'midL', 'botL'], ['topM', 'midM', 'botM'], ['topR', 'midR', 'botR'],
                      ['topL', 'midM', 'botR'], ['topR', 'midM', 'botL']]
    for con in win_conditions:
        if board[con[0]] == board[con[1]] == board[con[2]] == player:
            return True
    return False    
        
def checkValidMove(move):
    moveSet = ('topL', 'topM', 'topR', 'midL', 'midM', 'midR', 'botL', 'botM', 'botR')
    if move not in moveSet:
        return False
    
def onePlayerTTT(board):
    gameWon = False
    turn = "X" #X will always start 
    for i in range(0,10,1): #Maximum number of moves in game. 
        if turn == "X":
            move = input("Player X will move now. Where do you want to move? ")
            checkValidMove(move)
            board[move] = turn
            printBoard(board)
            if checkWinCon(board, turn) == True:
                print("Congratulations {} for winning the game! ".format(turn))
                gameWon = True
                break
            turn = "O"
        elif turn == "O":
            print("The computer will move now. ")
            computerPlay(board)
            printBoard(board)
            if checkWinCon(board, turn) == True:
                print("Congratulations {} for winning the game! ".format(turn))
                gameWon = True
                break
            turn = "X"
    if gameWon == True:
        print("That was a great match! ")
    else:                
        print("Nobody won this time! Better luck next time!")        

def computerPlay(board):
    print("The computer is thinking...")
    time.sleep(3)
    move = best_move(board)
    board[move] = "O"
      
def checkValid(num):
    try:
        num = int(num)
        return num
    except ValueError:
        print("This is not a valid choice. ")
    except:
        print("Why do you keep breaking things? ")

# Prompt for one player or two player game


def main():

    num = input("Do you need to hear the instructions? Press 1 for yes and 2 for no. ")
    num = checkValid(num)
    if num == 1:
        print("""The instructions are as follows:
              The board is divided into top, mid, and bot on the horizontal. On the vertical, there is L, M, and R for
              left, mid, and right. In order to build a move, combine the horizontal term, with the vertical letter.
              For example: A move in the top row, middle position would be topM. A move in the middle row, left side
              would be midL. """)
    else:
        print("OK! Let's play! ")    
    
    while True:
        choice = input("Do you want to play one player or two player? (Enter 1 or 2 or 3 to quit) ")
        choice = checkValid(choice)
        # try:
        if choice == 1:
            liveBoard = {'topL': ' ', 'topM': ' ', 'topR' : ' ', 'midL': ' ', 'midM' : ' ', 'midR': ' ', 'botL' : ' ', 'botM' : ' ', 'botR' : ' '}
            print("Okay. You can play against the computer. The computer will play as \'O\'")
            onePlayerTTT(liveBoard)
            print("Great game! ")
        elif choice == 2:
            liveBoard = {'topL': ' ', 'topM': ' ', 'topR' : ' ', 'midL': ' ', 'midM' : ' ', 'midR': ' ', 'botL' : ' ', 'botM' : ' ', 'botR' : ' '}
            print("Okay. Player one will be \'X\' and player two will be \'O\'. ")
            twoPersonTTT(liveBoard)
            print("Great game! ")
        elif choice == 3:
            print("Okay! Thanks for playing. ")
            time.sleep(3)
            sys.exit(0)
        else:
            print("Not a valid response. Please enter 1 for one player or 2 for two player, or 3 to quit. ")
            
        
        
    
            

if __name__ == '__main__':
    main()