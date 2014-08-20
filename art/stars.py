from tealight.art import (color, line, spot, circle, box, image, text, background)

from math import sin, cos, pi

def ellipse(x, y, c, sizex, sizey, spines):
  
  color(c)
  
  angle = 0
  
  for i in range(0, spines):
    x0 = x + (sizex * cos(angle))
    y0 = y + (sizey * sin(angle))
    
    line(x, y, x0, y0)
    
    angle = angle + 1

ellipse(300, 300, "blue", 100, 50, 3)
ellipse(600, 400, "purple", 200,50, 3)
ellipse(450, 200, "orange", 125,50, 3)