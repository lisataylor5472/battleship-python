from models.cell import Cell


class GameBoard(object): 
    def __init__(self):
        self.grid = {
            'A': [Cell('1'), Cell('2'), Cell('3'), Cell('4')], 
            'B': [Cell('1'), Cell('2'), Cell('3'), Cell('4')],
            'C': [Cell('1'), Cell('2'), Cell('3'), Cell('4')],
            'D': [Cell('1'), Cell('2'), Cell('3'), Cell('4')],
        }

    def is_valid_coordinate(self, coordinate):
        coordinate = coordinate.upper()
        if len(coordinate) == 2 and type(coordinate) == str: 
            if coordinate[0] in self.grid.keys() and coordinate[1] in [str(n) for n in range(1,4)]:
                return True 
            else: 
                return False
        else: 
            return False

    def is_valid_placement(self, ship, coordinates):
        if len(coordinates) != ship.length: 
            return False 

        rows = []
        columns = []
        
        for coord in coordinates: 
            cell = self.grid[coord[0]][int(coord[1]) - 1]
            rows.append(coord[0])
            columns.append(coord[1])

            if cell.ship != None: 
                return False

        if len(set(rows)) == 1 and ''.join(columns) in '1234':
            return True
        elif len(set(columns)) == 1 and ''.join(rows) in 'ABCD':
            return True
        else: 
            return False

    def validate_coordinates(self, ship, coordinates):
        try: 
            for coord in coordinates: 
                if self.is_valid_coordinate(coord): 
                    return True
            if self.is_valid_placement(ship, coordinates):
                return True
        except: 
            return False 

    def place_ship(self, ship, coordinates):
        if self.validate_coordinates(ship, coordinates): 
            for coord in coordinates: 
                # Locate the cell in the grid 
                cell = self.grid[coord[0]][int(coord[1]) - 1]
                # Assign the ship to the cell
                cell.ship = ship

