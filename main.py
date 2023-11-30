from graphic import Window
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(50, 50, 10, 10, 50, 50, win)
    maze._break_walls_r(0,0)
    maze._reset_cells_visited()
    maze._solve(0, 0)
    win.wait_for_close()

main()