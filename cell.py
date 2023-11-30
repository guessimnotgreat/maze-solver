from graphic import Point, Line

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = win
        self._x1, self._x2, self._y1, self._y2 = None, None, None, None
        self.visited = False

    def draw(self, x1, x2, y1, y2):
        if self._win is None:
            return

        self._x1, self._x2, self._y1, self._y2 = x1, x2, y1, y2

        top_left = Point(x1, y1)
        bottom_left = Point(x1, y2)
        top_right = Point(x2, y1)
        bottom_right = Point(x2, y2)

        left_color = self.get_wall_color(self.has_left_wall)
        right_color = self.get_wall_color(self.has_right_wall)
        top_color = self.get_wall_color(self.has_top_wall)
        bottom_color = self.get_wall_color(self.has_bottom_wall)

        self._win.draw_line(Line(top_left, bottom_left), left_color)
        self._win.draw_line(Line(top_right, bottom_right), right_color)
        self._win.draw_line(Line(top_left, top_right), top_color)
        self._win.draw_line(Line(bottom_left, bottom_right), bottom_color)

    def get_paths(self, col, row, max_col, max_row):
        paths = []
        if not self.has_left_wall and col != 0:
            paths.append((col - 1, row))
        if not self.has_right_wall and col != max_col:
            paths.append((col + 1, row))
        if not self.has_top_wall and row != 0:
            paths.append((col, row - 1))
        if not self.has_bottom_wall and row != max_row:
            paths.append((col, row + 1))
        return paths

    def get_wall_color(self, has_wall):
        return "black" if has_wall else "white"

    def get_center(self):
        center_x = (self._x1 + self._x2) / 2
        center_y = (self._y1 + self._y2) / 2
        return Point(center_x, center_y)

    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        fill_color = 'red' if undo else 'gray'
        self._win.draw_line(Line(self.get_center(), to_cell.get_center()), fill_color)
