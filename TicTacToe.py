class Menus(object):
    """contains all the games menus
    """
    
    def start_menu(self, selected:int = 2):
        """
        gives player options to play as each marker or exit the game
        """
        print("Welcome to TicTacToe written in Python 3.7")

        while True:
            print("Please Enter X or O to select Player. \nTo exit the game enter 1")
            selected = input()
            if selected == "1":
                print("And encase I don't see you, good afternoon, good evening and goodnight")
                break
            if selected.strip().upper() == "X":
                game = Game("X")
                game.start_game()
            elif selected.strip().upper() == "O" or selected.strip().upper() == "0": 
                game = Game("O")
                game.start_game()
            else:
                print(f"{selected} is not a valid input.")

    def game_menu(board):
        """
        Takes 2 user inputs to select the a tile
        If tile is not played then it'll return row, column else it will repeat
        """
        print("Please enter the row then column of the tile you want to play")
        while True:
            row = -1
            while 0>row or row>2:
                print("Please select a row")
                try:
                    row= int(input())
                except ValueError:
                    print("Enter a valid row 0-2")
            column = -1
            while 0> column or column>2:
                print("Please select a column")
                try:
                    column= int(input())
                except ValueError:
                    print("Enter a valid column 0-2")

            if board[row][column] != "X" or board[row][column] != "O":
                return row,column
            else:
                print(f"{row}, {column} is already taken by {board[row,column]}, Please Select an empty Tile")

 
