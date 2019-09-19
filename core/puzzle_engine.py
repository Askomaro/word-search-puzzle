import random
import string


class PuzzleEngine:
    def __init__(self):
        self.board = []

    def generate_board(self, n: int, m: int) -> [[str]]:
        """
        Generates board n x m with random lowercase characters
        :param n: number of rows
        :param m: number of elements in a row
        :rtype: [[str]]
        :return: generated board
        """
        self.board = [[random.choice(string.ascii_lowercase) for _ in range(n)] for _ in range(m)]

    def show_board(self):
        """
        Print in console output a generated board
        """
        for row in self.board:
            print(' '.join(row))

    def get_all_possible_words(self) -> [str]:
        """
        Get all possible words form a random generated board with next rules:
        Words can be found along any diagonal, forwards, upwards, downwards or backwards
        and must not ‘wrap’ between edges
        :rtype: [str]
        :return: all possible words
        """
        result = []
        for idx_i, row in enumerate(self.board):
            for idx_j, _ in enumerate(row):
                result.extend(self._get_strings_for_pos(idx_i, idx_j))

        return result

    def _get_strings_for_pos(self, i: int, j: int) -> [str]:
        result = []

        result.extend(self._get_forwards(i, j))
        result.extend(self._get_right_down_diagonal(i, j))
        result.extend(self._get_downwards(i, j))
        result.extend(self._get_left_down_diagonal(i, j))
        result.extend(self._get_backwards(i, j))
        result.extend(self._get_left_up_diagonal(i, j))
        result.extend(self._get_upwards(i, j))
        result.extend(self._get_right_up_diagonal(i, j))

        # filter out string with one element as considered not a possible word
        return filter(lambda el: len(el) > 1, result)

    def _get_forwards(self, i: int, j: int) -> str:
        result = []
        temp = ''

        while j < len(self.board[i]):
            temp += self.board[i][j]
            result.append(temp)
            j += 1

        return result

    def _get_backwards(self, i: int, j: int) -> str:
        result = []
        temp = ''

        while j >= 0:
            temp += self.board[i][j]
            result.append(temp)
            j -= 1

        return result

    def _get_upwards(self, i: int, j: int) -> str:
        result = []
        temp = ''

        while i >= 0:
            temp += self.board[i][j]
            result.append(temp)
            i -= 1

        return result

    def _get_downwards(self, i: int, j: int) -> str:
        result = []
        temp = ''

        while i < len(self.board):
            temp += self.board[i][j]
            result.append(temp)
            i += 1

        return result

    def _get_left_up_diagonal(self, i: int, j: int) -> str:
        result = []
        temp = ''

        while i >= 0 and j >= 0:
            temp += self.board[i][j]
            result.append(temp)
            i -= 1
            j -= 1

        return result

    def _get_right_up_diagonal(self, i: int, j: int) -> str:
        result = []
        temp = ''
        row_ln = len(self.board[0])

        while i >= 0 and j < row_ln:
            temp += self.board[i][j]
            result.append(temp)
            i -= 1
            j += 1

        return result

    def _get_right_down_diagonal(self, i: int, j: int) -> str:
        result = []
        temp = ''
        row_ln = len(self.board[0])

        while i < len(self.board) and j < row_ln:
            temp += self.board[i][j]
            result.append(temp)
            i += 1
            j += 1

        return result

    def _get_left_down_diagonal(self, i: int, j: int) -> str:
        result = []
        temp = ''
        while i < len(self.board) and j >= 0:
            temp += self.board[i][j]
            result.append(temp)
            i += 1
            j -= 1

        return result
