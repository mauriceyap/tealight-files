from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "green", "blue"]

for i in range(0,200):
  move(i)
  turn(90)
  color(colors[i%3])