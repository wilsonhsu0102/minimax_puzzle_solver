"""Phrase Puzzler: functions"""

# Phrase Puzzler constants

# Name of file containing puzzles
DATA_FILE = 'puzzles_small.txt'

# Letter values
CONSONANT_POINTS = 1
VOWEL_PRICE = 1
CONSONANT_BONUS = 2

# Players' names
PLAYER_ONE = 'Player One'
PLAYER_TWO = 'Player Two'

# Menu options - includes letter types
CONSONANT = 'C'
VOWEL = 'V'
SOLVE = 'S'
QUIT = 'Q'


# Define your functions here.

def is_win(puzzle: str, view: str) -> bool:
    """Return True if and only if puzzle is the same as view.

    >>> is_win('banana', 'banana')
    True
    >>> is_win('apple', 'a^^le')
    False
    """
    # put the function body here
    return puzzle == view


def game_over(puzzle: str, view: str, current_selection: str) -> bool:
    """Return True if and only if the puzzle is the same as the view or the 
    current selection is QUIT.
    
    >>> game_over('banana', 'banana', 'CONSONANT')
    True
    >>> game_over('apple', 'a^^le', 'QUIT')
    True
    >>> game_over('apple', 'a^^le', 'VOWEL')
    False
    """
    
    if current_selection == 'QUIT':
        return True
    else:
        return puzzle == view


def bonus_letter(puzzle: str, view: str, letter_to_evaluate: str) -> bool:
    """Return True if and only if the letter appears in the puzzle but not in 
    its view.
    
    >>> bonus_letter('apple', 'a^^le', 'p')
    True
    >>> bonus_letter('banana', 'ba^a^a', 'd')
    False
    >>> bonus_letter('banana', 'ba^a^a', 'a')
    False
    """
    
    return (letter_to_evaluate not in view) and (letter_to_evaluate in puzzle)
    
        
def update_letter_view(puzzle: str, view: str, index: int, guessed: str) -> str:
    """Return a single character string representing the next view of the 
    character at the given index. If the character at that index of the puzzle 
    matches the guess, then return that character. Otherwise, return the 
    character at that index of the view.
    
    >>> update_letter_view('apple', 'a^^le', 3, 'l')
    'l'
    >>> update_letter_view('apple', 'a^^le', 2, 'l')
    '^'
    """
    
    if puzzle[index] == guessed:
        return guessed
    else:
        return view[index]
        
    
def calculate_score(current_score: int, num_occurence: int, letter: str) -> int:
    """Return the new score by adding CONSONANT_POINTS per occurrence of the 
    letter to the current score if the letter is a consonant, or by deducting 
    the VOWEL_PRICE from the score if the letter is a vowel.
    
    >>> calculate_score(0, 2, CONSONANT)
    2
    >>> calculate_score(2, 2, VOWEL)
    1
    """
    
    if letter in CONSONANT:
        return current_score + num_occurence * CONSONANT_POINTS
    elif letter in VOWEL:
        return current_score - VOWEL_PRICE
    
    
def next_player(current_player: str, num_occurrence_current: int) -> str:
    """If and only if the number of occurrences is greater than zero, the 
    current player plays again. Return the next player 
    (one of PLAYER_ONE or PLAYER_TWO).
    
    >>> next_player(PLAYER_ONE, 1)
    'Player One'
    >>> next_player(PLAYER_TWO, 0)
    'Player One'
    """
    
    if current_player == PLAYER_ONE and num_occurrence_current == 0:
        return PLAYER_TWO
    elif current_player == PLAYER_TWO and num_occurrence_current == 0:
        return PLAYER_ONE
    else:
        return current_player
    
if _name_ == "_main_":
    import doctest
    doctest.testmod()