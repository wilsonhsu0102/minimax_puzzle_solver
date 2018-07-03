"""
A module for strategies.

NOTE: Make sure this file adheres to python-ta.
Adjust the type annotations as needed, and implement both a recursive
and an iterative version of minimax.
"""
from typing import Any, List
from tree import Tree
from stack import Stack


# TODO: Adjust the type annotation as needed.
def interactive_strategy(game: Any) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def rough_outcome_strategy(game: Any) -> Any:
    """
    Return a move for game by picking a move which results in a state with
    the lowest rough_outcome() for the opponent.

    NOTE: game.rough_outcome() should do the following:
        - For a state that's over, it returns the score for the current
          player of that state.
        - For a state that's not over:
            - If there is a move that results in the current player winning,
              return 1.
            - If all moves result in states where the other player can
              immediately win, return -1.
            - Otherwise; return a number between -1 and 1 corresponding to how
              'likely' the current player will win from the current state.

        In essence: rough_outcome() will only look 1 or 2 states ahead to
        'guess' the outcome of the game, but no further. It's better than
        random, but worse than minimax.
    """
    current_state = game.current_state
    best_move = None
    best_outcome = -2  # Temporarily -- just so we can replace this easily later

    # Get the move that results in the lowest rough_outcome for the opponent
    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(move)

        # We multiply the below by -1 since a state that's bad for the opponent
        # is good for us.
        guessed_score = new_state.rough_outcome() * -1
        if guessed_score > best_outcome:
            best_outcome = guessed_score
            best_move = move

    # Return the move that resulted in the best rough_outcome
    return best_move


# TODO: Implement a recursive version of the minimax strategy.
def re_minimax(game: Any) -> Any:
    """
    Play a move that guarantee a win for the current player. Using recursive
    implementation
    """

    state = game.current_state
    player = state.get_current_player_name()
    lst = [recursive_helper(game, x, state, player)
           for x in state.get_possible_moves()]
    pos_move = state.get_possible_moves()

    if 1 in lst:
        return pos_move[lst.index(1)]

    elif 0 in lst:
        return pos_move[lst.index(0)]

    return pos_move[0]


def recursive_helper(game: Any, move: Any, starting_state: Any,
                     player: str) -> int:
    """
    A helper for re_minimax, returns the score of the starting_state
    after applying move
    """
    new_state = starting_state.make_move(move)
    game.current_state = new_state

    if game.is_over(new_state):
        if game.is_winner(player):
            return 1
        elif not game.is_winner(player) and \
                not game.is_winner(opponent(player)):
            return 0
        return -1

    elif new_state.get_current_player_name() == player:
        return max([recursive_helper(game, move1, new_state, player)
                    for move1 in new_state.get_possible_moves()])

    return min([recursive_helper(game, move2, new_state, player)
                for move2 in new_state.get_possible_moves()])


# TODO: Implement an iterative version of the minimax strategy.
def it_minimax(game: Any) -> Any:
    """
    Play a move that guarantee a win for the current player.
    Using iterative implementation
    """
    start = game.current_state
    lst = iterative_helper(game, start)
    pos_move = start.get_possible_moves()

    if 1 in lst:
        return pos_move[lst.index(1)]

    elif 0 in lst:
        return pos_move[lst.index(0)]

    return pos_move[0]


def iterative_helper(game: Any, start: Any) -> List[int]:
    """
    A helper for it_minimax, returns a list containing the score
    of the possible moves
    """
    storage = []
    s = Stack()
    s.add([Tree(start), None])
    while not s.is_empty():
        data = s.remove()

        if not game.is_over(data[0].value) and data[0].children == []:
            intermediate = []
            for move in data[0].value.get_possible_moves():
                intermediate.append([Tree(data[0].value.make_move(move)), None])
            s.add([Tree(data[0].value, intermediate), None])
            for rest in intermediate:
                s.add(rest)

        elif game.is_over(data[0].value):
            game.current_state = data[0].value
            player = data[0].value.get_current_player_name()
            if game.is_winner(player):
                data[1] = 1
            elif not game.is_winner(player) and not game.\
                    is_winner(opponent(player)):
                data[1] = 0
            else:
                data[1] = -1
            storage.append(data)

        else:
            num = []
            for i in data[0].children:
                num += [x[1] * -1 for x in storage if i[0].value is x[0].value]
            data[1] = max(num)
            storage.append(data)

    final = []
    for i in storage[-1][0].children:
        for data1 in storage:

            if i[0].value == data1[0].value:
                final.append(data1[1] * -1)
    return final


def opponent(player: str) -> str:
    """
    Return the opponent of the player

    >>> opponent('p1')
    'p2'
    >>> opponent('p2')
    'p1'
    """
    if player == 'p1':
        return 'p2'
    return 'p1'


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
