winnerRed=0
winnerYellow=0
reset=0

rowSelYellow=9
colSelYellow=9

rowSelRed=0
colSelRed=0
rowSelRed=0
colSelRed=1
rowSelRed=0
colSelRed=2
rowSelRed=0
colSelRed=3

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
    boardArray [rowSelRed][colSelRed]=1
   if button == "right" and turn ==1:
    boardArray [rowSelYellow][colSelYellow]=2 
  

  
#1winnerchecker
row = 0
col = 0



#2verticals
for i in range (0,5):
  for i in range (0,8):
    if boardArray [row][col] ==boardArray [row +1][col]==boardArray [row +2][col]==boardArray [row+3][col]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row +1][col]==boardArray [row +2][col]==boardArray [row+3][col]==2:
      winnerYellow = 1
    col = col + 1
  col=0
  row = row+1

row = 0
col = 0

#2horizontals
for i in range (0,5):
  for i in range (0,8):
    if boardArray [row][col] ==boardArray [row][col+1]==boardArray [row][col+2]==boardArray [row][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row][col+1]==boardArray [row][col+2]==boardArray [row][col+3]==2:
      winnerYellow = 1
    row = row + 1
  row=0
  col=col+1

row = 0
col = 0

#2diagonals positive

row=3
col=0


for i in range (0,5):
    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
      winnerYellow = 1
    row = row + 1
  
row=4	
col=0

for i in range (0,4):
    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
      winnerYellow = 1
    row = row + 1

row=5	
col=0

for i in range (0,3):
    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
      winnerYellow = 1
    row = row + 1

row=6	
col=0

for i in range (0,2):
    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
      winnerYellow = 1
    row = row + 1

row=7	
col=0

for i in range (0,1):
    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
      winnerYellow = 1
    row = row + 1

row=3	
col=1

for i in range (0,5):
    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
      winnerYellow = 1
    row = row + 1

row=4	
col=1

for i in range (0,4):
    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
      winnerYellow = 1
    row = row + 1

row=5	
col=1

for i in range (0,3):
    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
      winnerYellow = 1
    row = row + 1

row=6	
col=1

for i in range (0,2):
    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
      winnerYellow = 1
    row = row + 1

row=7	
col=1

for i in range (0,1):
    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
      winnerYellow = 1
    row = row + 1

row=3	
col=2

for i in range (0,5):
    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
      winnerYellow = 1
    row = row + 1

row=4	
col=2

for i in range (0,4):
    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
      winnerYellow = 1
    row = row + 1

row=5	
col=2

for i in range (0,3):
    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
      winnerYellow = 1
    row = row + 1

row=6	
col=2

for i in range (0,2):
    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
      winnerYellow = 1
    row = row + 1

row=7	
col=2

for i in range (0,1):
    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
      winnerYellow = 1
    row = row + 1

row=3	
col=3

for i in range (0,5):
    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
      winnerYellow = 1
    row = row + 1

row=4	
col=3

for i in range (0,4):
    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
      winnerYellow = 1
    row = row + 1

row=5	
col=3

for i in range (0,3):
    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
      winnerYellow = 1
    row = row + 1

row=6	
col=3

for i in range (0,2):
    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
      winnerYellow = 1
    row = row + 1

row=7	
col=3

for i in range (0,1):
    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
      winnerYellow = 1
    row = row + 1

row=3	
col=4

for i in range (0,5):
    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
      winnerYellow = 1
    row = row + 1

row=4	
col=4

for i in range (0,4):
    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
      winnerYellow = 1
    row = row + 1

row=5	
col=4

for i in range (0,3):
    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
      winnerYellow = 1
    row = row + 1

row=6	
col=4

for i in range (0,2):
    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
      winnerYellow = 1
    row = row + 1

row=7	
col=4

for i in range (0,1):
    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row-1][col+1]==boardArray [row-2][col+2]==boardArray [row-3][col+3]==2:
      winnerYellow = 1
    row = row + 1

#2diag neg

row=0
col=4

for i in range (0,5):
    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
      winnerYellow = 1
    row = row + 1
row=1
col=4

for i in range (0,4):
    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
      winnerYellow = 1
    row = row + 1
row=2
col=4

for i in range (0,3):
    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
      winnerYellow = 1
    row = row + 1
row=3
col=4

for i in range (0,2):
    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
      winnerYellow = 1
    row = row + 1
row=4
col=4

for i in range (0,1):
    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
      winnerYellow = 1
    row = row + 1
row=0
col=3

for i in range (0,5):
    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
      winnerYellow = 1
    row = row + 1
row=1
col=3

for i in range (0,4):
    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
      winnerYellow = 1
    row = row + 1
row=2
col=3

for i in range (0,3):
    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
      winnerYellow = 1
    row = row + 1
row=3
col=3

for i in range (0,2):
    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
      winnerYellow = 1
    row = row + 1
row=4
col=3

for i in range (0,1):
    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
      winnerYellow = 1
    row = row + 1
row=0
col=2

for i in range (0,5):
    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
      winnerYellow = 1
    row = row + 1
row=1
col=2

for i in range (0,4):
    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
      winnerYellow = 1
    row = row + 1
row=2
col=2

for i in range (0,3):
    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
      winnerYellow = 1
    row = row + 1
row=3
col=2

for i in range (0,2):
    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
      winnerYellow = 1
    row = row + 1
row=4
col=2

for i in range (0,1):
    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
      winnerYellow = 1
    row = row + 1
row=0
col=1

for i in range (0,5):
    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
      winnerYellow = 1
    row = row + 1
row=1
col=1

for i in range (0,4):
    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
      winnerYellow = 1
    row = row + 1
row=2
col=1

for i in range (0,3):
    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
      winnerYellow = 1
    row = row + 1
row=3
col=1

for i in range (0,2):
    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
      winnerYellow = 1
    row = row + 1
row=4
col=1

for i in range (0,1):
    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
      winnerYellow = 1
    row = row + 1
row=0
col=0

for i in range (0,5):
    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
      winnerYellow = 1
    row = row + 1
row=1
col=0

for i in range (0,4):
    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
      winnerYellow = 1
    row = row + 1
row=2
col=0

for i in range (0,3):
    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
      winnerYellow = 1
    row = row + 1
row=3
col=0

for i in range (0,2):
    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
      winnerYellow = 1
    row = row + 1
row=4
col=0

for i in range (0,1):
    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==1:
      winnerRed = 1

    if boardArray [row][col] ==boardArray [row+1][col+1]==boardArray [row+2][col+2]==boardArray [row+3][col+3]==2:
      winnerYellow = 1
    row = row + 1


  


row = 0
col = 0




#2declaration  
if winnerRed == 1:
  print 'Red is the winner'
if winnerYellow == 1:
  print 'Yellow is the winner'

#End Winner Checker