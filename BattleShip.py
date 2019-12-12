board = []
print ("Please give board dimensions")
xDimension = int(input("Horizontal dimension (x): "))
yDimension = int(input("Vertical dimension (y): "))

def place_multi_deck_ship(xPos, yPos, shipSize, board, allignment):
    if allignment.lower() == "v":
        for i in range(0, shipSize):
            board[xPos + i][yPos] = "H"
    elif allignment.lower() == "h":
        for i in range(0, shipSize):
            board[xPos][yPos + i] = "H"

def place_single_deck_ship(xPos, yPos, board):
    board[xPos][yPos] = "H"

def create_board(board,xDim, yDim):
    for i in range(0,yDim):
        board.append(["~"]*xDim)

def print_board(board):
    for row in board:
        print(" ".join(row))

def place_ships(board):
    #dictionary which represents size:count
    ship_count = {4:1, 3:1, 2:1, 1:1}

    xPlacement = 0
    yPlacement = 0
    suma = 1
    while suma > 0:
        suma = sum(ship_count.values())
        print("To print how many ships are left type 'Left'")
        print("To print board type 'board'")
        whichToPlace = input("Which ship you want to place? Choose 1 to 4 (1 - 1-deck),(2-2-deck) etc.")
        if whichToPlace == str(1) and ship_count[1] > 0:
            shipSize = list(ship_count.keys())[3]
            print("Now place %d-deck ship" % shipSize)
            x = int(input("Input X position where ship should be placed: "))
            y = int(input("Input Y position where ship should be placed: "))
            place_single_deck_ship(x, y, board)
            ship_count[1] -= 1
        elif whichToPlace == str(2) and ship_count[2] > 0:
            shipSize = list(ship_count.keys())[2]
            print("Now place %d-deck ship" % shipSize)
            x = int(input("Input X position where ship should be placed: "))
            y = int(input("Input Y position where ship should be placed: "))
            allign = str(input("How should it be alligned vertically(V) or horizontally(H)? :"))
            place_multi_deck_ship(x, y, shipSize, board, str(allign))
            ship_count[2] -= 1
        elif whichToPlace == str(3) and ship_count[3] > 0:
            shipSize = list(ship_count.keys())[1]
            print("Now place %d-deck ship" % shipSize)
            x = int(input("Input X position where ship should be placed: "))
            y = int(input("Input Y position where ship should be placed: "))
            allign = str(input("How should it be alligned vertically(V) or horizontally(H)? :"))
            place_multi_deck_ship(x, y, shipSize, board, str(allign))
            ship_count[3] -= 1
        elif whichToPlace == str(4) and ship_count[4] > 0:
            shipSize = list(ship_count.keys())[0]
            print("Now place %d-deck ship"% shipSize)
            x = int(input("Input X position where ship should be placed: "))
            y = int(input("Input Y position where ship should be placed: "))
            allign = str(input("How should it be alligned vertically(V) or horizontally(H)? :"))
            place_multi_deck_ship(x,y,shipSize,board,str(allign))
            ship_count[4] -= 1
        elif whichToPlace.lower() == "left" :
            print("You have:\n"
                "%d - HHHH 4-deck ship\n"
                 "%d - HHH 3-deck ships\n"
                "%d - HH 2-deck ships\n"
                "%d - H 1-deck ships" % (ship_count.get(4),ship_count.get(3),ship_count.get(2),ship_count.get(1)))
        elif whichToPlace.lower() == "board":
            print_board(board)
        else:
            print("Bad arguments provided or ships of given type are finished")
    print("All ship are in places. Let's start the game!")
    print_board(board)


create_board(board,xDimension,yDimension)
print_board(board)
place_ships(board)