# from models.cell import Cell
import time
from models.ship import Ship
from models.game_board import GameBoard

class GamePlay(object): 
    def __init__(self):
        self.player_board = GameBoard()
        self.cpu_board = GameBoard()
        self.ships = { 
            'player': [ 
                Ship("BATTLESHIP", 4), 
                Ship("CRUISER", 3), 
                Ship("SUBMARINE", 3), 
                Ship("DESTROYER", 2)
            ],
            'cpu': [ 
                Ship("BATTLESHIP", 4), 
                Ship("CRUISER", 3), 
                Ship("SUBMARINE", 3), 
                Ship("DESTROYER", 2)
            ]
        }

    def start_game(self): 
        self.render_game_intro()
        user_input = input().lower()
        if user_input == 'p':
            self.render_game_start()
            self.place_ships()
        elif user_input == 'q':
            # TODO - build in retry logic to eventually quit out of the game
            self.render_attempt_to_quit()
            self.start_game()      
        else:
            self.start_game()

    def place_ships(self):
        for ship in self.ships['player']:
            print('o----------------o')
            print('|   YOUR BOARD   |')
            print('o----------------o')
            print(self.player_board.render(True))
            print('o================o')
            print('\n\n')
            print(f'>>> Enter {ship.length} consecutive coordinates for the {ship.name} \n')
            print('============ COORDINATE SELECTION GUIDELINES ============') 
            print('--- - enter row (LETTER) first - then column (DIGIT) second')
            print('--- - example - A1 B1 C1 D1 (for the BATTLESHIP)') 
            print('--- - separate each pair of coordinates with a space') 
            print('--- - cannot select diagonal coordinates\n')
            user_input = input().upper()
            self.player_board.place_ship(ship, user_input)

    def render_game_intro(self):
        print("\n\n")
        print("------------------------------------------------")
        print("o o o o o o o      WELCOME TO      o o o o o o o")
        print("================================================")
        print("  _           _   _   _           _     _       ")      
        print(" | |         | | | | | |         | |   (_)      ")     
        print(" | |__   __ _| |_| |_| | ___  ___| |__  _ _ __  ")  
        print(" | '_ \ / _` | __| __| |/ _ \/ __| '_ \| | '_ \ ")
        print(" | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) |")
        print(" |_.__/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/ ")
        print("                                         | |    ")
        print("                                         |_|    ")
        print("================================================")
        print("\n\n")
        print(">>> Enter 'P' to PLAY. Enter 'Q' to QUIT.")

    def render_game_start(self):
        self._imitate_slow_loading()
        print("...just getting a few things ready...")
        self._imitate_slow_loading()
        print("...ok!")
        self._imitate_quick_loading()
        print("/////////////////////////////////////////")
        print(">>>>>>>>>>>    Let's Play!    <<<<<<<<<<<")
        print("/////////////////////////////////////////")
        print("\n")
        print("=========== YOUR FLEET  ===========\n")
        for ship in self.ships['player']:
            print(f'--- Ship: {"{:<10}".format(ship.name)} - Length: {ship.length}')
        print("\n===================================\n")

    def render_attempt_to_quit(self):
        self._imitate_slow_loading()
        print("...quitting...")
        self._imitate_slow_loading()
        print("...psyche!")
        self._imitate_slow_loading()

    def render_invalid_input(self):
        self._imitate_slow_loading()
        print("you had one job...")
        self._imitate_slow_loading()

    def _imitate_slow_loading(self):
        for i in range(3):
            time.sleep(1)
            print(".")

    def _imitate_quick_loading(self):
        for i in range(3):
            time.sleep(0.5)
            print(".")