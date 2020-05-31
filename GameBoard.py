#
#   @name: Morgan Van Valkenburgh
#   @date: May 14th 2020
#   @brief: 
#

import GameSpace

class GameBoard(object):
    def __init__(self):
        self.Board = []
        for i in range(8):
            self.Board.append([GameSpace.GameSpace('N')]*8)
        pass

    def print_board(self):
        self.Board[0][0].print_piece()
    pass
