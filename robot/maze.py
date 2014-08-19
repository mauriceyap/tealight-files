from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

for i in range (0,10):
 if touch() == 'fruit':
  move()

if touch() == 'wall':
  turn(1)
  for i in range (0,10):
    move()
    
if touch() == 'wall':
 turn(-1)
 for i in range (0,20):
   move()
