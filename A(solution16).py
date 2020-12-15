# 16 . Imagine you are creating a Super Mario game.You need to define a class to represent Mario.What would it look like?
# If you are n't familiar with SuperMario,use your own favorite video or board game to model a player.
class Mario(object):

    def __init__(self):
        self.x=0
        self.y=0
        self.getValues()

    def reset(self):
        self.x=0
        self.y=0

    def setPosition(self, newX, newY):
        self.x=newX
        self.y=newY

    def setSize(self, width, height):
        self.w=width
        self.h=height

    def update(self):
        self.getValues()




def __init__(self, fileHandle):
    self.currentFileHandle=fileHandle
    self.reset()


def reset(self):
    self.f=open(self.currentFileHandle)
    self.tileRows=self.f.readlines()
    self.map=[]
    self.entities=[]
