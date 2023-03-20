"""
This module defines a `Board` class representing a board for the Tic-Tac-Toe game.
"""


class Board:
    """ A class representing a board for a Tic-Tac-Toe game. """
    def __init__(self):
        self._board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def get_board(self):
        """ Gets the current state of the board. """
        return self._board

    def update_board(self, player, cell_number):
        """Updates the state of the board."""
        for row in range(len(self._board)):
            for col in range(len(self._board[row])):
                if self._board[row][col] == int(cell_number):
                    self._board[row][col] = player


    def __str__(self):
        """ Returns a formatted string representation of the board. """
        board_layout = "************************\n"\
                    "*    Current Board!    *\n"\
                    "************************\n"\
                    "*                      *\n"\
                    "*    {}  |  {}  |  {}     *\n"\
                    "*  ------------------  *\n"\
                    "*    {}  |  {}  |  {}     *\n"\
                    "*  ------------------  *\n"\
                    "*    {}  |  {}  |  {}     *\n"\
                    "*                      *\n"\
                    "************************"

        formatted_board = board_layout.format(*[elem for row in self._board for elem in row])
        return formatted_board
