class GUI:

    def showStartUI():
        print("============================================================")
        print("Welcome to Battleship Game")
        print("This is one player game, you place ships, you shoot to them")
        print("Now let's start ! ")
        print("============================================================")
        print("Please give board dimensions")
        xDimension = int(input("Horizontal dimension (x): "))
        yDimension = int(input("Vertical dimension (y): "))
        print("============================================================")
        print("Now let's start placing ships")
        print("============================================================")
        return xDimension,yDimension

    def askForShipPosition():
        xPos = int(input(("Provide X position of where to place ship: ")))
        yPos = int(input(("Provide Y position of where to place ship: ")))
        return xPos,yPos

    def availShips():
        print("============================================================")
        print("=====================Available ships========================")
        print("============================================================")

    def placeShip():
        print("============================================================")
        xPos = int(input("Input X position for ship to place :"))
        yPos = int(input("Input Y position for ship to place :"))
        alligment = str(input("How ship should be placed 'V'- Vertically, 'H' - Horizontally :"))
        print("============================================================")
        return xPos,yPos,alligment
