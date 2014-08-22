#head

from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.net import connect, send


winnerRed=0
winnerYellow=0
reset=0

rowSelYellow=9
colSelYellow=9


#1Resetting Mechanism
if reset ==1:
 boardArray=[[0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0]] 

#1The board

boardArray =[[0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0]] 
turn=1

#1inserter
for i in range (0,64):
  def handle_mousedown(x,y,button):
   if button == "left" and turn ==1:
    boardArray [x][y]=1
   if button == "left" and turn ==2:
    boardArray [rowSelYellow][colSelYellow]=2 
  



#delete

color("red")
spot(445,500,150)

color("black")
text(390,480,"Red Wins!!!")
image(310,490,"misc/WhiteBalloon.png")
image(325,400,"misc/BlackBalloon.png")
image(375,360,"misc/BlueBalloon.png")
image(450,360,"misc/GreenBalloon.png")
image(375,540,"misc/OrangeBalloon.png")
image(450,540,"misc/PinkBalloon.png")
image(510,400,"misc/RedBalloon.png")
image(510,510,"misc/YellowBalloon.png")