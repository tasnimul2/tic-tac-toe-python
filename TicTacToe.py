'''

@project       : Queens College CSCI 381/780 Machine Learning
@Instructor    : Dr. Alex Pang

@Date          : Spring 2022

@Author        : Mohammed Chowdhury
A Object-Oriented Implementation of the TicTacToe Game 

references

'''

import enum

class GamePiece(enum.Enum):
    CROSS = "X"
    CIRCLE = "O"
    

class GameBoard(object):
    '''
    TODO: explain what the class is about, definition of various terms
    etc
    
    1. to run this project , in the terminal type : python TicTacToe.py
    2. in the "do you want to play?" prompt enter "y"
    3. enter a number between 1 to 9 to select which box you want to place your X or O.
    4. the program will print the current state of the board to make it easier for the user to pick the next spot.
    5. repeat steps 3 and 4 until game is over. 
    
    
    the GameBoard class is the implementation of the tac tac toe game. 
    
    the class is initialized with a list of lists called _board, to represent a 3x3 grid. 
    
    the display() method iterates through the _board list of lists and prints out each index in a tac tac toe table format. 
    the reset() method iterates through the _board list and numbers each index 1 to 9. 
    place_into() method uses an if else statement to see which spot the user wants to place their GamePiece. Then places the GamePiece value into the _board list.
    has_winner() method checks if any 3  across or diagonal values are the same GamePiece. If it is, then we have a winner.
    is_valid() method uses a helper method to see if the indicated spot is populated by a GamePiece already or if the spot chosen is invalid. 
    get_spot_value() method is a helper method that returns the list index that corresponds to the spot value. 
    
    '''
    
    def __init__(self):
        self.nsize = 3
        self._board = []
        for r in range(self.nsize):
            self._board.append(['' for c in range(self.nsize)])

        # set the board to its initial state
        self.reset()
        
    def display(self):
        '''
        display the game board which will look like something like this

           1 | X | 3
           4 | 5 | O
           7 | 8 | 9

        '''
        print(" ")
        # TODO
        for i in range(len(self._board)):
            for j in range(len(self._board[i])):
                if j == 1:
                    print(' | ' + self._board[i][j],end=' | ')
                else:
                    print(self._board[i][j],end='')
            
            print('\n')

        # end TODO

    def reset(self):
        '''
        Reset the game board so that each cell is index from 1 to 9.
        So when display it will look like

           1 | 2 | 3
           4 | 5 | 6
           7 | 8 | 9

        '''
        counter = 1
        # TODO
        for i in range(len(self._board)):
            for j in range(len(self._board[i])):
                self._board[i][j] = str(counter)
                counter+=1
        

        # end TODO


    
    def place_into(self, symbol, spot):
        '''
        Find the cell that spot is located, then replace the cell by 
        the symbol X or O
        '''
        # TODO
        if spot == '1':
            self._board[0][0] = symbol.value
        elif spot == '2':
            self._board[0][1] = symbol.value
        elif spot == '3':
            self._board[0][2] = symbol.value
        elif spot == '4':
            self._board[1][0] = symbol.value
        elif spot == '5':
            self._board[1][1] = symbol.value
        elif spot == '6':
            self._board[1][2] = symbol.value
        elif spot == '7':
            self._board[2][0] = symbol.value
        elif spot == '8':
            self._board[2][1] = symbol.value
        elif spot == '9':
            self._board[2][2] = symbol.value

        
        # end TODO


    def has_winner(self):
        '''
        Determine if one side has won (ie a winning row, column or a winning diagonal.
        If there is a winner, display who is the winner and return true
        otherwise return false
        '''
        # TODO
        if self.get_spot_value('1') == self.get_spot_value('2') == self.get_spot_value('3'):
            return True
        elif self.get_spot_value('4') == self.get_spot_value('5') == self.get_spot_value('6'):
            return True
        elif self.get_spot_value('7') == self.get_spot_value('8') == self.get_spot_value('9'):
            return True
        elif self.get_spot_value('1') == self.get_spot_value('4') == self.get_spot_value('7'):
            return True
        elif self.get_spot_value('2') == self.get_spot_value('5') == self.get_spot_value('8'):
            return True
        elif self.get_spot_value('3') == self.get_spot_value('6') == self.get_spot_value('9'):
            return True
        elif self.get_spot_value('1') == self.get_spot_value('5') == self.get_spot_value('9'):
            return True
        elif self.get_spot_value('3') == self.get_spot_value('5') == self.get_spot_value('7'):
            return True
        else:
            return False
        # end TODO

    def is_valid(self, spot):
        '''
        return true if spot is a valid location that you can place a symbol into
        ie. it has not been occupied by an X or an O
        '''

        # TODO
        
        if self.get_spot_value(spot) is None :
            return False
        elif self.get_spot_value(spot) == GamePiece.CIRCLE.value or self.get_spot_value(spot) == GamePiece.CROSS.value:
            return False
        
        # end TODO
        return True 
    
    def get_spot_value(self, spot):
        
        if spot == '1':
            return self._board[0][0]
        elif spot == '2':
            return self._board[0][1]
        elif spot == '3':
            return self._board[0][2]
        elif spot == '4':
            return self._board[1][0]
        elif spot == '5':
            return self._board[1][1]
        elif spot == '6':
            return self._board[1][2]
        elif spot == '7':
            return self._board[2][0]
        elif spot == '8':
            return self._board[2][1]
        elif spot == '9':
            return self._board[2][2]
        else :
            return None

    
def run():

    count = 0
    turn = GamePiece.CROSS
    
    start = input("Do you want to play Tic-Tac-Toe? (y/n)")
    if start.lower() == "y":
        board = GameBoard()
        board.display()
        
        while count < 9:

            print(f"It is {turn} turn. Which spot you want to pick?")
            spot = input()

            if board.is_valid(spot):
                board.place_into(turn, spot)

                #check if there is a winner, if yes, announce who is the winner
                # and close the game, otherwise set the turn to the other player
                board.display()
                # TODO
                if(board.has_winner()):
                    print("***********************")
                    print(f"THE WINNER IS PlAYER {turn.value}")
                    print("***********************")
                    break
                

                # end TODO
                
                count = count + 1
                if turn == GamePiece.CROSS:
                    turn = GamePiece.CIRCLE
                elif turn == GamePiece.CIRCLE:
                    turn = GamePiece.CROSS
                    
            else:
                print("Invalid spot. Please try again")
                
        
        if not board.has_winner() :
            print("***********************")
            print("  THE GAME IS A TIE")
            print("***********************")
            
        board.display()
        
        print("***********************")
        print("     GAVE OVER!!!!!!    ")
        print("***********************")
        #TODO announce it is a tie game
       
        #end TODO

#test method was created by me
def test():
    board = GameBoard()
    board.display()
    
    
if __name__ == "__main__":
    run()
