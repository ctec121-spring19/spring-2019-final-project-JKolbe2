# View.py
# 
# For TicTacToe
'''
notes:

self.win=graph.win(parameters)
def draw o.(self, cellnum)
circ = circle()
circ.draw(self.win)

v = view()
v.drawo(cellnum) #this calls the function that draws an o 

cellnum = int(point.gety()) * 3 + int (point.getx())

for errors if getx( < 3 and get y( < 3))
'''

from graphics import *

class View:

    def __init__(self):
        win=GraphWin("Tic Tac Toe", 3, 3)
        draw.win(self)
          


def ViewTest():
    # delete and enter your code here
    pass
    
if __name__ == "__main__":
    ViewTest()
