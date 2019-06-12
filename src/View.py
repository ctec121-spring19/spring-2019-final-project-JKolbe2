# View.py
# 
# For TicTacToe
'''
notes:

self.win=graph.win(parameters)
win.setCoords((0,0), (3,0), (3,3), (0,3))
def draw o.(self, cellnum)
circ = circle()
circ.draw(self.win)

v = view()
v.drawo(cellnum) #this calls the function that draws an o 

cellnum = int(point.gety()) * 3 + int(point.getx())

for errors if getx( < 3 and get y( < 3))


'''

from graphics import *

class View:

    def __init__(self):
        self.win=GraphWin("Tic Tac Toe", 300, 400)
        self.win.setCoords(0, 0, 3, 4)
        self.objectList = []
        self.msg = Text(Point(2.5, 3.5), "")

        # horizontal lines
        Line(Point(0,1), Point(3,1)).draw(self.win)


        '''
         #line1 = Line(Point(100,0), Point(100,300))
         #line1.setOutline("black")
         #line1.draw(self.win)

         line2 = Line(Point(200,0), Point(200,300))
         line2.setOutline("black")
         line2.draw(self.win)

         line3 = Line(Point(0,100), Point(300,100))
         line3.setOutline("black")
         line3.draw(self.win)

         line4 = Line(Point(0,200), Point(300,200))
         line4.setOutline("black")
         line4.draw(self.win) 

         '''   


    def drawO(self, cellnum):
        drawo = Circle(20)
        drawo.setOutline("red")
        drawO()

    def drawX(self, cellnum): 
        drawx = Line(Point(0,0), Point(20,20)), Line(Point(20,0), (0,20))
        drawx.setOutline("red")
        drawX()


    def getmouse():
    
        pt = self.win.getMouse()
        cellNum = int(pt.getY())*3 + int(pt.getX())
        return cellNum
        



def ViewTest():
    v = View()    

    input()

if __name__ == "__main__":
    ViewTest()
