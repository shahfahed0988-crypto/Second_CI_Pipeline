import importlib

module = importlib.import_module("39_transpose_matrix")


def test_transpose_matrix():
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    expected = [
        [1, 4],
        [2, 5],
        [3, 6]
    ]

    assert module.transpose_matrix(matrix) == expected


def test_square_matrix():
    matrix = [
        [1, 2],
        [3, 4]
    ]

    expected = [
        [1, 3],
        [2, 4]
    ]

    assert module.transpose_matrix(matrix) == expected


def test_empty_matrix():
    assert module.transpose_matrix([]) == []