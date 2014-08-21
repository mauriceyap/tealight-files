winnerRed=0
winnerYellow=0

boardArray =[[0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,1,0,0,0,0,0,0],
             [0,1,0,0,0,0,0,0],
             [0,1,0,0,0,0,0,0],
             [0,1,0,0,0,0,0,0]]


#winnerchecker
row = 0
col = 0

#verticals
for i in range (0,5):
  for i in range (0,8):
    if boardArray [row][col] ==boardArray [row +1][col]==boardArray [row +2][col]==boardArray [row+3][col]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row +1][col]==boardArray [row +2][col]==boardArray [row+3][col]==2:
      winnerYellow = 1
    col = col + 1
  col=0
  row = row+1



#declaration  
if winnerRed == 1:
  print 'Red is the winner'
if winnerYellow == 1:
  print 'Yellow is the winner'

#End Winner Cheecker