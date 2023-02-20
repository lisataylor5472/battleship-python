class Cell(object): 
    def __init__(self):
        self.ship = None
        self.is_fired_upon = False

    def place_ship(self, ship):
        self.ship = ship 
        self.is_empty = False
    
    def fire_upon(self):
        self.is_fired_upon = True
        if self.ship != None:
            self.ship.hit()

    def render(self, show_ships=False): 
        if self.ship != None and self.ship.is_sunk() == True:
            return 'X'
        elif self.ship != None and self.is_fired_upon == True:
            return 'H'
        elif self.ship == None and self.is_fired_upon == True:
            return 'M'
        elif self.ship != None and show_ships == True: 
            return 'S'
        else: 
            return '.'
