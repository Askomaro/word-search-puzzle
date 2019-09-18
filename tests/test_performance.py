import timeit

import pytest


def test__find_operation():
    # arrange
    code_to_test = '''
board = generate_board(15, 15)
possible_words = walk_through(board)
trie = Trie()
trie.insert_list(possible_words)
with open('words.txt', 'r') as words:
    for word in words:
        trie.find(word.rstrip())'''

    # act
    speed = timeit.timeit(code_to_test, globals=globals(), number=10) / 10

    assert speed < 0.5
