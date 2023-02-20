# from models.cell import Cell
from models.ship import Ship
from models.game_board import GameBoard

class GamePlay(object): 
    def __init__(self):
        self.player_board = GameBoard()
        self.cpu_board = GameBoard()
        self.player_ships = [Ship("CRUISER", 3), Ship("SUBMARINE", 2)]
        self.cpu_ships = [Ship("CRUISER", 3), Ship("SUBMARINE", 2)]

    def start_game(self): 
        print("\n\n---------------------------------")
        print("o o o WELCOME TO BATTLESHIP o o o")
        print("=================================\n\n")
        print(">>> Enter 'p' to play. Enter 'q' to quit.")
        user_input = input().lower()
        if user_input == 'p':
            print("\n\n\n")
            print("///////////////////////")
            print("///// Let's Play! /////")
            print("///////////////////////")
            self.place_ships()
     
        elif user_input == 'q':
            print("K, Bye then.")
        else:
            print("Invalid input")
            self.start_game()

    def place_ships(self):
        for ship in self.player_ships:
            print(f'\n\n>>> Enter {ship.length} consecutive coordinates for the {ship.name} \n')
            print('> example - "A1" "B1" "C1"') 
            print('> seperate coordinates with a space') 
            print('> enter row letter first - then column digit - i.e. "A1" "B1" "C1"')
            print('> cannot select diagonal coordinates"]\n')
            print('--------------')
            print('| YOUR BOARD |')
            print('--------------')
            print(self.player_board.render(True))
            print('==============')
            user_input = input().upper()
            self.player_board.place_ship(ship, user_input)