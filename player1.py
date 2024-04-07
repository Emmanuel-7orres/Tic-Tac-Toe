import socket
import gameboard as Board
import tkinter as tk
from tkinter import messagebox
from tkinter.constants import RAISED

class playgame():
    def __init__(self):
        self.game = Board.gameboard()
        self.BoardFull = False
        self.game.Click = False
        self.Turn = False #False = player 2 turn, true is player 1 turn
        self.getPlayer2info = True
        self.playerData = 0
        self.player2data = 0
        self.player2Name = ''
        self.player2Connected = False
        self.firstMove = False

        #call my method to create canvas and add widgets
        self.BoardSetup()
        self.Server = tk.StringVar()
        self.Port = tk.IntVar()
        self.Serv = tk.StringVar()
        self.Por = tk.StringVar()
        self.createButton1()
        self.createButton2()
        self.createButton3()
        self.createButton4()
        self.createButton5()
        self.createButton6()
        self.createButton7()
        self.createButton8()
        self.createButton9()
        self.getServerInfo()
        self.createPlayButton()
        self.createQuitButton()
        self.runUI()


    def getServerInfo(self):
        self.newFrame = tk.Frame(self.Board)

        self.Serv.set('Enter Server Address')
        self.addressEntryLabel = tk.Label(self.newFrame, textvariable=self.Serv, relief=RAISED).pack()
        self.addressEntry = tk.Entry(self.newFrame, text=self.Serv, textvariable=self.Server).pack()

        self.Por.set('Enter Port')
        self.portEntryLabel = tk.Label(self.newFrame, textvariable=self.Por, relief=RAISED).pack()
        self.portEntry = tk.Entry(self.newFrame, text=self.Por, textvariable=self.Port).pack()

        self.newFrame.grid(row = 0, column = 3)
        
    def startServer(self):
        messagebox.showinfo('Server Started!', 'Wait for Player 2 To Connect')
        self.Address = self.Server.get()
        self.PortNum = self.Port.get()
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.bind((self.Address, self.PortNum))
        self.serverSocket.listen(1)
        self.clientSocket,self.clientAddress = self.serverSocket.accept()
        self.getInfo()
        self.updateinfo()
        messagebox.showinfo('Connected!', 'Wait for ' +  self.player2Name + '\'s Move!')
        #self.disableButtons()
        self.clientSocket.send(b'player1')
        self.getInfo()
        self.player2Connected = True #Makes it so that player 1 has to wait for player 2 by messagebox while its False

    def getInfo(self):
        self.playerData = self.clientSocket.recv(1024)
        self.player2data = self.playerData.decode('ascii')
        self.clientInfo(self.player2data)
        
    def updateinfo(self):
        self.stats = self.game.computeStats() 
        self.stats = [str(x) for x in self.stats]
        self.playerTurn = self.updateturn()
        self.stats = 'Turn: ' + self.playerTurn + '\n' + 'Players: ' + self.stats[0] + ', ' + self.stats[1] + '\n' + 'Last Player to move: ' + self.stats[2] + '\n' + 'Total games played: ' + self.stats[3] + '\n' + 'Wins: ' + self.stats[4] + '\n' + 'Losses: ' + self.stats[5] + '\n' + 'Ties: ' + self.stats[6]
        self.Play = tk.Label(self.Board, text=self.stats).grid(row = 1, column = 3)
        self.Board.update()

    def updateturn(self):
        if self.Turn == False: 
            self.playerTurn = self.player2Name
        else:
            self.playerTurn = 'player1'
        return self.playerTurn
            
    def BoardSetup(self):
        self.Board = tk.Tk()
        self.Board.title("Tic Tac Toe- Player 1") #set window title
        self.Board.resizable(0,0)#setting the x and y to be/not be resizable
    def runUI(self):
        self.Board.mainloop()

    def createPlayButton(self):
        self.Play = tk.Button(self.Board, text = 'Play', height = 12, width = 24, command = self.startServer).grid(row = 1, column = 3)
    def createButton1(self):
        self.Button1 = tk.Button(self.Board, text = "", height = 12, width = 24, command = self.buttonClick1).grid(row = 0, column = 0)
    def createButton2(self):
        self.Button2 = tk.Button(self.Board, text = "", height = 12, width = 24, command = self.buttonClick2).grid(row = 0, column = 1)
    def createButton3(self):
        self.Button3 = tk.Button(self.Board, text = "", height = 12, width = 24, command = self.buttonClick3).grid(row = 0, column = 2)
    def createButton4(self):
        self.Button4 = tk.Button(self.Board, text = "", height = 12, width = 24, command = self.buttonClick4).grid(row = 1, column = 0)
    def createButton5(self):
        self.Button5 = tk.Button(self.Board, text = "", height = 12, width = 24, command = self.buttonClick5).grid(row = 1, column = 1)
    def createButton6(self):
        self.Button6 = tk.Button(self.Board, text = "", height = 12, width = 24, command = self.buttonClick6).grid(row = 1, column = 2)
    def createButton7(self):
        self.Button7 = tk.Button(self.Board, text = "", height = 12, width = 24, command = self.buttonClick7).grid(row = 2, column = 0)
    def createButton8(self):
        self.Button8 = tk.Button(self.Board, text = "", height = 12, width = 24, command = self.buttonClick8).grid(row = 2, column = 1)
    def createButton9(self):
        self.Button9 = tk.Button(self.Board, text = "", height = 12, width = 24, command = self.buttonClick9).grid(row = 2, column = 2)
    def createQuitButton(self):
        self.quitButton = tk.Button(self.Board, text = 'Quit', height = 12, width = 24, command = self.quitgame).grid(row = 2, column = 3)

    def clientInfo(self, player2data):
        print(player2data)
        if player2data == '1':
            self.Button1 = tk.Button(self.Board, text = "X", height = 12, width = 24, command = self.buttonClick1).grid(row = 0, column = 0)
            self.game.boardRow1[0] = 'X'
            #self.enableButtons()
            self.Turn = True
            self.updateinfo()
            if self.firstMove == True: #
                self.firstMove = False
            else:
                self.WinLoseTie()
        elif player2data == '2':
            self.Button2 = tk.Button(self.Board, text = "X", height = 12, width = 24, command = self.buttonClick2).grid(row = 0, column = 1)
            self.game.boardRow1[1] = 'X'
            #self.enableButtons()
            self.updateinfo()
            self.Turn = True
            if self.firstMove == True: #
                self.firstMove = False
            else:
                self.WinLoseTie()
        elif player2data == '3':
            self.Button3 = tk.Button(self.Board, text = "X", height = 12, width = 24, command = self.buttonClick3).grid(row = 0, column = 2)
            self.game.boardRow1[2] = 'X'
            #self.enableButtons()
            self.Turn = True
            self.updateinfo()
            if self.firstMove == True: #
                self.firstMove = False
            else:
                self.WinLoseTie()
        elif player2data == '4':
            self.Button4 = tk.Button(self.Board, text = "X", height = 12, width = 24, command = self.buttonClick4).grid(row = 1, column = 0)
            self.game.boardRow2[0] = 'X'
            #self.enableButtons()
            self.Turn = True
            self.updateinfo()
            if self.firstMove == True: #
                self.firstMove = False
            else:
                self.WinLoseTie()
        elif player2data == '5':
            self.Button5 = tk.Button(self.Board, text = "X", height = 12, width = 24, command = self.buttonClick5).grid(row = 1, column = 1)
            self.game.boardRow2[1] = 'X'
            #self.enableButtons()
            self.Turn = True
            self.updateinfo()
            if self.firstMove == True: #
                self.firstMove = False
            else:
                self.WinLoseTie()
        elif player2data == '6':
            self.Button6 = tk.Button(self.Board, text = "X", height = 12, width = 24, command = self.buttonClick6).grid(row = 1, column = 2)
            self.game.boardRow2[2] = 'X'
            #self.enableButtons()
            self.Turn = True
            self.updateinfo()
            if self.firstMove == True: #
                self.firstMove = False
            else:
                self.WinLoseTie()
        elif player2data == '7':
            self.Button7 = tk.Button(self.Board, text = "X", height = 12, width = 24, command = self.buttonClick7).grid(row = 2, column = 0)
            self.game.boardRow3[0] = 'X'
            #self.enableButtons()
            self.Turn = True
            self.updateinfo()
            if self.firstMove == True: #
                self.firstMove = False
            else:
                self.WinLoseTie()
        elif player2data == '8':
            self.Button8 = tk.Button(self.Board, text = "X", height = 12, width = 24, command = self.buttonClick8).grid(row = 2, column = 1)
            self.game.boardRow3[1] = 'X'
            #self.enableButtons()
            self.Turn = True
            self.updateinfo()
            if self.firstMove == True: #
                self.firstMove = False
            else:
                self.WinLoseTie()
        elif player2data == '9':
            self.Button9 = tk.Button(self.Board, text = "X", height = 12, width = 24, command = self.buttonClick9).grid(row = 2, column = 2)
            self.game.boardRow3[2] = 'X'
            #self.enableButtons()
            self.Turn = True
            self.updateinfo()
            if self.firstMove == True: #
                self.firstMove = False
            else:
                self.WinLoseTie()
        elif player2data == 'y': #restart game and board and keep count of who won/lost
            self.resetBoard()
            #self.disableButtons()
            print(self.game.boardRow1)
            print(self.game.boardRow2)
            print(self.game.boardRow3)
            self.firstMove = True
            self.Turn = False
            self.updateinfo()
            self.getInfo()
        elif player2data == 'n': #end game and print stats
            self.stats = self.game.computeStats() 
            self.stats = [str(x) for x in self.stats]
            self.stats = 'Players: '+ self.stats[0] + ', ' + self.stats[1] + '\n' + 'Last Player to move: ' + self.stats[2] + '\n' + 'Total games played: ' + self.stats[3] + '\n' + 'Wins: ' + self.stats[4] + '\n' + 'Losses: ' + self.stats[5] + '\n' + 'Ties: ' + self.stats[6]
            print(self.stats)
            messagebox.showinfo('player1 Stats', self.stats)
            self.Board.destroy()
        else:
            self.player2Name = player2data
            self.game.Player2Name = self.player2Name

    def WinLoseTie(self):
        self.fullBoard = self.game.isBoardFull() #returns true(board is full), or False(board not full)
        if self.fullBoard == False:
            self.gameOver = self.game.isGameFinished() #returns X or O for who won and Tie for a tie
            if self.gameOver == 'X' or self.gameOver == 'O' or self.gameOver == 'Tie':
                self.recieveInfo = False
                self.result(self.gameOver)
            else:
                self.recieveInfo = True
        elif self.fullBoard == True:
            self.gameOver = self.game.isGameFinished() #returns X or O for who won and Tie for a tie
            if self.gameOver == 'X' or self.gameOver == 'O' or self.gameOver == 'Tie':
                self.recieveInfo = False
                self.result(self.gameOver)#crashing after player a few games, this function could be the issue., trying  to double recieve

    def result(self, result):
        if self.fullBoard == False and result == 'X':
            self.updateinfo()
            messagebox.showinfo('The Winner is:', self.player2Name)
            self.getInfo()
        elif self.fullBoard == False and result == 'O':
            self.updateinfo()
            messagebox.showinfo('The Winner is:', 'player1')
            self.getInfo()
        elif self.fullBoard == True and result == 'X':
            self.updateinfo()
            messagebox.showinfo('The Winner is:', self.player2Name)
            self.getInfo()
        elif self.fullBoard == True and result == 'O':
            self.updateinfo()
            messagebox.showinfo('The Winner is:', 'player1')
            self.getInfo()
        elif self.fullBoard == True and result == 'Tie':
            self.updateinfo()
            messagebox.showinfo('Draw!', 'Game ended in a Draw')
            self.getInfo()

    def quitgame(self):
        self.clientSocket.send(b'q')
        self.stats = self.game.computeStats() 
        self.stats = [str(x) for x in self.stats]
        self.stats = 'Players: '+ self.stats[0] + ', ' + self.stats[1] + '\n' + 'Last Player to move: ' + self.stats[2] + '\n' + 'Total games played: ' + self.stats[3] + '\n' + 'Wins: ' + self.stats[4] + '\n' + 'Losses: ' + self.stats[5] + '\n' + 'Ties: ' + self.stats[6]
        messagebox.showinfo('player1 Stats', self.stats)
        self.Board.destroy()

    def resetBoard(self):
        self.Button1 = tk.Button(self.Board, text = "", height = 12, width = 24, command = self.buttonClick1).grid(row = 0, column = 0)
        self.Button2 = tk.Button(self.Board, text = "", height = 12, width = 24, command = self.buttonClick2).grid(row = 0, column = 1)
        self.Button3 = tk.Button(self.Board, text = "", height = 12, width = 24, command = self.buttonClick3).grid(row = 0, column = 2)
        self.Button4 = tk.Button(self.Board, text = "", height = 12, width = 24, command = self.buttonClick4).grid(row = 1, column = 0)
        self.Button5 = tk.Button(self.Board, text = "", height = 12, width = 24, command = self.buttonClick5).grid(row = 1, column = 1)
        self.Button6 = tk.Button(self.Board, text = "", height = 12, width = 24, command = self.buttonClick6).grid(row = 1, column = 2)
        self.Button7 = tk.Button(self.Board, text = "", height = 12, width = 24, command = self.buttonClick7).grid(row = 2, column = 0)
        self.Button8 = tk.Button(self.Board, text = "", height = 12, width = 24, command = self.buttonClick8).grid(row = 2, column = 1)
        self.Button9 = tk.Button(self.Board, text = "", height = 12, width = 24, command = self.buttonClick9).grid(row = 2, column = 2)
        self.Board.update()
    

    def buttonClick1(self):
        if self.Turn == False and self.game.boardRow1[0] == '':
            messagebox.showwarning('No Cheating!', 'Its not your turn!')
        else:
            if self.game.boardRow1[0] == 'X' or self.game.boardRow1[0] == 'O':
                self.recieveInfo = False
                messagebox.showwarning('No Cheating!', "Select an open box please")
            elif self.player2Connected == False:
                messagebox.showwarning('Wait!', "Input Server Address and Port then Wait for Player 2")
            else:
                self.Button1 = tk.Button(self.Board, text = "O", height = 12, width = 24, command = self.buttonClick1).grid(row = 0, column = 0)
                self.Turn = False
                self.updateinfo()
                self.clientSocket.send(b'1')
                self.game.boardRow1[0] = 'O'
                #self.disableButtons()
                self.WinLoseTie()
            if self.recieveInfo != False:
                self.getInfo()

    def buttonClick2(self):
        if self.Turn == False and self.game.boardRow1[1] == '':
            messagebox.showwarning('No Cheating!', 'Its not your turn!')
        else:
            if self.game.boardRow1[1] == 'X' or self.game.boardRow1[1] == 'O':
                self.recieveInfo = False
                messagebox.showwarning('No Cheating!', "Select an open box please")
            elif self.player2Connected == False:
                messagebox.showwarning('Wait!', "Input Server Address and Port then Wait for Player 2")
            else:
                self.Button2 = tk.Button(self.Board, text = "O", height = 12, width = 24, command = self.buttonClick2).grid(row = 0, column = 1)
                self.Turn = False
                self.updateinfo()
                self.clientSocket.send(b'2')
                self.game.boardRow1[1] = 'O'
                #self.disableButtons()
                self.WinLoseTie()
            if self.recieveInfo != False:
                self.getInfo()

    def buttonClick3(self):
        if self.Turn == False and self.game.boardRow1[2] == '':
            messagebox.showwarning('No Cheating!', 'Its not your turn!')
        else:
            if self.game.boardRow1[2] == 'X' or self.game.boardRow1[2] == 'O':
                self.recieveInfo = False
                messagebox.showwarning('No Cheating!', "Select an open box please")
            elif self.player2Connected == False:
                messagebox.showwarning('Wait!', "Input Server Address and Port then Wait for Player 2")
            else:
                self.Button3 = tk.Button(self.Board, text = "O", height = 12, width = 24, command = self.buttonClick3).grid(row = 0, column = 2)
                self.Turn = False
                self.updateinfo()
                self.clientSocket.send(b'3')
                self.game.boardRow1[2] = 'O'
                #self.disableButtons()
                self.WinLoseTie()
            if self.recieveInfo != False:
                self.getInfo()

    def buttonClick4(self):
        if self.Turn == False and self.game.boardRow2[0] == '':
            messagebox.showwarning('No Cheating!', 'Its not your turn!')
        else:
            if self.game.boardRow2[0] == 'X' or self.game.boardRow2[0] == 'O':
                self.recieveInfo = False
                messagebox.showwarning('No Cheating!', "Select an open box please")
            elif self.player2Connected == False:
                messagebox.showwarning('Wait!', "Input Server Address and Port then Wait for Player 2")
            else:
                self.Button4 = tk.Button(self.Board, text = "O", height = 12, width = 24, command = self.buttonClick4).grid(row = 1, column = 0)
                self.Turn = False
                self.updateinfo()
                self.clientSocket.send(b'4')
                self.game.boardRow2[0] = 'O'
                #self.disableButtons()
                self.WinLoseTie()
            if self.recieveInfo != False:
                self.getInfo()

    def buttonClick5(self):
        if self.Turn == False and self.game.boardRow2[1] == '':
            messagebox.showwarning('No Cheating!', 'Its not your turn!')
        else:
            if self.game.boardRow2[1] == 'X' or self.game.boardRow2[1] == 'O':
                self.recieveInfo = False
                messagebox.showwarning('No Cheating!', "Select an open box please")
            elif self.player2Connected == False:
                messagebox.showwarning('Wait!', "Input Server Address and Port then Wait for Player 2")      
            else:
                self.Button5 = tk.Button(self.Board, text = "O", height = 12, width = 24, command = self.buttonClick5).grid(row = 1, column = 1)
                self.Turn = False
                self.updateinfo()
                self.clientSocket.send(b'5')
                self.game.boardRow2[1] = 'O'
                #self.disableButtons()
                self.WinLoseTie()
            if self.recieveInfo != False:
                self.getInfo()

    def buttonClick6(self):
        if self.Turn == False and self.game.boardRow2[2] == '':
            messagebox.showwarning('No Cheating!', 'Its not your turn!')
        else:
            if self.game.boardRow2[2] == 'X' or self.game.boardRow2[2] == 'O':
                self.recieveInfo = False
                messagebox.showwarning('No Cheating!', "Select an open box please")
            elif self.player2Connected == False:
                messagebox.showwarning('Wait!', "Input Server Address and Port then Wait for Player 2")
            else:
                self.Button6 = tk.Button(self.Board, text = "O", height = 12, width = 24, command = self.buttonClick6).grid(row = 1, column = 2)
                self.Turn = False
                self.updateinfo()
                self.clientSocket.send(b'6')
                self.game.boardRow2[2] = 'O'
                #self.disableButtons()
                self.WinLoseTie()
            if self.recieveInfo != False:
                self.getInfo()

    def buttonClick7(self):
        if self.Turn == False and self.game.boardRow3[0] == '':
            messagebox.showwarning('No Cheating!', 'Its not your turn!')
        else:
            if self.game.boardRow3[0] == 'X' or self.game.boardRow3[0] == 'O':
                self.recieveInfo = False
                messagebox.showwarning('No Cheating!', "Select an open box please")
            elif self.player2Connected == False:
                messagebox.showwarning('Wait!', "Input Server Address and Port then Wait for Player 2")
            else:
                self.Button7 = tk.Button(self.Board, text = "O", height = 12, width = 24, command = self.buttonClick7).grid(row = 2, column = 0)
                self.Turn = False
                self.updateinfo()
                self.clientSocket.send(b'7')
                self.game.boardRow3[0] = 'O'
                #self.disableButtons()
                self.WinLoseTie()
            if self.recieveInfo != False:
                self.getInfo()

    def buttonClick8(self):
        if self.Turn == False and self.game.boardRow3[1] == '':
            messagebox.showwarning('No Cheating!', 'Its not your turn!')
        else:
            if self.game.boardRow3[1] == 'X' or self.game.boardRow3[1] == 'O':
                self.recieveInfo = False
                messagebox.showwarning('No Cheating!', "Select an open box please")
            elif self.player2Connected == False:
                messagebox.showwarning('Wait!', "Input Server Address and Port then Wait for Player 2")
            else:
                self.Button8 = tk.Button(self.Board, text = "O", height = 12, width = 24, command = self.buttonClick8).grid(row = 2, column = 1)
                self.Turn = False
                self.updateinfo()
                self.clientSocket.send(b'8')
                self.game.boardRow3[1] = 'O'
                #self.disableButtons()
                self.WinLoseTie()
            if self.recieveInfo != False:
                self.getInfo()

    def buttonClick9(self):
        if self.Turn == False and self.game.boardRow3[2] == '':
            messagebox.showwarning('No Cheating!', 'Its not your turn!')
        else:
            if self.game.boardRow3[2] == 'X' or self.game.boardRow3[2] == 'O':
                self.recieveInfo = False
                messagebox.showwarning('No Cheating!', "Select an open box please")
            elif self.player2Connected == False:
                messagebox.showwarning('Wait!', "Input Server Address and Port then Wait for Player 2")
            else:
                self.Button9 = tk.Button(self.Board, text = "O", height = 12, width = 24, command = self.buttonClick9).grid(row = 2, column = 2)
                self.Turn = False
                self.updateinfo()
                self.clientSocket.send(b'9')
                self.game.boardRow3[2] = 'O'
                #self.disableButtons()
                self.WinLoseTie()
            if self.recieveInfo != False:
                self.getInfo()

    def disableButtons(self):
        self.Button1['state'] = tk.DISABLED
        self.Button2['state'] = tk.DISABLED
        self.Button3['state'] = tk.DISABLED
        self.Button4['state'] = tk.DISABLED
        self.Button5['state'] = tk.DISABLED
        self.Button6['state'] = tk.DISABLED
        self.Button7['state'] = tk.DISABLED
        self.Button8['state'] = tk.DISABLED
        self.Button9['state'] = tk.DISABLED
        self.Board.update()

    def enableButtons(self):
        self.Button1['state'] = tk.NORMAL
        self.Button2['state'] = tk.NORMAL
        self.Button3['state'] = tk.NORMAL
        self.Button4['state'] = tk.NORMAL
        self.Button5['state'] = tk.NORMAL
        self.Button6['state'] = tk.NORMAL
        self.Button7['state'] = tk.NORMAL
        self.Button8['state'] = tk.NORMAL
        self.Button9['state'] = tk.NORMAL
        self.Board.update()

run = playgame()