import tkinter as tk
from tkinter import messagebox
#import pickle
class gameboard():
    Board = 0         #The current board of the game that keeps track of all the moves
    Player1Name = 0      #Usernames of both players
    Player2Name = 0
    LastPlayerName = 0   #Username of the last player to have a turn
    TotalGamesPlayed = 0    #Total Number of games played
    TotalNumWins = 0        #Total Number of wins
    TotalNumLoss = 0        #Total Number of losses
    TotalNumTies = 0        #Total Number of ties
    Button1 = ''
    Button2 = ''
    Button3 = ''
    Button4 = ''
    Button5 = ''
    Button6 = ''
    Button7 = ''
    Button8 = ''
    Button9 = ''
    list_Buttons = []
    boardRow1 = [0, 0, 0]
    boardRow2 = [0, 0, 0]
    boardRow3 = [0, 0, 0]
    #define my constructor for my baord
    #initiatlize my class variables as part of my initial constructor
    def __init__(self):
        #Variables
        self.Board_Full = True
        self.Turn = True # True = X, False = Y
        self.Player1Name = 'player1'
        self.Player2Name = ''
        self.LastPlayerName = ''

        self.TotalNumTies = 0
        self.TotalGamesPlayed = 0
        self.player1Wins = 0
        self.player1Loss = 0
        self.player2Wins = 0
        self.player2Loss = 0        

        self.list_Buttons = []
        self.boardRow1 = [0, 0, 0]
        self.boardRow2 = [0, 0, 0]
        self.boardRow3 = [0, 0, 0]

    def recordGamePlayed(self): #Updates how many total games have been played
        self.TotalGamesPlayed += 1
    def getGamePlayed(self):
        return self.TotalGamesPlayed
    def recordPlayer1Name(self, Player1):
        self.Player1Name = Player1
    def recordPlayer1Name(self, Player2):
        self.Player2Name = Player2
    def getPlayer1Name(self):
        return self.Player1Name
    def getPlayer2Name(self):
        return self.Player2Name

    def resetGameBoard(self): #Clear all the moves from game board
        self.boardRow1[0] = 0
        self.boardRow1[1] = 0
        self.boardRow1[2] = 0

        self.boardRow2[0] = 0
        self.boardRow2[1] = 0
        self.boardRow2[2] = 0

        self.boardRow3[0] = 0
        self.boardRow3[1] = 0
        self.boardRow3[2] = 0

    def isBoardFull(self): #Checks if the board is full (I.e. no more moves to make)
        self.combined_Board = self.boardRow1 + self.boardRow2 + self.boardRow3
        self.Board_Full = True
        for i in range(len(self.combined_Board)):
            if self.combined_Board[i] == 0:
                self.Board_Full = False #False = board is not full
        return self.Board_Full
        

    def isGameFinished(self): #Checks if the latest move resulted in a win, loss or tie. Updates the wins, losses and ties count if the game is over
        if self.boardRow1[0] == 'X' and self.boardRow1[1] == 'X' and self.boardRow1[2] == 'X':
            self.player2Wins += 1
            self.player1Loss += 1
            self.TotalGamesPlayed += 1
            self.resetGameBoard()
            self.Turn = True
            return 'X'
        elif self.boardRow2[0] == 'X' and self.boardRow2[1] == 'X' and self.boardRow2[2] == 'X':
            self.player2Wins += 1
            self.player1Loss += 1
            self.TotalGamesPlayed += 1
            self.resetGameBoard()
            self.Turn = True
            return 'X'
        elif self.boardRow3[0] == 'X' and self.boardRow3[1] == 'X' and self.boardRow3[2] == 'X':
            self.player2Wins += 1
            self.player1Loss += 1
            self.TotalGamesPlayed += 1
            self.resetGameBoard()
            self.Turn = True
            return 'X'
        elif self.boardRow1[0] == 'X' and self.boardRow2[0] == 'X' and self.boardRow3[0] == 'X':
            self.player2Wins += 1
            self.player1Loss += 1
            self.TotalGamesPlayed += 1
            self.resetGameBoard()
            self.Turn = True
            return 'X'
        elif self.boardRow1[1] == 'X' and self.boardRow2[1] == 'X' and self.boardRow3[1] == 'X':
            self.player2Wins += 1
            self.player1Loss += 1
            self.TotalGamesPlayed += 1
            self.resetGameBoard()
            self.Turn = True
            return 'X'
        elif self.boardRow1[2] == 'X' and self.boardRow2[2] == 'X' and self.boardRow3[2] == 'X':
            self.player2Wins += 1
            self.player1Loss += 1
            self.TotalGamesPlayed += 1
            self.resetGameBoard()
            self.Turn = True
            return 'X'
        elif self.boardRow1[0] == 'X' and self.boardRow2[1] == 'X' and self.boardRow3[2] == 'X':
            self.player2Wins += 1
            self.player1Loss += 1
            self.TotalGamesPlayed += 1
            self.resetGameBoard()
            self.Turn = True
            return 'X'
        elif self.boardRow1[2] == 'X' and self.boardRow2[1] == 'X' and self.boardRow3[0] == 'X':
            self.player2Wins += 1
            self.player1Loss += 1
            self.TotalGamesPlayed += 1
            self.resetGameBoard()
            self.Turn = True
            return 'X'
        #Checks "O" win
        elif self.boardRow1[0] == 'O' and self.boardRow1[1] == 'O' and self.boardRow1[2] == 'O':
            self.player1Wins += 1
            self.player2Loss += 1
            self.TotalGamesPlayed += 1
            self.resetGameBoard()
            self.Turn = False
            return 'O'
        elif self.boardRow2[0] == 'O' and self.boardRow2[1] == 'O' and self.boardRow2[2] == 'O':
            self.player1Wins += 1
            self.player2Loss += 1
            self.TotalGamesPlayed += 1
            self.resetGameBoard()
            self.Turn = False
            return 'O'
        elif self.boardRow3[0] == 'O' and self.boardRow3[1] == 'O' and self.boardRow3[2] == 'O':
            self.player1Wins += 1
            self.player2Loss += 1
            self.TotalGamesPlayed += 1
            self.resetGameBoard()
            self.Turn = False
            return 'O'
        elif self.boardRow1[0] == 'O' and self.boardRow2[0] == 'O' and self.boardRow3[0] == 'O':
            self.player1Wins += 1
            self.player2Loss += 1
            self.TotalGamesPlayed += 1
            self.resetGameBoard()
            self.Turn = False
            return 'O'
        elif self.boardRow1[1] == 'O' and self.boardRow2[1] == 'O' and self.boardRow3[1] == 'O':
            self.player1Wins += 1
            self.player2Loss += 1
            self.TotalGamesPlayed += 1
            self.resetGameBoard()
            self.Turn = False
            return 'O'
        elif self.boardRow1[2] == 'O' and self.boardRow2[2] == 'O' and self.boardRow3[2] == 'O':
            self.player1Wins += 1
            self.player2Loss += 1
            self.TotalGamesPlayed += 1
            self.resetGameBoard()
            self.Turn = False
            return 'O'
        elif self.boardRow1[0] == 'O' and self.boardRow2[1] == 'O' and self.boardRow3[2] == 'O':
            self.player1Wins += 1
            self.player2Loss += 1
            self.TotalGamesPlayed += 1
            self.resetGameBoard()
            self.Turn = False
            return 'O'
        elif self.boardRow1[2] == 'O' and self.boardRow2[1] == 'O' and self.boardRow3[0] == 'O':
            self.player1Wins += 1
            self.player2Loss += 1
            self.TotalGamesPlayed += 1
            self.resetGameBoard()
            self.Turn = False
            return 'O'
        else:
            if self.Board_Full == True:
                self.TotalNumTies += 1
                self.TotalGamesPlayed += 1
                self.resetGameBoard()
                return 'Tie'
            else:
                return 'P'
    def computeStats(self): #Gathers and returns:Usernames of both players,username of last person to move,number of games,number of w,number of L,number of ties
        if self.Turn == True: #player 2 last turn
            self.LastPlayerName = self.Player2Name
            self.stats = ['player1', self.Player2Name, self.LastPlayerName, self.TotalGamesPlayed, self.player1Wins, self.player2Wins, self.TotalNumTies]
            return self.stats
        elif self.Turn == False: #player 1 last turn
            self.LastPlayerName = self.Player1Name
            self.stats = ['player1', self.Player2Name, self.LastPlayerName, self.TotalGamesPlayed, self.player1Wins, self.player2Wins, self.TotalNumTies]
            return self.stats
            # return [player1, player2, last player to move, num games, num of w, num Ls, num ties]