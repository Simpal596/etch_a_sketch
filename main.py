from turtle import Turtle, Screen


timmy = Turtle()
def forward() :
    timmy.fd(10)

def backward() :
    timmy.bk(10)

def clockwise() :
    timmy.right(10)

def counter_clockwise() :
    timmy.left(10)

def clear_drawing() :
    timmy.home()
    timmy.clear()




my_screen = Screen()
my_screen.listen()
my_screen.onkeypress(key="W", fun=forward)
my_screen.onkeypress(key="S", fun=backward)
my_screen.onkeypress(key="A", fun=clockwise)
my_screen.onkeypress(key="D", fun=counter_clockwise)
my_screen.onkeypress(key="C", fun=clear_drawing)
my_screen.exitonclick()