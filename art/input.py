from tealight.art import (color, line, spot, circle, box, image, text, background)

def handle_mousedown(x,y):
  color("blue")
  spot(x,y,10)
  
def handle_mousemove(x,y,button):
  if button == "left":
    color("red")
    circle(x,y,10)
#new

turn=1

while n<64:
  def handle_mousemove(x,y,button):
  if button == 'left':
    turn = 2
  elif button == 'left':
    turn = 1
  n=n+1
  
if turn = 1:
  color(
    

