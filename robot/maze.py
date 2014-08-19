from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

for i in range (0,100):
 if left_side() == 'wall' and touch() == None:
   move()
   
 if touch() == 'wall' and left_side() == 'None':
   turn(-1)
      
 if touch() == 'wall' and right_side() == 'None':
    turn(1)

