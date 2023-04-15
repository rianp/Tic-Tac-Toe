class Players:

    def __init__(self, player_1, player_2):
        self._players = (player_1, player_2)
        self._turn = 1

    def get_players(self):
        return self._players

    def change_turn(self):
        if self._turn == 1:
            self._turn = 2
        else:
            self._turn = 1

    def get_current_player(self):
        return self._players[self._turn - 1]
