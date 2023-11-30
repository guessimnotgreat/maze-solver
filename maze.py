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
        self._cells = self._create_cells()

    def _create_cells(self):
        col = []
        for i in range(self.num_cols):
            row = []
            for j in range(self.num_rows):
                cell = self._draw_cell(i, j)
                row.append(cell)
            col.append(row)
            row = []
        return col

    def _draw_cell(self, i, j):
        if self._win == None:
            return
        col = i
        row = j
        cell_x1 = self.x1 + (self.cell_size_x * col)
        cell_y1 = self.y1 + (self.cell_size_y * row)
        cell_x2 = cell_x1 + self.cell_size_x
        cell_y2 = cell_y1 + self.cell_size_y
        cell = Cell(cell_x1, cell_x2, cell_y1, cell_y2, self._win)
        cell.draw()
        self._animate()
        return cell

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)  
        