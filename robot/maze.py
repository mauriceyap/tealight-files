from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

for i in range (0,10):
 if touch() == None:
  move()

 if touch() == 'wall':
  turn(1)
  move()
 if touch() == 'wall':
  turn(-1)
  move()   

