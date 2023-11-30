from cell import Cell
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.x1 = x1
        self.y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._initialize_cells()
        self._break_entrance_and_exit()

    def _initialize_cells(self):
        for i in range(self._num_cols):
            row = [Cell(self._win) for _ in range(self._num_rows)]
            self._cells.append(row)
            for j in range(self._num_rows):
                self._draw_cell(i, j)
    
    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        col = i
        row = j
        # Only focus on x1 and y1 if you want to specify the position.
        # x1 represents the distance from the left side of the canvas to the starting x-coordinate.
        # y1 represents the distance from the top side of the canvas to the starting y-coordinate.
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

        exit_cell = self._cells[self._num_cols - 1][self._num_rows - 1]
        exit_cell.has_bottom_wall = False
        exit_cell.draw(exit_cell._x1, exit_cell._x2, exit_cell._y1, exit_cell._y2)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            available_directions = []

            # Check Left
            if i > 0 and not self._cells[i - 1][j].visited:
                available_directions.append((i - 1, j))
            # Check Right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                available_directions.append((i + 1, j))
            # Check Up
            if j > 0 and not self._cells[i][j - 1].visited:
                available_directions.append((i, j - 1))
            # Check Down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                available_directions.append((i, j + 1))

            if not available_directions:
                self._draw_cell(i, j)
                return

            next_direction = random.choice(available_directions)
            next_i, next_j = next_direction
            self._knock_down_walls(i, j, next_i, next_j)

            i, j = next_direction
            self._break_walls_r(i, j)

    def _knock_down_walls(self, i, j, new_i, new_j):
        # Knock right/left & left/right walls
        if i < new_i:
            self._cells[i][j].has_right_wall = False
            self._cells[new_i][new_j].has_left_wall = False
        elif i > new_i:
            self._cells[i][j].has_left_wall = False
            self._cells[new_i][new_j].has_right_wall = False
        # Knock bottom/top & top/bottom walls
        elif j < new_j:
            self._cells[i][j].has_bottom_wall = False
            self._cells[new_i][new_j].has_top_wall = False
        elif j > new_j:
            self._cells[i][j].has_top_wall = False
            self._cells[new_i][new_j].has_bottom_wall = False

    # for future use maybe ?
    def _solve(self, i, j):
        _i, _j = i, j
        return self._solve_r(_i, _j)
    
    def _solve_r(self, i, j):
        self._animate()
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        current_cell = self._cells[i][j]
        current_cell.visited = True
        valid_paths = current_cell.get_paths(i, j, self._num_cols - 1, self._num_rows - 1)
        for path in valid_paths:
            next_i, next_j = path
            next_cell = self._cells[next_i][next_j]
            if not next_cell.visited:
                current_cell.draw_move(next_cell)
                if self._solve_r(next_i, next_j):
                    return True
                else:
                    current_cell.draw_move(next_cell, undo=True)
        return False

