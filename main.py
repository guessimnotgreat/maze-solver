from graphic import Window, Line, Point, Cell

def main():
    win = Window(800, 600)
    cell = Cell(400, 450, 300, 350, win)
    cell.draw()
    win.wait_for_close()

main()