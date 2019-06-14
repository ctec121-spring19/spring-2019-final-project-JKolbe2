# Controller.py
#
# For TicTacToe

from View import View
from Model import Model

'''
notes: 

v = view()
m = model(v)
self.player = "x"
v.message("x's turn")
while TRUE:
    cn=v.getmouse()
    
'''

class Controller:

    def __init__(self):
        self.v = View()
        self.m = Model(self.v)
        self.player = 'X'


    def gametime(self): 
        pass

    def PlayAGame(self):
        self.v.reset()
        self.player = 'X'
        #tell view to put up message saying its x's turn
        done = False
        #loop for one play
        while  not done:
            #get cellnum from view = get players click
            #loop until get valid cellnum and cellnum is empty
                #if cellnum == -1: (set that in view to where bad click is negative 1)
                    #update message in view asking for user to click in empty cell
                #elif not self.m.isempty(cellnum):   -isempty returns true or false
                    #update message in view asking for user to click in empty cell
                #else:
                    #done = true
            #self.model.turn(cellnum, self.player) - draw X or O on the screen
            #model updates its data and tells view to draw player symbol

            #ask mdoel if there is a winner 
            #if there is a winner
                #done = True
                #update view with message about who won
                #break 
            #ask model if there is a draw
            #if there is a draw 
                #done = true
                #update view with message abou draw
                #break

            #alternate player
            #update view with whos turn it is

