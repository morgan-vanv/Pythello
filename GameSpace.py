#
#   @name: Morgan Van Valkenburgh
#   @date: May 14th 2020
#   @brief: 
#

class GameSpace(object):
    def __init__(self, p_type):
        self.piece_type = p_type

    def is_white(self):
        pass

    def is_black(self):
        pass

    def is_empty(self):
        pass

    def set_white(self):
        pass

    def set_black(self):
        pass

    def set_empty(self):
        pass

    def flip_piece(self):
        pass

    def print_piece(self):
        print(self.piece_type)
    pass
