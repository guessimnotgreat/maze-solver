from graphic import Window
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    # cell = Cell(50, 100, 50, 100, win)
    # cell.draw()
    maze = Maze(50, 50, 9, 9, 50, 50, win)
    win.wait_for_close()

main()