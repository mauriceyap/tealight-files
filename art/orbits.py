from tealight.art import (color, line, spot, circle, box, image, text, background)
from tealight.art import (screen_width, screen_height)

x = 600
y = 400
vx = 0
vy = 0
ax = 0
ay = 0
# parity = ((abs(vx + ax))/(vx + ax))

power = 0.3

line

def handle_keydown(key):
  global ax, ay
  

  if key == "a":
    ax = -power
  elif key == "d":
    ax = power
  elif key == "w":
    ay = -power
  elif key == "s":
    ay = power

def handle_keyup(key):
  global ax, ay

  if key == "a" or key == "d":
    ax = 0
  elif key == "w" or key == "s":
    ay = 0
    
def handle_frame():
  global x,y,vx,vy,ax,ay
  
  color("white")
  
  spot(x,y,8)

  vx = (vx+ax)*0.97
  vy = vy + ay +0.12
  if vy > 10:
    vy =10
  
  x = x + vx
  y = y + vy
  if y >= 800:
    vy=-1*abs(0.4*vy)
    if y>805:
      y=805
  
  color("blue")
  
  spot(x,y,8)


background("paper.jpg")

line(0,813,screen_width, 813)
