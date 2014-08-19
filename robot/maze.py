from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

for i in range (0,1250):
  
 if touch() == None and left_side() == 'wall':
   move()
    
 if touch() == None and left_side() == None:
   turn (-1)
   
 if touch() == 'wall' and left_side() == None:
   turn(-1)
      
 if touch() == 'wall' and right_side() == None:
    turn(1)
    
 if touch() == 'wall' and left_side() == 'wall' and right_side() == 'wall':
    turn (2)

