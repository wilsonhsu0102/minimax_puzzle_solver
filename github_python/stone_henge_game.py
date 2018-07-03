"""
An implementation of Stone Henge.
"""
from game import Game
from stone_henge_state import StoneHengeState


class StoneHengeGame(Game):
    """
    Abstract class for a game to be played with two players.
    """
    def __init__(self, p1_starts: bool) -> None:
        """
        Initialize this Game, using p1_starts to find who the first player is.

        :param p1_starts: A boolean representing whether Player 1 is the first
                          to make a move.
        :type p1_starts: bool
        """
        self.ll = ['I', 'II', 'III', 'IV', 'V', 'VI']
        self.size = int(input("Enter the size of the board: "))

        if self.size == 1:
            self.board = [{'I': ['@', 'A', 'B'],
                           'II': ['@', 'C']},
                          {'I': ['@', 'A', 'C'],
                           'II': ['@', 'B']},
                          {'I': ['@', 'A'],
                           'II': ['@', 'B', 'C']}]
        elif self.size == 2:
            self.board = [{'I': ['@', 'A', 'B'],
                           'II': ['@', 'C', 'D', 'E'],
                           'III': ['@', 'F', 'G']},
                          {'I': ['@', 'C', 'F'],
                           'II': ['@', 'A', 'D', 'G'],
                           'III': ['@', 'B', 'E']},
                          {'I': ['@', 'A', 'C'],
                           'II': ['@', 'B', 'D', 'F'],
                           'III': ['@', 'E', 'G']}]
        elif self.size == 3:
            self.board = [{'I': ['@', 'A', 'B'],
                           'II': ['@', 'C', 'D', 'E'],
                           'III': ['@', 'F', 'G', 'H', 'I'],
                           'IV': ['@', 'J', 'K', 'L']},
                          {'I': ['@', 'F', 'J'],
                           'II': ['@', 'C', 'G', 'K'],
                           'III': ['@', 'A', 'D', 'H', 'L'],
                           'IV': ['@', 'B', 'E', 'I']},
                          {'I': ['@', 'A', 'C', 'F'],
                           'II': ['@', 'B', 'D', 'G', 'J'],
                           'III': ['@', 'E', 'H', 'K'],
                           'IV': ['@', 'I', 'L']}]
        elif self.size == 4:
            self.board = [{'I': ['@', 'A', 'B'],
                           'II': ['@', 'C', 'D', 'E'],
                           'III': ['@', 'F', 'G', 'H', 'I'],
                           'IV': ['@', 'J', 'K', 'L', 'M', 'N'],
                           'V': ['@', 'O', 'P', 'Q', 'R']},
                          {'I': ['@', 'J', 'O'],
                           'II': ['@', 'F', 'K', 'P'],
                           'III': ['@', 'C', 'G', 'L', 'Q'],
                           'IV': ['@', 'A', 'D', 'H', 'M', 'R'],
                           'V': ['@', 'B', 'E', 'I', 'N']},
                          {'I': ['@', 'A', 'C', 'F', 'J'],
                           'II': ['@', 'B', 'D', 'G', 'K', 'O'],
                           'III': ['@', 'E', 'H', 'L', 'P'],
                           'IV': ['@', 'I', 'M', 'Q'],
                           'V': ['@', 'N', 'R']}]
        else:
            self.board = [{'I': ['@', 'A', 'B'],
                           'II': ['@', 'C', 'D', 'E'],
                           'III': ['@', 'F', 'G', 'H', 'I'],
                           'IV': ['@', 'J', 'K', 'L', 'M', 'N'],
                           'V': ['@', 'O', 'P', 'Q', 'R', 'S', 'T'],
                           'VI': ['@', 'U', 'V', 'W', 'X', 'Y']},
                          {'I': ['@', 'O', 'U'],
                           'II': ['@', 'J', 'P', 'V'],
                           'III': ['@', 'F', 'K', 'Q', 'W'],
                           'IV': ['@', 'C', 'G', 'L', 'R', 'X'],
                           'V': ['@', 'A', 'D', 'H', 'M', 'S', 'Y'],
                           'VI': ['@', 'B', 'E', 'I', 'N', 'T']},
                          {'I': ['@', 'A', 'C', 'F', 'J', 'O'],
                           'II': ['@', 'B', 'D', 'G', 'K', 'P', 'U'],
                           'III': ['@', 'E', 'H', 'L', 'Q', 'V'],
                           'IV': ['@', 'I', 'M', 'R', 'W'],
                           'V': ['@', 'N', 'S', 'X'],
                           'VI': ['@', 'T', 'Y']}]
        self.current_state = StoneHengeState(p1_starts, self.board)

    def get_instructions(self) -> str:
        """
        Return the instructions for this Game.

        :return: The instructions for this Game.
        :rtype: str
        """
        instructions = "Players take turns occupying spots" + \
            " on the board to own a ley-line. The winner is the" + \
                       "person who own half of the ley-lines."
        return instructions

    def is_over(self, state: "StoneHengeState") -> bool:
        """
        Return whether or not this game is over.

        :return: True if the game is over, False otherwise.
        :rtype: bool
        """
        p1_num = 0
        p2_num = 0
        num_ll = 0
        over = False
        for x in state.h_line:
            num_ll += 3
            if state.h_line[x][0] == 1:
                p1_num += 1
            if state.h_line[x][0] == 2:
                p2_num += 1
            if state.dr_line[x][0] == 1:
                p1_num += 1
            if state.dr_line[x][0] == 2:
                p2_num += 1
            if state.dl_line[x][0] == 1:
                p1_num += 1
            if state.dl_line[x][0] == 2:
                p2_num += 1
        if p1_num >= 0.5 * num_ll or p2_num >= 0.5 * num_ll:
            over = True
        return over

    def is_winner(self, player: str) -> bool:
        """
        Return whether player has won the game.

        Precondition: player is 'p1' or 'p2'.

        :param player: The player to check.
        :type player: str
        :return: Whether player has won or not.
        :rtype: bool
        """
        return (self.current_state.get_current_player_name() != player
                and self.is_over(self.current_state))

    def str_to_move(self, string: str) -> str:
        """
        Return the move that string represents. If string is not a move,
        return an invalid move.
        """
        return string


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
