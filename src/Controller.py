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
            self.anothergame()

    #the code that defines the players turns. 
    
    def playerturns(self):

        self.player = "X"
        self.v.msg.setText("Player X goes first.")

        while True: