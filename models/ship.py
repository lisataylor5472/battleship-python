class Ship(object): 
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.health = length

    def hit(self): 
        self.health -= 1 

    def is_sunk(self): 
        if self.health > 0: 
            return False
        else: 
            return True

