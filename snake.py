import turtle
import time
import random

# 1. Setup Graphics & Coordinate System
screen = turtle.Screen()
screen.title("Snake Graphics Demo")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0) # Disable auto-updates for manual frame control

# 2. Entity Creation
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = [] # List to manage snake body data structure

# 3. Input Handling (Event Callbacks)
def go_up():
    if head.direction != "down": head.direction = "up"
def go_down():
    if head.direction != "up": head.direction = "down"
def go_left():
    if head.direction != "right": head.direction = "left"
def go_right():
    if head.direction != "left": head.direction = "right"

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# 4. Movement Logic (Coordinate Updating)
def move():
    if head.direction == "up": head.sety(head.ycor() + 20)
    if head.direction == "down": head.sety(head.ycor() - 20)
    if head.direction == "left": head.setx(head.xcor() - 20)
    if head.direction == "right": head.setx(head.xcor() + 20)

# 5. Main Game Loop (Rendering Pipeline)
while True:
    screen.update() # Manual refresh
    
    # Border Collision
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        for s in segments: s.goto(1000, 1000) # Move segments off-screen
        segments.clear()

    # Food Collision (AABB approximation)
    if head.distance(food) < 20:
        food.goto(random.randint(-280, 280), random.randint(-280, 280))
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    # Shift segments (Move tail to previous position of piece ahead)
    for i in range(len(segments) - 1, 0, -1):
        segments[i].goto(segments[i-1].xcor(), segments[i-1].ycor())
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()
    time.sleep(0.1) # Frame rate control

