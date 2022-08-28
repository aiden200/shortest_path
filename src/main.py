from board_class import Board_class
from shortest_path import find_shortest_path
import logging as log

def init():
    log.basicConfig(level=log.INFO)
    width = 10
    length = 10
    start_xcord = 0
    start_ycord = 0
    finish_xcord = 10
    finish_ycord = 10
    log.info(f"Creating board with length: {length}, width: {width}")
    board = Board_class(length, width)
    log.info(f"Starting at {start_xcord}, {start_ycord}")
    log.info(f"Finishing at {finish_xcord}, {finish_ycord}")
    find_shortest_path((start_xcord, start_ycord), (finish_xcord, finish_ycord), board, log)


    





