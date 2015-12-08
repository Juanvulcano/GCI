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

    def surrounded(self, row, col): #Determine all the neighbours of an item (HARD PART LOL)
        neighbours = 0 #This is not the best approach but it's the most readable
        if row == 0 and col == 0: # Quick hint, it looked better in my mind
            if self.board[row+1][col] == "X":
                    neighbours += 1
            if self.board[row+1][col+1] == "X":
                    neighbours += 1
            if self.board[row][col+1] == "X":
                    neighbours += 1

        if  1 <= row <= 2  and col == 0:	
            if self.board[row+1][col] == "X":
                    neighbours += 1
            if self.board[row+1][col+1] == "X":
                    neighbours += 1
            if self.board[row][col+1] == "X":
                    neighbours += 1
            if self.board[row-1][col] == "X":
                    neighbours += 1
            if self.board[row-1][col+1] == "X":
                    neighbours += 1

        if row == 0 and col == 3: 
            if self.board[row+1][col] == "X":
                    neighbours += 1
            if self.board[row+1][col-1] == "X":
                    neighbours += 1
            if self.board[row][col-1] == "X":
                    neighbours += 1
       
        if row == 3 and col == 3:
            if self.board[row-1][col] == "X":
                    neighbours += 1
            if self.board[row-1][col-1] == "X":
                    neighbours += 1
            if self.board[row][col-1] == "X":
                    neighbours += 1

        if row == 3 and col == 0:
            if self.board[row-1][col] == "X":
                    neighbours += 1
            if self.board[row-1][col+1] == "X":
                    neighbours += 1
            if self.board[row][col+1] == "X":
                    neighbours += 1

        if 1 <= row <= 2 and col == 3:
            if self.board[row+1][col] == "X":
                    neighbours += 1
            if self.board[row-1][col] == "X":
                    neighbours += 1
            if self.board[row-1][col-1] == "X":
                    neighbours += 1
            if self.board[row][col-1] == "X":
                    neighbours += 1
            if self.board[row+1][col-1] == "X":
                    neighbours += 1

        if row == 0 and 1 <= col <= 2:
            if self.board[row+1][col] == "X":
                    neighbours += 1
            if self.board[row+1][col+1] == "X":
                    neighbours += 1
            if self.board[row+1][col-1] == "X":
                    neighbours += 1                
            if self.board[row][col-1] == "X":
                    neighbours += 1
            if self.board[row][col+1] == "X":
                    neighbours += 1

        if row == 3 and 1 <= col <= 2:
            if self.board[row-1][col] == "X":
                    neighbours += 1
            if self.board[row-1][col+1] == "X":
                    neighbours += 1
            if self.board[row-1][col-1] == "X":
                    neighbours += 1
            if self.board[row][col-1] == "X":
                    neighbours += 1
            if self.board[row][col+1] == "X":
                    neighbours += 1

        if 1 <= row <= 2 and 1 <= col <= 2:  
            try:
                if self.board[row-1][col - 1] == "X":
                    neighbours += 1
            except IndexError:
                pass
            try:
                if self.board[row][col-1] == "X":
                    neighbours += 1
            except IndexError:
                pass
            try:
                if self.board[row+1][col - 1] == "X":
                    neighbours += 1
            except IndexError:
                pass
            try:
                if self.board[row-1][col] == "X":
                    neighbours += 1
            except IndexError:
                pass
            try:
                if self.board[row+1][col] == "X":
                    neighbours += 1
            except IndexError:
                pass
            try:
                if self.board[row-1][col+1] == "X":
                    neighbours += 1
            except IndexError:
                pass
            try:
                if self.board[row][col+1] == "X":
                    neighbours += 1
            except IndexError:
                pass
            try:
                if self.board[row+1][col+1] == "X":
                    neighbours += 1
            except IndexError:
                pass
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
