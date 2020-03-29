class ut_TicTacToe(object):
    """description of class"""
    from TicTacToe import Game
    def __init__(self, game:Game):
        self.game = game
        self.check_fresh_board()
        self.check_boards()
    def check_fresh_board(self):
        sucessful = True
        print("-----Building New Board-----")
        board = self.game.build_fresh_grid()
        legnth = len(board)
        if legnth != 3:
            print("board is the wrong legnth")
            sucessful = False
        for row in board:
            legnth = len(row)
            if legnth != 3:
                print("A row is the incorrect legnth")
                sucessful = False
            for tile in row:
                if tile != " ":
                    print("Fresh board failed to print clean board")
                    sucessful = False
        
        print("-----Ending New Board Test -----")
        return sucessful

    def check_boards(self):
        """
        checks that check_win_conditions returns correct values for each win case
        a player win should return 10
        an ai win should return -10
        a tie should return 0
        """
        succesful = True
        marker = self.game.player
        print(f"-----Starting check_winning_boards-----")
        winning_boards= [
            [
                [marker]*3,
                [" "]*3,
                [" "]*3
            ],
            [
                [" "]*3,
                [marker]*3,
                [" "]*3
            ],
            [
                [" "]*3,
                [" "]*3,
                [marker]*3
            ],
            [
                [marker, " ", " "],
                [marker, " ", " "],
                [marker, " ", " "]
            ],
            [
                [" ",marker, " "],
                [" ",marker, " "],
                [" ",marker, " "]
            ],
            [
                [" ", " ",marker],
                [" ", " ",marker],
                [" ", " ",marker]
            ],
            [
                [marker, " ", " "]
                ,[" ", marker," "],
                [" ", " ",marker]
            ],
            [
                [" ", " ", marker],
                [" ",marker, " "],
                [marker, " ", " "]
            ]
        ]
        for board in winning_boards:
                if self.game.check_win_conditions(board) != -10:
                    succesful = False
                    print(f"board failed checkWins \n{board}")
        marker = self.game.ai_player
        print(f"-----Starting check_winning_boards-----")
        winning_boards= [
            [
                [marker]*3,
                [" "]*3,
                [" "]*3
            ],
            [
                [" "]*3,
                [marker]*3,
                [" "]*3
            ],
            [
                [" "]*3,
                [" "]*3,
                [marker]*3
            ],
            [
                [marker, " ", " "],
                [marker, " ", " "],
                [marker, " ", " "]
            ],
            [
                [" ",marker, " "],
                [" ",marker, " "],
                [" ",marker, " "]
            ],
            [
                [" ", " ",marker],
                [" ", " ",marker],
                [" ", " ",marker]
            ],
            [
                [marker, " ", " "]
                ,[" ", marker," "],
                [" ", " ",marker]
            ],
            [
                [" ", " ", marker],
                [" ",marker, " "],
                [marker, " ", " "]
            ]
        ]
        for board in winning_boards:
                if self.game.check_win_conditions(board) != 10:
                    succesful = False
                    print(f"board failed checkWins \n{board}")
        
        tie_boards = [
            [   
                ["O","O","X"],
                ["X","O","O"],
                ["X","X"," "]
             ],
            [
                ["O","X"," "],
                [" ","X"," "],
                [" ","O"," "]
            ],
            [
                ['O', 'O', 'X'],
                ['X', 'X', 'O'],
                ['O', 'O', 'X']
            ]
            ]
        for board in tie_boards:
            if self.game.check_win_conditions(board) != 0:
                succesful = False
                print(f"board failed checkWins \n{board}")

        print(f"-----Ending check_winning_boards-----")

from TicTacToe import Game
game = Game("X")
ut_TicTacToe(game)
game = Game("O")
ut_TicTacToe(game)


    



