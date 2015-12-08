import random

board = []
for x in range(0,4):
    board.append(["O"] * 4) #Create list of lists 4 x 4
    
class Board(object):
    def __init__(self, board):
	    self.board = board
   
    def print_board(self):
        for row in self.board:
            print " ".join(row)
        # Print board function

    def shuffle(self):
        treasures = 9
        while treasures:
            row = random.randint(0, len(self.board)-1)
            col = random.randint(0, len(self.board[0])-1)	
            if self.board[row][col] != "X":
                    self.board[row][col] = "X"
                    treasures = treasures-1
        #Assign random card function

    def surrounded(self, row, col): #Determine all the neighbours of an item - This approach took me some time
        neighbours = 0 #This is the best approach :)
        row_limit = len(self.board);
        if row_limit > 1:
            column_limit = len(self.board[0]);
            for x in range(max(0, row-1), min(row+2, row_limit)):
                for y in range(max(0, col-1),min(col+2, column_limit)):
                    if x != row or y != col:
                        if self.board[x][y]== "X":
                            neighbours = neighbours + 1;
        return str(neighbours)
    

    def final(self):
       for x in range(0,len(self.board)):
          for number in range(0,len(self.board[x])):
              if self.board[x][number] == "O":
                    self.board[x][number] = self.surrounded(x, number)	
       return self.board

Finish = Board(board)
print Finish.print_board() # Normal Board Game function
Finish.shuffle() # Assign random cards 
print Finish.print_board() # Debug function = Print board after random 
Finish.final() #Change empty spaces for their corresponding adjacent treasures
print Finish.print_board()#Glorious ending
