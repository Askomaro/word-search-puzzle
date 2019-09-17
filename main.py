def test(i: int, j: int) -> [str]:
    a = [['a', 'v', 'b', 'y', 'z'],
         ['k', 'c', 'p', 'o', 'l'],
         ['c', 'a', 'l', 'n', 'm']]

    result = [_get_forwards(a, i, j),
              _get_backwards(a, i, j),
              _get_upwards(a, i, j),
              _get_downwards(a, i, j),
              _get_left_up_diagonal(a, i, j),
              _get_right_up_diagonal(a, i, j),
              _get_right_down_diagonal(a, i, j),
              _get_left_down_diagonal(a, i, j)]

    return result


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


if __name__ == '__main__':
    print(test(0, 1))
