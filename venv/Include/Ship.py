class Ship:
    __xPos = 0
    __yPos = 0
    __size = 0
    __alligment = 'n'
    __health = 0
    __ship = []

    def __init__(self,size,alligment='n'):
        self.__size = size
        self.__alligment = alligment
        self.__health = 100
        self.__ship = "H" * size

    def getSize(self):
        return self.__size

    def getShip(self):
        return self.__ship

    def getHealth(self):
        return self.__health

    def getAlligment(self):
        return self.__alligment

    def setAlligment(self,alligment):
        self.__alligment = alligment

    def showShip(self):
        print(self.__ship)


