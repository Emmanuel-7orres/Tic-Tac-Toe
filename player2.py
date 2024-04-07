import socket
import gameboard as Board
import tkinter as tk
from tkinter import messagebox
from tkinter.constants import NORMAL, RAISED

class playgame():
    def __init__(self):
        self.game = Board.gameboard()
        self.getPlayer1info = True
        self.game.Click = True
        self.BoardFull = False
        self.connectionCounter = 0
        self.serverData = 0
        self.player1data = 0
        self.player1Connected = False
        self.Turn = True

        #call my method to create canvas and add widgets
        self.BoardSetup()
        self.Server = tk.StringVar()
        self.Port = tk.IntVar()
        self.Serv = tk.StringVar()
        self.Por = tk.StringVar()
        self.player2Name = tk.StringVar()
        self.player2N = tk.StringVar()
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

        self.player2Name.set('Name')
        self.NameEntryLabel = tk.Label(self.newFrame, textvariable=self.player2Name, relief=RAISED).pack()
        self.NameEntry = tk.Entry(self.newFrame, textvariable=self.player2N).pack()

        self.Serv.set('Enter Server Address')
        self.addressEntryLabel = tk.Label(self.newFrame, textvariable=self.Serv, relief=RAISED).pack()
        self.addressEntry = tk.Entry(self.newFrame, textvariable=self.Server).pack()

        self.Por.set('Enter Port')
        self.portEntryLabel = tk.Label(self.newFrame, textvariable=self.Por, relief=RAISED).pack()
        self.portEntry = tk.Entry(self.newFrame, text=self.Por, textvariable=self.Port).pack()

        self.newFrame.grid(row = 0, column = 3)

    def connectToServer(self):
        self.Address = self.Server.get()
        self.PortNum = self.Port.get()
        self.PlayerName = self.player2N.get() #
        self.game.Player2Name = self.PlayerName
        self.connectionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.connectionSocket.connect((self.Address, self.PortNum))
            self.connectionSocket.send(bytes(self.PlayerName, 'ascii'))
            self.getInfo()
            self.updateinfo()
            messagebox.showinfo('Connection Success!', self.PlayerName + '\'s Move!')
            self.player1Connected = True #Makes it so that player 1 has to wait for player 2 by messagebox while its False
        except (ConnectionRefusedError, TimeoutError, OSError):
            self.retry()
            
    def retry(self):
        self.response = messagebox.askquestion('Connection Failed!', 'Do you want to try inputting IP and Port again?')
        if self.response == 'yes':
            messagebox.showinfo('Input IP and Port then press Play', 'Input IP and Port then press Play')
        else:
            self.stats = self.game.computeStats() 
            self.stats = [str(x) for x in self.stats]
            self.stats = 'Players: '+ self.stats[0] + ', ' + self.PlayerName + '\n' + 'Last Player to move: ' + self.stats[2] + '\n' + 'Total games played: ' + self.stats[3] + '\n' + 'Wins: ' + self.stats[5] + '\n' + 'Losses: ' + self.stats[4] + '\n' + 'Ties: ' + self.stats[6]
            messagebox.showinfo(self.PlayerName + ' Stats', self.stats)
            self.Board.destroy()

    def getInfo(self):
        self.serverData = self.connectionSocket.recv(1024)
        self.player1data = self.serverData.decode('ascii')
        self.serverInfo(self.player1data)
        
    def updateinfo(self):
        self.stats = self.game.computeStats() 
        self.stats = [str(x) for x in self.stats]
        self.playerTurn = self.updateturn()
        self.stats = 'Turn: ' + self.playerTurn + '\n' + 'Players: '+ self.stats[0] + ', ' + self.PlayerName + '\n' + 'Last Player to move: ' + self.stats[2] + '\n' + 'Total games played: ' + self.stats[3] + '\n' + 'Wins: ' + self.stats[5] + '\n' + 'Losses: ' + self.stats[4] + '\n' + 'Ties: ' + self.stats[6]
        self.Play = tk.Label(self.Board, text=self.stats).grid(row = 1, column = 3)
        self.Board.update()
    
    def updateturn(self):
        if self.Turn == True:
            self.playerTurn = self.PlayerName
        else:
            self.playerTurn = 'player1'
        return self.playerTurn

    def BoardSetup(self):
        self.Board = tk.Tk()
        self.Board.title("Tic Tac Toe- Player 2") #set window title
        self.Board.resizable(0,0)#setting the x and y to be/not be resizable

    def runUI(self):
        self.Board.mainloop()

    def createPlayButton(self):
        self.Play = tk.Button(self.Board, text = 'Play', height = 12, width = 24, command = self.connectToServer).grid(row = 1, column = 3)
    def createButton1(self):
        self.Button1 = tk.Button(self.Board, text = "", height = 12, width = 24, command = self.buttonClick1, state = NORMAL).grid(row = 0, column = 0)
    def createButton2(self):
        self.Button2 = tk.Button(self.Board, text = "", height = 12, width = 24, command = self.buttonClick2, state = NORMAL).grid(row = 0, column = 1)
    def createButton3(self):
        self.Button3 = tk.Button(self.Board, text = "", height = 12, width = 24, command = self.buttonClick3, state = NORMAL).grid(row = 0, column = 2)
    def createButton4(self):
        self.Button4 = tk.Button(self.Board, text = "", height = 12, width = 24, command = self.buttonClick4, state = NORMAL).grid(row = 1, column = 0)
    def createButton5(self):
        self.Button5 = tk.Button(self.Board, text = "", height = 12, width = 24, command = self.buttonClick5, state = NORMAL).grid(row = 1, column = 1)
    def createButton6(self):
        self.Button6 = tk.Button(self.Board, text = "", height = 12, width = 24, command = self.buttonClick6, state = NORMAL).grid(row = 1, column = 2)
    def createButton7(self):
        self.Button7 = tk.Button(self.Board, text = "", height = 12, width = 24, command = self.buttonClick7, state = NORMAL).grid(row = 2, column = 0)
    def createButton8(self):
        self.Button8 = tk.Button(self.Board, text = "", height = 12, width = 24, command = self.buttonClick8, state = NORMAL).grid(row = 2, column = 1)
    def createButton9(self):
        self.Button9 = tk.Button(self.Board, text = "", height = 12, width = 24, command = self.buttonClick9, state = NORMAL).grid(row = 2, column = 2)
    def createQuitButton(self):
        self.quitButton = tk.Button(self.Board, text = 'Quit', height = 12, width = 24, command = self.quitgame).grid(row = 2, column = 3)

    def serverInfo(self, player1data):
        print(player1data)
        if player1data == '1':
            self.Button1 = tk.Button(self.Board, text = "O", height = 12, width = 24, command = self.buttonClick1).grid(row = 0, column = 0)
            self.game.boardRow1[0] = 'O'
            #self.enableButtons()
            self.Turn = True
            self.updateinfo()
            self.WinLoseTie()
        elif player1data == '2':
            #self.enableButtons()
            self.Button2 = tk.Button(self.Board, text = "O", height = 12, width = 24, command = self.buttonClick2).grid(row = 0, column = 1)
            self.game.boardRow1[1] = 'O'
            self.Turn = True
            self.updateinfo()
            self.WinLoseTie()
        elif player1data == '3':
            self.Button3 = tk.Button(self.Board, text = "O", height = 12, width = 24, command = self.buttonClick3).grid(row = 0, column = 2)
            self.game.boardRow1[2] = 'O'
            #self.enableButtons()
            self.Turn = True
            self.updateinfo()
            self.WinLoseTie()
        elif player1data == '4':
            self.Button4 = tk.Button(self.Board, text = "O", height = 12, width = 24, command = self.buttonClick4).grid(row = 1, column = 0)
            self.game.boardRow2[0] = 'O'
            #self.enableButtons()
            self.Turn = True
            self.updateinfo()
            self.WinLoseTie()
        elif player1data == '5':
            self.Button5 = tk.Button(self.Board, text = "O", height = 12, width = 24, command = self.buttonClick5).grid(row = 1, column = 1)
            self.game.boardRow2[1] = 'O'
            #self.enableButtons()
            self.Turn = True
            self.updateinfo()
            self.WinLoseTie()
        elif player1data == '6':
            self.Button6 = tk.Button(self.Board, text = "O", height = 12, width = 24, command = self.buttonClick6).grid(row = 1, column = 2)
            self.game.boardRow2[2] = 'O'
            #self.enableButtons()
            self.Turn = True
            self.updateinfo()
            self.WinLoseTie()
        elif player1data == '7':
            self.Button7 = tk.Button(self.Board, text = "O", height = 12, width = 24, command = self.buttonClick7).grid(row = 2, column = 0)
            self.game.boardRow3[0] = 'O'
            #self.enableButtons()
            self.Turn = True
            self.updateinfo()
            self.WinLoseTie()
        elif player1data == '8':
            self.Button8 = tk.Button(self.Board, text = "O", height = 12, width = 24, command = self.buttonClick8).grid(row = 2, column = 1)
            self.game.boardRow3[1] = 'O'
            #self.enableButtons()
            self.Turn = True
            self.updateinfo()
            self.WinLoseTie()
        elif player1data == '9':
            self.Button9 = tk.Button(self.Board, text = "O", height = 12, width = 24, command = self.buttonClick9).grid(row = 2, column = 2)
            self.game.boardRow3[2] = 'O'
            #self.enableButtons()
            self.Turn = True
            self.updateinfo()
            self.WinLoseTie()
        elif player1data == 'q':
            self.stats = self.game.computeStats() 
            self.stats = [str(x) for x in self.stats]
            self.stats = 'Players: '+ self.stats[0] + ', ' + self.PlayerName + '\n' + 'Last Player to move: ' + self.stats[2] + '\n' + 'Total games played: ' + self.stats[3] + '\n' + 'Wins: ' + self.stats[5] + '\n' + 'Losses: ' + self.stats[4] + '\n' + 'Ties: ' + self.stats[6]
            messagebox.showinfo(self.PlayerName + ' Stats', self.stats)
            self.Board.destroy()
        else:
            self.player1Name = player1data


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
                self.result(self.gameOver)

    def result(self, result):
        if self.fullBoard == False and result == 'X':
            messagebox.showinfo('The Winner is:', self.PlayerName)
            self.updateinfo()
            self.YesNo()
        elif self.fullBoard == False and result == 'O':
            messagebox.showinfo('The Winner is:', 'player1')
            self.updateinfo()
            self.YesNo()
        elif self.fullBoard == True and result == 'X':
            messagebox.showinfo('The Winner is:', self.PlayerName)
            self.updateinfo()
            self.YesNo()
        elif self.fullBoard == True and result == 'O':
            messagebox.showinfo('The Winner is:', 'player1')
            self.updateinfo()
            self.YesNo()
        elif self.fullBoard == True and result == 'Tie':
            messagebox.showinfo('Draw!', 'Game ended in a Draw')
            self.updateinfo()
            self.YesNo()

    def YesNo(self):
        self.response = messagebox.askquestion('Go Agane?', 'Do you want to play again?')
        if self.response == 'yes':
            self.connectionSocket.send(b'y')
            self.resetBoard()
            #self.enableButtons()
            self.Turn = True
            self.updateinfo()
        else:
            self.connectionSocket.send(b'n')
            self.stats = self.game.computeStats() 
            self.stats = [str(x) for x in self.stats]
            self.stats = 'Players: '+ self.stats[0] + ', ' + self.PlayerName + '\n' + 'Last Player to move: ' + self.stats[2] + '\n' + 'Total games played: ' + self.stats[3] + '\n' + 'Wins: ' + self.stats[5] + '\n' + 'Losses: ' + self.stats[4] + '\n' + 'Ties: ' + self.stats[6]
            messagebox.showinfo(self.PlayerName + ' Stats', self.stats)
            self.Board.destroy()

    def quitgame(self):
        self.connectionSocket.send(b'n')
        self.stats = self.game.computeStats() 
        self.stats = [str(x) for x in self.stats]
        self.stats = 'Players: '+ self.stats[0] + ', ' + self.PlayerName + '\n' + 'Last Player to move: ' + self.stats[2] + '\n' + 'Total games played: ' + self.stats[3] + '\n' + 'Wins: ' + self.stats[5] + '\n' + 'Losses: ' + self.stats[4] + '\n' + 'Ties: ' + self.stats[6]
        messagebox.showinfo(self.PlayerName + ' Stats', self.stats)
        self.Board.destroy()

    def resetBoard(self):
        self.Button1 = tk.Button(self.Board, text = "", height = 12, width = 24, command = self.buttonClick1, state = NORMAL).grid(row = 0, column = 0)
        self.Button2 = tk.Button(self.Board, text = "", height = 12, width = 24, command = self.buttonClick2, state = NORMAL).grid(row = 0, column = 1)
        self.Button3 = tk.Button(self.Board, text = "", height = 12, width = 24, command = self.buttonClick3, state = NORMAL).grid(row = 0, column = 2)
        self.Button4 = tk.Button(self.Board, text = "", height = 12, width = 24, command = self.buttonClick4, state = NORMAL).grid(row = 1, column = 0)
        self.Button5 = tk.Button(self.Board, text = "", height = 12, width = 24, command = self.buttonClick5, state = NORMAL).grid(row = 1, column = 1)
        self.Button6 = tk.Button(self.Board, text = "", height = 12, width = 24, command = self.buttonClick6, state = NORMAL).grid(row = 1, column = 2)
        self.Button7 = tk.Button(self.Board, text = "", height = 12, width = 24, command = self.buttonClick7, state = NORMAL).grid(row = 2, column = 0)
        self.Button8 = tk.Button(self.Board, text = "", height = 12, width = 24, command = self.buttonClick8, state = NORMAL).grid(row = 2, column = 1)
        self.Button9 = tk.Button(self.Board, text = "", height = 12, width = 24, command = self.buttonClick9, state = NORMAL).grid(row = 2, column = 2)
        self.Board.update()

    def buttonClick1(self):
        if self.Turn == False and self.game.boardRow1[0] == '':
            messagebox.showwarning('No Cheating!', 'Its not your turn!')
        else:
            if self.game.boardRow1[0] == 'X' or self.game.boardRow1[0] == 'O':
                self.recieveInfo = False
                messagebox.showwarning('No Cheating!', "Select an open box please")
            elif self.player1Connected == False:
                messagebox.showwarning('Wait!', "Input Server Address and Port to Start")
            else:
                self.Button1 = tk.Button(self.Board, text = "X", height = 12, width = 24, command = self.buttonClick1).grid(row = 0, column = 0)
                self.Turn = False
                self.updateinfo()
                self.connectionSocket.send(b'1')
                self.game.boardRow1[0] = 'X'
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
            elif self.player1Connected == False:
                messagebox.showwarning('Wait!', "Input Server Address and Port to Start")
            else:
                self.Button2 = tk.Button(self.Board, text = "X", height = 12, width = 24, command = self.buttonClick2).grid(row = 0, column = 1)
                self.Turn = False
                self.updateinfo()
                self.connectionSocket.send(b'2')
                self.game.boardRow1[1] = 'X'
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
            elif self.player1Connected == False:
                messagebox.showwarning('Wait!', "Input Server Address and Port to Start")
            else:
                self.Button3 = tk.Button(self.Board, text = "X", height = 12, width = 24, command = self.buttonClick3).grid(row = 0, column = 2)
                self.Turn = False
                self.updateinfo()
                self.connectionSocket.send(b'3')
                self.game.boardRow1[2] = 'X'
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
            elif self.player1Connected == False:
                messagebox.showwarning('Wait!', "Input Server Address and Port to Start")
            else:
                self.Button4 = tk.Button(self.Board, text = "X", height = 12, width = 24, command = self.buttonClick4).grid(row = 1, column = 0)
                self.Turn = False
                self.updateinfo()
                self.connectionSocket.send(b'4')
                self.game.boardRow2[0] = 'X'
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
            elif self.player1Connected == False:
                messagebox.showwarning('Wait!', "Input Server Address and Port to Start")
            
            else:
                self.Button5 = tk.Button(self.Board, text = "X", height = 12, width = 24, command = self.buttonClick5).grid(row = 1, column = 1)
                self.Turn = False
                self.updateinfo()
                self.connectionSocket.send(b'5')
                self.game.boardRow2[1] = 'X'
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
            elif self.player1Connected == False:
                messagebox.showwarning('Wait!', "Input Server Address and Port to Start")
            else:
                self.Button6 = tk.Button(self.Board, text = "X", height = 12, width = 24, command = self.buttonClick6).grid(row = 1, column = 2)
                self.Turn = False
                self.updateinfo()
                self.connectionSocket.send(b'6')
                self.game.boardRow2[2] = 'X'
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
            elif self.player1Connected == False:
                messagebox.showwarning('Wait!', "Input Server Address and Port to Start")
            else:
                self.Button7 = tk.Button(self.Board, text = "X", height = 12, width = 24, command = self.buttonClick7).grid(row = 2, column = 0)
                self.Turn = False
                self.updateinfo()
                self.connectionSocket.send(b'7')
                self.game.boardRow3[0] = 'X'
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
            elif self.player1Connected == False:
                messagebox.showwarning('Wait!', "Input Server Address and Port to Start")
            else:
                self.Button8 = tk.Button(self.Board, text = "X", height = 12, width = 24, command = self.buttonClick8).grid(row = 2, column = 1)
                self.Turn = False
                self.updateinfo()
                self.connectionSocket.send(b'8')
                self.game.boardRow3[1] = 'X'
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
            elif self.player1Connected == False:
                messagebox.showwarning('Wait!', "Input Server Address and Port to Start")
            else:
                self.Button9 = tk.Button(self.Board, text = "X", height = 12, width = 24, command = self.buttonClick9).grid(row = 2, column = 2)
                self.Turn = False
                self.updateinfo()
                self.connectionSocket.send(b'9')
                self.game.boardRow3[2] = 'X'
                #self.disableButtons()
                self.WinLoseTie()
            if self.recieveInfo != False:
                self.getInfo()

    def disableButtons(self):
        self.Button1['state'] = 'DISABLED'
        self.Button2['state'] = 'DISABLED'
        self.Button3['state'] = 'DISABLED'
        self.Button4['state'] = 'DISABLED'
        self.Button5['state'] = 'DISABLED'
        self.Button6['state'] = 'DISABLED'
        self.Button7['state'] = 'DISABLED'
        self.Button8['state'] = 'DISABLED'
        self.Button9['state'] = 'DISABLED'
        self.Board.update()

    def enableButtons(self):
        self.Button1['state'] = 'NORMAL'
        self.Button2['state'] = 'NORMAL'
        self.Button3['state'] = 'NORMAL'
        self.Button4['state'] = 'NORMAL'
        self.Button5['state'] = 'NORMAL'
        self.Button6['state'] = 'NORMAL'
        self.Button7['state'] = 'NORMAL'
        self.Button8['state'] = 'NORMAL'
        self.Button9['state'] = 'NORMAL'
        self.Board.update()
run = playgame()