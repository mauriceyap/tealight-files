winnerRed=0
winnerYellow=0

boardArray =[[0,0,0,0,0,0,0,0],
             [0,0,0,1,0,0,0,0],
             [0,0,0,1,0,0,0,0],
             [0,0,0,1,0,0,0,0],
             [1,0,0,1,0,0,0,0],
             [1,0,0,1,0,0,0,0],
             [1,1,1,1,0,0,0,0],
             [1,0,0,0,0,0,0,0]]



row = 0
col = 0
j=1

for i in range (0,8):
  for j in range (0,3):
    if boardArray [row][col] ==boardArray [row +1][col]==boardArray [row +2][col]==boardArray [row+3][col]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row +1][col]==boardArray [row +2][col]==boardArray [row+3][col]==2:
      winnerYellow = 1
    row = row+1
    j=j+1
  col = col + 1
  
  
if winnerRed == 1:
  print 'Red is the winner'
if winnerYellow == 1:
  print 'Yellow is the winner'