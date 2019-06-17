# Model.py
#
# For TicTacToe

#imports the view for use in this code.

from View import View

#start of the model class.

class Model:

    def __init__(self, View):
        self.v = View

        #lists for playerclicks

        self.Xclicks = []
        self.Oclicks = []


    #tells the view to draw the x's based on the click and adds them to the list. 

    def PlayerX(self, playerclick):
        if playerclick == 0:
            self.v.drawX(0)
            self.Xclicks.append(0)
        elif playerclick == 1:
            self.v.drawX(1)
            self.Xclicks.append(1)
        elif playerclick == 2:
            self.v.drawX(2)
            self.Xclicks.append(2)
        elif playerclick == 3:
            self.v.drawX(3)
            self.Xclicks.append(3)
        elif playerclick == 4:
            self.v.drawX(4)
            self.Xclicks.append(4)
        elif playerclick == 5:
            self.v.drawX(5)
            self.Xclicks.append(5)
        elif playerclick == 6:
            self.v.drawX(6)
            self.Xclicks.append(6)
        elif playerclick == 7:
            self.v.drawX(7)
            self.Xclicks.append(7)
        elif playerclick == 8:
            self.v.drawX(8)
            self.Xclicks.append(8)
        elif playerclick < 0 or playerclick > 8:
            set.self.v.msg("Please click in an empty cell")

    #same as above but for O's

    def PlayerO(self, playerclick):
        if playerclick == 0:
            self.v.drawO(0)
            self.Oclicks.append(0)
        elif playerclick == 1:
            self.v.drawO(1)
            self.Oclicks.append(1)
        elif playerclick == 2:
            self.v.drawO(2)
            self.Oclicks.append(2)
        elif playerclick == 3:
            self.v.drawO(3)
            self.Oclicks.append(3)
        elif playerclick == 4:
            self.v.drawO(4)
            self.Oclicks.append(4)
        elif playerclick == 5:
            self.v.drawO(5)
            self.Oclicks.append(5)
        elif playerclick == 6:
            self.v.drawO(6)
            self.Oclicks.append(6)
        elif playerclick == 7:
            self.v.drawO(7)
            self.Oclicks.append(7)
        elif playerclick == 8:
            self.v.drawO(8)
            self.Oclicks.append(8)
        elif playerclick <0 or playerclick > 8:
            set.self.v.msg("Please click in an empty cell")

    #Different win options for player x or o, or whether or not there is a draw. 

    def winOptions(self):
        if (0 in self.Xclicks and 1 in self.Xclicks and 2 in self.Xclicks) or (3 in self.Xclicks and 4 in self.Xclicks and 5 in self.Xclicks) or (6 in self.Xclicks and 7 in self.Xclicks and 8 in self.Xclicks)
        or (0 in self.Xclicks and 3 in self.Xclicks and 6 in self.Xclicks) or (1 in self.Xclicks and 5 in self.Xclicks and 7 in self.Xclicks) or (2 in self.Xclicks and 5 in self.Xclicks and 8 in self.Xclicks)
        or (0 in self.Xclicks and 5 in self.Xclicks and 8 in self.Xclicks) or (2 in self.Xclicks and 4 in self.Xclicks and 6 in self.Xclicks):
            set.self.v.msg("X wins!!!!")
        elif (0 in self.Oclicks and 1 in self.Oclicks and 2 in self.Oclicks) or (3 in self.Oclicks and 4 in self.Oclicks and 5 in self.Oclicks) or (6 in self.Oclicks and 7 in self.Oclicks and 8 in self.Oclicks)
        or (0 in self.Oclicks and 3 in self.Oclicks and 6 in self.Oclicks) or (1 in self.Oclicks and 5 in self.Oclicks and 7 in self.Oclicks) or (2 in self.Oclicks and 5 in self.Oclicks and 8 in self.Oclicks)
        or (0 in self.Oclicks and 5 in self.Oclicks and 8 in self.Oclicks) or (2 in self.Oclicks and 4 in self.Oclicks and 6 in self.Oclicks):
            set.self.v.msg("O wins!!!!")
        elif len(self.Xclicks) + len(self.Oclicks) == 9:
            set.self.v.msg("The game is a draw!!!")

    #resets the list. 

    def ResetClickLists():
        self.Xclicks.clear()
        self.Oclicks.clear()

    #model test, which I do not believe needs anything more than just the pass. 

def ModelTest():

    pass

if __name__ == "__main__":
    ModelTest()

