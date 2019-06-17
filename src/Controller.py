# Controller.py
#
# For TicTacToe

#imports the view and model so the controller can use them

from View import View
from Model import Model

#defines the controller class

class Controller:

    def __init__(self):
        self.v = View()
        self.m = Model(self.v)
        self.player = 'X'

    #the code to start the game. 

    def PlaytheGame(self):
        done = False
        while not done:
            self.playerturns()

    #the code that defines the players turns and checks that the click is valid. 
    
    def playerturns(self):

        self.player = "X"
        self.v.msg.setText("Player X goes first.")

        while True:

            cellnum = self.v.playerclick()

            while cellnum:
                if cellnum < 0 or cellnum > 8:
                    self.v.msg.setText("Please click within the grid")
                elif cellnum in self.m.Xclicks:
                    self.v.msg.setText("Please click in an unoccupied square")
                elif cellnum in self.m.Oclicks:
                    self.v.msg.setText("Please click in an unoccupied square")
                else: 
                    break  


