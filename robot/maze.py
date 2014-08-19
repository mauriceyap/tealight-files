from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

for i in range (0,100):
 if left_side() == 'wall':
  for i in range (0,100):
   move()
   turn(1)
  if touch() == 'wall':
   turn(1)
  for i in range (0,100):
   move()
   if touch() == 'wall':
    turn(1)
  for i in range (0,100):
   move() 
  for i in range (0,100):
   move()

