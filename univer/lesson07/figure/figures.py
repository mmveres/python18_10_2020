class Cell:
    def __init__(self, value):
        self.value = value

class Row:
    def __init__(self):
        self.row = [Cell(1), Cell(2)]

class Matrix:
    def __init__(self):
        self.matrix =[Row(), Row()]

class Cube:
    def __init__(self):
        self.cube =[Matrix(), Matrix()]