import timeit

import pytest

from core.puzzle_engine import PuzzleEngine
from models.trie import Trie


def test__find_operations():
    # arrange
    code_to_test = '''
found_words = []

puzzle = PuzzleEngine()
puzzle.generate_board(15, 15)
possible_words = puzzle.get_all_possible_words()

trie = Trie()
trie.insert_list(possible_words)

with open('words.txt', 'r') as words:
    for raw_word in words:
        word = raw_word.rstrip()
        if trie.find(word):
            found_words.append(word)
'''

    # act
    speed = timeit.timeit(code_to_test, globals=globals(), number=10) / 10

    assert speed < 0.5
