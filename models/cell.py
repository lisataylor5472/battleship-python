class Cell(object): 
    def __init__(self, column):
        self.column = column
        self.ship = None
        self.is_fired_upon = False

    def place_ship(self, ship):
        self.ship = ship 
        self.is_empty = False
    
    def fire_upon(self):
        self.is_fired_upon = True
        if self.ship is not None:
            self.ship.hit()

    def render(self, show_ships=False): 
        if self.is_fired_upon == True: 
            if self.ship == None: 
                return "M"
            elif self.ship.is_sunk == True: 
                return "X"
            else:
                self.ship.hit()
                return "H"
        elif show_ships == True and self.ship != None: 
            return "S"
        else: 
            return "." 
