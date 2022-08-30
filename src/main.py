from board_class import Board_class
from shortest_path import find_shortest_path
import logging as log
import sys, pygame, time


WHITE = (200, 200, 200)
COLOR = True

def init():
    pygame.init()
    window_width = 800
    window_height = 800
    gameDisplay = pygame.display.set_mode((window_width,window_height))
    pygame.display.set_caption('A* algorithm simulation')
    exit = False
    log.basicConfig(level=log.INFO)
    log.info("Starting GUI")
    width = 50
    length = 50
    start_xcord = 0
    start_ycord = 0
    finish_xcord = 25
    finish_ycord = 25
    log.info(f"Creating board with length: {length}, width: {width}")
    board = Board_class(length, width)
    log.info(f"Starting at {start_xcord}, {start_ycord}")
    log.info(f"Finishing at {finish_xcord}, {finish_ycord}")
    block_size = int(window_width/width)
    log.info(f"Block size: {block_size}")
    for i in range(0,window_width,block_size):
        for j in range(0,window_width,block_size):
            rect = pygame.Rect(i,j,block_size,block_size)
            pygame.draw.rect(gameDisplay, WHITE, rect, 1)
    pygame.display.update()

    repeat = True
    return_path = []
    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and repeat:
                    end_node = find_shortest_path((start_xcord, start_ycord), (finish_xcord, finish_ycord), board, log, gameDisplay, block_size, COLOR)
                    log.info("Printing shortest path")
                    while end_node.parent != None:
                        rect = pygame.Rect(end_node.x_cord*block_size,end_node.y_cord*block_size,block_size,block_size)
                        pygame.draw.rect(gameDisplay, 'blue', rect)
                        return_path.insert(0, (end_node.x_cord, end_node.y_cord))
                        end_node = end_node.parent
                    pygame.display.update()
                    repeat = False
                
                if event.key == pygame.K_RETURN and not repeat:
                    exit = True
                    pygame.display.update()
            
            left, middle, right = pygame.mouse.get_pressed()
 
            if left:
                pos = pygame.mouse.get_pos()
                board.non_traverse[pos[0]//block_size, pos[1]//block_size] = 1
                rect = pygame.Rect(pos[0]//block_size*block_size, pos[1]//block_size*block_size,block_size,block_size)
                pygame.draw.rect(gameDisplay, 'grey', rect)
                pygame.display.update()
    pygame.quit()
    log.info(f"Path: {return_path}")



init() 





