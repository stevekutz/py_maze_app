import turtle
wn. turtle.Screen()
wn.bgcolor("black")
wn.title("Maze Game")
wn.setup(700, 700)

# Create Pen
class Pen(turtle.Turtle):
    def _init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('white')
        self.penup()
        self.speed(0)

# Create Levels
levels = [""]

# First Level
level_1 = []
