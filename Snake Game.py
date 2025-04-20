import turtle
import time
import random

delay = 0.1
score=0
high_score=0

# This is the Screen:
win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("Green")
win.setup(width=700, height=700)
win.tracer(0)

# This is the Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("Red")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# This is the food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("Yellow")
food.penup()
food.goto(0, 100)

# Snake body ka list
segments = []

#Pen 
pen= turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,280)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier",24,"normal"))


# Function to move the snake the functions only
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


# Functions to control movement to take input from keyboard
def goup():
    if head.direction != "down":  # Prevents reversing direction
        head.direction = "up"


def godown():
    if head.direction != "up":
        head.direction = "down"


def goleft():
    if head.direction != "right":
        head.direction = "left"


def goright():
    if head.direction != "left":
        head.direction = "right"

win.listen()
win.onkeypress(goup, "Up")
win.onkeypress(godown, "Down")
win.onkeypress(goleft, "Left")
win.onkeypress(goright, "Right")

# Main Game Loop
while True:
    win.update()

    # To check for border collision
    if head.xcor() > 350 or head.xcor() < -350 or head.ycor() > 350 or head.ycor() < -350:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # to remove the segments after crash
        for seg in segments:
            seg.goto(1000, 1000)

        segments.clear()

        # Reset the score
        score = 0

        #To reset the delay
        delay=0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


    # Move the body first (from back to front)
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # To check for food collision
    if head.distance(food) < 20:
        x = random.randint(-340, 340)
        y = random.randint(-340, 340)
        food.goto(x, y)  # Moves food to a new random location

        # Add a new segment to the snake
        newseg = turtle.Turtle()
        newseg.speed(0)
        newseg.shape("square")
        newseg.color("orange")
        newseg.penup()
        segments.append(newseg)

        #To shorten the delay
        delay -= 0.001

        # To increase the score
        score+=10

        if score > high_score:
          high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # To check for body collisions
    for segment in segments:
        if head.distance(segment) < 20: 
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for seg in segments:
                seg.goto(1000, 1000)

                segments.clear()

             # Reset the score
            score = 0

            #To reset the delay
            delay=0.1

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))    
 
    time.sleep(delay)

win.mainloop()
