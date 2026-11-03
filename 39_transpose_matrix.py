"""Program 39: Transpose a matrix."""


def transpose_matrix(matrix):
    """Return the transpose of the given matrix."""
    if not matrix:
        return []

    return [list(row) for row in zip(*matrix)]


if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))

    matrix = []

    for row in range(rows):
        values = list(
            map(int, input(f"Enter values for row {row + 1}: ").split())
        )
        matrix.append(values)

    print("Transposed matrix:")

    for row in transpose_matrix(matrix):
        print(row)