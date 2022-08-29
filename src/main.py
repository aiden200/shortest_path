from board_class import Board_class
from shortest_path import find_shortest_path
import logging as log
import sys, pygame, time


WHITE = (200, 200, 200)

def init():
    pygame.init()
    window_width = 800
    window_height = 800
    gameDisplay = pygame.display.set_mode((window_width,window_height))
    pygame.display.set_caption('A* algorithm simulation')
    exit = False
    log.basicConfig(level=log.INFO)
    log.info("Starting GUI")
    width = 10
    length = 10
    start_xcord = 0
    start_ycord = 0
    finish_xcord = 10
    finish_ycord = 5
    log.info(f"Creating board with length: {length}, width: {width}")
    board = Board_class(length, width)
    log.info(f"Starting at {start_xcord}, {start_ycord}")
    log.info(f"Finishing at {finish_xcord}, {finish_ycord}")
    block_size = int(window_width/width)
    for i in range(0,window_width,block_size):
        for j in range(0,window_width,block_size):
            rect = pygame.Rect(i,j,block_size,block_size)
            pygame.draw.rect(gameDisplay, WHITE, rect, 1)
    pygame.display.update()


    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            print(event)
        board.non_traverse[(5,5)] = 1
        board.non_traverse[(1,1)] = 1
        board.non_traverse[(3,1)] = 1

        end_node = find_shortest_path((start_xcord, start_ycord), (finish_xcord, finish_ycord), board, log, gameDisplay, block_size)
        log.info("Printing shortest path")
        while end_node.parent != None:
            rect = pygame.Rect(end_node.x_cord*block_size,end_node.y_cord*block_size,block_size,block_size)
            pygame.draw.rect(gameDisplay, 'blue', rect)
            print(end_node.x_cord, end_node.y_cord)
            end_node = end_node.parent
        pygame.display.update()
        time.sleep(10)
        exit = True
        pygame.display.update()
    
    pygame.quit()



init() 





