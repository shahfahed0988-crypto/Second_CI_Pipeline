"""Program 34: Check whether a list is sorted."""


def is_sorted(numbers):
    """Return True if the list is sorted in ascending order."""
    for index in range(len(numbers) - 1):
        if numbers[index] > numbers[index + 1]:
            return False

    return True


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

    if is_sorted(numbers):
        print("The list is sorted.")
    else:
        print("The list is not sorted.")