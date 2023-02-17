class Ship(object): 
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.health = length
        self.is_sunk = False


    def hit(self): 
        self.health -= 1 
        if self.health == 0:
            self.is_sunk = True 
 

