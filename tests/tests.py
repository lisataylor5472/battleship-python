import unittest

from battleship.ship import Ship
from battleship.cell import Cell

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
        cell = Cell("A1")
        self.assertEqual(type(cell), Cell)
        self.assertEqual(cell.coordinate, "A1")
        self.assertEqual(cell.ship, None)
        cruiser = Ship("Cruiser", 3)
        cell.place_ship(cruiser)
        cell.ship
        self.assertNotEqual(cell.ship, None)

    def test_firing_on_ship_and_cell(self):
        cell = Cell("A1")
        cruiser = Ship("Cruiser", 3)
        cell.place_ship(cruiser)
        self.assertEqual(cell.is_fired_upon, False)
        cell.fire_upon()
        self.assertEqual(cell.ship.health, 2)
        self.assertEqual(cell.is_fired_upon, True)

    def test_rendering_cell(self):
        cell_1 = Cell("A1")
        cruiser = Ship("Cruiser", 3)
        self.assertEqual(cell_1.render(), ".")
        # Fire upon empty cell - should show "M" for miss 
        cell_1.fire_upon()
        self.assertEqual(cell_1.render(), "M")
        # Place ship on 3 cells - and fire again - check behavior 
        cruiser = Ship("Cruiser", 3)
        cell_2 = Cell("A2")
        cell_3 = Cell("A3")
        cell_4 = Cell("A4")
        cell_5 = Cell("A5")
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
    

if __name__ == '__main__':
    unittest.main()