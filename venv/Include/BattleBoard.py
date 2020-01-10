from Include.Ship import Ship
from Include.GUI import GUI

class BattleBoard:
    __xSize = 0
    __ySize = 0
    __board = []
    __ships = []
    __shipsToPlaceCount = {1:4, 2:3, 3:2, 4:1}

    def __init__(self, xSize, ySize):
        self.xSize = xSize
        self.ySize = ySize
        for i in range(0, ySize):
            self.__board.append(["~"] * xSize)

    def showBoard(self):
        for row in self.__board:
            print(" ".join(row))

    def createShips(self):
        for i in self.__shipsToPlaceCount:
            for j in range(self.__shipsToPlaceCount[i]):
                self.__ships.append(Ship(i))

    def showShips(self):
        for ship in self.__ships:
            ship.showShip()

    def setBoardAroundShip(self,xPos,yPos):

        pass

    def checkIfShipCouldBePlaced(self):

        pass

    def placeShipsOnBoard(self):
        for ship in self.__ships:
            while True:
                try:
                    print("Now placing %d deck ship" % len(ship.getShip()))
                    xPos,yPos,alligment = GUI.placeShip()
                    if alligment.lower() == 'h':
                        for shipLength in range(len(ship.getShip())):
                            self.__board[yPos][xPos + shipLength] = ship.getShip()[shipLength]
                        break
                    elif alligment.lower() == 'v':
                        for shipLength in range(len(ship.getShip())):
                            self.__board[yPos + shipLength][xPos] = ship.getShip()[shipLength]
                        break
                    else :
                        continue
                except Exception:
                    continue

