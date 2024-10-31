import pygame as pg
from copy import deepcopy
WIDTH, HEIGHT = 1280,1280
WINDOW = pg.display.set_mode((WIDTH,HEIGHT))
ROWS = 640
COLLS = ROWS
CELL_SIZE = WIDTH/COLLS
BOARD = [[0 for i in range(COLLS)] for j in range(ROWS)]
BOARD[0][COLLS//2+1] = 1

pg.display.set_caption("Elemetary Celular Automaton")
def draw():
    WINDOW.fill("black")

    for i in range(ROWS): #Col
        for j in range(COLLS): # ROW
            if BOARD[i][j] == True:
                color = "white"
            else:
                color = "black"

            pg.draw.rect(WINDOW,color,((j*CELL_SIZE,i*CELL_SIZE),(CELL_SIZE,CELL_SIZE)))
    pg.display.update()

def dec_to_bin(num):
    result = ""
    while num >0:
        if num%2==0:
            result += "0"
        else:
            result += "1"
        num//=2
    result = result[::-1]
    if len(result) <8:
        result = "0" *(8-len(result)) + result
    return result

    
def create_rule(rule):
    rules = {}
    bin_rule = dec_to_bin(rule)
    for i in range(8):
        bin_i = bin(i)[2:]
        if len(bin_i) <3:
            bin_i = "0"*(3-len(bin_i)) + bin_i
        rules[bin_i] = int(bin_rule[i])
    return rules # return dict ex. {"000":1}
        
def next_gen(gen,rules):
    new_gen = [0 for _ in range(COLLS)]

    for i in range(1,COLLS-2): # we skip first and last index
        neighbours = "".join([ str(x) for x in gen[i-1:i+2]])#  elements before and after i
        new_gen[i] = rules[neighbours]
        
    return new_gen
    
def main():
    running = True
    rules = create_rule(126)
    row = 1
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        draw()
        
        BOARD[row] = next_gen(BOARD[row-1],rules)
        row +=1 
        
        



if __name__ == "__main__":
    main()