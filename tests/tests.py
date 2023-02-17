import unittest

from battleship.ship import Ship

class Battleship(unittest.TestCase):
    def test_ship(self):
        cruiser = Ship("Cruiser", 3)
        self.assertEqual(type(cruiser), Ship)
        self.assertEqual(cruiser.name, "Cruiser")
        self.assertEqual(cruiser.length, 3)
        self.assertEqual(cruiser.health, 3)
        self.assertEqual(cruiser.is_sunk(), False)
        cruiser.hit()
        self.assertEqual(cruiser.health, 2)
        cruiser.hit()
        self.assertEqual(cruiser.health, 1)
        cruiser.hit()
        self.assertEqual(cruiser.health, 0)
        self.assertEqual(cruiser.is_sunk(), True)



if __name__ == '__main__':
    unittest.main()