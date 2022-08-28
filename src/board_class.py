

class Board_class:
    def __init__(self, length, height):
        self.length = length
        self.height = height
        if length > 10: self.length = 10
        if height > 10: self.height = 10
        self.open = {}
        self.close = {}
        self.current = None
    
    

