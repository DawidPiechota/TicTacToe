#!/usr/bin/env python3

import os
from random import randint, choice
clear = lambda: os.system('cls') # 'clear' for linux

def printBoard(board):
    print ("Board:         Moves:\n")
    print (' '  + board[0] + " | " + board[1] + " | " + board[2] + '     ' + " 1 | 2 | 3")
    print ("-----------    -----------")
    print (' '  + board[3] + " | " + board[4] + " | " + board[5] + '     ' + " 4 | 5 | 6")
    print ("-----------    -----------")
    print (' '  + board[6] + " | " + board[7] + " | " + board[8] + '     ' + " 7 | 8 | 9")

def doesPlayerWin2(board):
    toCheckList =  [[0, 1, 2], [3, 4, 5], [6, 7, 8], # rzedy
                [0, 3, 6], [1, 4, 7], [2, 5, 8], # kolumny
                [0, 4, 8], [2, 4, 6]]            # przekatne

    for toCheck in toCheckList:
        if((''.join(board[toCheck[0]]+board[toCheck[1]]+board[toCheck[2]])) in ('ooo', 'xxx')):
            print('\n' + board[toCheck[0]] + ' won!\n')
            exit(0)
    if(' ' not in board):
        print('Draw!')
        exit(0)

def isSpaceFree(board, move):
    if(board[move-1] == ' '):
        return True
    else: return False

def getUserMove(board, char):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)): # pomysl na .split() z neta
        move = raw_input("\n" + char + '\'s turn (1-9): ')
    board[int(move)-1] = char

def getAIRandomMove(board):
    while True:
        move = randint(1, 9)
        if(isSpaceFree(board, int(move))): break
    board[int(move) - 1] = 'x'

def getAIMove(board):
    
    if(len(set(board))==2): # pierwszy ruch po rozpoczeciu gracza
        if(isSpaceFree(board, 5)):
            board[4] = 'x'
            return
        else:
            board[choice([0, 2, 6, 8])] = 'x'
            return

    toCheckList =  [[0, 1, 2], [3, 4, 5], [6, 7, 8], # rzedy
                [0, 3, 6], [1, 4, 7], [2, 5, 8], # kolumny
                [0, 4, 8], [2, 4, 6]]            # przekatne

    # petla przechodzi po pozycjach do sprawdzenia i jesli trzeba, wstawia 'x' w miejsce wygrywajacego ruchu lub zagrozonego miejsca
    for toCheck in toCheckList:
        if((''.join(board[toCheck[0]]+board[toCheck[1]]+board[toCheck[2]])) in ('x x', 'xx ', ' xx')):
            if  (board[toCheck[0]] == ' '): board[toCheck[0]] = 'x'
            elif(board[toCheck[1]] == ' '): board[toCheck[1]] = 'x'
            elif(board[toCheck[2]] == ' '): board[toCheck[2]] = 'x'
            return
    for toCheck in toCheckList:
        if((''.join(board[toCheck[0]]+board[toCheck[1]]+board[toCheck[2]])) in ('o o', 'oo ', ' oo')):
            if  (board[toCheck[0]] == ' '): board[toCheck[0]] = 'x'
            elif(board[toCheck[1]] == ' '): board[toCheck[1]] = 'x'
            elif(board[toCheck[2]] == ' '): board[toCheck[2]] = 'x'
            return
    # zabezpieczenie przed podwojnym zagrozonym polem
    if( 'oo' in [board[0] + board[8], board[2] + board[6]]):
        allMiddlePoints = [1, 3, 5, 7]
        while(len(allMiddlePoints) > 0):
            middlePoint = choice(allMiddlePoints)
            if(isSpaceFree(board, middlePoint+1)):
                board[middlePoint] = 'x'
                return
            else: allMiddlePoints.remove(middlePoint)
	
	# zabezpieczenie przed podwojnym zagrozonym polem 2.
	
    if('oo' in [board[1] + board[5], board[3] + board[7], board[1] + board[3], board[7] + board[5]]):
	if(isSpaceFree(board, 4+1)):
		board[4] = "x"
		return
			

    
    # priorytet maja rogi
    allCorners = [0, 2, 6, 8]
    while(len(allCorners) > 0):
        corner = choice(allCorners)
        if(isSpaceFree(board, corner+1)):
            board[corner] = 'x'
            return
        else: allCorners.remove(corner)
    # jak wszystkie zajete to losowo (chyba nigdy tego nie uzywa)
    getAIRandomMove(board)

def playerOrPc():
    clear()
    who = ' '
    while who not in '1 2'.split():
        who = raw_input('Who are you playing with?\n1- "AI", 2- Another player\n')
    clear()
    return who

def whoIsStarting():
    clear()
    who = ' '
    while who not in "1 2".split():
        who = raw_input('Who goes first?\n1- You, 2- "AI"\n')
    clear()
    return who

def playerVsPlayerGame(board):
    printBoard(board)
    while True:
        getUserMove(board, 'o')
        clear()
        printBoard(board)
        doesPlayerWin2(board)

        getUserMove(board, 'x')
        clear()
        printBoard(board)
        doesPlayerWin2(board)

def playerVsAIGame(board, first):
    printBoard(board)
    if(first == '1'): # Player goes first
        while True:
            getUserMove(board, 'o')
            clear()
            printBoard(board)
            doesPlayerWin2(board)
            
            getAIMove(board)
            clear()
            printBoard(board)
            doesPlayerWin2(board)

    else:           # AI goes first
        while True:
            getAIMove(board)
            clear()
            printBoard(board)
            doesPlayerWin2(board)
            
            getUserMove(board, 'o')
            clear()
            printBoard(board)
            doesPlayerWin2(board)

# _________________________________________________________________________ #

board = [' '] * 9

if(playerOrPc() == "1"): opponent = "Ai"
else: opponent = "Player"

while True:
    if(opponent == "Player"): playerVsPlayerGame(board)
    else: playerVsAIGame(board, whoIsStarting())

