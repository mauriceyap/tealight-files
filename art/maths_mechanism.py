#ALL FILES ARE HERE:
#http://mauriceyap.co.uk/connectfour/
#username: sutton
#password: sutton


#head

from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.net import connect, send

from github.mauriceyap.art.check_winner import check_winner

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

def drop_counter(col,turn):
  for i in range (7,-1,-1):
    if boardArray [i][col]==0:
      boardArray [i][col] = turn
      return

print check_winner(boardArray)