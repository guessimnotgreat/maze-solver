from graphic import Window
from cell import Cell

def main():
    win = Window(800, 600)
    cell = Cell(400, 450, 300, 350, win)
    cell.has_top_wall = False
    cell.draw()
    win.wait_for_close()

main()