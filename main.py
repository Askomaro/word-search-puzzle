import click

from models.trie import Trie
from core.puzzle_engine import PuzzleEngine


@click.command()
@click.option('--i', default=15, help='Number of rows.')
@click.option('--j', default=15, help='Number of elements in a row.')
@click.option('--file_name', default='words.txt', help='Name of file with words.')
def start_app(i, j, file_name):
    found_words = []

    puzzle = PuzzleEngine()
    puzzle.generate_board(i, j)
    puzzle.show_board()
    possible_words = puzzle.get_all_possible_words()

    trie = Trie()
    trie.insert_list(possible_words)

    with open(file_name, 'r') as words:
        for raw_word in words:
            word = raw_word.rstrip()
            if trie.find(word):
                found_words.append(word)

    print(found_words)


if __name__ == '__main__':
    start_app()
