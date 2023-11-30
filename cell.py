from graphic import Point, Line

class Cell:
    def __init__(self, x1, x2, y1, y2, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = win
        self.top_left = Point(x1, y1)
        self.bottom_left = Point(x1, y2)
        self.top_right = Point(x2, y1)
        self.bottom_right = Point(x2, y2)

    def draw(self):
        if self._win == None:
            return
        if self.has_left_wall:
            self._win.draw_line(Line(self.top_left, self.bottom_left))
        if self.has_right_wall:
            self._win.draw_line(Line(self.top_right, self.bottom_right))
        if self.has_top_wall:
            self._win.draw_line(Line(self.top_left, self.top_right))
        if self.has_bottom_wall:
            self._win.draw_line(Line(self.bottom_left, self.bottom_right))

    def get_center(self):
        center_x = (self.top_left.x + self.top_right.x) / 2
        center_y = (self.top_left.y + self.bottom_left.y) / 2
        return Point(center_x, center_y)

    def draw_move(self, to_cell, undo=False):
        if self._win == None:
            return
        fill_color = 'red' if undo else 'gray'
        self._win.draw_line(Line(self.get_center(), to_cell.get_center()), fill_color)