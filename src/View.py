# View.py
# 
# For TicTacToe

from graphics import *

class View:

    def __init__(self):
        self.win=GraphWin("Tic Tac Toe", 300, 400)
        self.win.setCoords(0, 0, 3, 4)
        self.objectList = []
        self.msg = Text(Point(2.5, 3.5), "")

        # horizontal lines
        Line(Point(0,1), Point(3,1)).draw(self.win)

        Line(Point(0,2), Point(3,2)).draw(self.win)

        Line(Point(0,3), Point(3,3)).draw(self.win)

        # vertical lines
        Line(Point(1,0), Point(1,3)).draw(self.win)

        Line(Point(2,0), Point(2,3)).draw(self.win)

    def playerclick(self):

        pt = self.win.getMouse()
        pt.getY()
        pt.getX()
        cellNum = int(pt.getY())*3 + int(pt.getX())
        return cellNum

    def drawO(self, cellnum):
        if cellnum == 0: 
            self.objectList.appened(Circle(Point(0.5, 0.5), 0.75).draw(self.win))
        elif cellnum == 1:
            self.objectList.appened(Circle(Point(1.5, 0.5), 0.75).draw(self.win))
        elif cellnum == 2:
            self.objectList.appened(Circle(Point(2.5, 0.5), 0.75).draw(self.win))
        elif cellnum == 3:
            self.objectList.appened(Circle(Point(0.5, 1.5), 0.75).draw(self.win))
        elif cellnum == 4:
            self.objectList.appened(Circle(Point(1.5, 1.5), 0.75).draw(self.win))
        elif cellnum == 5:
            self.objectList.appened(Circle(Point(2.5, 1.5), 0.75).draw(self.win))
        elif cellnum == 6:
            self.objectList.appened(Circle(Point(0.5, 2.5), 0.75).draw(self.win))
        elif cellnum == 7:
           self.objectList.appened(Circle(Point(1.5, 2.5), 0.75).draw(self.win))
        elif cellnum == 8:
            self.objectList.appened(Circle(Point(2.5, 2.5), 0.75).draw(self.win))    

    def drawX(self, cellnum): 
        if cellnum == 0:
            self.items.append(Line(Point(0.05,0.05), Point(0.95,0.95)).draw(self.win)), Line(Point(0.95,0.05), Point(0.05,0.95)).draw(self.win)
        elif cellnum == 1:
            self.items.append(Line(Point(1.05,0.05), Point(1.95,0.95)).draw(self.win)), Line(Point(1.95,0.05), Point(1.05,0.95)).draw(self.win)
        elif cellnum == 2:
            self.items.append(Line(Point(2.05,0.05), Point(2.95,0.95)).draw(self.win)), Line(Point(2.95,0.05), Point(2.05,0.95)).draw(self.win)
        elif cellnum == 3:
            self.items.append(Line(Point(0.05,1.05), Point(0.95,1.95)).draw(self.win)), Line(Point(0.95,1.05), Point(0.05,1.95)).draw(self.win)
        elif cellnum == 4:
            self.items.append(Line(Point(1.05,1.05), Point(1.95,1.95)).draw(self.win)), Line(Point(1.95,1.05), Point(1.05,1.95)).draw(self.win)
        elif cellnum == 5:
            self.items.append(Line(Point(2.05,1.05), Point(2.95,1.95)).draw(self.win)), Line(Point(2.95,1.05), Point(2.05,1.95)).draw(self.win)
        elif cellnum == 6:
            self.items.append(Line(Point(0.05,2.05), Point(0.95,2.95)).draw(self.win)), Line(Point(0.95,2.05), Point(0.05,2.95)).draw(self.win)
        elif cellnum == 7:
            self.items.append(Line(Point(1.05,2.05), Point(1.95,2.95)).draw(self.win)), Line(Point(1.95,2.05), Point(1.05,2.95)).draw(self.win)
        elif cellnum == 8:
            self.items.append(Line(Point(2.05,2.05), Point(2.95,2.95)).draw(self.win)), Line(Point(2.95,2.05), Point(2.05,2.95)).draw(self.win)

    def reset(self):
        for object in self.objectList():
            object.undraw()
        self.objectList.clear()

    


    
        



def ViewTest():
    v = View()    

    input()

if __name__ == "__main__":
    ViewTest()
