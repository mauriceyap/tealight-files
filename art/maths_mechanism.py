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
             [0,0,1,0,0,0,0,0],
             [2,2,1,2,2,1,0,0],
             [2,1,1,1,2,1,2,2]] 
turn=1

##1inserter
#for i in range (0,64):
#  def handle_mousedown(x,y,button):
#   if button == "left" and turn ==1:
#    boardArray [x][y]=1
#   if button == "left" and turn ==2:
#    boardArray [rowSelYellow][colSelYellow]=2 
  

print check_winner(boardArray)