class Ship(object): 
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.health = length
        self.sunk = False


    def hit(self): 
        self.health -= 1 
        pass

    def is_sunk(self): 
        if self.health == 0:
            self.sunk = True
            return self.sunk 
        else: 
            self.sunk = False
            return self.sunk