class Game(object):
    def __init__(self, player:str):
        """
            Creates board and sets marker values for player and ai_player
        """
        self.board = self.build_fresh_grid()
        if player == "X": 
            self.player = "X"
            self.ai_player = "O"
        elif player == "O":
            self.player = "O"
            self.ai_player = "X"
        
    def start_game(self):
        """
            begins the game by resetting board and game_live, printing a welcome message and calling the firest game_round
        """
        print("*cannonfire* may the odds forever be in your favour")
        self.board = self.build_fresh_grid()
        self.game_live = True
        self.game_round()
        
    def build_fresh_grid(self):
        """
            returns a 3x3 board with " " as the value of each tile
        """
        board = [[" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]]
        return board

    def print_board(self):
        """
            clears the screen and prints the game goard
        """
        import subprocess as sp
        cls = sp.call('cls',shell=True)
        for row in self.board:
            print(row)

    def game_round(self, counter = 0):
        """
            checks if the game is tsill in play and calls player and ai_player turn. Once each player has completed their turn it calls itself until end of game
        """
        if counter > 8 or self.check_win_conditions(self.board) != 0:# used to exit game after 9 turns if no victory condition is found
            self.game_over(0)
            self.game_live = False
        else:
            #0's always go first
            if self.player == "O":
                if self.game_live == True and counter<9:
                    self.player_turn()
                    counter+=1
                    score = self.check_win_conditions(self.board)
                    if score == -10 or score == 10:
                        self.game_over(score)
                        self.game_live = False
                if self.game_live == True and counter<9:
                    self.ai_turn(self.board)
                    counter+=1
                    score = self.check_win_conditions(self.board)
                    if score == -10 or score == 10:
                        self.game_over(score)
            else:
                if self.game_live == True and counter<9:
                    self.ai_turn(self.board)
                    counter+=1
                    score = self.check_win_conditions(self.board)
                    if score == -10 or score == 10:
                        self.game_over(score)
                if self.game_live == True and counter<9:
                    self.player_turn()
                    counter+=1
                    score = self.check_win_conditions(self.board)
                    if score == -10 or score == 10:
                        self.game_over(score)
        if self.game_live == True:
            return  self.game_round(counter)
        
    def player_turn(self):
        """
            Calls game_menu to get user input and updates the board with their marker if tile is playable
        """
        while True:
            updated_values = Menus.game_menu(self.board)
            if self.board[updated_values[0]][updated_values[1]] == " ":
                self.board[updated_values[0]][updated_values[1]] = self.player
                break
            else:
                print("Tile has already been played")
        self.print_board()
                   
    def copy_board(self, board):
        """
            returns a copy of the board that is passed in
        """
        i=0
        board_copy = [[" "," "," "],[" "," "," "],[" "," "," "]]
        while i < len(self.board): # row
            k=0 
            while k < len(board[i]): #tile 
                board_copy[i][k] = board[i][k]
                k+= 1 
            i+= 1 
        return board_copy
    
    def check_live_board(self,board):
        """
            returns True if there are any playable tiles, False if not
        """
        x=0
        while x < 3:
            y=0
            while y < 3:
                tile = board[x][y]
                if  tile == " ":
                    return True
                y+=1
            x+=1
        return False
        
    def check_win_conditions(self,board):
        """ Checks to see if there's any victory and returns value of victor or False
            returns 10 if ai_player wins, returns 0 if a tie returns -10 if player wins
        """
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] == self.ai_player: # \ diagonal
            return 10
        elif board[0][2] == board[1][1] == board[2][0] and board[0][2] == self.ai_player: # / diagonal
            return 10
        elif board[0][0] == board[1][1] == board[2][2] and board[0][0] == self.player: # \ diagonal
            return -10
        elif board[0][2] == board[1][1] == board[2][0] and board[0][2] == self.player: # / diagonal
            return -10    
        k=0
        while k < 3:
            if board[0][k] == board[1][k] == board[2][k] and board[0][k] == self.ai_player: #collumn
                return 10
            elif board[k][0] == board[k][1] == board[k][2]and board[k][0] == self.ai_player: # row        
                return 10
            elif board[0][k] == board[1][k] == board[2][k] and board[0][k] == self.player: #collumn
                return -10
            elif board[k][0] == board[k][1] == board[k][2]and board[k][0] == self.player: # row 
                return -10
            k+=1
        return 0
        
    def game_over(self, winner):
        """
            prints a message based off the winner
            sets game_live to False
        """
        if winner == 0:
            print("It's was a close battle and in the end we have a tie")
        elif winner == 10:
            print(f"The AI has won")
        elif winner == -10:
            print("Congratz, you won")
        else:
            raise Invalid_Game_Over_Input(winner)
        self.game_live = False
               
    def ai_turn(self, board):
        """
            Uses minimax to select the optimal play on the board before printing the updated board
        """
        best_score = -1000
        move = [-1,-1]
        x=0
        while x<3:
            y=0
            while y<3:
                if board[x][y] == " ":
                    board[x][y] = self.ai_player
                    move_score = self.minimax(board,0, False)
                    board[x][y] = " "
                    if best_score< move_score:
                        best_score = move_score
                        move=[x,y]
                y+=1
            x+=1
        self.board[move[0]][move[1]] = self.ai_player
        print("_______________________")
        self.print_board()
        print("_______________________")

    def minimax(self, board,depth=0,min_or_max=False ):
        """
            minimax algorith to find best play in passed in board returns the best value based off score +/-depth
        """
        score = self.check_win_conditions(board)
        if score == 10: #maximizer
            return score -depth
        if score == -10: #minimizer 
            return score + depth
        if self.check_live_board(board) == False or depth>8:
            return 0

        if min_or_max: #maximizer
            best_value = -999
            x=0
            while x<3: #iterate board
                y=0
                while y<3:
                    if board[x][y] == " ": 
                        board[x][y] = self.ai_player
                        best_value = max(best_value, self.minimax(board, depth+1, not min_or_max))#call recursively and overwrite best_value when better
                        board[x][y] = " "
                    y+=1
                x+=1
            return best_value
        else: #minimizer
            best_value = 999
            x=0
            while x<3: #iterate board
                y=0
                while y<3:
                    if board[x][y] == " ": 
                        board[x][y] = self.player
                        best_value = min(best_value, self.minimax(board, depth+1, not min_or_max)) #call recursively and overwrite best_value when better
                        board[x][y] = " "
                    y+=1
                x+=1

            return best_value

class Invalid_Game_Over_Input(Exception):
    print(f"Invalid parameter passed into game_over: \n{input}")

#region testArea
menu = Menus()
menu.start_menu()

#endregion




#