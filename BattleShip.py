def create_board(board,xDim, yDim):
    for i in range(0,yDim):
        board.append(["~"]*xDim)

def print_board(board):
    for row in board:
        print(" ".join(row))

def place_ship(xPos,yPos,board,allignment,shipSize):
    if shipSize == 1:
        board[yPos][xPos] = "H"
        return True
    elif 2 <= shipSize <= 4:
        if allignment.lower() == "v":
            if yPos+shipSize > len(board):
                return False
            else:
                for i in range(0, shipSize):
                    board[yPos + i][xPos] = "H"
                return True
        elif allignment.lower() == "h":
            if xPos+shipSize > len(board[yPos]):
                return False
            else:
                for i in range(0, shipSize):
                    board[yPos][xPos + i] = "H"
                return True
    else:
        return False

def ask_for_ship_positions(shipSize):
    print("Now place %d-deck ship" % shipSize)
    x = int(input("Input X position where ship should be placed: "))
    y = int(input("Input Y position where ship should be placed: "))
    return x, y

def add_ship_procedure(shipCount,whichToPlace):
    shipSize = list(shipCount.keys())[whichToPlace - 1]
    if shipSize == 1:
        xPos, yPos = ask_for_ship_positions(shipSize)
        if place_ship(xPos, yPos, board, "H", shipSize) == True:
            shipCount[whichToPlace] -= 1
        else:
            print("Ship couldnt be placed here!")
    elif 2 <= shipSize <= 4 :
        xPos, yPos = ask_for_ship_positions(shipSize)
        allign = str(input("How should it be alligned vertically(V) or horizontally(H)? :"))
        if place_ship(xPos, yPos, board, allign, shipSize) == True:
            shipCount[whichToPlace] -= 1
        else:
            print("Ship couldnt be placed here!")

def place_ships(board):
    #dictionary which represents size:count
    shipCount = {1: 4, 2: 3, 3: 2, 4: 1}
    print("To print how many ships are left type 'Left'")
    print("To print board type 'board'")
    xPlacement = 0
    yPlacement = 0
    suma = 1
    while suma > 0:
        whichToPlace = input("Which ship you want to place? Choose 1 to 4 (1 - 1-deck),(2-2-deck) etc.")
        if whichToPlace == str(1) and shipCount[int(whichToPlace)] > 0:
            add_ship_procedure(shipCount, int(whichToPlace))
            suma = sum(shipCount.values())
        elif whichToPlace == str(2) and shipCount[int(whichToPlace)] > 0:
            add_ship_procedure(shipCount, int(whichToPlace))
            suma = sum(shipCount.values())
        elif whichToPlace == str(3) and shipCount[int(whichToPlace)] > 0:
            add_ship_procedure(shipCount, int(whichToPlace))
            suma = sum(shipCount.values())
        elif whichToPlace == str(4) and shipCount[int(whichToPlace)] > 0:
            add_ship_procedure(shipCount, int(whichToPlace))
            suma = sum(shipCount.values())
        elif whichToPlace.lower() == "left" :
            print("You have:\n"
                "%d - HHHH 4-deck ship\n"
                "%d - HHH 3-deck ships\n"
                "%d - HH 2-deck ships\n"
                "%d - H 1-deck ships" % (shipCount.get(4),shipCount.get(3),shipCount.get(2),shipCount.get(1)))
        elif whichToPlace.lower() == "board":
            print_board(board)
        elif whichToPlace.lower() == "exit":
            break
        else:
            print("Bad arguments provided or ships of given type are finished")
    print("All ship are in places. Let's start the game!")
    print_board(board)

def shoot(board):
    
    while 'H' in board:
        x = int(input("Input X position where to shoot: "))
        y = int(input("Input Y position where to shoot: "))
        if x == 99:
            print("You have exited the game, Bye!")
            break
        if board[y][x] == "~":
            board[y][x] = "O"
            print("MISS!")
        elif board[y][x] == "H":
            print("Got it !")
            board[y][x] = "X"
        elif board[y][x] == "O":
            print("You already shoot there! try again ")

board = []
print("Please give board dimensions")
xDimension = int(input("Horizontal dimension (x): "))
yDimension = int(input("Vertical dimension (y): "))

create_board(board, xDimension, yDimension)
print_board(board)
place_ships(board)
shoot(board)
print_board(board)