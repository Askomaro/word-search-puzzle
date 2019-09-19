import pytest

from core.puzzle_engine import PuzzleEngine


def test__generate_board():
    # arrange
    row_count = 3
    el_in_row = 3

    # act
    puzzle = PuzzleEngine()
    puzzle.generate_board(row_count, el_in_row)

    assert len(puzzle.board) == row_count
    assert len(puzzle.board[0]) == el_in_row
    assert type(puzzle.board[0][0]) == str


def test__get_all_possible_words_from_board():
    # arrange
    dummy_board = [
        ['a', 'c', 'd'],
        ['e', 'f', 'g'],
        ['m', 'n', 'l']]
    puzzle = PuzzleEngine()
    puzzle.board = dummy_board

    # act
    all_possible_word = puzzle.get_all_possible_words()

    assert all_possible_word == [
        'ac', 'acd', 'af', 'afl', 'ae', 'aem',
        'cd', 'cg', 'cf', 'cfn', 'ce', 'ca',
        'dg', 'dgl', 'df', 'dfm', 'dc', 'dca',
        'ef', 'efg', 'en', 'em', 'ea', 'ec',
        'fg', 'fl', 'fn', 'fm', 'fe', 'fa', 'fc', 'fd',
        'gl', 'gn', 'gf', 'gfe', 'gc', 'gd',
        'mn', 'mnl', 'me', 'mea', 'mf', 'mfd',
        'nl', 'nm', 'ne', 'nf', 'nfc', 'ng',
        'ln', 'lnm', 'lf', 'lfa', 'lg', 'lgd']
