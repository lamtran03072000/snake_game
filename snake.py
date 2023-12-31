# Snake Game by Mahesh Sawant

import turtle
import time
import random



from PIL import Image

img = Image.open('buoi4.gif')
img_resized = img.resize((50, 30))  # Thay đổi kích thước thành 20x20 pixel
img_resized.save('buoi4out.gif', 'GIF')

img_snake_d = Image.open('snake_head_d.gif')
img_snake_d_resized = img_snake_d.resize((40, 60))  # Thay đổi kích thước thành 20x20 pixel
img_snake_d_resized.save('snake_head_d_out.gif', 'GIF')


img_snake_r = Image.open('snake_head_r.gif')
img_snake_r_resized = img_snake_r.resize((60, 40))  # Thay đổi kích thước thành 20x20 pixel
img_snake_r_resized.save('snake_head_r_out.gif', 'GIF')


img_snake_u = Image.open('snake_head_u.gif')
img_snake_u_resized = img_snake_u.resize((40, 60))  # Thay đổi kích thước thành 20x20 pixel
img_snake_u_resized.save('snake_head_u_out.gif', 'GIF')



img_snake_l = Image.open('snake_head_l.gif')
img_snake_l_resized = img_snake_l.resize((60, 40))  # Thay đổi kích thước thành 20x20 pixel
img_snake_l_resized.save('snake_head_l_out.gif', 'GIF')
delay = 0.1

# Score
score=0
high_score=0

# set up the screen
wn=turtle.Screen()
wn.title("Snake Game by Mahesh Sawant")
wn.bgcolor("#BF3DC2")
wn.setup(width=600, height=600)
wn.tracer(0)

# Snake head
wn.addshape("snake_head_d_out.gif")
wn.addshape("snake_head_r_out.gif")
wn.addshape("snake_head_l_out.gif")
wn.addshape("snake_head_u_out.gif")

head=turtle.Turtle()
head.speed(0)

head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"

# Snake food

wn.addshape("buoi4out.gif")
food=turtle.Turtle()
food.speed(0)
food.shape("buoi4out.gif")
food.color("red")
food.penup()
food.goto(0,100)
segments=[]

# Pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction="up"
        head.shape("snake_head_u_out.gif")

def go_down():
    if head.direction != "up":
        head.direction="down"
        head.shape("snake_head_d_out.gif")


def go_left():
    if head.direction != "right":
        head.direction="left"
        head.shape("snake_head_l_out.gif")


def go_right():
    if head.direction != "left":
        head.direction="right"
        head.shape("snake_head_r_out.gif")


def move():
    if head.direction == "up":
        y=head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y=head.ycor()
        head.sety(y-20)

    if head.direction == "left":
        x=head.xcor()
        head.setx(x-20)

    if head.direction == "right":
        x=head.xcor()
        head.setx(x+20)

# keyboard bindings
wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000,1000)

        # Clear the segments list
        segments.clear()

        # Reset the score
        score=0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))



    #Check for a collision with the food

    if head.distance(food)<20:
        # move the food to a random spot
        x=random.randint(-285,285)
        y=random.randint(-285,285)
        food.goto(x,y)

        # Add a segment
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("#A0C431")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score+=10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score,high_score),align="center",font=("Courier", 24, "normal"))

    # Move the end segment first in reverse order
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)

    # Move segment 0 to where the head is
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)

    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000,1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            #Reset the delay
            delay = 0.1

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",font=("Courier", 24, "normal"))


    time.sleep(delay)

wn.mainloop()