"""Program 35: Move all zeros in a list to the end."""


def move_zeros(numbers):
    """Return a list with all zeros moved to the end."""
    non_zero = []

    for number in numbers:
        if number != 0:
            non_zero.append(number)

    zeros = [0] * numbers.count(0)

    return non_zero + zeros


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

    print("After moving zeros:", move_zeros(numbers))