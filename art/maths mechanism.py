boardArray =[[44,22,1,1,1,1,1,1],
             [1,9,1,1,1,1,1,1],
             [1,1,1,1,1,1,1,1],
             [1,1,1,1,1,1,1,1],
             [1,r,1,1,1,1,1,1],
             [1,r,1,1,1,1,1,1],
             [1,r,1,1,1,1,1,1],
             [1,1,1,1,1,1,1,1]]


boardArray [3][1] =r
row = 3
col = 1

if boardArray [row][col] ==boardArray [row +1][col]==boardArray [row +2][col]==boardArray [row+3][col]==r:
  winnerRed = 1

if boardArray [row][col] ==boardArray [row +1][col]==boardArray [row +2][col]==boardArray [row+3][col]==y:
  winnerYellow = 1
  
if winnerRed = 1:
  print 'Red is the winner'
if winnerYellow = 1:
  print 'Yellow is the winner'