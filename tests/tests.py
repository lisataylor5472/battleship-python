import unittest      

from models.ship import Ship
from models.cell import Cell
from models.game_board import GameBoard

class Battleship(unittest.TestCase):
    def test_ship(self):
        cruiser = Ship("Cruiser", 3)
        self.assertEqual(type(cruiser), Ship)
        self.assertEqual(cruiser.name, "Cruiser")
        self.assertEqual(cruiser.length, 3)
        self.assertEqual(cruiser.health, 3)
        self.assertEqual(cruiser.is_sunk, False)
        cruiser.hit()
        self.assertEqual(cruiser.health, 2)
        cruiser.hit()
        self.assertEqual(cruiser.health, 1)
        cruiser.hit()
        self.assertEqual(cruiser.health, 0)
        self.assertEqual(cruiser.is_sunk, True)

    def test_cell(self):
        cell = Cell("1")
        self.assertEqual(type(cell), Cell)
        self.assertEqual(cell.column, "1")
        self.assertEqual(cell.ship, None)
        cruiser = Ship("Cruiser", 3)
        cell.place_ship(cruiser)
        cell.ship
        self.assertNotEqual(cell.ship, None)

    def test_cell_and_ship_firing(self):
        cell = Cell("1")
        cruiser = Ship("Cruiser", 3)
        cell.place_ship(cruiser)
        self.assertEqual(cell.is_fired_upon, False)
        cell.fire_upon()
        self.assertEqual(cell.ship.health, 2)
        self.assertEqual(cell.is_fired_upon, True)

    def test_cell_rendering(self):
        cell_1 = Cell("1")
        cruiser = Ship("Cruiser", 3)
        self.assertEqual(cell_1.render(), ".")
        # Fire upon empty cell - should show "M" for miss 
        cell_1.fire_upon()
        self.assertEqual(cell_1.render(), "M")
        # Place ship on 3 cells - and fire again - check behavior 
        cruiser = Ship("Cruiser", 3)
        cell_2 = Cell("2")
        cell_3 = Cell("3")
        cell_4 = Cell("4")
        cell_5 = Cell("5")
        cell_3.place_ship(cruiser)
        cell_4.place_ship(cruiser)
        cell_2.place_ship(cruiser)
        self.assertEqual(cell_2.render(True), "S")
        self.assertEqual(cell_2.render(), ".")
        cell_2.fire_upon()
        cell_3.fire_upon()
        self.assertEqual(cell_2.render(), "H")
        cell_4.fire_upon()
        self.assertEqual(cruiser.is_sunk, True)
        self.assertEqual(cell_1.render(), "M")
        self.assertEqual(cell_2.render(), "X")
        self.assertEqual(cell_3.render(), "X")
        self.assertEqual(cell_4.render(), "X")
        self.assertEqual(cell_5.render(), ".")

    def test_game_board_valid_coordinate(self):
        board = GameBoard()
        self.assertEqual(board.is_valid_coordinate("00"), False)
        self.assertEqual(board.is_valid_coordinate("A1"), True)
        self.assertEqual(board.is_valid_coordinate("ZZ"), False)
        self.assertEqual(board.is_valid_coordinate("a1cd"), False)
        self.assertEqual(board.is_valid_coordinate("b1"), True)

    def test_game_board_valid_placement(self):
        board = GameBoard()
        cruiser = Ship("Cruiser", 3)
        submarine = Ship("Submarine", 2)

        # Test that quantity of coordinates matches length of ship
        self.assertEqual(board.is_valid_placement(cruiser, ["A1", "A2"]), False)
        self.assertEqual(board.is_valid_placement(submarine, ["A1", "A2"]), True)
        # Test that coordinates are consecutive
        self.assertEqual(board.is_valid_placement(cruiser, ["A1", "B1", "C1"]), True)
        self.assertEqual(board.is_valid_placement(cruiser, ["A3", "A2", "A1"]), False)
        self.assertEqual(board.is_valid_placement(cruiser, ["A1", "B1", "D1"]), False)
        self.assertEqual(board.is_valid_placement(submarine, ["A2", "A4"]), False)
        self.assertEqual(board.is_valid_placement(submarine, ["A2", "A3"]), True)
        # Test that coordinates are not diagonal
        self.assertEqual(board.is_valid_placement(submarine, ["A1", "B2"]), False)
    
    def test_game_board_place_ship(self):
        board = GameBoard()
        cruiser = Ship("Cruiser", 3)
        submarine = Ship("Submarine", 2)

        board.place_ship(cruiser, ["A1", "A2", "A3"])

        cell_1 = board.grid['A'][0]
        cell_2 = board.grid['A'][1]
        cell_3 = board.grid['A'][2]

        self.assertEqual(cell_1.ship, cruiser)
        self.assertEqual(cell_2.ship, cruiser)
        self.assertEqual(cell_3.ship, cruiser)
        self.assertEqual(cell_3.ship, cell_2.ship)

        self.assertEqual(board.is_valid_placement(submarine, ["A1", "A2"]), False)


if __name__ == '__main__':
    unittest.main()