"""
A class to record the states in the game Stone Henge
"""
import copy
from game_state import GameState


class StoneHengeState(GameState):
    """
    The state of the game at certain point in time
    """

    def __init__(self, is_p1_turn: bool, current_board: list) -> None:
        """
        Initialize this game state and set the current player based on
        is_p1_turn.
        """
        self.letters = []
        for letter in range(ord('A'), ord('Z') + 1):
            self.letters.append(chr(letter))
        super().__init__(is_p1_turn)
        self.h_line = current_board[0]
        self.dr_line = current_board[1]
        self.dl_line = current_board[2]

    def __str__(self) -> str:
        """
        Return a string representation of the current state of the game.
        """
        if len(self.h_line.keys()) == 2:
            board = """    
                          {}   {}
                          /   /
                    {} - {} - {}
                         \\ / \\
                      {} - {}   {}
                           \\
                            {} 
                    """.format(self.dl_line['I'][0],
                               self.dl_line['II'][0],
                               self.h_line['I'][0],
                               self.h_line['I'][1],
                               self.h_line['I'][2],
                               self.h_line['II'][0],
                               self.h_line['II'][1],
                               self.dr_line['II'][0],
                               self.dr_line['I'][0])

        elif len(self.h_line.keys()) == 3:
            board = """      
                            {}   {}
                            /   /
                      {} - {} - {}   {}
                         / \\ / \\ /
                    {} - {} - {} - {}
                         \\ / \\ / \\
                      {} - {} - {}   {}
                           \\   \\
                            {}   {}
                    """.format(self.dl_line['I'][0],
                               self.dl_line['II'][0],
                               self.h_line['I'][0],
                               self.h_line['I'][1],
                               self.h_line['I'][2],
                               self.dl_line['III'][0],
                               self.h_line['II'][0],
                               self.h_line['II'][1],
                               self.h_line['II'][2],
                               self.h_line['II'][3],
                               self.h_line['III'][0],
                               self.h_line['III'][1],
                               self.h_line['III'][2],
                               self.dr_line['III'][0],
                               self.dr_line['I'][0],
                               self.dr_line['II'][0])

        elif len(self.h_line.keys()) == 4:
            board = """
                         {}   {}
                        /   /
                   {} - {} - {}   {}
                      / \\ / \\ /
                {} - {} -  {} - {}   {}
                   / \\  / \\ / \\ /
              {} - {} - {} -  {} - {}   
                   \\ / \\  / \\ / \\
                {} - {} - {}  - {}   {}
                     \\    \\   \\
                      {}    {}   {}
            """.format(self.dl_line['I'][0], self.dl_line['II'][0],
                       self.h_line['I'][0], self.h_line['I'][1],
                       self.h_line['I'][2], self.dl_line['III'][0],
                       self.h_line['II'][0], self.h_line['II'][1],
                       self.h_line['II'][2], self.h_line['II'][3],
                       self.dl_line['IV'][0], self.h_line['III'][0],
                       self.h_line['III'][1], self.h_line['III'][2],
                       self.h_line['III'][3], self.h_line['III'][4],
                       self.h_line['IV'][0], self.h_line['IV'][1],
                       self.h_line['IV'][2], self.h_line['IV'][3],
                       self.dr_line['IV'][0], self.dr_line['I'][0],
                       self.dr_line['II'][0], self.dr_line['III'][0])

        elif len(self.h_line.keys()) == 5:
            board = """
                         {}   {}
                        /   /
                   {} - {} - {}   {}
                      / \\ / \\ /
                {} - {} - {}  - {}   {}
                   / \\ / \\  / \\ /
              {} - {} - {} -  {} - {}   {}
                 / \\ / \\  / \\ / \\ /
            {} - {} - {} - {} -  {} - {}  
                 \\ / \\ / \\  / \\ / \\ 
              {} - {} - {} - {}  - {}   {}
                   \\   \\   \\    \\   
                    {}   {}   {}    {}
            """.format(self.dl_line['I'][0], self.dl_line['II'][0],
                       self.h_line['I'][0], self.h_line['I'][1],
                       self.h_line['I'][2], self.dl_line['III'][0],
                       self.h_line['II'][0], self.h_line['II'][1],
                       self.h_line['II'][2], self.h_line['II'][3],
                       self.dl_line['IV'][0], self.h_line['III'][0],
                       self.h_line['III'][1], self.h_line['III'][2],
                       self.h_line['III'][3], self.h_line['III'][4],
                       self.dl_line['V'][0], self.h_line['IV'][0],
                       self.h_line['IV'][1], self.h_line['IV'][2],
                       self.h_line['IV'][3], self.h_line['IV'][4],
                       self.h_line['IV'][5], self.h_line['V'][0],
                       self.h_line['V'][1], self.h_line['V'][2],
                       self.h_line['V'][3], self.h_line['V'][4],
                       self.dr_line['V'][0], self.dr_line['I'][0],
                       self.dr_line['II'][0], self.dr_line['III'][0],
                       self.dr_line['IV'][0])

        else:
            board = """
                             {}   {}
                            /   /
                      {} - {} - {}    {}
                         / \\ /  \\ /
                    {} - {} - {}  - {}   {}
                       / \\ / \\  / \\ /
                  {} - {} - {} -  {} - {}   {}
                     / \\ /  \\ / \\ / \\ /
                {} - {} - {} -  {} - {} - {}   {}
                   / \\ / \\  / \\ / \\ / \\ /
              {} - {} - {} - {} - {} - {}  - {}   
                   \\ / \\ / \\ / \\ / \\ /  \\
                {} - {} - {} - {} - {} - {}    {}
                     \\   \\   \\   \\   \\
                      {}   {}   {}   {}   {}
            """.format(self.dl_line['I'][0], self.dl_line['II'][0],
                       self.h_line['I'][0], self.h_line['I'][1],
                       self.h_line['I'][2], self.dl_line['III'][0],
                       self.h_line['II'][0], self.h_line['II'][1],
                       self.h_line['II'][2], self.h_line['II'][3],
                       self.dl_line['IV'][0], self.h_line['III'][0],
                       self.h_line['III'][1], self.h_line['III'][2],
                       self.h_line['III'][3], self.h_line['III'][4],
                       self.dl_line['V'][0], self.h_line['IV'][0],
                       self.h_line['IV'][1], self.h_line['IV'][2],
                       self.h_line['IV'][3], self.h_line['IV'][4],
                       self.h_line['IV'][5], self.dl_line['VI'][0],
                       self.h_line['V'][0], self.h_line['V'][1],
                       self.h_line['V'][2], self.h_line['V'][3],
                       self.h_line['V'][4], self.h_line['V'][5],
                       self.h_line['V'][6], self.h_line['VI'][0],
                       self.h_line['VI'][1], self.h_line['VI'][2],
                       self.h_line['VI'][3], self.h_line['VI'][4],
                       self.h_line['VI'][5], self.dr_line['VI'][0],
                       self.dr_line['I'][0], self.dr_line['II'][0],
                       self.dr_line['III'][0], self.dr_line['IV'][0],
                       self.dr_line['V'][0])

        return board

    def get_possible_moves(self) -> list:
        """
        Return all possible moves that can be applied to this state.

        >>> j = StoneHengeState(True, [{'I': ['@', 'A', 'B'], \
        'II': ['@', 'C']}, \
        {'I': ['@', 'A', 'C'], \
        'II': ['@', 'B']}, \
        {'I': ['@', 'A'], \
        'II': ['@', 'B', 'C']}])
        >>> j.get_possible_moves()
        ['A', 'B', 'C']
        >>> s = StoneHengeState(True, [{'I': [1, 'A', 1], \
        'II': ['@', 'C']}, \
        {'I': ['@', 'A', 'C'], \
        'II': [1, 1]}, \
        {'I': ['@', 'A'], \
        'II': [1, 1, 'C']}])
        >>> s.get_possible_moves()
        []
        """
        possible_moves = []
        p1_num = 0
        p2_num = 0
        num_ll = 0
        over = False
        for x in self.h_line:
            num_ll += 3
            if self.h_line[x][0] == 1:
                p1_num += 1
            if self.h_line[x][0] == 2:
                p2_num += 1
            if self.dr_line[x][0] == 1:
                p1_num += 1
            if self.dr_line[x][0] == 2:
                p2_num += 1
            if self.dl_line[x][0] == 1:
                p1_num += 1
            if self.dl_line[x][0] == 2:
                p2_num += 1
        if p1_num >= 0.5 * num_ll or p2_num >= 0.5 * num_ll:
            over = True
        if over:
            return []

        for x in self.h_line:
            for i in self.h_line[x]:
                if i in self.letters:
                    possible_moves.append(i)
        return possible_moves

    def make_move(self, move: str) -> "StoneHengeState":
        """
        Return the a new GameState that results from
        applying move to the original GameState.
        """
        num = 1
        if self.get_current_player_name() == 'p2':
            num = 2
        d1 = copy.deepcopy(self.h_line)
        d2 = copy.deepcopy(self.dr_line)
        d3 = copy.deepcopy(self.dl_line)

        for x in d1:
            for i in d1[x]:
                if i == move:
                    d1[x][d1[x].index(i)] = num
            for j in d2[x]:
                if j == move:
                    d2[x][d2[x].index(j)] = num
            for k in d3[x]:
                if k == move:
                    d3[x][d3[x].index(k)] = num
        for d in d1:
            if (d1[d].count(1) >= 0.5 * (len(d1[d]) - 1)) and d1[d][0] == '@':
                d1[d][0] = 1
            if (d1[d].count(2) >= 0.5 * (len(d1[d]) - 1)) and d1[d][0] == '@':
                d1[d][0] = 2
            if (d2[d].count(1) >= 0.5 * (len(d2[d]) - 1)) and d2[d][0] == '@':
                d2[d][0] = 1
            if (d2[d].count(2) >= 0.5 * (len(d2[d]) - 1)) and d2[d][0] == '@':
                d2[d][0] = 2
            if (d3[d].count(1) >= 0.5 * (len(d3[d]) - 1)) and d3[d][0] == '@':
                d3[d][0] = 1
            if (d3[d].count(2) >= 0.5 * (len(d3[d]) - 1)) and d3[d][0] == '@':
                d3[d][0] = 2

        new_state = StoneHengeState(not self.p1_turn, [d1, d2, d3])
        return new_state

    def __repr__(self) -> str:
        """
        Return a representation of this state (which can be used for
        equality testing).
        """
        return "P1's Turn: {} - Current Board: {}".format(self.p1_turn,
                                                          self.__str__())

    def rough_outcome(self) -> float:
        """
        Return an estimate in interval [LOSE, WIN] of best outcome the current
        player can guarantee from state self.

        >>> j = StoneHengeState(True, [{'I': ['@', 'A', 'B'], \
        'II': ['@', 'C']}, \
        {'I': ['@', 'A', 'C'], \
        'II': ['@', 'B']}, \
        {'I': ['@', 'A'], \
        'II': ['@', 'B', 'C']}])
        >>> j.rough_outcome()
        1
        >>> j = StoneHengeState(True, [{'I': [1, 1, 'B'], \
        'II': ['@', 'C']}, \
        {'I': [1, 1, 'C'], \
        'II': ['@', 'B']}, \
        {'I': [1, 1], \
        'II': ['@', 'B', 'C']}])
        >>> j.rough_outcome()
        -1
        """

        x = [self.make_move(move) for move in self.get_possible_moves()]
        if any([j.get_possible_moves() == [] for j in x]):
            return self.WIN

        checker = []
        for state in x:
            new_state = [state.make_move(moves) for moves in
                         state.get_possible_moves()]
            if any([k.get_possible_moves() == [] for k in new_state]):
                checker.append('OK')
        if checker.count('OK') == len(x):
            return self.LOSE
        return self.DRAW


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
