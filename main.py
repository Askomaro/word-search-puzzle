def get_strings_for_pos(a: [[str]], i: int, j: int) -> [str]:

    result = [_get_forwards(a, i, j),
              _get_backwards(a, i, j),
              _get_upwards(a, i, j),
              _get_downwards(a, i, j),
              _get_left_up_diagonal(a, i, j),
              _get_right_up_diagonal(a, i, j),
              _get_right_down_diagonal(a, i, j),
              _get_left_down_diagonal(a, i, j)]

    return filter(lambda el: len(el) > 1, result)


def _get_forwards(arr: [[int]], i: int, j: int) -> str:
    return ''.join(arr[i][j:])


def _get_backwards(arr: [[int]], i: int, j: int) -> str:
    return ''.join(arr[i][j::-1])


def _get_upwards(arr: [[int]], i: int, j: int) -> str:
    return ''.join([el[j] for el in arr[i::-1]])


def _get_downwards(arr: [[int]], i: int, j: int) -> str:
    return ''.join([el[j] for el in arr[i:]])


def _get_left_up_diagonal(arr: [[int]], i: int, j: int) -> str:
    result = ''
    while i >= 0 and j >= 0:
        result += arr[i][j]
        i -= 1
        j -= 1

    return result


def _get_right_up_diagonal(arr: [[int]], i: int, j: int) -> str:
    result = ''
    row_ln = len(arr[0])

    while i >= 0 and j < row_ln:
        result += arr[i][j]
        i -= 1
        j += 1

    return result


def _get_right_down_diagonal(arr: [[int]], i: int, j: int) -> str:
    result = ''
    row_ln = len(arr[0])

    while i < len(arr) and j < row_ln:
        result += arr[i][j]
        i += 1
        j += 1

    return result


def _get_left_down_diagonal(arr: [[int]], i: int, j: int) -> str:
    result = ''
    while i < len(arr) and j >= 0:
        result += arr[i][j]
        i += 1
        j -= 1

    return result


def walk_through(arr: [[str]]) -> [str]:
    result = []
    for idx_i, row in enumerate(arr):
        for idx_j, _ in enumerate(row):
            result.extend(get_strings_for_pos(arr, idx_i, idx_j))

    return result


if __name__ == '__main__':
    b = [['a', 'v', 'b', 'y', 'z'],
         ['k', 'c', 'p', 'o', 'l'],
         ['c', 'a', 'l', 'n', 'm']]

    print(walk_through(b))
