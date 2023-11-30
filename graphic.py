from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        print("call constructor")
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        print("window open...")
        while self.__running == True:
            self.redraw()
        print("window closed...")

    def close(self):
        print("from close")
        self.__running = False
    
    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2)
        canvas.pack(fill=BOTH, expand=1)

class Cell:
    def __init__(self, x1, x2, y1, y2, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

    def draw(self):
        if self.has_left_wall == True:
            self._win.draw_line(Line(self._x1, self._y1))
        if self.has_right_wall == True:
            self._win.draw_line(Line(self._x2, self._y2))
        if self.has_top_wall == True:
            self._win.draw_line(Line(self._y1, self._y2))
        if self.has_bottom_wall == True:
            self.win.draw_line(Line(self._x1, self._x2))