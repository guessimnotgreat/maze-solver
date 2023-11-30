from cell import Cell
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._initialize_cells()
        self._break_entrance_and_exit()

    def _initialize_cells(self):
        for i in range(self.num_cols):
            row = [Cell(self._win) for _ in range(self.num_rows)]
            self._cells.append(row)
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        col = i
        row = j
        cell_x1 = self.x1 + (self.cell_size_x * col)
        cell_y1 = self.y1 + (self.cell_size_y * row)
        cell_x2 = cell_x1 + self.cell_size_x
        cell_y2 = cell_y1 + self.cell_size_y
        self._cells[i][j].draw(cell_x1, cell_x2, cell_y1, cell_y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        entrance_cell.has_top_wall = False
        entrance_cell.draw(entrance_cell._x1, entrance_cell._x2, entrance_cell._y1, entrance_cell._y2)

        exit_cell = self._cells[self.num_cols - 1][self.num_rows - 1]
        exit_cell.has_bottom_wall = False
        exit_cell.draw(exit_cell._x1, exit_cell._x2, exit_cell._y1, exit_cell._y2)
