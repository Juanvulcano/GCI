import random

board = []
for x in range(0,4):
    board.append([0] * 4) #Create list of lists 4 x 4
    
class Board(object):
    def __init__(self, board):
	    self.board = board
   
    def shuffle(self):
        treasures = 9
        while treasures:
            row = random.randint(0, len(self.board)-1)
            col = random.randint(0, len(self.board[0])-1)	
            if self.board[row][col] != 1:
                    self.board[row][col] = 1
                    treasures = treasures-1
        #Linear time algorithm
        for array in range(len(self.board)):
            for item in range(len(self.board[0])):
                if self.board[array][item] == 0:
                    self.board[array][item] = -1 

    def surrounded(self, row, col): #Determine all the neighbours of an item - This approach took me some time
        neighbours = 0 #This is the best approach :)
        row_limit = len(self.board);
        if row_limit > 1:
            column_limit = len(self.board[0]);
            for x in range(max(0, row-1), min(row+2, row_limit)):
                for y in range(max(0, col-1),min(col+2, column_limit)):
                    if x != row or y != col:
                        if self.board[x][y] == 1:
                            neighbours = neighbours + 1;
        return str(neighbours)
    

    def final(self):
       for x in range(0,len(self.board)):
          for number in range(0,len(self.board[x])):
              if self.board[x][number] == 0:
                    self.board[x][number] = self.surrounded(x, number)	
       return self.board

Finish = Board(board)
Finish.shuffle() # Assign random cards  
Finish.final() #Change empty spaces for their corresponding adjacent treasures
