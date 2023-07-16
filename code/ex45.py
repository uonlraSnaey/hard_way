import turtle
import time
import random

delay = 0.12
Score = 0
height_score = 0
# Set up the screen
window = turtle.Screen()
window.title("Snake Game by @ciencat")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)

#head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
food.goto(0, 100)

segments = []

# Score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color = ("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 Hight Score: 0" , align="center", font=("Arial", 24, "normal"))

# Move
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# keybord bindings

window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")

# Mian loop

while True:
    window.update()
    
    # collisions
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)
        
        segments.clear()

    if head.distance(food) < 20: #eat
        # move food in a random position
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        #food.goto(random.randint(-290, 290), random.randint(-290, 290))
    
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collision with the body segments

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)
        
            segments.clear()

    time.sleep(delay)


window.mainloop()