#head

from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.net import connect, send

from github.mauriceyap.art.check_winner import check_winner

#1The board

boardArray =[[0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,2,1,0,0,0,0,0],
             [0,0,2,0,0,0,0,0],
             [2,2,1,2,2,1,0,0],
             [0,0,1,1,2,1,2,2]] 
turn=1

##1inserter
#for i in range (0,64):
#  def handle_mousedown(x,y,button):
#   if button == "left" and turn ==1:
#    boardArray [x][y]=1
#   if button == "left" and turn ==2:
#    boardArray [rowSelYellow][colSelYellow]=2 
  

print check_winner(boardArray)

if check_winner =="red":
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

if check_winner =="red":
	color("yellow")
	spot(445,500,150)
	circle (445,500,170)

	color("black")
	text(390,480,"Yellow Wins!!!")
	image(310,490,"misc/WhiteBalloon.png")
	image(325,400,"misc/BlackBalloon.png")
	image(375,360,"misc/BlueBalloon.png")
	image(450,360,"misc/GreenBalloon.png")
	image(375,540,"misc/OrangeBalloon.png")
	image(450,540,"misc/PinkBalloon.png")
	image(510,400,"misc/RedBalloon.png")
	image(510,510,"misc/YellowBalloon.png")
    