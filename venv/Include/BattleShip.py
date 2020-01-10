from Include.BattleBoard import BattleBoard
from Include.GUI import GUI
from Include.Ship import Ship

xDimension, yDimension = GUI.showStartUI()
battleShipBoard = BattleBoard(xDimension,yDimension)
battleShipBoard.showBoard()
battleShipBoard.createShips()
GUI.availShips()
battleShipBoard.showShips()
battleShipBoard.placeShipsOnBoard()
battleShipBoard.showBoard()