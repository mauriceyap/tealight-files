from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["black", "yellow"]

n=1

while n < 100:

 for i in range(0,4):
  color ("black")
  move (50)
  color ("yellow")
  move (50)
  n = n + 1