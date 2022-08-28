

class Board_node:
    def __init__(self, x_cord, y_cord, gcost, hcost, status):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.gcost = gcost
        self.hcost = hcost
        self.fcost = gcost + hcost
        self.status = status
        self.parent = None
    
    def get_status(self):
        return self.status
    
