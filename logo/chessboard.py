from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["black", "yellow"]
revColors = ["black", "yellow"]




while n <50:
 for i in range(0,4):
  color (colors [0])
  move (50)
  color (colors [1])
  move (50)
  
 turn (90)
 move (1)
 turn (90)

 for i in range(0,4):
  color (colors [1])
  move (50)
  color (colors [0])
  move (50)