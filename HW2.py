import tkinter 

from enum import Enum

class axis(Enum):
    left = 4
    right = 6
    up = 8
    down = 10

class grid():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
    def __repr__(self):
        return f"({self.x}, {self.y})"
    def __bounds(self):
        if self.x < 1 or self.x > 50:
            self.x = 1
        if self.y < 1 or self.y > 50:
            self.y = 1
    def up(self):
        self.y += 1
        self.__bounds()
    def down(self):
        self.y -= 1
        self.__bounds()
    def left(self):
        self.x -= 1
        self.__bounds()
    def right(self):
        self.x += 1
        self.__bounds()
    x: int = 0
    y: int = 0
    
def hello(args: str)->None:
    global label_output
    
def xaxis(dir: axis, grid: grid):
    global label_output
    if dir == axis.left:
        grid.left()
    elif dir == axis.right:
        grid.right()
    label_output.set(grid.__str__())
    return label_output.get()

    
def yaxis(dir: axis, grid: grid)-> str:
    global label_output, mylabel
    if dir == axis.down:
        grid.down()
    elif dir == axis.up:
        grid.up()
    label_output.set(grid.__str__())
    return label_output.get()

def main()->None:
    x: int = 25
    y: int = 25
    menu = tkinter.Tk()
    menu.title("CS314 HW2")
    menu.geometry("200x150")
    
    mygrid = grid(x, y)
    button1 = tkinter.Button(menu, text="UP", command=lambda:yaxis(axis.up, mygrid))
    button2 = tkinter.Button(menu, text="DOWN", command=lambda:yaxis(axis.down, mygrid))
    button4 = tkinter.Button(menu, text="RIGHT", command=lambda:xaxis(axis.right, mygrid))
    button3 = tkinter.Button(menu, text="LEFT", command=lambda:xaxis(axis.left, mygrid))
    global label_output, mylabel 
    label_output = tkinter.StringVar()
    label_output.set(mygrid.__str__())
    mylabel = tkinter.Label(textvariable=label_output)
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    mylabel.pack()
    menu.mainloop()
    
if __name__ == "__main__":
    main()