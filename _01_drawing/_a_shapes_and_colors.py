import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    theTurtle = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    theTurtle.shape('turtle')
    # Set your turtle's speed using .speed(2)
    theTurtle.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    theTurtle.color('green')
    theTurtle.pencolor('blue')
    # Move your turtle forward using .forward(100)
    # TEST    Did your turtle move forward?
    theTurtle.forward(100)
    # Move your turtle left or right using .left(90) or .right(90)
    theTurtle.begin_fill()
    for i in range(4):
        theTurtle.forward(150)
        theTurtle.left(90)
    theTurtle.end_fill()
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?

    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    theTurtle.goto(x=0, y=0)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?
    theTurtle.color('red')
    theTurtle.begin_fill()
    theTurtle.circle(radius=80, steps=30)
    theTurtle.end_fill()
    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below

    # Draw 3 more shapes with different fill colors!
    theTurtle.color('yellow')
    theTurtle.begin_fill()
    for i in range(5):
        theTurtle.backward(150)
        theTurtle.left(70)
    theTurtle.end_fill()
    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
