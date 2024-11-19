"""
Connor Cox
U3 Project
Turtle Tree Drawing
"""
import turtle as bert

ROTATE_ANGLE = 15
START_LENGTH = 60
START_THICK = 10
INTERVAL = 5
LEAF_THICK = START_THICK * 1.5

LEAF = "#f8add8"
TRUNK = "#331e29"

bert.speed("fastest")
bert.shape("classic")

def do_color(length, thickness):
  if length == 10 + INTERVAL:
    bert.color(TRUNK)

  if length > 10:
    tree(length-INTERVAL, thickness-1)
  
  if length == 10 + INTERVAL:
    bert.color(LEAF)
    bert.pensize(LEAF_THICK)

def tree(length, thickness):
  if length == 10:
    return

  if length == 10 + INTERVAL:
    bert.color(LEAF)
    bert.pensize(LEAF_THICK)

  bert.pensize(thickness)
  
  bert.lt(ROTATE_ANGLE)
  bert.fd(length)

  do_color(length, thickness)

  bert.bk(length)
  bert.rt(ROTATE_ANGLE*2)
  bert.fd(length)

  do_color(length, thickness)

  bert.pensize(thickness)
  bert.bk(length)
  bert.lt(ROTATE_ANGLE)

  if length == 10 + INTERVAL:
    bert.color(TRUNK)
    bert.pensize(thickness)

  return

bert.lt(90)
bert.penup()
bert.bk(200)
bert.pendown()

bert.color(TRUNK)
bert.pensize(START_THICK)
bert.forward(START_LENGTH)

tree(START_LENGTH-INTERVAL, START_THICK-1)

bert.mainloop()

