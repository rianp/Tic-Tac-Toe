"""
This module contains the `main` function that creates any
necessary objects and calls functions to execute the program's logic.
"""
from console import *
from board import *
from score import *
from players import *
from turn import *


def main():
    """ Creates any necessary objects and calls functions to execute the program's logic. """
    game = Board()
    players = Players()
    turn = Turn()
    Console.print_string("Hello friend, welcome to Tic-Tac-Toe!")

    message = """
*------------------------------------------------------------*  
* Here are the instructions to the game!                     *
*------------------------------------------------------------*
* 1. there are two players in the game (X and O)             *
* 2. a game has nine fields in a 3x3 grid                    *
* 3. a player can take a field if not already taken          *
* 4. players take turns taking fields until the game is over *
* 5. a game is over when:                                    *
*   - all fields in a row are taken by a player              *
*   - all fields in a column are taken by a player           *
*   - all fields in a diagonal are taken by a player         *
*   - all fields are taken                                   *
*------------------------------------------------------------* 
"""
    Console.print_string(message)

    while True:
        turn.change_turn(players)
        Console.print_string(str(game))

        user_input = Console.prompt_input(f'\nHi {turn.get_current_turn()[0]}! Enter a value please: ')
        game.update_board(turn.get_current_turn()[1], user_input)
        Console.print_string(str(game))

        if Score().get_game_status(game.get_board()):
            break

if __name__ == "__main__":
    main()
