boardArray =[[44,22,1,1,1,1,1,1],
             [1,9,1,1,1,1,1,1],
             [1,1,1,1,1,1,1,1],
             [1,1,1,1,1,1,1,1],
             [1,1,1,1,1,1,1,1],
             [1,1,1,1,1,1,1,1],
             [1,1,1,1,1,1,1,1],
             [1,1,1,1,1,1,1,1]]


boardArray [3][1] =6
row = 3
col = 1

if boardArray [row][col] ==boardArray [row +1][col]==boardArray [row +2][col]==boardArray [row+3][col]:
  print 'winner'
