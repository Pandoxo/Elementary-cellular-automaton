import pygame as pg
WIDTH, HEIGHT = 1280,1280
WINDOW = pg.display.set_mode((WIDTH,HEIGHT))
CELLS_IN_ROW = 256
CELLS_IN_COLL = CELLS_IN_ROW
CELL_SIZE = WIDTH/CELLS_IN_ROW
BOARD = [[False for i in range(CELLS_IN_ROW)] for j in range(CELLS_IN_COLL)]
BOARD[0][128] = True

pg.display.set_caption("Elemetary Celular Automaton")

def draw():
    WINDOW.fill("black")

    for i in range(CELLS_IN_COLL): #Col
        for j in range(CELLS_IN_ROW): # ROW
            if BOARD[j][i] == True:
                color = "white"
            else:
                color = "black"

            pg.draw.rect(WINDOW,color,((i*CELL_SIZE,j*CELL_SIZE),(CELL_SIZE,CELL_SIZE)))
    pg.display.update()


def main():
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        draw()
        


if __name__ == "__main__":
    main()