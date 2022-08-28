'''
Some properties to keep in mind:
Board_node takes in 5 arguments:
    x_cord, y_cord, gcost, hcost, status

This is the A* algo taking place, here is the basic pseudocode. In the actual code, there is more to this: 

OPEN //the set of nodes to be evaluated
CLOSED //the set of nodes already evaluated
add the start node to OPEN
 
loop
        current = node in OPEN with the lowest f_cost
        remove current from OPEN
        add current to CLOSED
 
        if current is the target node //path has been found
                return
 
        foreach neighbour of the current node
                if neighbour is not traversable or neighbour is in CLOSED
                        skip to the next neighbour
 
                if new path to neighbour is shorter OR neighbour is not in OPEN
                        set f_cost of neighbour
                        set parent of neighbour to current
                        if neighbour is not in OPEN
                                add neighbour to OPEN
'''

from node_class import Board_node
import math


def find_dist(start, end):
    #check the rounding, this might come back and bite me later when replacing shorter distances
    return round(math.dist([start[0],start[1]], [end[0],end[1]]),2)


def find_shortest_path(start_cord, end_cord, board, log):
    log.info("Starting algorithm")
    board.open[start_cord] = Board_node(start_cord[0], end_cord[0], 0, find_dist(start_cord, end_cord))

    while True:
        # choosing which node to look at
        low = float('inf')
        temp = []
        for key in board.open:
            check_val = board.open[key]
            if check_val.fcost < low:
                temp = [check_val]
                low = check_val.fcost
                board.current = check_val
            elif check_val.fcost == low:
                temp.append(check_val)
        
        # we have tied values, we choose the one with the lowest hcost, if still a tie, we just choose the first one
        if len(temp > 1):
            low = temp[0].hcost
            board.current = temp[0]
            for val in temp:
                if val.hcost < low:
                    board.current = val


        #remove the current coordinates from the open section
        current_cords = (board.current.x_cord, board.current.y_cord)
        board.open.pop(current_cords)
        board.close[current_cords] = board.current
        if current_cords == end_cord:
            return board.current # traverse back with parent to get total path

        
        


