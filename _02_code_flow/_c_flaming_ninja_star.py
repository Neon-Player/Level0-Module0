import random
import turtle


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


def get_next_color(i):
    return colors[i % len(colors)]

# ====================== DO NOT EDIT THE CODE ABOVE ===========================


if __name__ == '__main__':
    window = turtle.Screen()
    colors = ['red', 'blue', 'green', 'yellow', 'orange']

    baseSize = 200          # the size of the black part of the star
    flameSize = 130         # the length of the flaming arms
    
    # Make a new turtle
    mTurtle = turtle.Turtle()
    # Make the turtle shape 'turtle', .shape('turtle')
    mTurtle.shape('turtle')
    # Set the turtle width to 2
    mTurtle.turtlesize(stretch_wid=2)
    # Set the turtle speed to 0 (fastest)
    mTurtle.speed(0)
    # Use a for loop to repeat all of the code below ONE time (we will change
    # this later)
    for i in range(25):
        mTurtle.fillcolor('orange')
        mTurtle.begin_fill()
        mTurtle.right(360/8)
        mTurtle.forward(64)
        mTurtle.left(40)
        mTurtle.forward(flameSize)
        mTurtle.right(170)
        mTurtle.forward(flameSize)
        mTurtle.right(62)
        mTurtle.forward(baseSize)
        mTurtle.end_fill()

        # Set the turtle .fillcolor() to orange
        
        # Call the turtle .begin_fill() function
        
        # TURN RIGHT     Turn the turtle 1/8 of a circle (hint: 360 degrees
        #                will turn a full circle)
        
        # DRAW           Move the turtle 64 pixels
        
        # TURN LEFT      Turn the turtle 40 degrees to the LEFT. (Negative
        #                numbers will turn the turtle counter-clockwise.)
        
        # DRAW FLAME     Move the turtle the distance in the variable flameSize
        
        #                Turn the turtle to the right 170 degrees
         
        #                Move the turtle the distance in the variable flameSize (again)
         
        #  TURN RIGHT    Turn the turtle 62 degrees to the right
        
        #  DRAW          Move the turtle the distance in the variable baseSize
        
        # Call the turtle .end_fill() method
        
    # Hide your turtle so you can see the pattern.
        mTurtle.hideturtle()
    # TEST   Run the program. Check that your shape is the same as the first
    #        picture in the recipe. This is one arm of the ninja star.

    # COLOR  Change the turtle's pen color so that the flame is a different
    #        color to the rest of the star. Run the program again. Check the
    #        second picture in the recipe.

    # LOOP   When you have one arm looking right, change your for loop to
    #        repeat 25 times.
    
    # call the turtle .done() method
    turtle.done()
